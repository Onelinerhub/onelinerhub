# How to check docker network

```bash
docker container inspect 0548543a2e98 | grep Networks -A 20
```

- `inspect` - return details about specified container
- `0548543a2e98` - id of a container to get details about
- `grep Networks -A 20` - filter out only network block (20 lines after `Networks` text is found)

group: network

## Example: 
```bash
docker container inspect 0548543a2e98 | grep Networks -A 20
```
```
"Networks": {
  "bridge": {
      "IPAMConfig": null,
      "Links": null,
      "Aliases": null,
      "NetworkID": "11d59b5bebe0ca54c391a1399835e04fad712747e68854caef5e376ab65df3a9",
      "EndpointID": "15bd6c5021a0989ad0171c75f8264cb469bc95fd648fd80493145f6ca4b7a302",
      "Gateway": "172.17.0.1",
      "IPAddress": "172.17.0.2",
      "IPPrefixLen": 16,
      "IPv6Gateway": "",
      "GlobalIPv6Address": "",
      "GlobalIPv6PrefixLen": 0,
      "MacAddress": "02:42:ac:11:00:02",
      "DriverOpts": null
  }
}
```

link_youtube: https://youtu.be/AhtLqTPStjk
