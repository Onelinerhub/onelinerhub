# How can I use PostgreSQL on the Yandex Cloud platform?
// plain

PostgreSQL is a powerful, open source object-relational database system. It is available on the Yandex Cloud platform, allowing you to easily deploy and manage PostgreSQL databases in the cloud.

To use PostgreSQL on the Yandex Cloud platform, you will need to create a Yandex.Cloud account and deploy a PostgreSQL server instance. Here is an example of how to do this using the Yandex.Cloud CLI:

```
# Create a Yandex.Cloud account
yc init

# Create a PostgreSQL server instance
yc managed-postgresql create --name <instance-name> --memory 8 --disk-size 10
```

Once the instance is created, you can connect to it using the `yc managed-postgresql client` command.

```
# Connect to the instance
yc managed-postgresql client --name <instance-name>
```

You can also use the Yandex.Cloud console to manage and configure your PostgreSQL instance.

For more information on using PostgreSQL on the Yandex Cloud platform, please refer to the [Yandex.Cloud documentation](https://cloud.yandex.com/docs/managed-postgresql/).

onelinerhub: [How can I use PostgreSQL on the Yandex Cloud platform?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-on-the-yandex-cloud-platform)