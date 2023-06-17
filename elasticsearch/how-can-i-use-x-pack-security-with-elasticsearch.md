# How can I use X-Pack Security with Elasticsearch?
// plain

X-Pack Security for Elasticsearch is a security solution that provides authentication, authorization, encryption, and audit logging capabilities for Elasticsearch. It is available as part of the X-Pack subscription.

To use X-Pack Security with Elasticsearch, you must first install and configure the X-Pack plugin on your cluster. You can do this by running the following command:

```
./bin/elasticsearch-plugin install x-pack
```

Once the plugin is installed, you can configure X-Pack Security by creating a new user and assigning roles to them. For example, the following command will create a new user called “testuser” with the “superuser” role:

```
./bin/x-pack/users useradd testuser -r superuser
```

You can also configure X-Pack Security to use an external authentication source such as LDAP or Active Directory. This can be done by setting the `xpack.security.authc.realms` configuration option.

Once X-Pack Security is configured, you can use the X-Pack API to manage users, roles, and other security settings. You can also use the X-Pack API to enable audit logging and encryption.

For more information, please see the [X-Pack Security documentation](https://www.elastic.co/guide/en/x-pack/current/security-getting-started.html).

onelinerhub: [How can I use X-Pack Security with Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-use-x-pack-security-with-elasticsearch)