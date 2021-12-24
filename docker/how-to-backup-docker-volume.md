# How to backup docker volume

```bash
docker run -it --mount source=data,destination=/data ubuntu
docker run --rm --volumes-from 804e9d6977ba -v /tmp/data:/backup ubuntu tar czvf /backup/backup.tar.gz /data
```

- `docker run` - run specified image
- `-it` - instantly connects to container command line 
- `--mount` - mounts specified volume
- `source=data` - name of the volume to mount (`data`)
- `destination=/data` - path that the volume will be available from the container
- `--rm` - remove container automatically after it stopped (used for backup container only)
- `--volumes-from` - specify which container to mount volumes from (assume we have running containers to backup from)
- `804e9d6977ba` - id of our first container (to backup volume from)
- `-v` - mount directory for container
- `/tmp/data:/backup` - make local `/tmp/data` be accessible to container at `/backup`
- `tar czvf` - creates gzip acrhive
- `/backup/backup.tar.gz` - name of the backup file
- `/data` - which directory to create gzip from (`/data` is the path of `data` volume)

group: volume

## Example: 
```bash
docker run -it --mount source=data,destination=/data ubuntu
docker run --rm --volumes-from 804e9d6977ba -v /tmp/data:/backup ubuntu tar czvf /backup/backup.tar.gz /data
ls /tmp/data
```
```
tar: Removing leading `/' from member names
/data/
/data/hello.txt
backup.tar.gz
```
