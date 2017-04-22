import base64, imaplib, re
import email

from email_unit import Email

import properties

imaplib._MAXLINE = 400000

props = properties.get_properties()
FROM_EMAIL  = props["uname"]
FROM_PWD    = props["password"]
SMTP_SERVER = props["server"]
SMTP_PORT   = props["port"]

class Emailer(object):
    """docstring for Emailer"""
    def __init__(self):
        self.hello = "world"
        self.emails = []

    def read_mail(self):
        self.mail        = imaplib.IMAP4_SSL(SMTP_SERVER)
        self.mail.login(FROM_EMAIL,FROM_PWD)
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

                        # self.emails.append(curr_email)

                        # print(response_part[1])
                        # print('response_part')
                return True
                # self.emails = data[0][1]
        return True

    def get_emails( self ):
        return self.emails