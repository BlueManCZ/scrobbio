import asyncio
from shazamio import Shazam
from .shazam_track import ShazamTrack

shazam = Shazam()


def recognize_track_from_file(filename):
    """Recognize a track from a file using Shazam API."""
    shazam_data = asyncio.run(shazam.recognize(filename))
    return ShazamTrack(shazam_data)
