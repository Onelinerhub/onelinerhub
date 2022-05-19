# Concatenate (combine) several audio tracks

```bash
ffmpeg -i in1.mp3 -i in2.mp3 -filter_complex '[0:0][1:0]concat=n=2:v=0:a=1[out]' -map '[out]' out.mp3
```

- `-i in1.mp3` - first audio
- `-i in2.mp3` - second audio
- `-filter_complex` - applies specified video/audio complex filter
- `concat=` - concatenate filter allows joining multiple media files
- `out.mp3` - resulting file

group: concat


link_youtube: https://youtu.be/To2ULgLQ_6c
