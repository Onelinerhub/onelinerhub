# How do I download and install SQLite zip?
// plain

1. First, download the SQLite zip file from the [SQLite Download Page](https://www.sqlite.org/download.html).
2. Unzip the file into a folder of your choice.
3. Open your terminal and navigate to the folder containing the unzipped SQLite files.
4. Run the command `./configure` in the terminal to configure the SQLite library.
5. Run the command `make` in the terminal to compile the SQLite library.
6. Run the command `make install` in the terminal to install the SQLite library.
7. To test the installation, run the command `sqlite3` in the terminal. You should see the SQLite prompt if the installation was successful.

Example code block:
```
./configure
make
make install
sqlite3
```

Output of example code block:
```
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite>
```

onelinerhub: [How do I download and install SQLite zip?](https://onelinerhub.com/sqlite/how-do-i-download-and-install-sqlite-zip)