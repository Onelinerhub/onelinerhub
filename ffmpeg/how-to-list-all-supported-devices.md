# How to list all supported devices

```bash
ffmpeg -hide_banner -devices
```

- `ffmpeg` - ffmpeg utility
- `-devices` - will list all supported [devices](https://ffmpeg.org/ffmpeg-devices.html)
- `-hide_banner` - skip version details and print only what we need

## Example: 
```bash
ffmpeg -hide_banner -devices
```
```
Devices:
 D. = Demuxing supported
 .E = Muxing supported
 --
 DE alsa            ALSA audio output
  E caca            caca (color ASCII art) output device
 DE fbdev           Linux framebuffer
 D  iec61883        libiec61883 (new DV1394) A/V input device
 D  jack            JACK Audio Connection Kit
 D  kmsgrab         KMS screen capture
 D  lavfi           Libavfilter virtual input device
 D  libcdio          
 D  libdc1394       dc1394 v.2 A/V grab
 D  openal          OpenAL audio capture device
  E opengl          OpenGL output
 DE oss             OSS (Open Sound System) playback
 DE pulse           Pulse audio output
  E sdl,sdl2        SDL2 output device
 DE sndio           sndio audio playback
 DE video4linux2,v4l2 Video4Linux2 output device
 D  x11grab         X11 screen capture, using XCB
  E xv              XV (XVideo) output device
```

