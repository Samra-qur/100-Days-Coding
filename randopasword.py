import random
import string

#Greet the user
print("Hello, Welcome to random password generator program! .")

length=int(input("\n Enter the length of password !"))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
punct=string.punctuation
all=lower+upper+digits+punct

temp=random.sample(all,length)
p="".join(temp)
print(p)