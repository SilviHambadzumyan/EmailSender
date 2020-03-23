max_login_input_retries = 2
retries = 0


login_list = ['amana', 'gonama', 'kanhs', 'tavcd']
 
user_login = str(input("Please enter your login"))

 
while (not(user_login in login_list or retries >= max_login_input_retries)):
  if (retries < 2):
    print ("The login was incorrect")
  user_login = str(input("Please enter another login"))
  retries = retries + 1

if (user_login in login_list):
  print ("You have written a correct login")

else:
  print ("You have exceeded the amount of max retries")
