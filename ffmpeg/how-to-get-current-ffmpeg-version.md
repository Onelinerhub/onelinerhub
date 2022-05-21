# How to get current ffmpeg version

```bash
ffmpeg -version | grep "ffmpeg version"
```

- `ffmpeg` - basic ffmpeg utility
- `-version` - prints details about currently installed ffmpeg
- `grep "ffmpeg version"` - filter output so only version info is visible

group: install

## Example: 
```bash
ffmpeg -version | grep "ffmpeg version"
```
```
ffmpeg version 4.4.1-3ubuntu5 Copyright (c) 2000-2021 the FFmpeg developers
```

link_youtube: https://youtu.be/W9o88CAfXR0
