# How to download sound only from Youtube video

```bash
youtube-dl -f 'bestaudio[ext=m4a]' https://www.youtube.com/watch?v=sAmEhyZ4Jho
```

- `youtube-dl` - [youtube downloader](/ubuntu/how-to-install-youtube-downloader) utility
- `-f` - select format to download
- `bestaudio[ext=m4a]` - download best available audio format
- `watch?v=sAmEhyZ4Jho` - Youtube video to download sound from

group: youtube


