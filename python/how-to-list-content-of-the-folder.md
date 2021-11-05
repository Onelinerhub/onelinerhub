# How to list content of the folder

```python
from os import listdir

list = listdir('/var/www/onelinerhub')
```

- `listdir` - function to list all files and folders of a specified directory
- `'/var/www/onelinerhub'` - example directory to list contents of
- `list` - will contain resulting list of files and folders

group: list_files

## Example: 
```python
from os import listdir

list = listdir('/var/www/onelinerhub')
print(list)
```
```
['template_simple.md', 'pip', 'find', 'bulma', 'ssh', 'clickhouse', '.git', 'lua', 'php', 'LICENSE', 'webp', 'ubuntu', 'grep', 'golang', 'ls', 'django', 'php-swoole', 'google-chrome', 'nginx', 'imagemagick', 'solidity', 'jquery', 'c#', 'ace', 'htpasswd', 'postgres', '.github', 'supervisor', 'ffmpeg', 'http-headers', 'jpegoptim', 'nodejs', 'c', 'wget', 'java', 'optipng', 'bash', 'mysql', 'powershell', 'git', 'html', 'php-redis', 'javascript', 'certbot', 'README.md', 'example.png', 'react', 'xdotool', 'template.md', 'curl', 'nano', 'chrome-extension', 'css', 'python', 'chart.js', 'regex', 'jq', 'youtube']

```

## Additional keywords
- directory
- subdirectory
