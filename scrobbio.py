from modules.recorder import record_audio, save_audio_to_file
from modules.recognizer import recognize_track_from_file
from modules.scrobbler import apply_patches, scrobble_track
from modules.utils import show_diff

running = True
last_track = None
last_scrobbled_track = None

while running:
    # Record audio and save it to a file
    data, samplerate = record_audio()
    save_audio_to_file("/tmp/sample.wav", data, samplerate)

    # Recognize audio from a file
    track = recognize_track_from_file("/tmp/sample.wav")

    # Scrobble track metadata
    if track.title and track.artist:
        # To filter out wrong recognition results, scrobble only if the track is recognized twice in a row
        if track == last_track:
            # To avoid scrobbling the same track multiple times
            if track != last_scrobbled_track:
                title, artist, album, album_artist = apply_patches(
                    track.title, track.artist, track.album
                )

                print(
                    f"{show_diff(track.title, title)}\n"
                    f"{show_diff(track.artist, artist)}\n"
                    f"{show_diff(track.album, album)}\n"
                )

                scrobble_track(
                    title,
                    artist,
                    album,
                    album_artist,
                )
                last_scrobbled_track = track
            last_track = None
        else:
            last_track = track
