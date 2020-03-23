useremail = input("Please insert your email: ")
print(useremail)

recipientemaillist = input("Please insert your recipient email list separated by space: ")
recipient_list = recipientemaillist.split()
print("Recipient email list is: ", recipient_list)

followupnumber = int(input("Please insert the number of follow up emails after the initial email: "))
print("You want to send", followupnumber, "follow ups")

emailcontent = input("Please insert the the initial email content: ")
print("Your initial email will be the following: ", emailcontent)

followupcontent = input("Please insert the followup email content: ")
print("Your follow up email content will be the following: ", followupcontent)
