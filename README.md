
# Instructions

### Activate virtual environment and download dependencies

Linux/macOS:
```shell
source .venv/bin/activate
pip install -r requirements.txt
```
Windows:
```shell
.venv\Scripts\activate
pip install -r requirements.txt
```

### Run unit tests with coverage report


```shell
coverage run -m unittest discover tests
coverage report
```
