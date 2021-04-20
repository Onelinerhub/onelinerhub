# Convert audio file to mp3

Will convert ```in.wav``` to ```out.mp3``` with 192 kb/s bitrate.

```bash
ffmpeg -i in.wav -vn -ar 44100 -ac 2 -ab 192k out.mp3
```
