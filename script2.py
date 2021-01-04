import time
import requests
import sys
import decimal
varServ = "10.10.173.95"

#Head up, it might take a fine while to wait until port 1337 is open. Give it 5 mins ro run.
def web_request(Serv,Port):
    initport = Port
    finalport = initport
    url = f"http://{Serv}:{Port}"
    while finalport == initport: #If a new port is found, it will exit the loop.
        try:
            r = requests.get(url)
            #print(r.text)
            finalport = r.text.split(" ")[2]
        except: #If you cannot connect, it will retry
            #print(f"Failed to connect. Retrying at {url}")
            time.sleep(1)
    print(r.text)
    return (r.text.split(" "))

def process():
    varPort = 1337
    message = ""
    number = 0
    while varPort != "9765" and message != "STOP":
            v = web_request(varServ,varPort)
            message = v[0] #Looks for the word STOP
            math = decimal.Decimal(v[1])
            varPort = v[2] #Set the next port to connect to.
            if message == "add":
                number = number+math
            if message == "minus":
                number = number-math
            if message == "divide":
                number = number/math
            if message == "multiply":
                number = number*math
            print(f" {v[0]} {math} = {number}")

    print(f"FINISHED! Final Number is {number}")
process()