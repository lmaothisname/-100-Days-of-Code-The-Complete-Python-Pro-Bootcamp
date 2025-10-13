import os
from twilio.rest import Client
import smtplib
# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.email = os.environ["MY_EMAIL"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
        self.twiilio_virtual_number = os.environ["TWILIO_VIRTUAL_NUMBER"]
        self.twiilio_whatsapp_number = os.environ["TWILIO_WHATSAPP_NUMBER"]
        self.connection = smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"])
    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_VIRTUAL_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}'
        )
        print(message.sid)
    def send_email(self,email_list,email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email,self.email_password)
            for email in email_list:
                self.connection.sendmail(from_addr=self.email,to_addrs=email,msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8'))
