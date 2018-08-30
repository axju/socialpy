# SocialPy
Use social networks like a hacker.

SocialPy has multiple function and is designed to be very flexible. The command
line tools allowed you to post viva the terminal. This is the way hacker should
post. Write your own scrips to post automatically. To storage some post, i
implement a data-serve with a web front end. It's only a django project and has
vary low security settings. Don't push it to a public web-server.

SocialPy is a small private project. I do it just for fun. So some parts are
really dirty. I would clean them up, if I'm boring. Or watch Rick and Morty? :D

## quick start
It's a python package, use pip to install.
```bash
pip install socialpy
```
Now setup the gateway. All keys are storage in your home folder ~/.socialpy
```bash
python -m socialpy.client setup
```
Where you find the key's? That is a little bit difficult. Maybe I should write
something about that. Or should I watch Rick and Morty again?

It's time to post something funny.
```bash
???
```
You can write your own python script and do crazy stuff.
```python
???
```
Look in the examples folder for more fun.

Before you can use the data-server, you have to initialize the database.
```bash
python -m socialpy.server setup
```
Start the server
```bash
python -m socialpy.server run
```
and then go to http://your.ip:9999. Write some awesome text. Enter the data from your scrips
```python
from socialpy.data import Post

for post in Post.objects.all():
  #do something with the post
```

This was the quick start. You can you much more. The doc coming soon, I promise.

## Setup Raspberry Pi
I use a Raspberry Pi as a small server. This is how I set it up.

```bash
python3 -m venv venv
source venv/bin/activate
pip install socialpy
```

## Client
More information about the client module.

```bash
python -m socialpy.client setup
python -m socialpy.client --file your/file
python -m socialpy.client show
python -m socialpy.client post --networks facebook twitter --text "Hallo Welt"
```

## Server
More information about the server module.

```bash
python -m socialpy.server setup
python -m socialpy.server createadmin
python -m socialpy.server run --settings server
python -m socialpy.server deletedb
```

## Data
More information about the data module.

```bash
python -m socialpy.data show
```

## Bot
More information about the bot module.

coming soon

## Development
Only developer stuff.
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
