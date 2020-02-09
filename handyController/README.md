# Handy Controller

![HandyController on mac](resources/screenshot.png?raw=true "HandyController on mac")

## Usage
-----
Handy Controller is a simple client written with python, it has a simple interface that allows you to send simple commands to FIRASim.

## Installation

### Clone Sub Modules
```bash
git submodule update --recursive --init 
```

### creating virtualenv
#### Linux and macOS
```bash
pip3 install virtualenv
cd /path/to/handyController/directory
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

### run the app

#### Linux and macOS
```bash
python3 RefServer.py
```


