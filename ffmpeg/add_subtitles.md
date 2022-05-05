# Add subtitles to a video

```bash
ffmpeg -i input.mp4 -i subtitles.srt -c copy -c:s mov_text output.mp4
```

- `-i input.mp4` - input video file
- `-i subtitles.srt` - input subtitles file
- `-c copy` - just copies media, no encoding done
- `-c:s mov_text` - will encode text-based subtitles
- `output.mp4` - resulting video file


link_youtube: https://youtu.be/RXPKsUe_UPQ
