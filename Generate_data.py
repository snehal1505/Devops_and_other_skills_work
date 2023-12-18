import csv
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker('en_IN')  # Setting Faker to generate Indian names and locations

# Custom function to generate a four-digit job ID
def generate_job_id():
    return f'{random.randint(1000, 9999)}'

# Generate job titles specific to IT professionals
def generate_it_job_title():
    it_job_titles = ['Software Engineer', 'Data Analyst', 'Network Administrator', 'Web Developer', 'IT Support Specialist']
    return random.choice(it_job_titles)

def generate_other_department_job_title():
    other_dept_job_titles = ['Marketing Manager', 'HR Coordinator', 'Finance Analyst', 'Operations Supervisor', 'Sales Executive']
    return random.choice(other_dept_job_titles)

# Custom function to generate Indian city names
def generate_indian_city():
    indian_cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Kolkata', 'Pune', 'Jaipur', 'Ahmedabad', 'Lucknow']
    return random.choice(indian_cities)

# Custom function to generate Indian names
def generate_indian_name():
    return fake.name()

# Generate dummy data for Time to Fill metric
def generate_time_to_fill_data(num_records):
    time_to_fill_data = []
    for _ in range(num_records):
        open_date = fake.date_between(start_date='-90d', end_date='today')  # Random open date within the last 90 days
        acceptance_date = open_date + timedelta(days=random.randint(10, 60))  # Acceptance date within 10 to 60 days
        onboarding_date = acceptance_date + timedelta(days=random.randint(7, 14))  # Onboarding starts within 7 to 14 days after acceptance
        start_date = onboarding_date + timedelta(days=random.randint(1, 7))  # Start date after onboarding

        # Generate interview dates for different levels
        level1_interview_date = fake.date_between(start_date=open_date, end_date=acceptance_date).strftime('%Y-%m-%d')
        level2_interview_date = fake.date_between(start_date=open_date, end_date=acceptance_date).strftime('%Y-%m-%d')
        hr_interview_date = fake.date_between(start_date=open_date, end_date=acceptance_date).strftime('%Y-%m-%d')
        # Randomly select department
        department = random.choice(['IT', 'Marketing', 'HR', 'Finance', 'Operations', 'Sales'])
        data = {
            'Job ID': generate_job_id(),
            'Job Title': generate_it_job_title(),
            'Department': department,  # Assuming all jobs are in the IT department
            'Location': generate_indian_city(),
            'Hiring Manager': generate_indian_name(),
            'Recruiter': generate_indian_name(),
            'Job Description': fake.text(),
            'Open Date': open_date.strftime('%Y-%m-%d'),
            'Close Date': (open_date + timedelta(days=random.randint(30, 90))).strftime('%Y-%m-%d'),  # Close date within 30 to 90 days
            'Number of Applicants': random.randint(20, 100),
            'Shortlisted Candidates': random.randint(5, 20),
            'Level 1 Interview Date': level1_interview_date,
            'Level 2 Interview Date': level2_interview_date,
            'HR Discussion Date': hr_interview_date,
            'Offer Date': (acceptance_date - timedelta(days=random.randint(0, 5))).strftime('%Y-%m-%d'),
            'Acceptance Date': acceptance_date.strftime('%Y-%m-%d'),
            'Onboarding Start Date': onboarding_date.strftime('%Y-%m-%d'),
            'Selection Date': fake.date_between(start_date=acceptance_date, end_date=onboarding_date).strftime('%Y-%m-%d'),
            'Start Date': start_date.strftime('%Y-%m-%d'),
            'Time to Fill (in days)': (acceptance_date - open_date).days,
            'Reason for Rejection': fake.sentence() if random.random() < 0.3 else None,
            'Feedback from Interviewers': fake.paragraph() if random.random() < 0.5 else None,
        }
        time_to_fill_data.append(data)

    return time_to_fill_data

# Save Time to Fill data to a CSV file
def save_to_csv(data, filename):
    keys = data[0].keys() if data else []
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

# Example usage: Generate 20 records for Time to Fill and save to a CSV file
time_to_fill_records = generate_time_to_fill_data(200)
save_to_csv(time_to_fill_records, 'time_to_fill_data.csv')
