#! /usr/bin/python
print "content-type: text/html\n"

import cgitb # get the input information
cgitb.enable()

import cgi
fromQS = cgi.FieldStorage ()

# print fromQS

#creates a string of all the user's answer values
new = str(fromQS)

# counts the amount of times the user picked a choice for which college
amtUniversityofPennsylvania = new.count('UniversityofPennsylvania') 
amtBostonCollege = new.count('BostonCollege')

#creates a list with the amount of times each college appears
newlist =[]
newlist.append(amtUniversityofPennsylvania)
newlist.append(amtBostonCollege)

# print max(newlist)
#finds the college with the most appearances
collegename = max(newlist)
collegelistnumber = newlist.index(collegename)
collegelist = ['University of Pennsylvania', 'Boston College']
college = collegelist[collegelistnumber]

link = ["http://www.upenn.edu/", "http://www.bc.edu/"]

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
			<td> <center> <h2> It looks like you will be studying </h2> <h1> Business </h1> 
                        <h2> at </h2> <h1> COLLEGE </h1> </center> </td>
		</tr>
	</table>
	<br>
	<p class="start"> <a href="LINK" class="button"> Click HERE for more information! </a> </p>
	
</font>
</center>
</body>
</html>
'''

#replaces the write college and the corresponding link using its place in thwir lists
finalhtml = html.replace ("COLLEGE", college)
actualfinalhtml = finalhtml.replace ("LINK", link[collegelistnumber])
print actualfinalhtml