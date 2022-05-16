# How to encode video for Vimeo (with streaming support)

```bash
ffmpeg -i in.mov -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192k -pix_fmt yuv420p -movflags +faststart out.mp4
```

- `-i in.mov` - input video to prepare for Youtube upload
- `-c:v libx264` - use H.264 codec
- `-preset` - specify [preset](https://trac.ffmpeg.org/wiki/Encode/H.264#Preset) (mode) to use for conversion, where `ultrafast` is fastest but primitive and `veryslow` is slowest but most efficient
- `-crf 18` - preferred quality level (`bitrate`), where `0` is lossless and `51` is worst
- `-c:a aac` - use [`AAC` codec](/ffmpeg/encode-mp3-to-aac) for audio
- `-b:a 192k` - set audio bitrate to 192k
- `-pix_fmt yuv420p` - use yuv420p pixel format
- `-movflags +faststart` - adds metadata to the beginning of the file, so it can start playing before full download
- `out.mp4` - resulting video file

group: exporting


