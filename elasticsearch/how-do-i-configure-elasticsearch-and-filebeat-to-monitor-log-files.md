# How do I configure Elasticsearch and Filebeat to monitor log files?
// plain

1. Install Elasticsearch and Filebeat on the same machine.
   - [Elasticsearch Download Page](https://www.elastic.co/downloads/elasticsearch)
   - [Filebeat Download Page](https://www.elastic.co/downloads/beats/filebeat)

2. Configure Filebeat to read the log files you want to monitor.
   ```
   filebeat.inputs:
     - type: log
       paths:
         - /var/log/*.log
   ```

3. Configure Filebeat to output to Elasticsearch.
   ```
   output.elasticsearch:
     hosts: ["localhost:9200"]
   ```

4. Configure the Elasticsearch index template. This will ensure that the fields of your log files are properly mapped in Elasticsearch.
   ```
   curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_template/filebeat -d@/etc/filebeat/filebeat.template.json
   ```

5. Start Filebeat.
   ```
   sudo service filebeat start
   ```

6. Check the Filebeat logs to make sure it is outputting to Elasticsearch.
   ```
   sudo tail -f /var/log/filebeat/filebeat
   ```

7. Check the Elasticsearch logs to make sure it is receiving the data from Filebeat.
   ```
   sudo tail -f /var/log/elasticsearch/elasticsearch.log
   ```

onelinerhub: [How do I configure Elasticsearch and Filebeat to monitor log files?](https://onelinerhub.com/elasticsearch/how-do-i-configure-elasticsearch-and-filebeat-to-monitor-log-files)