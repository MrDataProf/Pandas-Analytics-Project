import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_emails, subject, body):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(receiver_emails)
    message['Subject'] = subject

    # Attach the body to the MIME
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server (in this case, Gmail's SMTP server)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        # Start the TLS connection
        server.starttls()

        # Log in to the email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_emails, message.as_string())

# Example usage:
sender_email = "your_email@gmail.com"
sender_password = "your_email_password"
receiver_emails = ["recipient1@example.com", "recipient2@example.com"]
subject = "Test Email"
body = "This is a test email sent from a Python program."

send_email(sender_email, sender_password, receiver_emails, subject, body)
