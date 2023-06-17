# How do I set up an Elasticsearch Yum repository?
// plain

1. First, create a Yum repository configuration file for Elasticsearch. This should include the repository name, URL and GPG key information. For example:

```
[elasticsearch-7.x]
name=Elasticsearch repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```

2. Then, install the Elasticsearch public signing key with the rpm command:

```
rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
```

3. Finally, use the yum command to install the repository-extras package:

```
yum install elasticsearch-7.x
```

The output of this command should be similar to the following:

```
Installed:
  elasticsearch-7.x.x.noarch

Complete!
```

This will set up an Elasticsearch Yum repository.

## Helpful links

- [Elasticsearch Yum Repository](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/yum.html)
- [Yum Repositories](https://www.centos.org/docs/5/html/yum/sn-yum-repositories.html)

onelinerhub: [How do I set up an Elasticsearch Yum repository?](https://onelinerhub.com/elasticsearch/how-do-i-set-up-an-elasticsearch-yum-repository)