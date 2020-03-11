#python code
email_title = "HW submission"
email_sander = "smnatsakanyan@aua.am"
email_receiver = "anna_alaverdyan2@edu.aua.am"
unsubscribe = 0
 
email_reply= int (input("Please input the number of replies"))
 
if (email_reply>=1):
 print("You have a reply")
else:
 unsubscribe = input("unsubscribe? please type yes or no")
 if (unsubscribe == "yes"):
   print("Junk")
 else:
   email_sent = int (input("Please input the number of emails"))
   if (email_sent < 2):
     print ("send another email")
   else:
     print("Junk")
