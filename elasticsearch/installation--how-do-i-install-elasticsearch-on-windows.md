# installation

How do I install Elasticsearch on Windows?
// plain

1. Download the latest version of Elasticsearch from [the official website](https://www.elastic.co/downloads/elasticsearch).
2. Unzip the downloaded file and move the `elasticsearch-x.x.x` folder to the directory of your choice.
3. Open a command prompt and navigate to the Elasticsearch directory.
4. Run the following command to start the Elasticsearch service:
```
bin\elasticsearch.bat
```
5. You should see an output like this:
```
[2020-01-01T12:34:56,345][INFO ][o.e.n.Node               ] [node_1] initializing ...
[2020-01-01T12:34:56,345][INFO ][o.e.e.NodeEnvironment    ] [node_1] using [1] data paths, mounts [[/ (C:)]], net usable_space [87.9gb], net total_space [232.3gb], types [NTFS]
[2020-01-01T12:34:56,345][INFO ][o.e.e.NodeEnvironment    ] [node_1] heap size [1.9gb], compressed ordinary object pointers [true]
[2020-01-01T12:34:56,345][INFO ][o.e.n.Node               ] [node_1] node name [node_1], node ID [mW3A3A-mTKmV2vTg7SzV_w]
[2020-01-01T12:34:56,345][INFO ][o.e.n.Node               ] [node_1] version[7.6.2], pid[26736], build[default/zip/f09d4f495d0c951d4f1fe2f2c5d2698f3f8e4eef/2020-04-21T17:47:17.086291Z], OS[Windows 10/10.0/amd64], JVM[Oracle Corporation/Java HotSpot(TM) 64-Bit Server VM/11.0.7+8/25.272-b10]
```

6. Open a web browser and navigate to `http://localhost:9200` to verify that the Elasticsearch service is running.
7. You should see a response like this:
```
{
  "name" : "node_1",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "mW3A3A-mTKmV2vTg7SzV_w",
  "version" : {
    "number" : "7.6.2",
    "build_flavor" : "default",
    "build_type" : "zip",
    "build_hash" : "f09d4f495d0c951d4f1fe2f2c5d2698f3f8e4eef",
    "build_date" : "2020-04-21T17:47:17.086291Z",
    "build_snapshot" : false,
    "lucene_version" : "8.5.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

onelinerhub: [installation

How do I install Elasticsearch on Windows?](https://onelinerhub.com/elasticsearch/installation--how-do-i-install-elasticsearch-on-windows)