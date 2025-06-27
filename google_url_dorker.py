# inurl:"/xmlrpc.php?rsd" & ext:php
from googlesearch import search
import argparse

parser = argparse.ArgumentParser(description="Tool to extract URLs using Google Dork. "+"""python3 google_dorker.py --dork 'inurl:"/xmlrpc.php?rsd" & ext:php' --count 50""")
parser.add_argument('-d', '--dork',required=True, help="Google dork query")
parser.add_argument('-c', '--count', default=10, type=int, help="Number of URLs to fetch (default: 10)")
parser.add_argument('-w', '--write', type=str, help="Save results to a text file")
parser.add_argument('-x', '--examples', action='store_true', help="Show usage examples and Contacts")

args = parser.parse_args()


links = []

# To bypass Google blocks, you can use a proxy:
# proxy = 'YOUR_HTTPS_PROXY'

def dorksearch(query, count):
    # Add 'proxy=proxy' if you want to use a proxy to avoid rate limits
    res = search(query, num_results=count, timeout=22) # ← Add proxy=proxy if needed
    
    for url in res:
        links.append(url + '\n')
        print(url)
        
        
def save(w):
    with open(str(w), "w") as f:
        f.writelines(links)
        print("Succesfully written!")
        


if args.examples:
    print("""Examples:
    python3 google_dorker.py --dork 'inurl:"/xmlrpc.php?rsd" & ext:php' -w results.txt -c 50
    python3 google_dorker.py --dork 'inurl:"/xmlrpc.php?rsd" & ext:php' --count 50
    python3 google_dorker.py -d 'inurl:"/xmlrpc.php?rsd" & ext:php' -c 20 -w res.txt -s 20
    Thanks for using this tool!
    My Github: https://github.com/WhiteeRabbit""")
    exit(0)

if args.dork:
    dorksearch(args.dork, args.count)
    
if args.write:
    save(args.write)
