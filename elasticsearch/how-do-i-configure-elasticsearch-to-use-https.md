# How do I configure Elasticsearch to use HTTPS?
// plain

To configure Elasticsearch to use HTTPS, you need to do the following:

1. Create a keystore with a private key and a self-signed certificate. For example, using the command `keytool -keystore <keystore_name> -genkey -alias <alias_name>`:

```
$ keytool -keystore my_keystore.jks -genkey -alias my_alias
Enter keystore password:
Re-enter new password:
What is your first and last name?
  [Unknown]:  John Doe
What is the name of your organizational unit?
  [Unknown]:  ES
What is the name of your organization?
  [Unknown]:  Elastic
What is the name of your City or Locality?
  [Unknown]:  London
What is the name of your State or Province?
  [Unknown]:  England
What is the two-letter country code for this unit?
  [Unknown]:  GB
Is CN=John Doe, OU=ES, O=Elastic, L=London, ST=England, C=GB correct?
  [no]:  yes

Generating 2,048 bit RSA key pair and self-signed certificate (SHA256withRSA) with a validity of 90 days
        for: CN=John Doe, OU=ES, O=Elastic, L=London, ST=England, C=GB
```
2. Configure the `xpack.security.http.ssl.keystore.path` and `xpack.security.http.ssl.keystore.password` settings in the `elasticsearch.yml` configuration file, pointing to the previously created keystore and its password:

```
xpack.security.http.ssl.keystore.path: /path/to/my_keystore.jks
xpack.security.http.ssl.keystore.password: my_password
```

3. Restart the Elasticsearch service.

This will enable HTTPS for the Elasticsearch service, and clients will be able to connect to it securely.

## Helpful links
- [Configuring TLS/SSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/configuring-tls.html)
- [SSL and HTTPS](https://www.elastic.co/guide/en/elasticsearch/reference/current/ssl-tls.html)

onelinerhub: [How do I configure Elasticsearch to use HTTPS?](https://onelinerhub.com/elasticsearch/how-do-i-configure-elasticsearch-to-use-https)