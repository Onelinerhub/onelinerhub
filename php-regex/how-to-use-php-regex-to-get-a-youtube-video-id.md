# How to use PHP regex to get a YouTube video ID?
// plain

Using PHP regex to get a YouTube video ID is a simple task. The following example code block will demonstrate how to do it:
```
$url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ';

preg_match('%(?:youtube(?:-nocookie)?\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)/|.*[?&]v=)|youtu\.be/)([^"&?/ ]{11})%i', $url, $match);

echo $match[1];
```
The output of the example code will be:
```
dQw4w9WgXcQ
```
## Code explanation


1. `$url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ';` - This is the URL of the YouTube video.

2. `preg_match('%(?:youtube(?:-nocookie)?\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)/|.*[?&]v=)|youtu\.be/)([^"&?/ ]{11})%i', $url, $match);` - This is the regular expression used to match the YouTube video ID.

3. `echo $match[1];` - This is the code to output the YouTube video ID.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to get a YouTube video ID?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-get-a-youtube-video-id)