# How do I download Elasticsearch?
// plain

1. Download the latest version of Elasticsearch from the official website at [elastic.co/downloads/elasticsearch](https://www.elastic.co/downloads/elasticsearch).
2. Extract the downloaded file.
3. Open a command prompt and navigate to the directory where you extracted the file.
4. Execute the following command to start the Elasticsearch server:
```
bin/elasticsearch
```
5. The output should look something like this:
```
[2020-03-25T17:17:10,788][INFO ][o.e.n.Node               ] [node-1] initializing ...
[2020-03-25T17:17:10,895][INFO ][o.e.e.NodeEnvironment    ] [node-1] using [1] data paths, mounts [[/ (rootfs)]], net usable_space [24.4gb], net total_space [29.5gb], spins? [unknown], types [rootfs]
[2020-03-25T17:17:10,898][INFO ][o.e.e.NodeEnvironment    ] [node-1] heap size [989.8mb], compressed ordinary object pointers [true]
[2020-03-25T17:17:10,908][INFO ][o.e.n.Node               ] [node-1] node name [node-1], node ID [V9tTq2GpQX-j_Kv5HUWKJQ]
[2020-03-25T17:17:10,908][INFO ][o.e.n.Node               ] [node-1] version[7.6.0], pid[14686], build[default/tar/2f90bbf/2020-02-14T02:00:36.839739Z], OS[Linux/4.15.0-66-generic/amd64], JVM[AdoptOpenJDK/OpenJDK 64-Bit Server VM/14.0.1/14.0.1+7]
```
6. You can verify that Elasticsearch is running by navigating to [localhost:9200](http://localhost:9200) in your browser.
7. You should see a response like this:
```
{
  "name" : "node-1",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "V9tTq2GpQX-j_Kv5HUWKJQ",
  "version" : {
    "number" : "7.6.0",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "2f90bbf",
    "build_date" : "2020-02-14T02:00:36.839739Z",
    "build_snapshot" : false,
    "lucene_version" : "8.4.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

onelinerhub: [How do I download Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-download-elasticsearch)