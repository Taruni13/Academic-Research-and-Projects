# ------------------------------------------------------
# University Dashboard Main App with Cards, Table Expand,
# Graphs, and AI Student Summary
# ------------------------------------------------------

from shiny import App, ui, render, reactive
import pandas as pd
import matplotlib.pyplot as plt
import openai

# Import helper functions
from helpers import load_data, get_student_count, calculate_average_grade

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"  # <-- Replace with your key

# Mapping for class codes to full names
CLASS_MAP = {
    "FR": "Freshman",
    "SO": "Sophomore",
    "JR": "Junior",
    "SR": "Senior"
}

# Load data
students = load_data()

def unique_sorted(col):
    vals = students[col].dropna().unique()
    if col == "CLAS_CODE":
        return [""] + [f"{code} - {CLASS_MAP.get(code, code)}" for code in sorted(vals) if code in CLASS_MAP]
    else:
        return [""] + sorted(vals)

def stat_card(icon, label, value):
    return ui.div(
        ui.div(
            ui.span(icon, style="font-size:2.5em; color:#1976d2; margin-right:10px;"),
            ui.div(
                ui.div(label, style="font-size:1em; color:#888;"),
                ui.div(value, style="font-size:2em; font-weight:bold;"),
                style="display:inline-block; vertical-align:top;"
            ),
            style="display:flex; align-items:center;"
        ),
        style=(
            "background:#fff; border-radius:10px; box-shadow:0 2px 8px #eee;"
            "padding:20px; margin:10px; display:inline-block; min-width:220px;"
        )
    )

def dashboard_card(title, content, tooltip=None):
    card_div = ui.div(
        ui.div(
            ui.div(title, style="font-weight:bold; font-size:1.1em; margin-bottom:10px;"),
            content,
            style="padding:10px;"
        ),
        style=(
            "background:#fff; border-radius:10px; box-shadow:0 2px 8px #eee;"
            "padding:15px; margin:10px; display:inline-block; min-width:320px; vertical-align:top;"
        ),
        title=tooltip if tooltip else ""
    )
    return card_div

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("entry_sem", "Entry Semester", unique_sorted("INIT_ENRL_TERM_DESC")),
        ui.input_select("level", "Level", unique_sorted("LEVL_CODE")),
        ui.input_select("class_", "Class", unique_sorted("CLAS_CODE")),
        ui.input_select("sport", "Sport Team", unique_sorted("SPRT_1_DESC")),
        ui.input_select("grad_sem", "Graduation Semester", unique_sorted("TERM_DESC_GRAD")),
        ui.input_select("major", "Major", unique_sorted("CURR_1_1_MAJR_DESC")),
        ui.input_select("second_deg", "Second Degree", unique_sorted("CURR_2_DEGC_DESC")),
        ui.input_slider("gpa", "GPA", 0.0, 4.0, 0.0, step=0.1),
        ui.input_select("advisor", "Advisor Name", unique_sorted("ADVR_1_FMIL")),
    ),
    ui.img(
        src="https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/University_of_the_Pacific_seal.svg/240px-University_of_the_Pacific_seal.svg.png",
        height="80px"
    ),
    ui.h2("Welcome to University Dashboard"),
    ui.output_ui("summary_stats"),
    ui.output_ui("student_table_card"),
    ui.div(
        ui.output_ui("gpa_hist_card"),
        ui.output_ui("student_count_bar_card"),
        style="display:flex; flex-wrap:wrap; gap:20px;"
    ),
    ui.output_ui("student_select"),
    ui.output_ui("student_detail"),
    ui.output_ui("student_ai_summary")
)

def server(input, output, session):
    @reactive.Calc
    def filtered_students():
        df = students.copy()
        if input.entry_sem():
            df = df[df["INIT_ENRL_TERM_DESC"] == input.entry_sem()]
        if input.level():
            df = df[df["LEVL_CODE"] == input.level()]
        if input.class_():
            class_code = input.class_().split(" - ")[0]
            df = df[df["CLAS_CODE"] == class_code]
        if input.sport():
            df = df[df["SPRT_1_DESC"] == input.sport()]
        if input.grad_sem():
            df = df[df["TERM_DESC_GRAD"] == input.grad_sem()]
        if input.major():
            df = df[df["CURR_1_1_MAJR_DESC"] == input.major()]
        if input.second_deg():
            df = df[df["CURR_2_DEGC_DESC"] == input.second_deg()]
        if input.gpa() > 0.0:
            df = df[pd.to_numeric(df["OVRL_GPA"], errors="coerce").fillna(0) >= input.gpa()]
        if input.advisor():
            df = df[df["ADVR_1_FMIL"] == input.advisor()]
        return df

    @output
    @render.ui
    def summary_stats():
        df = filtered_students()
        count = get_student_count(df)
        avg_gpa = calculate_average_grade(df) if "OVRL_GPA" in df.columns else None
        return ui.div(
            stat_card("👥", "Total students", count),
            stat_card("💼", "Average GPA", f"{round(avg_gpa, 2) if avg_gpa is not None else 'N/A'}"),
            style="display:flex; gap:20px;"
        )

    show_full_table = reactive.value(False)

    @output
    @render.ui
    def student_table_card():
        df = filtered_students()
        show_all = show_full_table()
        table_df = df if show_all else df.head(10)
        expand_label = "Collapse" if show_all else "Expand"
        expand_button = ui.input_action_button("expand_table", expand_label)
        return dashboard_card(
            "Student Data",
            ui.div(
                ui.output_table("student_table"),
                expand_button
            ),
            tooltip=f"Total students: {get_student_count(df)}"
        )

    @output
    @render.table
    def student_table():
        df = filtered_students()
        show_all = show_full_table()
        table_df = df if show_all else df.head(10)
        if "CLAS_CODE" in table_df.columns:
            table_df = table_df.copy()
            table_df["Class"] = table_df["CLAS_CODE"].map(CLASS_MAP)
        return table_df[["PACIFIC_ID", "LAST_NAME", "FIRST_NAME", "Class", "CURR_1_1_MAJR_DESC", "OVRL_GPA"]]

    @reactive.effect
    def _expand_table():
        if input.expand_table():
            show_full_table.set(not show_full_table())
            output.student_table_card.invalidate()
            output.student_table.invalidate()

    @output
    @render.ui
    def gpa_hist_card():
        return dashboard_card(
            "GPA Distribution",
            ui.output_plot("gpa_hist", width="300px", height="300px"),
            tooltip="Shows the distribution of GPA among filtered students."
        )

    @output
    @render.plot
    def gpa_hist():
        df = filtered_students()
        gpas = pd.to_numeric(df["OVRL_GPA"], errors="coerce").dropna()
        fig, ax = plt.subplots()
        ax.hist(gpas, bins=10, color="orange", edgecolor="black")
        ax.set_title("GPA Distribution")
        ax.set_xlabel("GPA")
        ax.set_ylabel("Number of Students")
        return fig

    @output
    @render.ui
    def student_count_bar_card():
        return dashboard_card(
            "Student Count by Class",
            ui.output_plot("student_count_bar", width="700px", height="300px"),
            tooltip="Shows the number of students in each class."
        )

    @output
    @render.plot
    def student_count_bar():
        df = filtered_students()
        class_counts = df["CLAS_CODE"].map(CLASS_MAP).value_counts()
        fig, ax = plt.subplots(figsize=(8, 4))
        class_counts.plot(kind="barh", ax=ax, color="skyblue")
        ax.set_title("Student Count by Class")
        ax.set_xlabel("Number of Students")
        ax.set_ylabel("Class")
        return fig

    @output
    @render.ui
    def student_select():
        df = filtered_students()
        options = [""] + df["PACIFIC_ID"].tolist()
        current = input.student_id()
        if current not in options:
            return ui.input_select("student_id", "Select Student", options, selected="")
        return ui.input_select("student_id", "Select Student", options, selected=current)

    @output
    @render.ui
    def student_detail():
        sid = input.student_id()
        df = filtered_students()
        if not sid or sid not in df["PACIFIC_ID"].tolist():
            return ui.p("Select a student to view details.")
        student = df[df["PACIFIC_ID"] == sid].iloc[0]
        class_full = CLASS_MAP.get(student.get("CLAS_CODE", ""), student.get("CLAS_CODE", ""))
        return ui.panel_well(
            ui.h4(f"{student['FIRST_NAME']} {student['LAST_NAME']}"),
            ui.p(f"Class: {class_full}"),
            ui.p(f"Email: {student.get('PAC_EMAIL', '')}"),
            ui.p(f"Major: {student.get('CURR_1_1_MAJR_DESC', '')}"),
            ui.p(f"Second Degree: {student.get('CURR_2_DEGC_DESC', '')}"),
            ui.p(f"GPA: {student.get('OVRL_GPA', '')}"),
            ui.p(f"Advisor: {student.get('ADVR_1_FMIL', '')}"),
            ui.p(f"Credits this semester: {student.get('CREDIT_HR_THIS_TERM', '')}"),
            ui.p(f"Total credits: {student.get('OVRL_HRS_EARNED', '')}")
        )

    @output
    @render.ui
    def student_ai_summary():
        sid = input.student_id()
        df = filtered_students()
        if not sid or sid not in df["PACIFIC_ID"].tolist():
            return ui.p("Select a student to get an AI summary.")
        student = df[df["PACIFIC_ID"] == sid].iloc[0]
        prompt = (
            f"Student Name: {student['FIRST_NAME']} {student['LAST_NAME']}\n"
            f"Class: {CLASS_MAP.get(student.get('CLAS_CODE', ''), student.get('CLAS_CODE', ''))}\n"
            f"Major: {student.get('CURR_1_1_MAJR_DESC', '')}\n"
            f"GPA: {student.get('OVRL_GPA', '')}\n"
            f"Advisor: {student.get('ADVR_1_FMIL', '')}\n"
            "Write a 3-4 line summary about this student for an academic dashboard."
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100,
                temperature=0.7
            )
            summary = response.choices[0].message.content.strip()
        except Exception as e:
            summary = f"AI summary unavailable: {e}"
        return ui.panel_well(ui.p(summary))

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
