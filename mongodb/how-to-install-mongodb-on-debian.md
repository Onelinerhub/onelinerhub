# How to install MongoDB on Debian?
// plain

1. Download the MongoDB package from the official website: [https://www.mongodb.com/download-center/community](https://www.mongodb.com/download-center/community)
2. Install the MongoDB package with the following command:
```
sudo apt-get install -y mongodb-org
```
3. Start the MongoDB service with the following command:
```
sudo systemctl start mongod
```
4. Check the status of the MongoDB service with the following command:
```
sudo systemctl status mongod
```
The output should look like this:
```
● mongod.service - MongoDB Database Server
   Loaded: loaded (/lib/systemd/system/mongod.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2020-05-14 11:45:45 UTC; 1min ago
 Main PID: 809 (mongod)
    Tasks: 23 (limit: 4704)
   CGroup: /system.slice/mongod.service
           └─809 /usr/bin/mongod --config /etc/mongod.conf
```
5. To enable MongoDB to start on boot, run the following command:
```
sudo systemctl enable mongod
```

group: install

onelinerhub: [How to install MongoDB on Debian?](https://onelinerhub.com/mongodb/how-to-install-mongodb-on-debian)