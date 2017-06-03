import re, base64
import email
import re

from bs4 import BeautifulSoup

from email.parser import Parser
parser = Parser()

class Email(object):
	"""docstring for Email"""
	def __init__(self, **email_props ):
		super(Email, self).__init__()
		for key, prop in email_props.items():
			setattr(Email, key, prop)

	def get_raw_email(self):
		return self.raw

	def get_formatted_body(self):
		return self.body

	def parse(self):
		encrypt = re.search("base64",str(self.raw))
		if encrypt:
			f1 			= re.split('(base64*)', str(self.raw))
			self.body 	= base64.b64decode(f1[2])
			self.body 	= re.sub(r'[^\x00-\x7F]+',' ', self.body )

		else:
			try:
				if( type(self.raw) is not str ):
					self.raw = str(self.raw)

				raw = BeautifulSoup( self.raw , 'html.parser')
				self.body = raw.body.get_text()
			except Exception as e:
				raise e