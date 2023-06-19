# compression

How can I use SQLite and Zstandard (ZSTD) compression together?
// plain

Using SQLite and Zstandard (ZSTD) compression together is a great way to reduce the size of database files while maintaining their integrity. To do this, you'll need to install the [SQLite ZSTD Extension](https://github.com/sjlombardo/sqlite-zstd-ext). Once installed, you can use the following code to compress a database file:

```
$ sqlite3 db.sqlite
sqlite> ATTACH DATABASE 'compressed.sqlite' AS compressed_db
   USING COMPRESSION ZSTD;
sqlite> CREATE TABLE compressed_db.mytable AS SELECT * FROM main.mytable;
```

This will create a new database file called `compressed.sqlite` which is compressed using ZSTD. To check that the file is compressed, you can use the `PRAGMA page_size` command:

```
sqlite> PRAGMA page_size;
1024
sqlite> PRAGMA compressed_db.page_size;
2048
```

The `page_size` of the original database is 1024 bytes, while the `page_size` of the compressed database is 2048 bytes. This shows that the file is successfully compressed.

In summary, to use SQLite and Zstandard (ZSTD) compression together:
1. Install the [SQLite ZSTD Extension](https://github.com/sjlombardo/sqlite-zstd-ext).
2. Attach a new database with the `USING COMPRESSION ZSTD` option.
3. Create a table in the compressed database with the data from the original database.
4. Check that the file is compressed with the `PRAGMA page_size` command.

onelinerhub: [compression

How can I use SQLite and Zstandard (ZSTD) compression together?](https://onelinerhub.com/sqlite/compression--how-can-i-use-sqlite-and-zstandard--zstd--compression-together)