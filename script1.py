from base64 import b64decode

f = open("b64.txt","r").read()
r = "SGVsbG8sIFdvcmxkIQ=="



def decode(string):
    decoded = b64decode(string)
    return (decoded)

def loop(number,string):
    statment = string
    for i in range(0,number):
        statment = decode(statment)
    return statment

print(loop(50,f))
#print(decode(r))



