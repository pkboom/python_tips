# load getpass module
from getpass import getpass

username = input("Enter your username: ")
password = getpass("Enter your password: ")

print('Your username is: ' + username)
print('Your password is: ' + password)
