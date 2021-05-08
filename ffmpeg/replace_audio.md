# Replace audio track in the video file

```bash
ffmpeg -i input.mp4 -i input.wav -map 0:v -map 1:a -c:v copy -shortest output.mp4
```

- -i input.mp4 - input video file
- -i input.wav - input audio file to replace for
- -map 0:v - take first video stream from first input (basically - take our video, exclude audio)
- -map 1:a - take first audio from the second input (basically - take our new audio)
- -c:v copy - just copy media, no encoding needed
- -shortest - make final video as long as the shortest input (video or audio)
- output.mp4 - resulting video file

group: change_audio
