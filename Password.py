message = {"name" : "İlknur", "pasword": "mystery_python"}
name = input("Please enter your first name : ")
if name in message["name"]:
  print("Hello {}! , The pasword is : {}".format(name, message["pasword"]))
else:  # name not in message["name"]
  print("Hello {}, see you later.". format(name))
