<div align="center">
  <h1>🔍 Google Dorking Script</h1>
  <p>Simple Automatizated Google dorker script written in python</p>
  <p>❗ This tool is for educational and testing purposes only.</p>
</div>


<h1>🚀 How to Use This Tool</h1>
<p>Before running the script, make sure Python is installed on your system.</p>

To do that you can run on terminal or cmd: `python3 --version` or `python --version`
Once Python is ready, install the required Python libraries.

```bash
pip install -r requirements.txt
```

<h1>✅ Usage:</h1>

```bash
usage: google_url_dorker.py [-h] -d DORK [-c COUNT] [-w WRITE]
                            [-x]

Tool to extract URLs using Google Dork. python3 google_dorker.py
--dork 'inurl:"/xmlrpc.php?rsd" & ext:php' --count 50

options:
  -h, --help            show this help message and exit
  -d DORK, --dork DORK  Google dork query
  -c COUNT, --count COUNT
                        Number of URLs to fetch (default: 10)
  -w WRITE, --write WRITE
                        Save results to a text file
  -x, --examples        Show usage examples and Contacts
```

If you run the script without count it will show you 10 URLs:
```bash
python3 google_url_dorker.py -d 'YOUR DORK'
```


