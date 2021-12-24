# How to get file from docker container

```docker
docker cp 7c27810f3d85:/var/www/test.txt /home/me
```

- `docker cp` - copies files local between containers and host
- `7c27810f3d85` - ID of the container to copy files from
- `/var/www/test.txt` - file path on container to copy to local machine
- `/home/me` - local directory to copy specified file into

group: file

