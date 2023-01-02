import soundcard as sc
import soundfile as sf

# Detect the loopback input of the default speaker.
# TODO: Let the user choose the input.
loopback_input = None
default_output = sc.default_speaker()
inputs = sc.all_microphones(include_loopback=True)
for i in inputs:
    if default_output.name in i.name:
        loopback_input = i
        break

# Exit if there is no loopback input.
if not loopback_input:
    print("No loopback input found")
    exit(1)

print(f"Using input: {loopback_input.name}\n")


def record_audio(samplerate=44100, numframes=500000):
    """Record audio from the loopback input at the given samplerate for the given number of frames."""
    with loopback_input.recorder(samplerate=samplerate) as mic:
        data = mic.record(numframes)
        return data, samplerate


def save_audio_to_file(filename, data, samplerate=44100):
    """Create file from audio data at the given samplerate."""
    sf.write(filename, data, samplerate)
