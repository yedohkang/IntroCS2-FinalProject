#! /usr/bin/python
# process account login or registration

import cgitb
cgitb.enable()

import cgi
fromClient = cgi.FieldStorage()

print 'content-type: text/html\n\r'

# start a standards-conforming web page
import htmlFunctions
print htmlFunctions.htmlSetup()
#print htmlFunctions.element( True, 0, 'h1', '',
 #                                 'login system')


# # for debugging, show field names and values from form
# print htmlFunctions.element( True, 0, 'h2', '',
  # 'Show the parts of the FieldStorage structure')
# for name in fromClient:
    # print name + ': ' + fromClient[name].value + '<br>'
# print '<br>'

# field values from form
accountFromForm = fromClient[ 'username'].value
passwordFromForm = fromClient[ 'password'].value
buttonFromForm = fromClient['userAction'].value

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
              '/home/students/2018/madeline.wong/public_html/project/nameuserpass.csv')
# print accounts

# handle the user's request
if buttonFromForm == "Login": # user requested "log me in"
    if accountFromForm in accounts and \
       passwordFromForm_encrypted == accounts[ accountFromForm][ 'password'] :
        print """ <!DOCTYPE html> \
<html> \
<head> \
	<title> WELCOME BACK </title> \
	<style> \
	.button {background-color: lightyellow; \
		    border: 5px solid lightblue; \
		    color: black;\
		    padding: 15px 32px;\
		    text-align: center; \
		    text-decoration: none; \
		    display: inline-block; \
		    font-size: 16px; \
		    margin: 4px 2px; \
		    cursor: pointer;} \
			.button:hover {background-color: lightblue;} \
	p {background-color: lightyellow; } \
	p.start {border: 3px green;\
		margin-top:50px; \
		margin-bottom:100px;\
		margin-right:600px; \
		margin-left:600px;} \
	table.welcome { \
					width: 30%; \
					margin-left: 35%; \
					margin-right: 35%; \
					table-layout: fixed; \
					border-collapse: collapse; \
					border: 6px solid lightblue; \
					background-color: lightyellow; \
				} \
	table.instructions { \
					width: 60%; \
					margin-left: 20%; \
					margin-right: 20%; \
					table-layout: fixed; \
					border-collapse: collapse; \
					border: 5px solid lightyellow; \
					background-color: #EAADEA; \
				} \
				table.retake { \
								width: 30%; \
								margin-left: 35%; \
								margin-right: 35%; \
								table-layout: fixed; \
								border-collapse: collapse; \
								border: 5px solid lightyellow; \
								background-color: lightblue; \
							} \
				p {background-color: lightgreen; } \
</style> \
</head> \
<body style="background-color:lightgreen"> \
<font face="courier"> \
<center> \
<br> \
<br>  \
<table class="welcome"> \
	<tr> \
		<td > <center> <h1> Welcome back! </h1> </center></td> </tr> </table> \
<br><br><br> \
<table class="instructions"> \
	<tr> \
		<td > <center><h2> Your information has probably changed since the last time you visited. </h2>
</center> </td> </tr> </table> \
<br> \
<br> \
<br> \
<table class="retake"> \
	<tr> \
		<td> <center> \
<h3> Let's take the quiz again! </h3> </center> </td> </tr> </table> \
<p class="start"> <a href="http://clyde.stuy.edu/~yedoh.kang/project/majorquiz.html" class="button"> Click HERE to Start the Major Quiz! </a> \
</center> \
</font> \
</body> \
</html>"""
    else: 
          print """<!DOCTYPE html> \
<html> \
<head> \
	<title> SORRY :( </title> \
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
<center> \
<br> \
<br> \
<h1> You seemed to have entered in the wrong information! <h1>
<p class="start"> <a href="http://clyde.stuy.edu/~yedoh.kang/project/login.html" class="button"> Click HERE to Try Again! </a> \
</center> \
</font> \
</body> \
</html> """
# if buttonFromForm == "Login": # user requested "log me in"
 #  print "hi"
#   if accountFromForm in accounts:
  #     print "part1 is working"
     #  if passwordFromForm_encrypted == accounts[ accountFromForm][ 'password'] :
  #         print "part2 is working"
else:   # user requested "sign me up"
    if accountFromForm in accounts:
        print """<!DOCTYPE html> \
<html> \
<head> \
	<title> SORRY :( </title> \
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
<center> \
<br> \
<br> \
<h1> Hi, someone has already made an account with your username! </h1> \
<p class="start"> <a href="http://clyde.stuy.edu/~yedoh.kang/project/login.html" class="button"> Click HERE to Register Again! </a> \
</center> \
</font> \
</body> \
</html> """
    else: 
        nameFromForm = fromClient[ 'name'].value
        ownerFromForm = accountFromForm 
        import addAccount
        addAccount.addAccount( ownerFromForm,passwordFromForm_encrypted,accountFromForm)
        finalhtml = """<!DOCTYPE html> \
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
<center> \
<br> \
<br> \
<h1> NAME, you have been successfully logged in! </h1> \
<p class="start"> <a href="http://clyde.stuy.edu/~yedoh.kang/project/majorquiz.html" class="button"> Click HERE to Start the Major Quiz! </a> \
</center> \
</font> \
</body> \
</html> """
      #  print htmlgood
        actualfinalhtml = finalhtml.replace("NAME", nameFromForm)
        print actualfinalhtml

     
# end a standards-conforming web page
print htmlFunctions.html_end()