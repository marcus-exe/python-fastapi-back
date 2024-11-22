# Fast API Implementation for AI Backend

## Configure the virtual enviroment
### Define the env
Before running it, turn on the virtual env:
```
python3 -m venv venv
```
### Activate env
Then you can run using:
_on windows:_
```
venv\Scripts\activate
``` 
_on macOS/linux_
```
source venv/bin/activate
```
### Setup Libs
Install `requirements.txt` dependencies:
```
pip install -r requirements.txt
```
### Run the project
```
uvicorn main:app --reload 
```

### Stoping the project and deactivating env
For stoping the project, just type `ctrl + c` on terminal

### For deactivating env:
```
deactivate
```