# How can I set up and use Elasticsearch on the Yandex Cloud platform?
// plain

1. Create a Yandex Cloud account and log in to the [Yandex Cloud Console](https://console.cloud.yandex.ru/).

2. Create a [virtual machine instance](https://cloud.yandex.ru/docs/compute/concepts/vm-create) with the latest version of Elasticsearch.

3. Connect to the instance via SSH and install the Elasticsearch package using the command `sudo apt-get install elasticsearch`.

4. Configure the Elasticsearch instance by editing the `/etc/elasticsearch/elasticsearch.yml` file.

5. Start the Elasticsearch instance with the command `sudo service elasticsearch start`.

6. Verify that the Elasticsearch instance is running by sending a simple API request to the server with `curl http://localhost:9200`.

7. You should see a response similar to this: `{"name":"instance_name","cluster_name":"elasticsearch","cluster_uuid":"cluster_uuid","version":{"number":"6.2.4","build_hash":"ccec39f","build_date":"2018-04-12T20:37:28.497551Z","build_snapshot":false,"lucene_version":"7.2.1","minimum_wire_compatibility_version":"5.6.0","minimum_index_compatibility_version":"5.0.0"},"tagline":"You Know, for Search"}`

## Helpful links
- [Yandex Cloud Console](https://console.cloud.yandex.ru/)
- [Creating a Virtual Machine Instance](https://cloud.yandex.ru/docs/compute/concepts/vm-create)
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

onelinerhub: [How can I set up and use Elasticsearch on the Yandex Cloud platform?](https://onelinerhub.com/elasticsearch/how-can-i-set-up-and-use-elasticsearch-on-the-yandex-cloud-platform)