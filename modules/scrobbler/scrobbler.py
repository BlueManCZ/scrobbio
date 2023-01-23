from dotenv import dotenv_values
from pylast import LastFMNetwork
from time import time
from modules.scrobbler.patches import all_available_patches
from modules.utils import find_processes

config = dotenv_values()

username = config.get("LASTFM_USERNAME")
password_hash = config.get("LASTFM_PASSWORD_HASH")
API_KEY = config.get("LASTFM_API_KEY")
API_SECRET = config.get("LASTFM_API_SECRET")

network = LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=username,
    password_hash=password_hash,
)


def apply_patches(title, artist, album, album_artist=None):
    """Apply patches to the track metadata."""
    for patch in all_available_patches:
        if patch.get("config", {}).get("process_name"):
            if not find_processes(patch.get("config").get("process_name")):
                continue
        if "remove" in patch:
            for remove in patch["remove"]:
                title = title.replace(remove, "")
                artist = artist.replace(remove, "")
                if album:
                    album = album.replace(remove, "")
        if "replace" in patch:
            for key, value in patch["replace"].items():
                if title == key:
                    title = title.replace(key, value)
                if artist == key:
                    artist = artist.replace(key, value)
                if album and album == key:
                    album = album.replace(key, value)
        if "partial_replace" in patch:
            for key, value in patch["partial_replace"].items():
                if key in title:
                    title = title.replace(key, value)
                if key in artist:
                    artist = artist.replace(key, value)
                if album and key in album:
                    album = album.replace(key, value)
        if "album" in patch:
            for album_name, album_dict in patch["album"].items():
                if album_name == album:
                    album_artist = album_dict.get("album_artist", None)
                if (
                    artist in album_dict.get("artist", "")
                    or artist in album_dict.get("album_artist", "")
                ) and title in album_dict.get("tracks", []):
                    artist = album_dict.get("artist", artist)
                    album = album_name
                    album_artist = album_dict.get("album_artist", album_artist)
                if type(album_dict.get("tracks", None)) == dict:
                    for track_name, track_artist in album_dict.get("tracks").items():
                        if title in track_name and (
                            artist in track_artist or track_artist in artist
                        ):
                            title = track_name
                            artist = track_artist
                            album = album_name
                            album_artist = album_dict.get("album_artist", album_artist)

    return title, artist, album, album_artist


def scrobble_track(title, artist, album=None, album_artist=None):
    """Scrobble track to last.fm."""
    network.scrobble(
        artist=artist,
        title=title,
        timestamp=int(time()),
        album=album,
        album_artist=album_artist,
    )
