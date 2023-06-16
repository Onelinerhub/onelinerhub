# stack

How do I set up and use the ELK stack with Elasticsearch?
// plain

The ELK stack is a combination of open source tools - Elasticsearch, Logstash, and Kibana - that can be used to collect, store, and analyze data. To set up and use the ELK stack with Elasticsearch, you will need to install and configure each of the components.

1. Install Elasticsearch:
    - Download the latest version of Elasticsearch from the [Elastic website](https://www.elastic.co/downloads/elasticsearch).
    - Unzip the downloaded file and run `bin/elasticsearch` to start the service.

2. Install Logstash:
    - Download the latest version of Logstash from the [Elastic website](https://www.elastic.co/downloads/logstash).
    - Unzip the downloaded file and run `bin/logstash` to start the service.

3. Install Kibana:
    - Download the latest version of Kibana from the [Elastic website](https://www.elastic.co/downloads/kibana).
    - Unzip the downloaded file and run `bin/kibana` to start the service.

4. Create an index in Elasticsearch:
    ```
    curl -XPUT 'localhost:9200/my_index?pretty'
    ```
    Output:
    ```
    {
      "acknowledged" : true,
      "shards_acknowledged" : true,
      "index" : "my_index"
    }
    ```

5. Configure Logstash to collect data and index it into Elasticsearch:
    - Create a Logstash configuration file.
    - Set the input source, filter, and output destination.
    - Start Logstash with the configuration file `bin/logstash -f logstash.conf`.

6. Use Kibana to visualize the data:
    - Go to `http://localhost:5601` in your browser.
    - Create an index pattern to view the data in Kibana.

Once you have completed these steps, you will be able to use the ELK stack with Elasticsearch to collect, store, and analyze data.

onelinerhub: [stack

How do I set up and use the ELK stack with Elasticsearch?](https://onelinerhub.com/elasticsearch/stack--how-do-i-set-up-and-use-the-elk-stack-with-elasticsearch)