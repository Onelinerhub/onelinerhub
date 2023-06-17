# How do I configure xpack.security.authc.realms in Elasticsearch?
// plain

X-Pack Security provides authentication and authorization for Elasticsearch and Kibana. To configure X-Pack Security for Elasticsearch, you will need to specify the authentication realms in the `xpack.security.authc.realms` setting.

For example, the following configuration adds two realms: a native realm that uses the native user database and a file realm that uses a file-based user database:

```
xpack.security.authc.realms:
  native1:
    type: native
  file1:
    type: file
    order: 0
    files.file1.type: users
    files.file1.enabled: true
    files.file1.path: esusers.yml
```

The `type` specifies the type of realm, and `order` specifies the order in which the realms are checked. The `files.file1.type` specifies the type of user database, `files.file1.enabled` specifies whether the realm is enabled and `files.file1.path` specifies the path to the file-based user database.

The output of the above configuration would be:

```
xpack.security.authc.realms:
  native1:
    type: native
  file1:
    type: file
    order: 0
    files.file1.type: users
    files.file1.enabled: true
    files.file1.path: esusers.yml
```

For more information about configuring X-Pack Security for Elasticsearch, see the [official documentation](https://www.elastic.co/guide/en/x-pack/current/setting-up-authentication.html).

onelinerhub: [How do I configure xpack.security.authc.realms in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-configure-xpack-security-authc-realms-in-elasticsearch)