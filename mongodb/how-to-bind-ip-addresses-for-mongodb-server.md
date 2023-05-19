# How to bind IP addresses for MongoDB server?
// plain

MongoDB provides the `net.bindIp` configuration option to bind the MongoDB server to a specific IP address. This option can be set in the `mongod.conf` configuration file.

```
net:
  bindIp: 192.168.1.100
```

The `net.bindIp` option can also be used to bind to multiple IP addresses.

```
net:
  bindIp: 192.168.1.100,127.0.0.1
```

- `net.bindIp`: This is the configuration option used to bind the MongoDB server to a specific IP address.
- `mongod.conf`: This is the configuration file used to set the `net.bindIp` option.
- `192.168.1.100`: This is an example of an IP address that can be used to bind the MongoDB server.
- `127.0.0.1`: This is an example of a localhost IP address that can be used to bind the MongoDB server.

## Helpful links
- [MongoDB Documentation - net.bindIp](https://docs.mongodb.com/manual/reference/configuration-options/#net.bindIp)

onelinerhub: [How to bind IP addresses for MongoDB server?](https://onelinerhub.com/mongodb/how-to-bind-ip-addresses-for-mongodb-server)