# IP address extractor
Python command-line script that extracts (optionally, unique) IPv4 addresses from a specified file. Useful for digital forensics while iterating through log files.

# Installation
Just download/clone this repo or the `main.py` file.

# Usage
```
python3 main.py -i /file/with/ips -o /output/file -u True|False
```

Reads the provided input file (`-i`), searches for IPv4 addresses and writes the found addresses to the provided output file (`-o`). Specify `-u` with `True` or `False` to check for unique addresses or not.

## Further help
```
python3 main.py -h
```
