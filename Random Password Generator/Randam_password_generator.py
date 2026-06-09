#Generate a random password
import random
import string

charVal=string.ascii_letters + string.digits + string.punctuation
#list comprehension
pass_len=8
password=""
password="".join([random.choice(charVal) for i in range(pass_len)])
#string method
# for i in range(pass_len):
#  password+=random.choice(charVal)
print(password)
