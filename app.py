import pyodbc
from db_config import connection_string

#Connection to the database

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()
conn.commit()

# Add jobs

def add_job():
    ID = input("Enter the JOB ID: ")
    company = input("Enter Company Name: ")
    position = input("Enter Job Position: ")
    status = input("Enter Application Status (Applied, Interview, Offer, Rejected): ")

    cursor.execute("INSERT INTO jobs (ID, company, position, status) VALUES (?, ?, ?, ?)", 
                   (ID, company, position, status))
    conn.commit()
    print("\nJob added successfully!\n")

# View all jobs
def view_jobs():
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()

    if not jobs:
        print("\nNo job applications found.\n")
    else:
        print("\n📌 Job Applications:")
        for job in jobs:
            print(f"ID: {job[0]} | {job[1]} - {job[2]} | Status: {job[3]}")
        print()

# Update job status
def update_status():
    job_id = input("Enter Job ID to update: ")
    new_status = input("Enter new status ")

    cursor.execute("UPDATE jobs SET status = ? WHERE id = ?", (new_status, job_id))
    conn.commit()
    print("\nJob status updated!\n")

# Delete a job
def delete_job():
    job_id = input("Enter Job ID to delete: ")
    cursor.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    conn.commit()
    print("\n Job deleted successfully!\n")

# Menu
while True:
    print("\nJob Applications Tracker")
    print("1️ - Add a Job")
    print("2️ - View Jobs")
    print("3️ - Update Job Status")
    print("4️ - Delete a Job")
    print("5️ - Exit")

    choice = input("\nPick an option: ")

    if choice == "1":
        add_job()
    elif choice == "2":
        view_jobs()
    elif choice == "3":
        update_status()
    elif choice == "4":
        delete_job()
    elif choice == "5":
        print("\nBye!")
        break
    else:
        print("\nInvalid choice, please try again.")

# Close database connection
conn.close()