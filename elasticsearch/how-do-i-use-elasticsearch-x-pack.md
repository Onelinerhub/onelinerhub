# How do I use Elasticsearch X-Pack?
// plain

X-Pack is an Elasticsearch plugin that provides authentication, security, alerting, monitoring, reporting, and graph capabilities. It is available for free with basic features, or as part of the subscription-based X-Pack Gold and Platinum tiers.

To install X-Pack on an existing Elasticsearch cluster, run the following command:

```
$ bin/elasticsearch-plugin install x-pack
```

This will install the X-Pack plugin into the Elasticsearch plugins directory. Once installed, you can enable the features you need by setting the appropriate configuration settings in the elasticsearch.yml file.

To enable authentication, for example, you would add the following to the elasticsearch.yml file:

```
xpack.security.enabled: true
```

To enable monitoring, you would add the following:

```
xpack.monitoring.enabled: true
```

Once the desired features are enabled, you can start using the X-Pack features. For example, to create an authentication user, you can use the X-Pack API:

```
$ curl -XPUT -u elastic 'http://localhost:9200/_xpack/security/user/<username>' -d '{
  "password" : "<password>",
  "full_name" : "<full_name>",
  "email" : "<email>",
  "roles" : [ "<role>" ],
  "enabled" : true
}'
```

This will create a user with the specified username, password, full name, email, and role.

For more information on using X-Pack, please see the [X-Pack documentation](https://www.elastic.co/guide/en/x-pack/current/xpack-introduction.html).

onelinerhub: [How do I use Elasticsearch X-Pack?](https://onelinerhub.com/elasticsearch/how-do-i-use-elasticsearch-x-pack)