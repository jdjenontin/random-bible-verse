# Random BIBLE Verse

This is a simple web app built in python using the Dash lib.
Tha app implements two versions of the bible : The **KJV** (King James Version) version and the the **LSG** (Louis Segond 1910) version.

The data used are from https://github.com/essodjolo/bible

## Installation


### Cloning

```bash
git clone git@github.com:jdjenontin/random-bible-verse.git
```

### Configuration

The app use an optional configuration file : .env

This file set the bible version to use and the verse refresh interval in seconds.

The file is not mandatory, the version default to "lsg" and the refresh interval to 60 seconds

```text
BIBLE_VERSION="lsg"
REFRESH_INTERVAL=60 # in seconds
```
[!IMPORTANT]
Every commands from here should be run at the root of the project

### For production

#### Using Docker

```bash
docker build . -t random-verse
docker run -p 8000:8000 -v ${PWD}/.env:/app/.env random-verse 
```

The app is available on http://localhost:8000

#### Using Docker Compose

```bash
docker compose build
docker compose up
```

The app is available on http://localhost:8000

#### Bare metal on linux

```bash
pip install poetry
poetry instal
gunicorn -b 0.0.0.0 random_bible_verse.app:server
```

The app is available on http://localhost:8000

### For development

```bash
pip install poetry
poetry instal
python -m random_bible_verse
```

The app is available on http://localhost:8050


## Further notes

### Adding new version

New bible version can be added to the database from json files by modifying `random_bible_verse/init_db.py`