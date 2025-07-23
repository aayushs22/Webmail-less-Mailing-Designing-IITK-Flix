import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(sender_email, sender_password, recipient_email, subject, body, cc=None, bcc=None, attachments=None):
    # SMTP server configuration
    smtp_server = 'mmtp.iitk.ac.in'
    smtp_port = 25

    # Create a message container
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Add CC and BCC if provided
    if cc:
        message['Cc'] = cc
    if bcc:
        message['Bcc'] = bcc

    # Attach body text
    message.attach(MIMEText(body, 'plain'))

    # Attachments
    if attachments:
        for attachment in attachments:
            with open(attachment, 'rb') as file:
                part = MIMEApplication(file.read(), Name=attachment)
                part['Content-Disposition'] = f'attachment; filename="{attachment}"'
                message.attach(part)

    # Establish a connection to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Use TLS encryption
        server.login(sender_email, sender_password)  # Authenticate

        # Send email
        server.sendmail(sender_email, [recipient_email] + (cc.split(',') if cc else []) + (bcc.split(',') if bcc else []), message.as_string())

if _name_ == "_main_":
    # Replace with your own email and password
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'

    recipient_email = 'friend@example.com'
    subject = 'Test Email'
    body = 'Hello, this is a test email sent from my Python script.'
    cc = 'cc_recipient@example.com'
    bcc = 'bcc_recipient@example.com'
    attachments = ['file1.txt', 'file2.pdf']  # Add file paths as needed

    send_email(sender_email, sender_password, recipient_email, subject, body, cc, bcc, attachments)