import re, base64
import email

class Email(object):
	"""docstring for Email"""
	def __init__(self, **email_props ):
		super(Email, self).__init__()
		for key, prop in email_props.items():
			setattr(Email, key, prop)

	def get_raw_email(self):
		return self.raw

	def parse(self):
		encrypt = re.search("base64",str(self.raw))
		if encrypt:
			f1 = re.split('(base64*)', str(self.raw))
			# print(f1)
			self.body = base64.decodestring(f1[2])
			print( self.body )
		else:
			# print(self.raw)
			self.body = email.message_from_string(self.raw)
			print(self.body)
		