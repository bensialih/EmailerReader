import unittest

from emailer import Emailer
from email_unit import Email

class TestEmailParser(unittest.TestCase):
	
	def setUp(self ):
		self.emailer = Emailer()

 	def test_login_to_account(self):
 		# print('login worked')
 		self.assertTrue(self.emailer.read_mail())

 	def test_get_mail(self):
 		# print('login worked')
 		self.emailer.read_mail()
 		self.assertTrue(self.emailer.process())

 	def test_email_init(self):
 		email = Email(raw="Hello world")
 		print(email.get_raw_email())

 	


if __name__ == '__main__' :
	unittest.main()