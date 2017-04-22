import base64, imaplib, re
import email

from email_unit import Email

class Emailer(object):
    """docstring for Emailer"""
    def __init__(self, properties):
        self.FROM_EMAIL  = properties["uname"]
        self.FROM_PWD    = properties["password"]
        self.SMTP_SERVER = properties["server"]
        self.SMTP_PORT   = properties["port"]
        self.hello = "world"
        self.emails = []

    def read_mail(self):
        imaplib._MAXLINE = 400000
        self.mail        = imaplib.IMAP4_SSL(self.SMTP_SERVER)
        self.mail.login(self.FROM_EMAIL,self.FROM_PWD)
        self.mail.select('INBOX', readonly=True)

        type, data  = self.mail.search(None, "ALL")
        mail_ids    = data[0]

        self.id_list = mail_ids.split()
        return True

    def process(self):
        for i in self.id_list:
            typ, data = self.mail.fetch( i, '(RFC822)')
            if typ == 'OK':
                for response_part in data:
                    if isinstance(response_part, tuple):
                        raw   = email.message_from_string(response_part[1])
                        curr_email  = Email(raw=raw)
                        curr_email.parse()
        return True

    def get_emails( self ):
        return self.emails