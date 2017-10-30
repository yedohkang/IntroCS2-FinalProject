#! /usr/bin/python
# process account login or registration

import cgitb
cgitb.enable()

import cgi
fromClient = cgi.FieldStorage()

print 'content-type: text/html\n\r'

# start a standards-conforming web page
#import htmlFunctions
# print htmlFunctions.htmlSetup()
#print htmlFunctions.element( True, 0, 'h1', '',
                                  'login system')


# # for debugging, show field names and values from form
# print htmlFunctions.element( True, 0, 'h2', '',
  # 'Show the parts of the FieldStorage structure')
# for name in fromClient:
    # print name + ': ' + fromClient[name].value + '<br>'
# print '<br>'

# field values from form
accountFromForm = fromClient[ 'username'].value
passwordFromForm = fromClient[ 'password'].value

# encrypt the password
# This should be in a separate function to make this 
# main routine shorter and easier to read.
import hashlib
encrypter = hashlib.sha256()
encrypter.update( passwordFromForm)
passwordFromForm_encrypted = encrypter.hexdigest()

# obtain account info from csv file
import hw55_csvToDict
accounts = hw55_csvToDict.csvToDict(
              '/home/support/dholmes/Documents/accounts.csv')
# print accounts

# handle the user's request
if 'login' in fromClient:   # user requested "log me in"
    if accountFromForm in accounts and \
       passwordFromForm_encrypted == accounts[ accountFromForm][ 'password'] :
        print 'welcome back', accounts[ accountFromForm]['owner']
    else: 
        print 'invalid password'
else:   # user requested "sign me up"
    if accountFromForm in accounts:
        print 'not registered because account', \
              repr( accountFromForm), \
              'already exists'
    else: 
        ownerFromForm = accountFromForm + ' owner (someday)'
        import addAccount
        addAccount.addAccount( ownerFromForm,passwordFromForm_encrypted,accountFromForm)
        print """<!DOCTYPE html> \
<html> \
<head> \
	<title> WELCOME! </title> \
	<style> \
	.button {background-color: lightyellow; \
		    border: 5px solid lightblue; \
		    color: black; \
		    padding: 15px 32px; \
		    text-align: center; \
		    text-decoration: none; \
		    display: inline-block; \
		    font-size: 16px; \
		    margin: 4px 2px; \
		    cursor: pointer;} \
			.button:hover {background-color: lightblue;} \
	p {background-color: lightyellow; } \
	p.start {border: 3px green; \
		margin-top:50px; \
		margin-bottom:100px; \
				margin-right:600px; \
				margin-left:600px;} \
</style> \
</head> \
<body style="background-color:lightgreen"> \
<font face="courier"> \
<center>
<p class="start"> <a href="http://clyde.stuy.edu/~madeline.wong/project/majorquiz.html" class="button"> Click HERE to Start the Major Quiz! </a> \
</center> \
</font> \
</body> \
</html> """
     
# end a standards-conforming web page
print htmlFunctions.html_end()