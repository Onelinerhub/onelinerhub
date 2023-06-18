# How do I install SQLite?
// plain

1. Download the [SQLite source code](https://www.sqlite.org/download.html) and compile it according to the [instructions](https://www.sqlite.org/howtocompile.html).

2. Unzip the downloaded file, then `cd` into the unzipped directory:

```
$ unzip sqlite-autoconf-*.zip
$ cd sqlite-autoconf-*
```

3. Configure the compilation process with the `configure` command:

```
$ ./configure
```

4. Compile the code with `make`:

```
$ make
```

5. Install SQLite with `make install`:

```
$ make install
```

6. Verify that the installation was successful by running `sqlite3`:

```
$ sqlite3
SQLite version 3.33.0 2020-08-14 16:22:30
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
```

7. To learn more about SQLite, check out the [SQLite Documentation](https://www.sqlite.org/docs.html).

onelinerhub: [How do I install SQLite?](https://onelinerhub.com/sqlite/how-do-i-install-sqlite)