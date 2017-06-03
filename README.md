# EmailerReader
Reads emails,ready to be used


### Installation
Clone
install dependancies
 -> run: pip install -r requirements.txt
copy & paste into properties.py the following

def get_properties():
	vars = {}
	vars['uname'] = "test@myemail.co.uk"
	vars['password'] = "mypassword"
	vars['server'] = "mail.server.co.uk"
	vars['port']	= "993"
	return vars

### Using
Please change the Username, Password & server deatils listed in properties.py
See email_parse_test.py for how to use

	props = properties.get_properties()
	emailer = Emailer(props)
	emails = emailer.read_mail()

### ToDo
tests need to be passing