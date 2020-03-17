import requests
username = ""
url = ""
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
def sendMsg(message):
	data = {"username": ""+username+"", "content": ""+message+""}
	r = requests.post(url, json=data, headers=headers)
	return

while True:
	message = input("Msg: ")
	sendMsg(message)

