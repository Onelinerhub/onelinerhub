# How do I set up basic authentication for Elasticsearch?
// plain

Setting up basic authentication for Elasticsearch can be done using the X-Pack security feature. X-Pack security provides authentication, authorization, and encryption for the Elastic Stack.

To set up basic authentication, you first need to install X-Pack. This can be done by running the following command:

```
bin/elasticsearch-plugin install x-pack
```

Once X-Pack is installed, you can enable basic authentication by adding the following configuration to your elasticsearch.yml file:

```
xpack.security.authc.realms.native.native1.order: 0
xpack.security.authc.realms.native.native1.type: native
```

You can then create a user with the following command:

```
bin/elasticsearch-users useradd <username> -p <password> -r superuser
```

Once the user is created, you can log in to Elasticsearch using the username and password you provided.

## Helpful links
- [X-Pack Security Documentation](https://www.elastic.co/guide/en/x-pack/current/security-getting-started.html)
- [Elasticsearch Users Command Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-cli-users.html)

onelinerhub: [How do I set up basic authentication for Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-set-up-basic-authentication-for-elasticsearch)