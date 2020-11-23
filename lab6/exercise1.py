true_email= "ceng113@example.com"

email= input("Enter your email address: ")
email= email.lower()

indx= email.index("@")
before_str= email[0:indx]
before_str= before_str.replace(".", "")

email= before_str + email[indx:]

print(email==true_email)

 
