# How do I download Elasticsearch for Windows?
// plain

1. Download the latest version of Elasticsearch from the [Elasticsearch Download Page](https://www.elastic.co/downloads/elasticsearch).
2. Choose the Windows zip package and download it to a local directory.
3. Unzip the package to the directory of your choice.
4. Open a command prompt and navigate to the directory where you unzipped the package.
5. Run the command `bin\elasticsearch` to start the Elasticsearch server.
6. You should see the following output in the command prompt:
   ```
   [2017-03-13T10:30:17,846][INFO ][o.e.n.Node               ] [node-1] initializing ...
   [2017-03-13T10:30:17,892][INFO ][o.e.e.NodeEnvironment    ] [node-1] using [1] data paths, mounts [[/ (C:)]], net usable_space [20.4gb], net total_space [47.7gb], types [NTFS]
   [2017-03-13T10:30:17,892][INFO ][o.e.e.NodeEnvironment    ] [node-1] heap size [1007.5mb], compressed ordinary object pointers [true]
   [2017-03-13T10:30:17,936][INFO ][o.e.n.Node               ] [node-1] initialized
   [2017-03-13T10:30:17,936][INFO ][o.e.n.Node               ] [node-1] starting ...
   [2017-03-13T10:30:18,068][INFO ][o.e.t.TransportService   ] [node-1] publish_address {127.0.0.1:9300}, bound_addresses {[::1]:9300}, {127.0.0.1:9300}
   [2017-03-13T10:30:18,099][INFO ][o.e.b.BootstrapChecks    ] [node-1] bound or publishing to a non-loopback address, enforcing bootstrap checks
   [2017-03-13T10:30:18,327][INFO ][o.e.n.Node               ] [node-1] started
   ```
7. You can now access the Elasticsearch API at http://localhost:9200.

**Explanation**
1. Download the latest version of Elasticsearch from the [Elasticsearch Download Page](https://www.elastic.co/downloads/elasticsearch).
- This step downloads the latest version of Elasticsearch from the official website.

2. Choose the Windows zip package and download it to a local directory.
- This step downloads the Windows zip package to a local directory.

3. Unzip the package to the directory of your choice.
- This step unzips the package to the directory of your choice.

4. Open a command prompt and navigate to the directory where you unzipped the package.
- This step opens a command prompt and navigates to the directory where the package was unzipped.

5. Run the command `bin\elasticsearch` to start the Elasticsearch server.
- This step runs the command to start the Elasticsearch server.

6. You should see the following output in the command prompt:
- This step displays the output in the command prompt.

```
[2017-03-13T10:30:17,846][INFO ][o.e.n.Node               ] [node-1] initializing ...
[2017-03-13T10:30:17,892][INFO ][o.e.e.NodeEnvironment    ] [node-1] using [1] data paths, mounts [[/ (C:)]], net usable_space [20.4gb], net total_space [47.7gb], types [NTFS]
[2017-03-13T10:30:17,892][INFO ][o.e.e.NodeEnvironment    ] [node-1] heap size [1007.5mb], compressed ordinary object pointers [true]
[2017-03-13T10:30:17,936][INFO ][o.e.n.Node               ] [node-1] initialized
[2017-03-13T10:30:17,936][INFO ][o.e.n.Node               ] [node-1] starting ...
[2017-03-13T10:30:18,068][INFO ][o.e.t.TransportService   ] [node-1] publish_address {127.0.0.1:9300}, bound_addresses {[::1]:9300}, {127.0.0.1:9300}
[2017-03-13T10:30:18,099][INFO ][o.e.b.BootstrapChecks    ] [node-1] bound or publishing to a non-loopback address, enforcing bootstrap checks
[2017-03-13T10:30:18,327][INFO ][o.e.n.Node               ] [node-1] started
```

7. You can now access the Elasticsearch API at http://localhost:9200.
- This step allows you to access the Elasticsearch API at http://localhost:9200.

onelinerhub: [How do I download Elasticsearch for Windows?](https://onelinerhub.com/elasticsearch/how-do-i-download-elasticsearch-for-windows)