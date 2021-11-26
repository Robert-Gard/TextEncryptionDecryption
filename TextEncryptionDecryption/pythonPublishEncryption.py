import base64
import time

#encoding user message
userMessage = input("Enter the message to be encrypted  ")
savedMessage = open ('savedMessage.txt', 'w')
savedMessage.write(userMessage)
savedMessage.close()


while True:
    keyValue = input ("Enter the key value to encode and decode the message (ascii,UTF-8)  ")
    if "ascii" in keyValue:
        bytesUserMessage = userMessage.encode('ascii')
        base64BytesUserMessage = base64.b64encode(bytesUserMessage)
        base64UserMessage = base64BytesUserMessage.decode('ascii')
        print(base64UserMessage)
        break
    elif "UTF-8" in keyValue.upper():
        bytesUserMessage = userMessage.encode('UTF-8')
        base64BytesUserMessage = base64.b64encode(bytesUserMessage)
        base64UserMessage = base64BytesUserMessage.decode('UTF-8')
        print(base64UserMessage)
        break
    
    input ("That was not a valid key word, press enter to try again.  ")
    

time.sleep(1)
savedValue = open ('savedValue.txt', 'w')
savedValue.write(keyValue)
savedValue.close()

print("We will now decrypt the message", end = '')
time.sleep(1)
print(".", end = '')
time.sleep(1)
print(".", end = '')
time.sleep(1)
print(".  ", end = '')
time.sleep(1)


if "ascii" in keyValue:
        base64BytesUserMessage = base64UserMessage.encode('ascii')
        bytesUserMessage = base64.b64decode(base64BytesUserMessage)
        userMessage = bytesUserMessage.decode('ascii')
        print(userMessage)

if "UTF-8" in keyValue.upper():
        base64BytesUserMessage = base64UserMessage.encode('UTF-8')
        bytesUserMessage = base64.b64decode(base64BytesUserMessage)
        userMessage = bytesUserMessage.decode('UTF-8')
        print(userMessage)



