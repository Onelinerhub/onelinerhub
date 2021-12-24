# How to find docker container id by name 

### Container ID is seen under the first column of `docker ps` command:

```bash
docker container inspect test | grep Id
```

- `container inspect` - return detailed data about specified container
- `test` - name of the container to find ID of
- `grep Id` - filter out only ID of the container

group: id

## Example: 
```bash
docker container inspect test | grep Id
```
```
"Id": "0548543a2e9824bc2df9ac...",

```
