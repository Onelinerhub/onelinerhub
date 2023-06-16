# How do I set up authentication for Elasticsearch?
// plain

To set up authentication for Elasticsearch, you need to enable Shield and configure roles and users. Shield is a plugin for Elasticsearch and is available in the X-Pack.

First, you need to install Shield in Elasticsearch. You can do this by running the command:

```
bin/elasticsearch-plugin install x-pack
```

This will install the X-Pack in Elasticsearch.

Next, you need to configure roles and users. You can do this by creating a `elasticsearch-users.yml` file and adding the following code:

```
admin:
  password: "adminpassword"
  roles: admin

user:
  password: "userpassword"
  roles: user
```

This will create two users, `admin` and `user`, with the respective passwords. The `admin` user will have the `admin` role and the `user` user will have the `user` role.

Finally, you need to load the `elasticsearch-users.yml` file into Elasticsearch. You can do this by running the command:

```
bin/elasticsearch-users useradd -b -c elasticsearch-users.yml
```

This will load the users and roles into Elasticsearch.

Once you have done this, authentication will be enabled for Elasticsearch.

## Code explanation


1. `bin/elasticsearch-plugin install x-pack`: This command installs the X-Pack in Elasticsearch.
2. `admin: password: "adminpassword" roles: admin`: This creates the `admin` user with the `admin` role and the `adminpassword` password.
3. `user: password: "userpassword" roles: user`: This creates the `user` user with the `user` role and the `userpassword` password.
4. `bin/elasticsearch-users useradd -b -c elasticsearch-users.yml`: This command loads the users and roles from the `elasticsearch-users.yml` file into Elasticsearch.

## Helpful links

- [Elasticsearch Security](https://www.elastic.co/guide/en/x-pack/current/security-getting-started.html)
- [Installing X-Pack](https://www.elastic.co/guide/en/x-pack/current/installing-xpack.html)
- [X-Pack User Management](https://www.elastic.co/guide/en/x-pack/current/managing-users.html)

onelinerhub: [How do I set up authentication for Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-set-up-authentication-for-elasticsearch)