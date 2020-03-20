max_email_input_retries = 3
retries = 0

user_login_email = int(input("Please enter you email address"))
email = 123


while (not(user_login_email == email or retries >= max_email_input_retries)):
  if (retries < 3):
    print ("The email address was incorrect")
  user_login_email = int(input("Please enter another email address"))
  retries = retries + 1

if (user_login_email == email):
  print ("You have written an correct email")

else:
  print ("You have exceeded the amount of max retries")
