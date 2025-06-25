<div align="center">
  <h1>🔍 Google Dorking Script</h1>
  <p>Simple Automatizated Google dorker script written in Python</p>
  <p>❗ This tool is for educational and testing purposes only.</p>
</div>


<h1>🚀 How to Use This Tool</h1>
<p>Before running the script, make sure Python is installed on your system.</p>

To do that you can run on terminal or cmd: `python3 --version` or `python --version`
<p>🟢 Once Python is ready, install the required Python libraries.</p>

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

<h2>🔴 Show Usage Examples and Contacts</h2>

```bash
python3 google_url_dorker.py -d 0 --examples
```
<h2>🟡 If you run the script without specifying count, it will fetch 10 URLs by default </h2>

```bash
python3 google_url_dorker.py -d 'YOUR DORK'
```
<h2>🔵 Fetch 50 URLs using your dork query </h2>

```bash
python3 google_url_dorker.py -d 'YOUR DORK' -c 50
```
<h2>🟣 Fetch 50 URLs and save results to a file named results.txt </h2>

```bash
python3 google_url_dorker.py -d 'YOUR DORK' -c 50 --write results.txt
```


<h2>⚪ 🛠️ Usage Options 📝</h2>

| Options | Description |
| ------ | ------ |
| `-h` or `--help` | Show help message and exit |
| `-d` or `--dork` | Specify the Google dork query (required) |
| `-c` or `--count` | Number of URLs to fetch (default: 10) |
| `-w` or `--write` | Save the fetched URLs to a text file |
| `-x` or `--examlpes` | Show usage examples and contacts |




## 📃 License: 
[LICENSE](https://github.com/WhiteeRabbit/Google_Dorking_Script/blob/main/LICENSE)

<h1> 🙏🏻 Big thanks to everyone who gave a ⭐️ to this project or helped in any way. </h1>
Your support means a lot and keeps this kind of work going!








