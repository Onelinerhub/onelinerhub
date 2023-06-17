# How do I configure elasticsearch xpack.security.transport.ssl?
// plain

To configure Elasticsearch Xpack.security.transport.ssl, you need to add the following settings to elasticsearch.yml:

```
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.verification_mode: certificate
xpack.security.transport.ssl.keystore.path: <path_to_keystore_file>
xpack.security.transport.ssl.truststore.path: <path_to_truststore_file>
```

The `xpack.security.transport.ssl.enabled` setting enables SSL/TLS for the transport layer.

The `xpack.security.transport.ssl.verification_mode` setting defines the verification mode for the transport layer. Possible values are `none`, `certificate` and `full`.

The `xpack.security.transport.ssl.keystore.path` and `xpack.security.transport.ssl.truststore.path` settings are used to specify the path to the keystore and truststore files.

For more information, please refer to the [Elasticsearch Security Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-settings.html).

onelinerhub: [How do I configure elasticsearch xpack.security.transport.ssl?](https://onelinerhub.com/elasticsearch/how-do-i-configure-elasticsearch-xpack-security-transport-ssl)