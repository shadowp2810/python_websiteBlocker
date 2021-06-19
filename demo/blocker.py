import time
from datetime import datetime as dt     

hosts_temp = "files/hosts"      # modifies hosts file in files folder to test modification of file
# hosts_path = "/private/etc/hosts"                          #For Mac and Linux
# hosts_path = r"C:\Windows\System32\drivers\etc\hosts"      #For Windows


redirect = "127.0.0.1"      # default page to show site can’t be reached, usually used by localhost

website_list=[ "www.facebook.com" ,
               "www.instagram.com" ,
               "instagram.com" ,
               "facebook.com" ]     # list of blocked sites

presentDT = dt.now()        # the present Date and Time
presentYear = presentDT.year
presentMonth = presentDT.month
presentDay = presentDT.day

startHour = 8       # 8 pm 
endHour = 16        # 8 pm

startDT = dt( presentYear, presentMonth, presentDay, startHour )      #datetime object of start time
endDT = dt( presentYear, presentMonth, presentDay, endHour )      #datetime object of end time

while True:                                     
    if startDT < presentDT < endDT:                             # Between 8 am and 8 pm
        print("Working Hours...")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
                    
                
    else:                                                       # Between 8 pm and 8 am
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)        #sets pointer to start of file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()     #deletes all files after current pointer position
        print("Fun hours")
    print(1)
    time.sleep(5)       # loop every 5 seconds
    
    
# To automate this task and have it run at startup:
# go to Terminal and type in without quotes "sudo crontab -e"
# at the bottom of file type in without quotes "@reboot python3 <Complete directory location of python script>"
# eg: @reboot python3 /Desktop/scripts/blocker.py
# exit by pressing cntrl and X keys together

# python loop runs every 5 second and checks if it should block sites or not by the time and modifies host file. 

# If not working for firefox enter without quotes "about:config" in address bar
# then search without quotes for boolean value named: "browser.fixup.dns_first_for_single_words"
# set it to true.