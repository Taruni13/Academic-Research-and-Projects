# app.py
from shiny import App, ui, render, reactive
import pandas as pd
import os

# Mapping for class codes to full names
CLASS_MAP = {
    "FR": "Freshman",
    "SO": "Sophomore",
    "JR": "Junior",
    "SR": "Senior"
}

# Path to your CSV file
DATA_PATH = os.path.join(os.path.dirname(__file__), "students_fake.csv")
students = pd.read_csv(DATA_PATH, dtype=str).fillna("")

def unique_sorted(col):
    vals = students[col].dropna().unique()
    # For class, use mapping; for others, just sort
    if col == "CLAS_CODE":
        return [""] + [f"{code} - {CLASS_MAP.get(code, code)}" for code in sorted(vals) if code in CLASS_MAP]
    else:
        return [""] + sorted(vals)

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
    # Add the logo at the top of the main panel
    ui.img(src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FUniversity_of_the_Pacific_%2528United_States%2529&psig=AOvVaw2eF9fsVg8i1pNP29SbF0ii&ust=1750465518384000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLD8za7e_o0DFQAAAAAdAAAAABAE", height="80px"),
    ui.h2("Welcome to University Dashboard"),
    ui.output_table("student_table"),
    ui.output_ui("student_select"),
    ui.output_ui("student_detail")
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
            # Extract code from "XX - Full Name"
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
    @render.table
    def student_table():
        df = filtered_students()
        # Show class as full name in the table
        if "CLAS_CODE" in df.columns:
            df = df.copy()
            df["Class"] = df["CLAS_CODE"].map(CLASS_MAP)
        return df[["PACIFIC_ID", "LAST_NAME", "FIRST_NAME", "Class", "CURR_1_1_MAJR_DESC", "OVRL_GPA"]]

    @output
    @render.ui
    def student_select():
        df = filtered_students()
        options = [""] + df["PACIFIC_ID"].tolist()
        return ui.input_select("student_id", "Select Student", options)

    @output
    @render.ui
    def student_detail():
        sid = input.student_id()
        if not sid:
            return ui.p("Select a student to view details.")
        student = students[students["PACIFIC_ID"] == sid].iloc[0]
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

app = App(app_ui, server)
if __name__ == "__main__":
    app.run()
