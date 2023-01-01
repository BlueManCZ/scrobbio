# Scrobbio

Scrobbio is a simple service that recognises songs in the system's default audio
output and scrobbles its metadata to [Last.fm](https://www.last.fm). It is written in Python and uses
the [ShazamIO](https://github.com/dotX12/ShazamIO) for audio recognition and
[pylast](https://github.com/pylast/pylast) for Last.fm scrobbling.

## Why?
You can scrobble songs from movies, TV shows, games, etc. It's a fun way to
explore new music and keep track of it.

## What?
Because Scrobbio doesn't just simply read the MPRIS metadata but actually "listens" to
the audio output, it is totally independent of the media player you use, and it
can recognise any songs playing in the background.

## How?
Just create `.env` file in the root directory where you provide your Last.fm
user and API credentials, and you are ready to go. Use the following format:

```
LASTFM_USERNAME=<YOUR-USERNAME>
LASTFM_PASSWORD_HASH=<MD5-PASSWORD-HASH-(32chars)>
LASTFM_API_KEY=<API-KEY-(32chars)>
LASTFM_API_SECRET=<API-SECRET-(32chars)>
```

Replace all <...> with your specific values.

You can generate your MD5 password hash in python:

```python
import pylast
pylast.md5("your-password-here")
```

You can get your API credentials from [here](https://www.last.fm/api/account/create).

Then just install the dependencies and run the script:

```
$ pip install -r requirements.txt
$ python scrobbio.py
```

## Can I contribute?
...and some nerdy stuff...

Yes, you can. I wrote this tool and tested it with the Stellaris game, but the
raw data it's getting from the Shazam is not always "ready to push". So I
implemented a post-processing steps allowing users to add their custom metadata patches.
The goal is to convert raw data from Shazam to the clean and correct Last.fm metadata
as closely as possible with as few patches as possible. The [stellaris.py](modules/scrobbler/patches/stellaris.py)
may seem to be overkill, but you get the idea.
