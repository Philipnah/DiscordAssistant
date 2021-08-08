# DiscordAssistant
Python script that can do your discord dirty work.

Basically it sends a message for you to whomever your want or whatever server you want, as long as you have the ID for it.

## Guide to get Authorization token
I followed method 2 in this video to get the auth token for your account: https://www.youtube.com/watch?v=WWHZoa0SxCc

When you have the token you should make a .txt file named token.txt and put it in your discord installation folder
In that file you want to write specifically (without the single quotes): 'Token: '
Followed by the token you got from the video. PS: You don't want to share your token with anyone, as it would give them access to your whole account.


## Guide to contacts
For your contacts you should make a .txt file in the same directory as the main.py file called "contacts.txt"
In this file you want to add the name of your contact followed by a colon(':') then the channel or DM id.

### Finding the channel id
You can find the id by pressing "ctrl + shift + i" to open the developper console.
Next click the "Network" tab.
You can now send a message in the channel to get a "messages" entry in the "name" column.
Click on the "messages" entry, and you will find a request URL at the top under "General".
Inside this URL there is a series of digits, which is the ID of that channel.