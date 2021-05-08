# Add audio track to the video file

```bash
ffmpeg -i input.mp4 -i input.wav -map 0 -map 1:a -c:v copy -shortest output.mp4
```

- -i input.mp4 - input video file
- -i input.wav - input audio file to replace for
- -map 0 - take first file (basically - take our video)
- -map 1:a - take first audio from the second file (basically - take our new audio)
- -c:v copy - just copy media, no encoding needed
- -shortest - make final video as long as the shortest input (video or audio)
- output.mp4 - resulting video file

group: change_audio
