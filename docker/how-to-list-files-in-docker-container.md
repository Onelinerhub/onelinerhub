# How to list files in docker container

```bash
docker exec 7c27810f3d85 ls -la /var
```

- `docker exec` - run command for specified container
- `7c27810f3d85` - container ID to list files for
- `ls -la` - list files with extra data
- `/var` - path to list files in

group: file

## Example: 
```bash
docker exec 7c27810f3d85 ls -la /var
```
```
total 60
drwxr-xr-x 1 root root  4096 Oct  6 19:58 .
drwxr-xr-x 1 root root  4096 Dec 24 13:49 ..
drwxr-xr-x 2 root root  4096 Apr 15  2020 backups
drwxr-xr-x 1 root root  4096 Dec 24 13:47 cache
drwxr-xr-x 1 root root  4096 Dec 24 13:47 lib
drwxrwsr-x 2 root staff 4096 Apr 15  2020 local
lrwxrwxrwx 1 root root     9 Oct  6 19:47 lock -> /run/lock
drwxr-xr-x 1 root root  4096 Dec 24 13:47 log
drwxrwsr-x 2 root mail  4096 Oct  6 19:47 mail
drwxr-xr-x 2 root root  4096 Oct  6 19:47 opt
lrwxrwxrwx 1 root root     4 Oct  6 19:47 run -> /run
drwxr-xr-x 2 root root  4096 Oct  6 19:47 spool
drwxrwxrwt 2 root root  4096 Oct  6 19:58 tmp
```

link_youtube: https://youtu.be/lwOyISmxpY8
