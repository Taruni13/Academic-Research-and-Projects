import pandas as pd
from faker import Faker
import random

fake = Faker()

# Read column headers from data.csv (do not overwrite it)
df = pd.read_csv("data.csv", nrows=0)
columns = df.columns.tolist()

num_rows = 100  # Number of fake rows to generate

def fake_value(col):
    col_lower = col.lower()
    if col_lower == "curr_1_1_majr_desc":
        return random.choice([
            "Business Administration",
            "Finance",
            "Accounting",
            "Marketing",
            "Management",
            "Economics",
            "International Business",
            "Entrepreneurship",
            "Business Analytics",
            "Human Resource Management"
        ])
    elif col_lower == "curr_2_degc_desc":
        return random.choice([
            "",
            "MBA",
            "MS in Business Analytics",
            "MS in Finance",
            "JD",
            "MA in Economics"
        ])
    elif "first" in col_lower and "name" in col_lower:
        return fake.first_name()
    elif "last" in col_lower and "name" in col_lower:
        return fake.last_name()
    elif "email" in col_lower:
        return fake.email()
    elif "gpa" in col_lower:
        return round(random.uniform(2.0, 4.0), 2)
    elif "levl_code" in col_lower:
        return random.choice(["UG", "GR"])
    elif "clas_code" in col_lower:
        return random.choice(["FR", "SO", "JR", "SR"])
    elif "sprt_1_desc" in col_lower:
        return random.choice([
            "", "Men's Water Polo", "Soccer", "Basketball", "Tennis"
        ])
    elif "term_desc" in col_lower:
        return random.choice([
            "Fall 2022", "Spring 2023", "Fall 2023", "Spring 2024"
        ])
    elif "advr_1_fmil" in col_lower:
        return random.choice([
            "Dr. Brown", "Dr. Smith", "Prof. Lee", "Dr. Johnson"
        ])
    elif "id" in col_lower:
        return fake.unique.random_number(digits=8)
    elif "credit_hr_this_term" in col_lower:
        return random.randint(12, 18)
    elif "ovrl_hrs_earned" in col_lower:
        return random.randint(30, 120)
    else:
        return fake.word()

data = []
for _ in range(num_rows):
    row = [fake_value(col) for col in columns]
    data.append(row)

fake_df = pd.DataFrame(data, columns=columns)
fake_df.to_csv("students_fake.csv", index=False)
print("Fake data written to students_fake.csv")