# getsetquiz-moderator-bot
The home of the GetSetQuiz Moderator discord bot

## Installation

* Clone the repo and change directory:  

```bash
git clone https://github.com/soumyankar/getsetquiz-moderator-bot.git
cd getsetquiz-moderator-bot/
```

* [**IMPORTANT**] Initialize a `virtualenv` and activate.  
As an additional check make sure that your console reads the `virtualenv` label as _getsetquiz-moderator-bot_ after activating.

```bash
virtualenv -p python3 ./
source bin/activate
```  

* Install necessary packages for the application: 

```bash
pip install -r requirements.txt
```

* Test run the application!

```bash
python bot.py
``` 

This should fire up the bot and allow you to host it on the server. Watch your terminal to get a live logging on the bot's transcript.

## Contributing  

* Fork the repo first.

* Clone the repo and change directory:  

```bash
git clone [your repo link]
cd getsetquiz-moderator-bot/
```

* Make changes to the code and submit a PR!

```bash
git add -A
git commit -m "Super cool feature added"
git push origin master
```

Now you can submit a PR!
Remember to change the `requirements.txt` file in case you make any changes to the package managers. You can do this by:

```bash
pip-chill --no-version > requirements.txt
```

## Troubleshooting

### Creating a command

To create a new command you need to create a new `cog`.
Try taking a look at the `/cogs/template.py` to create a new command. 
Make a copy of that file and edit that to create a new command. **DONT TRY TO CHANGE `template.py`**

Don't worry about adding the command - the `bot.py` will do that by itself as long as you follow the template.

### VirtualENV

In case you do not have `virtualenv` installed have a look down below.  

### Linux  
```bash
# Debian, Ubuntu
$ sudo apt-get install python-virtualenv

# CentOS, Fedora
$ sudo yum install python-virtualenv

# Arch
$ sudo pacman -S python-virtualenv
```

### Mac OS X or Windows  
```bash
$ sudo python2 Downloads/get-pip.py
$ sudo python2 -m pip install virtualenv
```

### On windows as administrator
```bash
> \Python27\python.exe Downloads\get-pip.py
> \Python27\python.exe -m pip install virtualenv
```

Now you can return to the Installation Notes to continue.