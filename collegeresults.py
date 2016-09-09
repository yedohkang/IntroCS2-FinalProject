#! /usr/bin/python
print "content-type: text/html\n"

import cgitb
cgitb.enable()

import cgi
fromQS = cgi.FieldStorage ()

# print fromQS

new = str(fromQS)

amtSocialSciences = new.count('SocialSciences')
amtPreMed =  new.count('PreMed')
amtComputerScience =  new.count('ComputerScience')
amtSciences =  new.count('Sciences')
amtEngineering =  new.count('Engineering')
amtBusiness =  new.count('Business')

newlist =[]
newlist.append(amtSocialSciences)
newlist.append(amtPreMed)
newlist.append(amtComputerScience)
newlist.append(amtSciences)
newlist.append(amtEngineering)
newlist.append(amtBusiness)

# print max(newlist)
majornumber = max(newlist)
majorlistnumber = newlist.index(majornumber)
majorlist = ['Social Sciences', 'PreMed', 'Computer Science', 'Sciences', 'Engineering', 'Business']
major = majorlist[majorlistnumber]

link = ["http://bart.stuy.edu/~madeline.wong/project/SocialSciencesquiz.html", "http://bart.stuy.edu/~madeline.wong/project/PreMedquiz.html", "http://bart.stuy.edu/~madeline.wong/project/ComputerSciencequiz.html", "http://bart.stuy.edu/~madeline.wong/project/Sciencesquiz.html", "http://bart.stuy.edu/~madeline.wong/project/Engineeringquiz.html", "http://bart.stuy.edu/~madeline.wong/project/Businessquiz.html"]

html = '''
<!DOCTYPE html>
<html>
<head>
	 <title> RESULTS!! </title>
	 <style>
	 table.major {
		width: 40%;
		margin-left: 30%;
		margin-right: 30%;
		table-layout: fixed;
		border-collapse: collapse;
		border: 5px solid lightblue;
		background-color: lightyellow;
	}
	.button {background-color: lightyellow;
		    border: 10px solid #EAADEA;
		    color: black;
		    padding: 15px 32px;
		    text-align: center;
		    text-decoration: none;
		    display: inline-block;
		    font-size: 16px;
		    margin: 8px 4px;
		    cursor: pointer;}
			.button:hover {background-color: #EAADEA;}
	</style>
</head>
<body style="background-color:lightgreen">
<font face="courier">
<center>
	<br>
	<br>
	<table class="major"> 
		<tr>
			<td> <center> <h2> Your top potential major is: </h2> <h1> MAJOR </h1> </center> </td>
		</tr>
	</table>
	<br>
	<p class="start"> <a href="LINK" class="button"> Click HERE to Start the Questionnaire! </a> </p>
	
</font>
</center>
</body>
</html>
'''

finalhtml = html.replace ("MAJOR", major)
finalhtml = html.replace ("LINK", link[majorlistnumber])
print finalhtml