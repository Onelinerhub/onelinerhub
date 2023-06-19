# How do I call sqlitepcl.raw.setprovider() when using SQLite?
// plain

To call `sqlitePCL.raw.setProvider()` when using SQLite, you need to include the `sqlitePCLRaw.core` NuGet package in your project.

You can then use the `sqlitePCL.raw.setProvider()` method to set the SQLite provider. This method takes two parameters:

1. `sqlitePCL.IProvider`: This is the SQLite provider that you want to set.
2. `bool`: This is a boolean value that indicates whether the provider should be set as the default provider.

The following code block shows an example of how to call `sqlitePCL.raw.setProvider()`:

```
using sqlitePCL;
using sqlitePCL.raw;

// ...

// Set the SQLite provider
var provider = new sqlite3Provider_e_sqlite3();
raw.setProvider(provider, true);
```

This example sets the `sqlite3Provider_e_sqlite3` provider as the default provider.

## Helpful links

- [sqlitePCL.raw.setProvider()](https://github.com/ericsink/SQLitePCL.raw/blob/master/doc/sqlitepclraw.core/api/setprovider.md)
- [sqlitePCL.IProvider](https://github.com/ericsink/SQLitePCL.raw/blob/master/doc/sqlitepclraw.core/api/IProvider.md)

onelinerhub: [How do I call sqlitepcl.raw.setprovider() when using SQLite?](https://onelinerhub.com/sqlite/how-do-i-call-sqlitepcl-raw-setprovider---when-using-sqlite)