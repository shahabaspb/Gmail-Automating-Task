import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# 1️⃣ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=***,
    user="root",
    password="your_app_password_here",
    database="dubai_companies"
)

cursor = conn.cursor()

# 2️⃣ Fetch data from 'indeed' table
cursor.execute("SELECT Name_of_company, email, role FROM indeed")
rows = cursor.fetchall()

# 3️⃣ Email server setup (Gmail)
smtp_server = "smtp.gmail.com"
port = 587
sender_email = "shahabazpb@gmail.com"
password = "your_app_password_here"  # Use Gmail App Password, not your real password

server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(sender_email, password)

# 4️⃣ Loop through rows and send emails
for row in rows:
    name_of_company, recipient_email, role = row

    # Create email
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = f"Application Follow-Up – {role}"

    # Email content
    text = f"""\
Dear Hiring Team at {name_of_company},

I am writing to follow up on my application for the {role}With over two years of experience in business analysis and business intelligence, I have honed my skills in optimizing processes, eliciting requirements, and delivering data-driven solutions across ERP and CRM platforms.

In my role as an Associate Business Intelligence Developer at Excellency Software Consulting, I achieved efficiency gains of 20–35% by automating ETL pipelines, building predictive models, and creating Power BI dashboards for MIS reporting and KPI tracking. My experience also spans requirement elicitation, backlog management, and Agile SDLC execution using tools like Jira, Confluence, and Azure DevOps. I am proficient in Python, SQL, Power BI, and cloud BI platforms such as AWS and Azure.

I am eager to bring my analytic mindset, technical expertise, and collaborative approach to support your team  in achieving its business goals. My resume is attached for your review.

Thank you for considering my application. I would welcome the opportunity to discuss how my skills and experience align with your team’s needs.

Best regards,
Shahabas PB
"""
    message.attach(MIMEText(text, "plain"))

    # Send email
    try:
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

    time.sleep(2)  # Wait 2 seconds to avoid Gmail blocking

# 5️⃣ Close connections
server.quit()
cursor.close()
conn.close()
