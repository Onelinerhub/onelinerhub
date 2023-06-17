# How do I enable Xpack security in Elasticsearch?
// plain

Enabling X-Pack Security in Elasticsearch requires a few steps:

1. Install the X-Pack plugin:

```
bin/elasticsearch-plugin install x-pack
```

2. Configure the X-Pack security settings in the `elasticsearch.yml` configuration file:

```
xpack.security.enabled: true
xpack.security.transport.ssl.enabled: true
```

3. Create a password for the built-in `elastic` user:

```
bin/elasticsearch-setup-passwords auto
```

4. Restart the Elasticsearch service:

```
systemctl restart elasticsearch
```

5. Check the status of the X-Pack security feature:

```
curl -u elastic:<password> -XGET 'localhost:9200/_xpack?pretty'
```

The output should look like this:

```
{
  "build" : {
    "hash" : "...",
    "date" : "..."
  },
  "license" : {
    "status" : "active",
    "uid" : "...",
    "type" : "basic",
    "expiry_date_in_millis" : 0
  },
  "features" : {
    "security" : {
      "description" : "Security for the Elastic Stack",
      "available" : true,
      "enabled" : true
    }
  }
}
```

The `available` and `enabled` fields should both be `true` to indicate that X-Pack security is enabled.

**## Helpful links**

- [X-Pack Security Documentation](https://www.elastic.co/guide/en/x-pack/current/security-getting-started.html)
- [Elasticsearch Security Configuration](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-settings.html)

onelinerhub: [How do I enable Xpack security in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-enable-xpack-security-in-elasticsearch)