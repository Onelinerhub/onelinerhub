# How do I create a user in Elasticsearch?
// plain

Creating a user in Elasticsearch is a simple process. The following example code will create a user with the username `elastic` and the password `changeme`:

```
PUT /_security/user/elastic
{
  "password" : "changeme",
  "roles" : [ "superuser" ]
}
```

This will return an output indicating that the user was created successfully:

```
{
  "created" : true
}
```

The code consists of a `PUT` request to the endpoint `/_security/user/elastic`, followed by a JSON object containing the user's password and roles. The roles in this example are set to `superuser`, which gives the user full access to the cluster.

You can also specify additional roles, such as `admin`, `monitoring` or `kibana_user`. For more information on roles and user management, see [the Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-users.html).

onelinerhub: [How do I create a user in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-create-a-user-in-elasticsearch)