text = str(input("Please write a text."))

if len(text) > 0 and len(text) <= 250:
  print(text)

else:
  if len(text) == 0:
    print("Please write a text.")
  else:
    if len(text) > 250:
      print("Your text is too long.")
  
