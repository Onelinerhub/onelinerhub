# How do I install Elasticsearch on Windows?
// plain

1. Download the latest version of Elasticsearch from [Elasticsearch Downloads](https://www.elastic.co/downloads/elasticsearch).
2. Unzip the downloaded zip file.
3. Open a command prompt and navigate to the unzipped Elasticsearch directory.
4. Run the following command to start the Elasticsearch server:
```
bin\elasticsearch
```
5. You should see the following output:
```
[INFO ][o.e.n.Node               ] [node-1] initializing ...
[INFO ][o.e.e.NodeEnvironment    ] [node-1] using [1] data paths, mounts [[/ (C:)]], net usable_space [8.2gb], net total_space [9.3gb], types [NTFS]
[INFO ][o.e.e.NodeEnvironment    ] [node-1] heap size [1007.7mb], compressed ordinary object pointers [true]
[INFO ][o.e.n.Node               ] [node-1] node name [node-1] derived from node ID [I9qkRjmBR6mhU1Dhx4_8DQ]; set [node.name] to override
[INFO ][o.e.n.Node               ] [node-1] version[7.3.2], pid[10692], build[default/tar/b7e28a7/2019-07-20T05:20:23.451332Z], OS[Windows 10/10.0/amd64], JVM[Oracle Corporation/Java HotSpot(TM) 64-Bit Server VM/12.0.1/12.0.1+12]
[INFO ][o.e.n.Node               ] [node-1] JVM arguments [-Xms1g, -Xmx1g, -XX:+UseConcMarkSweepGC, -XX:CMSInitiatingOccupancyFraction=75, -XX:+UseCMSInitiatingOccupancyOnly, -XX:+AlwaysPreTouch, -Xss1m, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djna.nosys=true, -XX:-OmitStackTraceInFastThrow, -Dio.netty.noUnsafe=true, -Dio.netty.noKeySetOptimization=true, -Dio.netty.recycler.maxCapacityPerThread=0, -Dlog4j.shutdownHookEnabled=false, -Dlog4j2.disable.jmx=true, -Djava.io.tmpdir=C:\Users\User\Downloads\elasticsearch-7.3.2\elasticsearch-7.3.2\tmp, -XX:+HeapDumpOnOutOfMemoryError, -XX:HeapDumpPath=data, -XX:ErrorFile=logs/hs_err_pid%p.log, -Xlog:gc*,gc+age=trace,safepoint:file=logs/gc.log:utctime,pid,tags:filecount=32,filesize=64m, -Djava.locale.providers=COMPAT, -XX:UseAVX=2, -Dio.netty.allocator.type=unpooled, -XX:MaxDirectMemorySize=4294967296, -Des.path.home=C:\Users\User\Downloads\elasticsearch-7.3.2\elasticsearch-7.3.2]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [aggs-matrix-stats]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [analysis-common]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [ingest-common]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [lang-expression]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [lang-mustache]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [lang-painless]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [mapper-extras]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [parent-join]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [percolator]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [rank-eval]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [reindex]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [repository-url]
[INFO ][o.e.p.PluginsService     ] [node-1] loaded module [transport-netty4]
[INFO ][o.e.p.PluginsService     ] [node-1] no plugins loaded
[INFO ][o.e.n.Node               ] [node-1] initialized
[INFO ][o.e.n.Node               ] [node-1] starting ...
[INFO ][o.e.t.TransportService   ] [node-1] publish_address {127.0.0.1:9300}, bound_addresses {127.0.0.1:9300}
[INFO ][o.e.b.BootstrapChecks    ] [node-1] bound or publishing to a non-loopback address, enforcing bootstrap checks
[INFO ][o.e.c.s.ClusterService   ] [node-1] new_master {node-1}{I9qkRjmBR6mhU1Dhx4_8DQ}{fEu2mP-4Qf6y_lU-JW3l_A}{127.0.0.1}{127.0.0.1:9300}, reason: zen-disco-elected-as-master ([0] nodes joined)
[INFO ][o.e.h.n.Netty4HttpServerTransport] [node-1] publish_address {127.0.0.1:9200}, bound_addresses {127.0.0.1:9200}
[INFO ][o.e.n.Node               ] [node-1] started
```
6. Open your browser and visit `http://localhost:9200` to see the Elasticsearch server running.
7. You can now use Elasticsearch to index and search your data.

## Helpful links
- [Elasticsearch Downloads](https://www.elastic.co/downloads/elasticsearch)
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

onelinerhub: [How do I install Elasticsearch on Windows?](https://onelinerhub.com/elasticsearch/how-do-i-install-elasticsearch-on-windows)