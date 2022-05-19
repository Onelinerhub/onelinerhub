# Concatenate (combine) several videos

```bash
ffmpeg -i part1.mkv -i part2.mkv -filter_complex "[0:v] [0:a] [1:v] [1:a] concat=n=2:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" output.mkv
```

- `-i part1.mkv` - first video to be concatenated
- `-i part2.mkv` - second video to be concatenated
- `-filter_complex` - filter option used to filter multiple inputs
- `[0:v] [0:a] [1:v] [1:a]` - this tells which video/audio streams take and send to concat filter
- `concat=n=2:v=1:a=1 [v] [a]` - concat filters takes 2 input segments and generates 1 video and 1 audio output stream
- `-map "[v]" -map "[a]"` - tells ffmpeg to use video and audio stream from concat filter
- `output.mkv` - is the resulting file

group: concat


link_youtube: https://youtu.be/ZFzv1a0pNLY
