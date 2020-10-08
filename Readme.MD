# Jugglerz Music RadioShow Downloader

This tool allows the download of all files from jugglerz.de server. 

## Setup

Install Python3 and run
```bash
pip3 install -r requirements.txt
```

## Run

To run the downloader, invoke the following command:
```bash
python3 main.py -i data.txt -o jugglerz
```

This will download all files specified in ```data.txt``` to the output directory ```jugglerz```. If the output directory does not exist, this will be created.