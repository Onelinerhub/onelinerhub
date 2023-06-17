# How do I install Elasticsearch on Ubuntu 22.04?
// plain

1. Download the .deb package from the Elastic website: [https://www.elastic.co/downloads/elasticsearch](https://www.elastic.co/downloads/elasticsearch).
2. Install the package with **`sudo dpkg -i elasticsearch-<version>.deb`**.
3. Enable the Elasticsearch service with **`sudo systemctl enable elasticsearch.service`**.
4. Start the Elasticsearch service with **`sudo systemctl start elasticsearch.service`**.
5. Check the status of the Elasticsearch service with **`sudo systemctl status elasticsearch.service`**.

```
sudo systemctl status elasticsearch.service

● elasticsearch.service - Elasticsearch
   Loaded: loaded (/usr/lib/systemd/system/elasticsearch.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2020-05-26 11:46:30 UTC; 1min 10s ago
     Docs: http://www.elastic.co
 Main PID: 28101 (java)
    Tasks: 47 (limit: 4661)
   CGroup: /system.slice/elasticsearch.service
           └─28101 /usr/bin/java -Xms1g -Xmx1g -XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -XX:+AlwaysPreTouch -Xss1m -Djava.awt.headless=true -Dfile.encoding=UTF-8 -Djna.nosys=true -XX:-OmitStackTraceInFastThrow -Dio.netty.noUnsafe=true -Dio.netty.noKeySetOptimization=true -Dio.netty.recycler.maxCapacityPerThread=0 -Dlog4j.shutdownHookEnabled=false -Dlog4j2.disable.jmx=true -Dlog4j.skipJansi=true -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=data -XX:ErrorFile=logs/hs_err_pid%p.log -Xlog:gc*,gc+age=trace,safepoint:file=logs/gc.log:utctime,pid,tags:filecount=32,filesize=64m -Djava.locale.providers=COMPAT -XX:UseAVX=2 -Des.path.home=/usr/share/elasticsearch -cp /usr/share/elasticsearch/lib/* org.elasticsearch.bootstrap.Elasticsearch -p /var/run/elasticsearch/elasticsearch.pid --quiet
```

6. Check if Elasticsearch is running by making a request to the server: **`curl -X GET "localhost:9200"`**.

```
curl -X GET "localhost:9200"

{
  "name" : "node-1",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "HXF5U5-lQ-q-7wTf-q3-A",
  "version" : {
    "number" : "7.6.2",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "ef48eb35cf30adf4db14086e8aabd07ef6fb113f",
    "build_date" : "2020-03-26T06:34:37.794943Z",
    "build_snapshot" : false,
    "lucene_version" : "8.4.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

7. You can now access the Elasticsearch API at `localhost:9200`.

For more detailed instructions, please refer to the official Elasticsearch documentation: [https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html).

onelinerhub: [How do I install Elasticsearch on Ubuntu 22.04?](https://onelinerhub.com/elasticsearch/how-do-i-install-elasticsearch-on-ubuntu------)