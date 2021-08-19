The module consists of two scripts.
1. `decoder.py` which verifies the keys, email address and 
2. `flask_app.py` is a web host over `decoder.py` so requests can be sent for testing

## Requirements
[Python>=3.8.10](https://www.python.org/downloads/release/python-3810/)
#### 

```bash 
$ pip3 install requirements.txt
```

### Additional Requirements for web host 

Only required if flask app is deployed
```bash 
$ pip3 install flask_requirements.txt
```