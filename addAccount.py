def addAccount(name,username,password):
    newcsv = open('/home/students/2018/madeline.wong/public_html/project/nameuserpass.csv','a',0) #opens file and writes in it
    newcsv.write('\n' + name + ',' + username + ',' + password)
    newcsv.close()