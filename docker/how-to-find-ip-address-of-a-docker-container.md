# How to find ip address of a docker container

```docker
docker container inspect 0548543a2e98 | grep 'IPAddress"'
```

- `inspect` - return details about specified container
- `0548543a2e98` - id of a container to get details about
- `grep 'IPAddress"'` - filter only IPAddress param

group: network

## Example: 
```docker
docker container inspect 0548543a2e98 | grep 'IPAddress"'
```
```
"IPAddress": "172.17.0.2",
```
