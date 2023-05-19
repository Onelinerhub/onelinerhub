# How to install MongoDB on Windows?
// plain

1. Download the MongoDB Windows Server 2008 R2 64-bit and later, MSI Installer from the [MongoDB Download Center](https://www.mongodb.com/download-center/community).

2. Run the downloaded `.msi` file to start the installation wizard.

3. Follow the instructions in the wizard to complete the installation.

4. After the installation is complete, open the Command Prompt and run the following command to start the MongoDB server:

```
mongod
```

5. To verify that the MongoDB server is running, open another Command Prompt window and run the following command:

```
mongo
```

You should see the following output:

```
MongoDB shell version v4.2.3
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("f9f9f9f9-f9f9-f9f9-f9f9-f9f9f9f9f9f9") }
MongoDB server version: 4.2.3
```

group: install

onelinerhub: [How to install MongoDB on Windows?](https://onelinerhub.com/mongodb/how-to-install-mongodb-on-windows)