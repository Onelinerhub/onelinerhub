# How do I install SQLite?
// plain

SQLite is an open source, lightweight relational database management system (RDBMS) that can be used to store and manage data. Installing SQLite is easy and straightforward.

1. Download the latest version of SQLite from the [SQLite download page](https://www.sqlite.org/download.html).
2. Unzip the downloaded file and navigate to the extracted folder.
3. Open a terminal window and enter the following command to compile the source code:
```
$ ./configure
```
4. Once the configuration is complete, enter the following command to build the SQLite library:
```
$ make
```
5. Once the build is complete, enter the following command to install the library:
```
$ make install
```
6. To check if the installation was successful, enter the following command to display the version of SQLite installed:
```
$ sqlite3 --version
```
This should output the version of SQLite installed, e.g. `3.30.1`.

For more detailed instructions, please refer to the [official documentation](https://www.sqlite.org/quickstart.html).

onelinerhub: [How do I install SQLite?](https://onelinerhub.com/sqlite/how-do-i-install-sqlite-1687122513)