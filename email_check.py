max_email_input_tries = 3
tries = 0

user_login_email = int(input("Please enter you email address"))
email = 123


while (not(user_login_email == email or tries == max_email_input_tries)):
  if (tries < 3):
    print ("The email address was incorrect")
  user_login_email = int(input("Please enter you email address"))
  tries = tries + 1

if (user_login_email == email):
  print ("You have written the correct email")

else:
  print ("You have exceeded the amount of max tries")
