# How to capture audio with mic

```bash
ffmpeg -f alsa -i hw:1 out.wav
```

- `-f alsa` - selects `ALSA` input device which allows capturing audio
- `-i` - specify input device (microphone in our case) from list of [installed audio devices](/ffmpeg/how-to-list-recording-sound-devices-on-pc-in-ubuntu)
- `hw:1` - use first mic available
- `out.wav` - resulting file with captured audio

group: capture


