# How do I install and configure Elasticsearch on Ubuntu?
// plain

1. Install Java 8:
```
sudo apt-get install openjdk-8-jre
```
2. Download and install the Public Signing Key:
```
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
```
3. Add the Elastic repository to your system:
```
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
```
4. Update the apt package manager:
```
sudo apt-get update
```
5. Install Elasticsearch:
```
sudo apt-get install elasticsearch
```
6. Configure Elasticsearch:

Edit the `/etc/elasticsearch/elasticsearch.yml` file and set the cluster and node names:
```
cluster.name: my-cluster
node.name: node-1
```
7. Start Elasticsearch:
```
sudo systemctl start elasticsearch
```

**## Helpful links**

* [Installing Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)
* [Configuring Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/configuring-elasticsearch.html)
* [Managing Services with systemd](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)

onelinerhub: [How do I install and configure Elasticsearch on Ubuntu?](https://onelinerhub.com/elasticsearch/how-do-i-install-and-configure-elasticsearch-on-ubuntu)