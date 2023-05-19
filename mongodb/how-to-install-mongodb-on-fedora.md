# How to install MongoDB on Fedora?
// plain

MongoDB can be installed on Fedora using the following steps:

1. Install the MongoDB packages with the following command:
```
sudo dnf install mongodb-server mongodb
```

2. Start the MongoDB service with the following command:
```
sudo systemctl start mongod
```

3. Enable the MongoDB service to start on boot with the following command:
```
sudo systemctl enable mongod
```

4. Verify that the MongoDB service is running with the following command:
```
sudo systemctl status mongod
```

5. You should see the following output:
```
● mongod.service - MongoDB Database Server
   Loaded: loaded (/usr/lib/systemd/system/mongod.service; enabled; vendor preset: disabled)
   Active: active (running) since Thu 2020-08-20 11:45:17 UTC; 1min ago
 Main PID: 8093 (mongod)
    Tasks: 23 (limit: 4704)
   Memory: 64.2M
   CGroup: /system.slice/mongod.service
           └─8093 /usr/bin/mongod -f /etc/mongod.conf
```

## Helpful links
- [MongoDB Documentation](https://docs.mongodb.com/manual/administration/install-on-linux/)

group: install

onelinerhub: [How to install MongoDB on Fedora?](https://onelinerhub.com/mongodb/how-to-install-mongodb-on-fedora)