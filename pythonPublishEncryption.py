import base64

#encoding user message
userMessage = input("Enter the message to be encrypted")
bytesUserMessage = userMessage.encode('ascii')
base64BytesUserMessage = base64.b64encode(bytesUserMessage)
base64UserMessage = base64BytesUserMessage.decode('ascii')

#decoding user message



keyValue = input ("Enter the key value to encode and decode the message")

