import os

excluded_list = ["config.py", "file_detector.py", "send_mail.py", "README.md", ".env"]
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
email_password = os.getenv("EMAIL_PASSWORD")