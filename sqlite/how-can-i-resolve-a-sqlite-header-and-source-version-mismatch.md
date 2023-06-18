# How can I resolve a SQLite header and source version mismatch?
// plain

A SQLite header and source version mismatch occurs when the header file and source code used to compile the SQLite library do not match. This can lead to unexpected errors and program crashes.

To resolve this issue, you must ensure that the header file and source code used to compile the SQLite library are the same version.

For example, if you are using the SQLite source code version 3.33.0, you must use the corresponding SQLite header file version 3.33.0.

To check the version of your SQLite library, you can use the following code:

```
#include <sqlite3.h>
#include <stdio.h>

int main() {
  printf("SQLite version: %s\n", sqlite3_libversion());
  return 0;
}
```

## Output example

```
SQLite version: 3.33.0
```

The code above includes the `sqlite3.h` header file, which is used to compile SQLite, and the `sqlite3_libversion()` function, which returns the version of the SQLite library.

## Helpful links
- [SQLite Version](https://www.sqlite.org/version.html)
- [sqlite3_libversion()](https://www.sqlite.org/c3ref/libversion.html)

onelinerhub: [How can I resolve a SQLite header and source version mismatch?](https://onelinerhub.com/sqlite/how-can-i-resolve-a-sqlite-header-and-source-version-mismatch)