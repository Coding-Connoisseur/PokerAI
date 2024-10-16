"""
email_notifier.py

Sends email notifications for notable bot events, such as large wins, cashouts,
or errors, using an email server configuration.

Classes:
- EmailNotifier: Manages email notification sending.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailNotifier:
    def __init__(self, smtp_server, port, username, password):
        """
        Initializes EmailNotifier with email server details.

        Args:
            smtp_server (str): SMTP server address.
            port (int): Port for the SMTP server.
            username (str): Email server username.
            password (str): Email server password.
        """
        pass

    def send_email(self, recipient, subject, body):
        """
        Sends an email notification to the specified recipient.

        Args:
            recipient (str): Email address of the recipient.
            subject (str): Subject line of the email.
            body (str): Body content of the email.

        Returns:
            None

        Logic:
        - Create an email message with subject and body.
        - Connect to SMTP server and send the email.
        """
        pass
