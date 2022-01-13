import requests

receiver = "" #Phone Number Ex. +66615699342
text = "" #Your message

x = requests.post("https://textbelt.com/text",{
			'phone' : receiver,
			'message' : text ,
			'key' : 'textbelt'
		})

print(x.text)