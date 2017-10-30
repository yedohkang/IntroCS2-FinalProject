#! /usr/bin/python
print "content-type: text/html\n\r"

import cgitb
cgitb.enable()

import cgi
fromQS = cgi.FieldStorage ()

# print fromQS

new = str(fromQS)

#counts the amount of times the user chose a choice corresponding to the major
amtSocialSciences = new.count('SocialSciences')
amtPreMed =  new.count('PreMed')
amtComputerScience =  new.count('ComputerScience')
amtSciences =  new.count('Sciences')
amtEngineering =  new.count('Engineering')
amtBusiness =  new.count('Business')

#converts string to list
newlist =[]
newlist.append(amtSocialSciences)
newlist.append(amtPreMed)
newlist.append(amtComputerScience)
newlist.append(amtSciences)
newlist.append(amtEngineering)
newlist.append(amtBusiness)

# finds the place of the biggest number and uses that in a list with the same order of majors and finds the major
# print max(newlist)
majornumber = max(newlist)
majorlistnumber = newlist.index(majornumber)
majorlist = ['Social Sciences', 'PreMed', 'Computer Science', 'Sciences', 'Engineering', 'Business']
major = majorlist[majorlistnumber]

#finds the links for the next step once you have your major
link = ["http://clyde.stuy.edu/~yedoh.kang/project/SocialSciencesquiz.html", "http://clyde.stuy.edu/~yedoh.kang/project/PreMedquiz.html", "http://clyde.stuy.edu/~yedoh.kang/project/ComputerSciencequiz.html", "clyde://bart.stuy.edu/~yedoh.kang/project/Sciencesquiz.html", "http://clyde.stuy.edu/~yedoh.kang/project/Engineeringquiz.html", "http://clyde.stuy.edu/~yedoh.kang/project/Businessquiz.html"]

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
actualfinalhtml = finalhtml.replace ("LINK", link[majorlistnumber])
print actualfinalhtml
# print major