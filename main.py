import requests

# Set this to your path to Discord
path2DiscordToken = r"C:\Users\phili\AppData\Local\Discord\token.txt"

# enter the message you want to send here
message = "cs?"

# the names of people you have put in your contacts
contactList = ["Fredrik", "Dyrving", "Morten"]

def GetToken(path):

	# Follow read.me guide for getting your authorization token set up
	with open(path, 'r') as f:
		lines = f.readlines()
		
		for line in lines:
			if "Token:" in line:
				authToken = line[7:]

	return authToken

def GetChannelIDs():
	with open("contacts.txt", "r") as f:
		receivers = f.readlines()

	contactIDs = []

	for receiver in receivers:
		for name in contactList:
			if name in receiver:

				# -19 removes everything but the ID and \n, -1 removes \n
				contactIDs.append(receiver[-19:-1])
				
	return contactIDs


token = GetToken(path2DiscordToken)
contactIDs = GetChannelIDs()


payload = {
	"content": message
}

header = {
	"authorization": token
}


	
for id in contactIDs:
	r = requests.post("https://discord.com/api/v9/channels/" + id + "/messages", data=payload, headers=header)

