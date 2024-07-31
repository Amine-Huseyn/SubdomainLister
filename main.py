import requests

def make_requests(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_input = "google.com"

with open ("subdomain.txt", "r") as subdomain_list :
    for word in subdomain_list :
        word = word.strip()
        url = " http://" +  word + "." + target_input
        response = make_requests(url)
        if response:
            print("Found subdomain ----> " + url)