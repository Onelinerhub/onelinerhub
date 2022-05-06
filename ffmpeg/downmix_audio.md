# Downmix 2 audio tracks

```bash
ffmpeg -i in1.mp3 -i in2.mp3 -filter_complex amix=inputs=2:duration=longest out.mp3
```

- `-i in1.mp3` - first audio file
- `-i in2.mp3` - second audio file
- `amix=inputs=2:duration=longest` - downmix 2 audio inputs and set the result duruation to the longest track (more [mixing options](https://trac.ffmpeg.org/wiki/AudioChannelManipulation))
- `out.mp3` - resulting mixed audio file


link_youtube: https://youtu.be/3iR7sc9vrGg
