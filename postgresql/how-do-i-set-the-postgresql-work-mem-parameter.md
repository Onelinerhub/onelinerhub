# How do I set the PostgreSQL work_mem parameter?
// plain

The `work_mem` parameter sets the amount of memory to be used by the server while performing internal operations such as sorting and hashing. To set this parameter, you can use the `ALTER SYSTEM` command.

For example, to set the `work_mem` parameter to 1MB, you can run the following command:

```
ALTER SYSTEM SET work_mem = '1MB';
```

The output of this command should be:

```
ALTER SYSTEM
```

The parts of this command are:

* `ALTER SYSTEM`: This command is used to modify the configuration parameters of the PostgreSQL server.
* `SET work_mem`: This sets the value of the `work_mem` parameter.
* `'1MB'`: This is the value of the `work_mem` parameter. This can be any value between `1KB` and `64MB`.

For more information, please refer to the [official PostgreSQL documentation](https://www.postgresql.org/docs/current/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-WORK-MEM).

onelinerhub: [How do I set the PostgreSQL work_mem parameter?](https://onelinerhub.com/postgresql/how-do-i-set-the-postgresql-work-mem-parameter)