# How to list databases in MongoDB?
// plain

To list databases in MongoDB, use the `show dbs` command. This command will display a list of all databases on the MongoDB server.

## Example

```
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
```

The output of the `show dbs` command will list all databases on the MongoDB server, along with their respective sizes in GB. The `admin`, `config`, and `local` databases are the default databases that come with MongoDB.

## Code explanation

- `show dbs`: command to list all databases on the MongoDB server
- `admin`, `config`, and `local`: default databases that come with MongoDB

## Helpful links
- [MongoDB Documentation - show dbs](https://docs.mongodb.com/manual/reference/program/mongo/#bin.mongo)

onelinerhub: [How to list databases in MongoDB?](https://onelinerhub.com/mongodb/how-to-list-databases-in-mongodb)