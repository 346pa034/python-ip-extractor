# A lightweight, easy-to-use, (log file) IP address extractor
Python command-line script that extracts (optionally, unique) IPv4 addresses from a specified (log) file. Useful for digital forensics while iterating through log files.

# Installation
Just download/clone this repo.

# Usage
```
python3 extract-ips.py -i /file/with/ips -o /output/file -u True|False
```

Reads the provided input file (`-i`), searches for IPv4 addresses and writes the found addresses to the provided output file (`-o`). Specify `-u` with `True` or `False` to check for unique addresses or not.

## Further help
```
python3 extract-ips.py -h
```
