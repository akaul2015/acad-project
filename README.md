# acad-project
weebcheck
Assumption: you're using ubuntu

how to set up environment on your PC?

Automatic way: Fork this repo, then clone it using git on bash(terminal). (easy 2 commands: google if u dont know)

if virutal environment doesnt get setup then set it up manually in acad-project folder (see end)

Manual shit: Folders look like this on my pc (ubuntu):
  1. do ls on home
  2. theres many folders. one of them is 'acad-project'
  3. make an empty 'instance' folder inside that
  4. setup virtual env in this folder (see end)
  5. now folders are: instance and venv (virtual env folder, can name it what u want)
  6. copy my repo in there
  
 Make a virtual environment and get python3 and flask on that virtualenv.
source: https://flask.palletsprojects.com/en/1.1.x/installation/


________________________________________________________

THINGS TO DO IN THE PROJECT:

    Things to learn
    SQLalchemy for database sharing between me and arpit. its a db migration system. migration is not equivalent to direct sharing but close enough
    Anime/Manga API to grab lists of manga and anime: AniList API. Note: This is tentative. Play around with it and see if this works properly else try some other API
    DB to use is MYSQL as asked in Ibit academy

part 1: (for now) Add DB. Current goals are to finish signup and login. make user personal page. Then fetch anime and manga lists. Dont do any special front end 
