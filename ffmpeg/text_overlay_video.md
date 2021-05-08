# Add text overlay (watermark) to video

```bash
ffmpeg -i in.mp4 -vf drawtext="fontfile=font.ttf: text='Test Text'" -codec:a copy out.mp4
```

- -i in.mp4 - input video file
- drawtext - video filter to add text to video (more [usage examples](https://ffmpeg.org/ffmpeg-filters.html#drawtext-1))
- fontfile=font.ttf - selected font file (you can download ttf fonts from the web)
- 'Test Text' - chosen text
- -codec:a copy - copy audio stream instead of encoding
- out.mp4 - resulting video file
