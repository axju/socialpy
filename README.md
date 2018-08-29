# Social-Py
Post on social networks like a hacker.

Social-Py is a gateway to all common uses social networks. It collect the
login-data and manage all apis. It has also a small database (a django-project),
for saving your posts. This help you to post stuff, if you now how to program.

## Attention
I have change the structure, so all examples and documentation will be wrong.
It will be fix soon.

## Install
It's still under develop. See the Development section for some install
instructions. The first working release will by push to PyPi, so you can uses
pip.

## The Data-Server
Run the server
```bash
python -m socialpy.cmd.server setup
python -m socialpy.cmd.server run
```
go to http://<ip>:9999 and save your post. You can uses this data in your
python script. Import the model
```python
from socialpy.data.post.models import Post
```

## The funcs module
This collect some functions to setup your environment. You can exes the function
from command-line (not working)
```shell
socialpy-funcs help
```
or with python
```bash
python -m socialpy.funcs help
```

## Uses as command-line-tool (not working)
```bash
socialpy-post --twitter --facebook --text "Yes, this is a example!"
```

## Uses as python package
```python
from socialpy import Gateway

gateway = Gateway()
gateway['twitter'].login('user', 'pw')
gateway.post(text='bla bla bla')
```
See the examples folder for more.


## Development
Clone the repo
```bash
git clone https://github.com/axju/socialpy.git
cd socialpy
```
Setup avirtual envirument
```bash
python3 -m venv venv
source venv/bin/activate
```
Install socialpy
```bash
pip install -e .
```
Setup the db for the data-server
```bash
python -m socialpy.funcs setupdb
```
You can uses the django manag.py like
```bash
python -m socialpy.data startapp newapp
```

## Some infos
https://github.com/tweepy/tweepy
https://github.com/LevPasha/Instagram-API-python
https://github.com/jgorset/facepy
