# ------------------------------------------------------
# University Dashboard 
# ------------------------------------------------------

from shiny import App, ui, render, reactive
import pandas as pd
import matplotlib.pyplot as plt
import openai
import faicons as fa

# --- Import helper functions for data loading and calculations ---
from helpers import load_data, get_student_count, calculate_average_grade

# --- Set your OpenAI API key (replace with your own key) ---
openai.api_key = "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"

# --- Mapping for class codes to full names ---
CLASS_MAP = {
    "FR": "Freshman",
    "SO": "Sophomore",
    "JR": "Junior",
    "SR": "Senior"
}

# --- Load student data from CSV or other source ---
students = load_data()

# --- Helper: Get unique sorted values for dropdowns ---
def unique_sorted(col):
    vals = students[col].dropna().unique()  # Drop missing values and get unique
    return [""] + sorted(vals)  # Add empty option and sort

# --- Helper: Create a stat card with icon, label, and value ---
def stat_card(icon, label, value, icon_color):
    return ui.div(
        ui.div(
            ui.span(icon, fill=icon_color, style="font-size:2.5em; margin-right:10px;"),  # Icon with color
            ui.div(
                ui.div(label, style="font-size:1em; color:#888;"),  # Label
                ui.div(value, style="font-size:2em; font-weight:bold;"),  # Value
                style="display:inline-block; vertical-align:top;"
            ),
            style="display:flex; align-items:center;"
        ),
        style=(
            "background:#fff; border-radius:10px; box-shadow:0 2px 8px #eee;"
            "padding:20px; margin:10px; display:inline-block; min-width:220px;"
        )
    )

# --- Helper: Create a dashboard card with a title and content ---
def dashboard_card(title, content, tooltip=None):
    return ui.card(
        ui.card_header(title),  # Card header/title
        content  # Card content
    )

# --- UI Layout ---
app_ui = ui.page_sidebar(
    # --- Sidebar with filters ---
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
    
    # --- Top summary row: total students, average GPA, AI summary ---
    ui.layout_columns(
        ui.value_box(
            "Total students",  # Box label
            ui.output_ui("total_students"),  # Output value
            showcase=fa.icon_svg("user-graduate", fill="cornflowerblue"),  # Blue icon
            style="min-height:220px; height:220px; width:100%;"  # Box style
        ),
        ui.value_box(
            "Average GPA",
            ui.output_ui("average_gpa"),
            showcase=fa.icon_svg("graduation-cap", fill="orange"),  # Orange icon
            style="min-height:220px; height:220px; width:100%;"
        ),
        ui.card(
            ui.card_header(
                fa.icon_svg("comment", fill="cornflowerblue"),  # Blue comment icon
                " Student Summary"
            ),
            ui.output_ui("student_ai_summary"),  # AI summary output
            style="min-height:120px; width:100%;"
        ),
        col_widths=[3, 3, 6]
    ),
    
    # --- Middle row: student table, search, and details ---
    ui.layout_columns(
        ui.card(
            ui.card_header(
                fa.icon_svg("users", fill="cornflowerblue"),  # Blue users icon
                " List of Students"
            ),
            ui.output_ui("student_table"),  # Student table output
            full_screen=True,
            style="height:300px; min-height:300px;"
        ),
        ui.card(
            ui.card_header(
                ui.span(
                    fa.icon_svg("magnifying-glass", fill="cornflowerblue"),  # Blue search icon
                    "Search Student"
                )
            ),
            ui.input_text("student_id", "Enter a valid PACIFIC_ID", placeholder="Type or paste student ID..."),  # Search input
            style="min-height:100px; width:100%;"
        ),
        ui.card(
            ui.card_header(
                fa.icon_svg("id-card", fill="cornflowerblue"),  # Blue id-card icon
                " Student Details"
            ),
            ui.output_ui("student_detail"),  # Student details output
            full_screen=True,
            style="height:300px; min-height:300px;"
        ),
        col_widths=[4, 2, 6]
    ),

    # --- Bottom row: GPA distribution and student count by class ---
    ui.layout_columns(
        ui.card(
            ui.card_header(
                fa.icon_svg("chart-column", fill="cornflowerblue"),  # Blue chart-column icon
                " GPA Distribution"
            ),
            ui.output_plot("gpa_hist", width="100%", height="500px"),  # GPA histogram output
            full_screen=True,
            style="height:400px; min-height:400px;"
        ),
        ui.card(
            ui.card_header(
                fa.icon_svg("chart-bar", fill="cornflowerblue"),  # Blue chart-bar icon
                " Student Count by Class"
            ),
            ui.output_plot("student_count_bar", width="100%", height="500px"),  # Student count bar output
            full_screen=True,
            style="height:400px; min-height:400px;"
        ),
        col_widths=[6, 6]
    ),
    title="Welcome to University Dashboard !!!",
    fillable=True,
)

# --- Server logic ---
def server(input, output, session):
    # --- Reactive: Filter students based on sidebar inputs ---
    @reactive.calc
    def filtered_students():
        df = students.copy()  # Start with all students
        # Apply filters one by one if selected
        if input.entry_sem():
            df = df[df["INIT_ENRL_TERM_DESC"] == input.entry_sem()]
        if input.level():
            df = df[df["LEVL_CODE"] == input.level()]
        if input.class_():
            df = df[df["CLAS_CODE"] == input.class_()]
        if input.sport():
            df = df[df["SPRT_1_DESC"] == input.sport()]
        if input.grad_sem():
            df = df[df["TERM_DESC_GRAD"] == input.grad_sem()]
        if input.major():
            df = df[df["CURR_1_1_MAJR_DESC"] == input.major()]
        if input.second_deg():
            df = df[df["CURR_2_DEGC_DESC"] == input.second_deg()]
        if input.gpa() > 0.0:
            # Filter by GPA threshold
            df = df[pd.to_numeric(df["OVRL_GPA"], errors="coerce").fillna(0) >= input.gpa()]
        if input.advisor():
            df = df[df["ADVR_1_FMIL"] == input.advisor()]
        return df

    # --- Output: Table of students (filtered) ---
    @output
    @render.table
    def student_table():
        # Show filtered students with selected columns and mapped class names
        df = filtered_students()
        if "CLAS_CODE" in df.columns:
            df = df.copy()
            df["Class"] = df["CLAS_CODE"].map(CLASS_MAP)
        return df[["PACIFIC_ID", "LAST_NAME", "FIRST_NAME", "Class", "CURR_1_1_MAJR_DESC", "OVRL_GPA"]]

    # --- Output: Student details panel ---
    @output
    @render.ui
    def student_detail():
        sid = input.student_id()  # Get entered PACIFIC_ID
        df = filtered_students()
        
        # Check if valid ID is entered
        if not sid or sid not in df["PACIFIC_ID"].astype(str).tolist():
            return ui.p("Enter a valid PACIFIC_ID to view details.")
        student = df[df["PACIFIC_ID"].astype(str) == sid]
        if student.empty:
            return ui.p("Student not found.")
        student = student.iloc[0]
        class_full = CLASS_MAP.get(student.get("CLAS_CODE", ""), student.get("CLAS_CODE", ""))
        
        # Display student details in a well panel
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

    # --- Output: GPA distribution histogram ---
    @output
    @render.plot
    def gpa_hist():
        df = filtered_students()
        gpas = pd.to_numeric(df["OVRL_GPA"], errors="coerce").dropna()  # Clean GPA values
        fig, ax = plt.subplots(figsize=(7, 2))  # Set figure size
        ax.hist(gpas, bins=8, color="cornflowerblue", edgecolor="black")  # Plot histogram
        ax.set_title("GPA(Grade Point Average) Distribution", fontsize=10)  # Graph title
        ax.set_xlabel("GPA", fontsize=8)  # X-axis label
        ax.set_ylabel("Number of Students", fontsize=8)  # Y-axis label
        fig.tight_layout()
        return fig

    # --- Output: Student count by class bar chart ---
    @output
    @render.plot
    def student_count_bar():
        df = filtered_students()
        class_counts = df["CLAS_CODE"].map(CLASS_MAP).value_counts()  # Count by class
        fig, ax = plt.subplots(figsize=(7, 2))
        class_counts.plot(kind="barh", ax=ax, color="cornflowerblue", edgecolor="black")  # Horizontal bar
        ax.set_title("Student Count by Class", fontsize=10)  # Graph title
        ax.set_xlabel("Number of Students", fontsize=8)  # X-axis label
        ax.set_ylabel("Class", fontsize=8)  # Y-axis label
        fig.tight_layout()
        return fig

    # --- Output: AI-generated student summary ---
    @output
    @render.ui
    def student_ai_summary():
        sid = input.student_id()
        df = filtered_students()
        # Check if a valid student is selected
        if not sid or sid not in df["PACIFIC_ID"].astype(str).tolist():
            return ui.p("Select a student to get an AI summary.")
        student = df[df["PACIFIC_ID"].astype(str) == sid].iloc[0]
        # Compose prompt for OpenAI
        prompt = (
            f"Student Name: {student['FIRST_NAME']} {student['LAST_NAME']}\n"
            f"Class: {CLASS_MAP.get(student.get('CLAS_CODE', ''), student.get('CLAS_CODE', ''))}\n"
            f"Major: {student.get('CURR_1_1_MAJR_DESC', '')}\n"
            f"GPA: {student.get('OVRL_GPA', '')}\n"
            f"Advisor: {student.get('ADVR_1_FMIL', '')}\n"
            "Write a 3-4 line summary about this student for an academic dashboard."
        )
        try:
            # Call OpenAI API for summary
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100,
                temperature=0.7
            )
            summary = response.choices[0].message.content.strip()
        except Exception as e:
            summary = f"AI summary unavailable: {e}"  # Show error if API fails
        return ui.panel_well(ui.p(summary))

    # --- Output: Total students value box ---
    @output
    @render.ui
    def total_students():
        return str(len(filtered_students()))  # Show count of filtered students

    # --- Output: Average GPA value box ---
    @output
    @render.ui
    def average_gpa():
        df = filtered_students()
        gpas = pd.to_numeric(df["OVRL_GPA"], errors="coerce")
        if gpas.notna().sum() == 0:
            return "N/A"  # Handle no GPA case
        return f"{gpas.mean():.2f}"  # Format mean GPA

# --- Create and run the Shiny app ---
app = App(app_ui, server)

if __name__ == "__main__":
    app.run()