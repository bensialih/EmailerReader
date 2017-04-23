import unittest

from emailer import Emailer
from email_unit import Email
import properties

class TestEmailParser(unittest.TestCase):
	
	def setUp(self ):
		props = properties.get_properties()
		self.emailer = Emailer(props)

 	def test_login_to_account(self):
 		# print('login worked')
 		self.assertTrue(self.emailer.read_mail())

 	def test_get_mail(self):
 		# print('login worked')
 		self.emailer.read_mail()
 		self.emailer.process()
 		emails = self.emailer.get_emails()
 		self.assertTrue(len(emails) == 5)

 	def test_email_init(self):
 		email = Email(raw="Hello Emailer")
 		email.get_raw_email()




if __name__ == '__main__' :
	unittest.main()