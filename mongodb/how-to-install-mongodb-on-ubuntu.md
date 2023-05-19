# How to install MongoDB on Ubuntu?
// plain

1. Install MongoDB on Ubuntu using the official MongoDB repository:
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
```
2. Update the packages list and install the MongoDB package:
```
sudo apt-get update
sudo apt-get install -y mongodb-org
```
3. Start MongoDB:
```
sudo service mongod start
```
4. Check the status of MongoDB:
```
sudo service mongod status
```
5. You can now connect to MongoDB using the mongo shell:
```
mongo
```

## Helpful links

- [MongoDB Documentation](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
- [MongoDB Download Center](https://www.mongodb.com/download-center/community)

group: install

onelinerhub: [How to install MongoDB on Ubuntu?](https://onelinerhub.com/mongodb/how-to-install-mongodb-on-ubuntu)