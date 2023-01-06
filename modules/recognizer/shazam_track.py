from modules.utils import normalize_string


class ShazamTrack:
    """Class to represent a track recognized by Shazam API."""

    def __init__(self, shazam_data):
        self.shazam_data = shazam_data if shazam_data else {}

    @property
    def title(self):
        title = self.shazam_data.get("track", {}).get("title")
        return normalize_string(title) if title else None

    @property
    def artist(self):
        artist = self.shazam_data.get("track", {}).get("subtitle")
        return normalize_string(artist) if artist else None

    @property
    def album(self):
        if self.shazam_data.get("track", {}).get("sections"):
            for metadata in (
                self.shazam_data.get("track", {})
                .get("sections", None)[0]
                .get("metadata", {})
            ):
                if metadata.get("title") == "Album":
                    return normalize_string(metadata.get("text"))
        return None

    def __str__(self):
        return f"Title:  {self.title}\nArtist: {self.artist}\nAlbum:  {self.album}"

    def __eq__(self, other):
        if not isinstance(other, ShazamTrack):
            return False
        return (
            self.title == other.title
            and self.artist == other.artist
            and self.album == other.album
        )
