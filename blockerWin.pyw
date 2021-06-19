import time
from datetime import datetime as dt     

hosts_temp = r"files/hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"      #For Windows, the location of hosts file that can specify blocked sites

redirect = "127.0.0.1"      # default page to show site can’t be reached, usually used by localhost

website_list=[ "www.facebook.com" ,
               "www.instagram.com" ,
               "instagram.com" ,
               "facebook.com" ]     # list of websites to be blocked

presentDT = dt.now()        # the present Date and Time
presentYear = presentDT.year
presentMonth = presentDT.month
presentDay = presentDT.day

startHour = 8       # 8 am
endHour = 16        # 8 pm

startDT = dt( presentYear, presentMonth, presentDay, startHour )      # datetime object of start time
endDT = dt( presentYear, presentMonth, presentDay, endHour )      # datetime object of end time

while True:
    if startDT < presentDT < endDT:             # When between 8 am to 8 pm
        print("Working Hours...")
        with open(hosts_path, 'r+') as file:    # r+ to read and modify file
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
                    
                
    else:                                       # When between 8 pm and 8 am
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)        #sets pointer to start of file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()     #deletes all files after current pointer position
        print("Fun hours")
    print(1)
    time.sleep(5)       # loop every 5 seconds
    
# To automate the task and have it run at starup:
# Go to Task Scheduler on Windows, 
# Create a new task, name it, eg: "Website blocker", check "Run with highest previleges", 
# go to "Triggers" tab in same task window and say Begin the task: "At Startup"
# go to "Actions" tab in same task window, click "New..", 
# select from dropdown "Start a program", and click Browse to locate the pyw file "blockerWin.pyw" #pyw files can execute without manually running on cmd
# go to "Conditions" tab and uncheck "Start the task only if computer is on AC power"

# python loop runs every 5 second and checks if it should block sites or not by the time and modifies host file. 






