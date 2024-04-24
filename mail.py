mail="sathvikvs12@gmail.com"
password=9876
umail=str(input("enter mailid"))
upassword=int(input("enter password")) 
if(mail == umail):
  if(password == upassword):
    print("Login successfull")
  else:
    print("Login failed due to incorrect password")
else:
  print("Login failed due to incorrect maiil id")
  