def sathvik():
  return "This is sathvik bank balence"

def mx():
  return "This is mx bank balence"

test_dict1={"fname": sathvik ,"age": 50,"address":"salem"}
test_dict2={"fname": mx ,"age": 100,"address":"banglore"}

print("The original dictonary is :"+str(test_dict1))
print("The original dictonary is :"+str(test_dict2))

res1=test_dict1['fname']()
res2=test_dict2['age']

print("The required call result :"+str(res1))
print("The required call result :"+str(res2)) 