# How to copy file to docker container

```docker
docker cp /home/me/test.txt 7c27810f3d85:/var/www
```

- `docker cp` - copies local files to docker container
- `/home/me/test.txt` - path to the file which should be copied to the conteiner
- `7c27810f3d85` - ID of the container to copy file to
- `/var/www` - folder from the container to copy file into

group: file


link_youtube: https://youtu.be/ZkvbsGI5K7w
