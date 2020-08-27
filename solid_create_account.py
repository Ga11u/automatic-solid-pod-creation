import http.client
import mimetypes
import urllib.parse
from http import HTTPStatus

print("Tell me which SOLID provider do you want:")
print("1: solid.community")
print("2: inrupt.net")
try:
    provider = input()
    if provider == "1":
        provider =  "solid.community"
    elif provider == "2":
        provider =  "inrupt.net"
except:
    print("Please enter '1' or '2' only")
    exit()

print("Tell me the username to be used as <username>XX:")
username = input()
print("The username is: "+ username + " and the first account will be " + username+"01")

print("Enter the password:")
password = input()
print("The password is: "+ password)

print("Enter the email:")
email = input()
print("The email is: "+ email)

print("How many accounts do you can to create at: "+provider +"?")
try:
    accounts = int(input())
except:
    print("Please introduce an integer number")
    exit()

print("We are going to create "+ str(accounts)+ " in " + provider + " with the username: " + username + " password: " + password + " email: " + email)
print("Do you want to start? (Enter any key)")
ack = input()


def account_exist(provider,account_name):
    conn = http.client.HTTPSConnection(account_name+'.'+provider)
    payload = ''
    headers = {}
    conn.request("HEAD", "", payload, headers)
    res = conn.getresponse()
    if res.status == HTTPStatus.NOT_FOUND:
        return False
    else:
        print(account_name + " already exists")
        return True

def create_account(provider,account_name,password,email):
    conn = http.client.HTTPSConnection(provider)
    payload = 'username='+account_name+'&password='+password+'&repeat_password='+password+'&name='+account_name+'&email='+email
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    conn.request("POST", "/api/accounts/new", payload, headers)
    res = conn.getresponse()
    if res.status == HTTPStatus.OK or res.status == HTTPStatus.FOUND:
        print("user: "+account_name+ " has been created")
    else:
        print("Error: " + str(res.status))

for n in range(accounts):
    uid = n+1
    if uid < 10:
        uid = "0"+str(uid)
    else:
        uid = str(uid)
    account_name = username + uid
    if not account_exist(provider,account_name):
        create_account(provider,account_name,password,email)

        


