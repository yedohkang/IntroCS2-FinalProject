#! /usr/bin/python
print "content-type: text/html\n\r"

import cgitb
cgitb.enable()

import cgi
fromQS = cgi.FieldStorage ()

# print fromQS

new = str(fromQS)

#finds the amount of times each college was chosen for a major
amtStanfordUniversity = new.count('StanfordUniversity')
amtCarnegieMellonUniversity = new.count('CarnegieMellonUniversity')

#makes a list of the number of times each college was chosen
newlist =[]
newlist.append(amtStanfordUniversity)
newlist.append(amtCarnegieMellonUniversity)

# print max(newlist)

#uses that number to find the college in the corresponding list
collegename = max(newlist)
collegelistnumber = newlist.index(collegename)
collegelist = ['Stanford University', 'CarnegieMellonUniversity']
college = collegelist[collegelistnumber]

#list of links for the college received
link = ["https://www.stanford.edu/", "http://www.cmu.edu/"]

#html
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
			<td> <center> <h2> It looks like you will be studying </h2> <h1> Computer Science </h1> 
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

finalhtml = html.replace ("COLLEGE", college)
actualfinalhtml = finalhtml.replace ("LINK", link[collegelistnumber])
print actualfinalhtml