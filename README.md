# Spotify-Data

Script collecting your recently played songs

## Installation



###### Linux
Make sure you have ```python-venv``` package installed (```pip install python-venv```)

```
chmod +x install.sh
./install.sh
```

###### Windows

```
pip install -r requirements.txt
```

In the main folder create file called ```.env``` and fill it with necessary data as follows:

```
DATABASE = "path/to/sqlite/database example: sqlite://my_database.sqlite"
USER_ID = "your spotify username (not profile name)"
TOKEN = "your spotify token"
```
