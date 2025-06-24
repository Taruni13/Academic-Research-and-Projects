# ------------------------------------------------------
# Helper Functions for University Dashboard
# Provides data loading, filtering, and retrieval utilities.
# ------------------------------------------------------

import pandas as pd

# ------------------------------------------------------
# Function: load_data
# Loads student data from students_fake.csv and drops rows
# with missing first or last names.
# ------------------------------------------------------
def load_data():
    df = pd.read_csv("students_fake.csv")
    df.dropna(subset=["FIRST_NAME", "LAST_NAME"], inplace=True)
    return df

# ------------------------------------------------------
# Function: filter_students
# Filters the DataFrame based on a dictionary of filters.
# ------------------------------------------------------
def filter_students(df, filters):
    for col, val in filters.items():
        if val:
            df = df[df[col] == val]
    return df

# ------------------------------------------------------
# Function: calculate_average_grade
# Returns the average grade if the GRADE column exists.
# ------------------------------------------------------
def calculate_average_grade(df):
    if "GRADE" in df.columns:
        return df["GRADE"].mean()
    else:
        return None 

# ------------------------------------------------------
# Function: get_student_count
# Returns the number of students (rows) in the DataFrame.
# ------------------------------------------------------
def get_student_count(df):
    return df.shape[0]  

# ------------------------------------------------------
# Function: get_unique_values
# Returns unique values for a given column.
# ------------------------------------------------------
def get_unique_values(df, column):
    if column in df.columns:
        return df[column].unique()
    else:
        return None 

# ------------------------------------------------------
# Function: get_student_details
# Returns a dictionary of details for a specific student.
# ------------------------------------------------------
def get_student_details(df, student_id):
    student = df[df["STUDENT_ID"] == student_id]
    if not student.empty:
        return student.iloc[0].to_dict()
    else:
        return None 

# ------------------------------------------------------
# Function: get_course_enrollment
# Returns the number of students enrolled in a course.
# ------------------------------------------------------
def get_course_enrollment(df, course_id):
    return df[df["COURSE_ID"] == course_id].shape[0]   

# ------------------------------------------------------
# Function: get_student_courses
# Returns a list of courses for a specific student.
# ------------------------------------------------------
def get_student_courses(df, student_id):
    student_courses = df[df["STUDENT_ID"] == student_id]
    if not student_courses.empty:
        return student_courses[["COURSE_ID", "COURSE_NAME"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_student_grades
# Returns a list of grades for a specific student.
# ------------------------------------------------------
def get_student_grades(df, student_id):
    student_grades = df[df["STUDENT_ID"] == student_id]
    if not student_grades.empty:
        return student_grades[["COURSE_ID", "GRADE"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_course_details
# Returns a dictionary of details for a specific course.
# ------------------------------------------------------
def get_course_details(df, course_id):
    course = df[df["COURSE_ID"] == course_id]
    if not course.empty:
        return course.iloc[0].to_dict()
    else:
        return None

# ------------------------------------------------------
# Function: get_student_attendance
# Returns attendance records for a specific student.
# ------------------------------------------------------
def get_student_attendance(df, student_id):
    attendance = df[df["STUDENT_ID"] == student_id]
    if not attendance.empty:
        return attendance[["COURSE_ID", "ATTENDANCE"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_course_attendance
# Returns attendance records for a specific course.
# ------------------------------------------------------
def get_course_attendance(df, course_id):
    course_attendance = df[df["COURSE_ID"] == course_id]
    if not course_attendance.empty:
        return course_attendance[["STUDENT_ID", "ATTENDANCE"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_student_performance
# Returns performance records for a specific student.
# ------------------------------------------------------
def get_student_performance(df, student_id):
    student_performance = df[df["STUDENT_ID"] == student_id]
    if not student_performance.empty:
        return student_performance[["COURSE_ID", "GRADE", "ATTENDANCE"]].to_dict(orient="records")
    else:
        return None 

# ------------------------------------------------------
# Function: get_course_performance
# Returns performance records for a specific course.
# ------------------------------------------------------
def get_course_performance(df, course_id):
    course_performance = df[df["COURSE_ID"] == course_id]
    if not course_performance.empty:
        return course_performance[["STUDENT_ID", "GRADE", "ATTENDANCE"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_student_feedback
# Returns feedback records for a specific student.
# ------------------------------------------------------
def get_student_feedback(df, student_id):
    feedback = df[df["STUDENT_ID"] == student_id]
    if not feedback.empty:
        return feedback[["COURSE_ID", "FEEDBACK"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_course_feedback
# Returns feedback records for a specific course.
# ------------------------------------------------------
def get_course_feedback(df, course_id):
    course_feedback = df[df["COURSE_ID"] == course_id]
    if not course_feedback.empty:
        return course_feedback[["STUDENT_ID", "FEEDBACK"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_student_progress
# Returns progress records for a specific student.
# ------------------------------------------------------
def get_student_progress(df, student_id):
    student_progress = df[df["STUDENT_ID"] == student_id]
    if not student_progress.empty:
        return student_progress[["COURSE_ID", "PROGRESS"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_course_progress
# Returns progress records for a specific course.
# ------------------------------------------------------
def get_course_progress(df, course_id):
    course_progress = df[df["COURSE_ID"] == course_id]
    if not course_progress.empty:
        return course_progress[["STUDENT_ID", "PROGRESS"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_student_exams
# Returns exam scores for a specific student.
# ------------------------------------------------------
def get_student_exams(df, student_id):
    student_exams = df[df["STUDENT_ID"] == student_id]
    if not student_exams.empty:
        return student_exams[["COURSE_ID", "EXAM_SCORE"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_course_exams
# Returns exam scores for a specific course.
# ------------------------------------------------------
def get_course_exams(df, course_id):
    course_exams = df[df["COURSE_ID"] == course_id]
    if not course_exams.empty:
        return course_exams[["STUDENT_ID", "EXAM_SCORE"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_student_projects
# Returns project scores for a specific student.
# ------------------------------------------------------
def get_student_projects(df, student_id):
    student_projects = df[df["STUDENT_ID"] == student_id]
    if not student_projects.empty:
        return student_projects[["COURSE_ID", "PROJECT_SCORE"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_course_projects
# Returns project scores for a specific course.
# ------------------------------------------------------
def get_course_projects(df, course_id):         
    course_projects = df[df["COURSE_ID"] == course_id]
    if not course_projects.empty:
        return course_projects[["STUDENT_ID", "PROJECT_SCORE"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_student_instructors
# Returns instructor names for a specific student.
# ------------------------------------------------------
def get_student_instructors(df, student_id):
    student_instructors = df[df["STUDENT_ID"] == student_id]
    if not student_instructors.empty:
        return student_instructors[["COURSE_ID", "INSTRUCTOR_NAME"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_course_instructors
# Returns instructor names for a specific course.
# ------------------------------------------------------
def get_course_instructors(df, course_id):
    course_instructors = df[df["COURSE_ID"] == course_id]
    if not course_instructors.empty:
        return course_instructors[["STUDENT_ID", "INSTRUCTOR_NAME"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_student_schedule
# Returns schedule info for a specific student.
# ------------------------------------------------------
def get_student_schedule(df, student_id):
    student_schedule = df[df["STUDENT_ID"] == student_id]
    if not student_schedule.empty:
        return student_schedule[["COURSE_ID", "SCHEDULE"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_course_schedule
# Returns schedule info for a specific course.
# ------------------------------------------------------
def get_course_schedule(df, course_id):
    course_schedule = df[df["COURSE_ID"] == course_id]
    if not course_schedule.empty:
        return course_schedule[["STUDENT_ID", "SCHEDULE"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_student_notifications
# Returns notifications for a specific student.
# ------------------------------------------------------
def get_student_notifications(df, student_id):
    student_notifications = df[df["STUDENT_ID"] == student_id]
    if not student_notifications.empty:
        return student_notifications[["COURSE_ID", "NOTIFICATION"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_course_notifications
# Returns notifications for a specific course.
# ------------------------------------------------------
def get_course_notifications(df, course_id):
    course_notifications = df[df["COURSE_ID"] == course_id]
    if not course_notifications.empty:
        return course_notifications[["STUDENT_ID", "NOTIFICATION"]].to_dict(orient="records")
    else:
        return None     

# ------------------------------------------------------
# Function: get_student_resources
# Returns resource links for a specific student.
# ------------------------------------------------------
def get_student_resources(df, student_id):
    student_resources = df[df["STUDENT_ID"] == student_id]
    if not student_resources.empty:
        return student_resources[["COURSE_ID", "RESOURCE_LINK"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_course_resources
# Returns resource links for a specific course.
# ------------------------------------------------------
def get_course_resources(df, course_id):
    course_resources = df[df["COURSE_ID"] == course_id]
    if not course_resources.empty:
        return course_resources[["STUDENT_ID", "RESOURCE_LINK"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_student_support
# Returns support tickets for a specific student.
# ------------------------------------------------------
def get_student_support(df, student_id):
    student_support = df[df["STUDENT_ID"] == student_id]
    if not student_support.empty:
        return student_support[["COURSE_ID", "SUPPORT_TICKET"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_course_support
# Returns support tickets for a specific course.
# ------------------------------------------------------
def get_course_support(df, course_id):
    course_support = df[df["COURSE_ID"] == course_id]
    if not course_support.empty:
        return course_support[["STUDENT_ID", "SUPPORT_TICKET"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_student_achievements
# Returns achievements for a specific student.
# ------------------------------------------------------
def get_student_achievements(df, student_id):
    student_achievements = df[df["STUDENT_ID"] == student_id]
    if not student_achievements.empty:
        return student_achievements[["COURSE_ID", "ACHIEVEMENT"]].to_dict(orient="records")
    else:
        return None

# ------------------------------------------------------
# Function: get_course_achievements
# Returns achievements for a specific course.
# ------------------------------------------------------
def get_course_achievements(df, course_id):
    course_achievements = df[df["COURSE_ID"] == course_id]
    if not course_achievements.empty:
        return course_achievements[["STUDENT_ID", "ACHIEVEMENT"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurriculars(df, student_id):   
    student_extracurriculars = df[df["STUDENT_ID"] == student_id]
    if not student_extracurriculars.empty:
        return student_extracurriculars[["EXTRACURRICULAR_ID", "EXTRACURRICULAR_NAME"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurriculars(df, course_id):
    course_extracurriculars = df[df["COURSE_ID"] == course_id]
    if not course_extracurriculars.empty:
        return course_extracurriculars[["STUDENT_ID", "EXTRACURRICULAR_NAME"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_details(df, extracurricular_id):
    extracurricular = df[df["EXTRACURRICULAR_ID"] == extracurricular_id]
    if not extracurricular.empty:
        return extracurricular.iloc[0].to_dict()
    else:
        return None
def get_course_extracurricular_details(df, extracurricular_id):
    course_extracurricular = df[df["EXTRACURRICULAR_ID"] == extracurricular_id]
    if not course_extracurricular.empty:
        return course_extracurricular.iloc[0].to_dict()
    else:
        return None
def get_student_extracurricular_participation(df, student_id):
    student_extracurriculars = df[df["STUDENT_ID"] == student_id]
    if not student_extracurriculars.empty:
        return student_extracurriculars[["EXTRACURRICULAR_ID", "PARTICIPATION_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_participation(df, course_id):
    course_extracurriculars = df[df["COURSE_ID"] == course_id]
    if not course_extracurriculars.empty:
        return course_extracurriculars[["STUDENT_ID", "PARTICIPATION_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_feedback(df, student_id):
    student_feedback = df[df["STUDENT_ID"] == student_id]
    if not student_feedback.empty:
        return student_feedback[["EXTRACURRICULAR_ID", "FEEDBACK"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_feedback(df, course_id):         
    course_feedback = df[df["COURSE_ID"] == course_id]
    if not course_feedback.empty:
        return course_feedback[["STUDENT_ID", "FEEDBACK"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_performance(df, student_id):
    student_performance = df[df["STUDENT_ID"] == student_id]
    if not student_performance.empty:
        return student_performance[["EXTRACURRICULAR_ID", "PERFORMANCE"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_performance(df, course_id):
    course_performance = df[df["COURSE_ID"] == course_id]
    if not course_performance.empty:
        return course_performance[["STUDENT_ID", "PERFORMANCE"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_schedule(df, student_id):
    student_schedule = df[df["STUDENT_ID"] == student_id]
    if not student_schedule.empty:
        return student_schedule[["EXTRACURRICULAR_ID", "SCHEDULE"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_schedule(df, course_id):
    course_schedule = df[df["COURSE_ID"] == course_id]
    if not course_schedule.empty:
        return course_schedule[["STUDENT_ID", "SCHEDULE"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_resources(df, student_id):
    student_resources = df[df["STUDENT_ID"] == student_id]
    if not student_resources.empty:
        return student_resources[["EXTRACURRICULAR_ID", "RESOURCE_LINK"]].to_dict(orient="records")
    else:
        return None     
def get_course_extracurricular_resources(df, course_id):
    course_resources = df[df["COURSE_ID"] == course_id]
    if not course_resources.empty:
        return course_resources[["STUDENT_ID", "RESOURCE_LINK"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_notifications(df, student_id):
    student_notifications = df[df["STUDENT_ID"] == student_id]
    if not student_notifications.empty:
        return student_notifications[["EXTRACURRICULAR_ID", "NOTIFICATION"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_notifications(df, course_id):
    course_notifications = df[df["COURSE_ID"] == course_id]
    if not course_notifications.empty:
        return course_notifications[["STUDENT_ID", "NOTIFICATION"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_support(df, student_id):
    student_support = df[df["STUDENT_ID"] == student_id]
    if not student_support.empty:
        return student_support[["EXTRACURRICULAR_ID", "SUPPORT_TICKET"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_support(df, course_id):
    course_support = df[df["COURSE_ID"] == course_id]
    if not course_support.empty:
        return course_support[["STUDENT_ID", "SUPPORT_TICKET"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_achievements(df, student_id):
    student_achievements = df[df["STUDENT_ID"] == student_id]
    if not student_achievements.empty:
        return student_achievements[["EXTRACURRICULAR_ID", "ACHIEVEMENT"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_achievements(df, course_id):
    course_achievements = df[df["COURSE_ID"] == course_id]
    if not course_achievements.empty:
        return course_achievements[["STUDENT_ID", "ACHIEVEMENT"]].to_dict(orient="records")
    else:
        return None     
def get_student_extracurricular_instructors(df, student_id):
    student_instructors = df[df["STUDENT_ID"] == student_id]
    if not student_instructors.empty:
        return student_instructors[["EXTRACURRICULAR_ID", "INSTRUCTOR_NAME"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_instructors(df, course_id):
    course_instructors = df[df["COURSE_ID"] == course_id]
    if not course_instructors.empty:
        return course_instructors[["STUDENT_ID", "INSTRUCTOR_NAME"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_exams(df, student_id):
    student_exams = df[df["STUDENT_ID"] == student_id]
    if not student_exams.empty:
        return student_exams[["EXTRACURRICULAR_ID", "EXAM_SCORE"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_exams(df, course_id):    
    course_exams = df[df["COURSE_ID"] == course_id]
    if not course_exams.empty:
        return course_exams[["STUDENT_ID", "EXAM_SCORE"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_projects(df, student_id):
    student_projects = df[df["STUDENT_ID"] == student_id]
    if not student_projects.empty:
        return student_projects[["EXTRACURRICULAR_ID", "PROJECT_SCORE"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_projects(df, course_id):
    course_projects = df[df["COURSE_ID"] == course_id]
    if not course_projects.empty:
        return course_projects[["STUDENT_ID", "PROJECT_SCORE"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_details(df, extracurricular_id):
    extracurricular = df[df["EXTRACURRICULAR_ID"] == extracurricular_id]
    if not extracurricular.empty:
        return extracurricular.iloc[0].to_dict()
    else:
        return None
def get_course_extracurricular_details(df, extracurricular_id):
    course_extracurricular = df[df["EXTRACURRICULAR_ID"] == extracurricular_id]
    if not course_extracurricular.empty:
        return course_extracurricular.iloc[0].to_dict()
    else:
        return None     
def get_student_extracurricular_participation_status(df, student_id):
    student_extracurriculars = df[df["STUDENT_ID"] == student_id]
    if not student_extracurriculars.empty:
        return student_extracurriculars[["EXTRACURRICULAR_ID", "PARTICIPATION_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_participation_status(df, course_id):
    course_extracurriculars = df[df["COURSE_ID"] == course_id]
    if not course_extracurriculars.empty:
        return course_extracurriculars[["STUDENT_ID", "PARTICIPATION_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_feedback_status(df, student_id):
    student_feedback = df[df["STUDENT_ID"] == student_id]
    if not student_feedback.empty:
        return student_feedback[["EXTRACURRICULAR_ID", "FEEDBACK_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_feedback_status(df, course_id):
    course_feedback = df[df["COURSE_ID"] == course_id]
    if not course_feedback.empty:
        return course_feedback[["STUDENT_ID", "FEEDBACK_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_performance_status(df, student_id): 
    student_performance = df[df["STUDENT_ID"] == student_id]
    if not student_performance.empty:
        return student_performance[["EXTRACURRICULAR_ID", "PERFORMANCE_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_performance_status(df, course_id):
    course_performance = df[df["COURSE_ID"] == course_id]
    if not course_performance.empty:
        return course_performance[["STUDENT_ID", "PERFORMANCE_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_schedule_status(df, student_id):
    student_schedule = df[df["STUDENT_ID"] == student_id]
    if not student_schedule.empty:
        return student_schedule[["EXTRACURRICULAR_ID", "SCHEDULE_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_schedule_status(df, course_id):
    course_schedule = df[df["COURSE_ID"] == course_id]
    if not course_schedule.empty:
        return course_schedule[["STUDENT_ID", "SCHEDULE_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_resources_status(df, student_id):   
    student_resources = df[df["STUDENT_ID"] == student_id]
    if not student_resources.empty:
        return student_resources[["EXTRACURRICULAR_ID", "RESOURCE_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_resources_status(df, course_id): 
    course_resources = df[df["COURSE_ID"] == course_id]
    if not course_resources.empty:
        return course_resources[["STUDENT_ID", "RESOURCE_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_notifications_status(df, student_id):
    student_notifications = df[df["STUDENT_ID"] == student_id]
    if not student_notifications.empty:
        return student_notifications[["EXTRACURRICULAR_ID", "NOTIFICATION_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_notifications_status(df, course_id): 
    course_notifications = df[df["COURSE_ID"] == course_id]
    if not course_notifications.empty:
        return course_notifications[["STUDENT_ID", "NOTIFICATION_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_support_status(df, student_id):
    student_support = df[df["STUDENT_ID"] == student_id]
    if not student_support.empty:
        return student_support[["EXTRACURRICULAR_ID", "SUPPORT_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_support_status(df, course_id):
    course_support = df[df["COURSE_ID"] == course_id]
    if not course_support.empty:
        return course_support[["STUDENT_ID", "SUPPORT_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_achievements_status(df, student_id):
    student_achievements = df[df["STUDENT_ID"] == student_id]
    if not student_achievements.empty:
        return student_achievements[["EXTRACURRICULAR_ID", "ACHIEVEMENT_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_achievements_status(df, course_id):
    course_achievements = df[df["COURSE_ID"] == course_id]
    if not course_achievements.empty:
        return course_achievements[["STUDENT_ID", "ACHIEVEMENT_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_instructors_status(df, student_id):
    student_instructors = df[df["STUDENT_ID"] == student_id]
    if not student_instructors.empty:
        return student_instructors[["EXTRACURRICULAR_ID", "INSTRUCTOR_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_instructors_status(df, course_id):
    course_instructors = df[df["COURSE_ID"] == course_id]
    if not course_instructors.empty:
        return course_instructors[["STUDENT_ID", "INSTRUCTOR_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_exams_status(df, student_id):
    student_exams = df[df["STUDENT_ID"] == student_id]
    if not student_exams.empty:
        return student_exams[["EXTRACURRICULAR_ID", "EXAM_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_exams_status(df, course_id):
    course_exams = df[df["COURSE_ID"] == course_id]
    if not course_exams.empty:
        return course_exams[["STUDENT_ID", "EXAM_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_projects_status(df, student_id):
    student_projects = df[df["STUDENT_ID"] == student_id]
    if not student_projects.empty:
        return student_projects[["EXTRACURRICULAR_ID", "PROJECT_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_course_extracurricular_projects_status(df, course_id):
    course_projects = df[df["COURSE_ID"] == course_id]
    if not course_projects.empty:
        return course_projects[["STUDENT_ID", "PROJECT_STATUS"]].to_dict(orient="records")
    else:
        return None
def get_student_extracurricular_details_status(df, extracurricular_id):
    extracurricular = df[df["EXTRACURRICULAR_ID"] == extracurricular_id]
    if not extracurricular.empty:
        return extracurricular.iloc[0].to_dict()
    else:
        return None
def get_course_extracurricular_details_status(df, extracurricular_id):
    course_extracurricular = df[df["EXTRACURRICULAR_ID"] == extracurricular_id]
    if not course_extracurricular.empty:
        return course_extracurricular.iloc[0].to_dict()
    else:
        return None