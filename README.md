The module consists of two scripts.
1. `decoder.py` which verifies the signing keys and additional keys. 
2. `flask_app.py` is a web host over `decoder.py` so requests can be sent for testing

## Requirements
The code was tested on [Python 3.8.10](https://www.python.org/downloads/release/python-3810/), but should be compatible with Python>=3.7.
#### 

To install required dependencies,
```bash 
$ pip3 install requirements.txt
```

### Additional Requirements for web host 

The following dependencies needs to be installed only if flask app needs to be deployed.
```bash 
$ pip3 install flask_requirements.txt
```