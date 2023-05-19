# How to install MongoDB on CentOS?
// plain

1. Install the MongoDB packages with the yum package manager:
```
sudo yum install -y mongodb-org
```
2. Start the MongoDB service:
```
sudo systemctl start mongod
```
3. Enable the MongoDB service to start on boot:
```
sudo systemctl enable mongod
```
4. Check the status of the MongoDB service:
```
sudo systemctl status mongod
```
5. Verify that MongoDB has started successfully by checking the log file at `/var/log/mongodb/mongod.log`.

## Helpful links
- [MongoDB Installation Guide for CentOS](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)

group: install

onelinerhub: [How to install MongoDB on CentOS?](https://onelinerhub.com/mongodb/how-to-install-mongodb-on-centos)