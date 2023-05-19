# How to install MongoDB on Mac?
// plain

1. Download the MongoDB Community Server from the [MongoDB Download Center](https://www.mongodb.com/download-center/community).
2. Unpack the downloaded `.tgz` file.
3. Create the `/data/db` directory.
   ```
   $ sudo mkdir -p /data/db
   ```
4. Change the permissions of the `/data/db` directory.
   ```
   $ sudo chown -R `id -u` /data/db
   ```
5. Run the MongoDB daemon.
   ```
   $ mongod
   ```
   Output:
   ```
   2020-04-20T14:45:12.845+0800 I  CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
   2020-04-20T14:45:12.848+0800 I  CONTROL  [initandlisten] MongoDB starting : pid=717 port=27017 dbpath=/data/db 64-bit host=MacBook-Pro.local
   2020-04-20T14:45:12.848+0800 I  CONTROL  [initandlisten] db version v4.2.3
   2020-04-20T14:45:12.848+0800 I  CONTROL  [initandlisten] git version: 6874650b362138df74be53d366bbefc321ea32d4
   2020-04-20T14:45:12.848+0800 I  CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.1.1d  10 Sep 2019
   2020-04-20T14:45:12.848+0800 I  CONTROL  [initandlisten] allocator: system
   2020-04-20T14:45:12.848+0800 I  CONTROL  [initandlisten] modules: none
   2020-04-20T14:45:12.848+0800 I  CONTROL  [initandlisten] build environment:
   2020-04-20T14:45:12.848+0800 I  CONTROL  [initandlisten]     distarch: x86_64
   2020-04-20T14:45:12.848+0800 I  CONTROL  [initandlisten]     target_arch: x86_64
   2020-04-20T14:45:12.848+0800 I  CONTROL  [initandlisten] options: {}
   2020-04-20T14:45:12.849+0800 I  STORAGE  [initandlisten] Detected data files in /data/db created by the 'wiredTiger' storage engine, so setting the active storage engine to 'wiredTiger'.
   2020-04-20T14:45:12.849+0800 I  STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=7680M,session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),
   2020-04-20T14:45:13.845+0800 I  STORAGE  [initandlisten] WiredTiger message [1587485913:84586][717:0x7f9f9f9f2700], txn-recover: Main recovery loop: starting at 15/1472 to 16/256
   2020-04-20T14:45:13.945+0800 I  STORAGE  [initandlisten] WiredTiger message [1587485913:94590][717:0x7f9f9f9f2700], txn-recover: Recovering log 15 through 16
   2020-04-20T14:45:14.039+0800 I  STORAGE  [initandlisten] WiredTiger message [1587485914:3909][717:0x7f9f9f9f2700], txn-recover: Recovering log 16 through 16
   2020-04-20T14:45:14.039+0800 I  STORAGE  [initandlisten] WiredTiger message [1587485914:3912][717:0x7f9f9f9f2700], txn-recover: Recovering log 16 through 16
   2020-04-20T14:45:14.039+0800 I  STORAGE  [initandlisten] WiredTiger message [1587485914:3914][717:0x7f9f9f9f2700], txn-recover: Recovering log 16 through 16
   2020-04-20T14:45:14.039+0800 I  STORAGE  [initandlisten] WiredTiger message [1587485914:3917][717:0x7f9f9f9f2700], txn-recover: Main recovery loop: finished at 16/256
   2020-04-20T14:45:14.039+0800 I  RECOVERY [initandlisten] WiredTiger recoveryTimestamp. Ts: Timestamp(1587485913, 1)
   2020-04-20T14:45:14.053+0800 I  STORAGE  [initandlisten] Timestamp monitor starting
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten]
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten]
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten] ** WARNING: You are running this process as the root user, which is not recommended.
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten]
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten]
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten] ** WARNING: This server is bound to localhost.
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten] **          Remote systems will be unable to connect to this server.
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten] **          Start the server with --bind_ip <address> to specify which IP
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten] **          addresses it should serve responses from, or with --bind_ip_all to
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten] **          bind to all interfaces. If this behavior is desired, start the
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten] **          server with --bind_ip 127.0.0.1 to disable this warning.
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten]
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten]
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten] ** WARNING: soft rlimits too low. Number of files is 256, should be at least 1000
   2020-04-20T14:45:14.054+0800 I  CONTROL  [initandlisten]
   2020-04-20T14:45:14.054+0800 I  FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/data/db/diagnostic.data'
   2020-04-20T14:45:14.054+0800 I  NETWORK  [initandlisten] waiting for connections on port 27017
   ```

## Helpful links

- [MongoDB Download Center](https://www.mongodb.com/download-center/community)
- [MongoDB Documentation](https://docs.mongodb.com/)

group: install

onelinerhub: [How to install MongoDB on Mac?](https://onelinerhub.com/mongodb/how-to-install-mongodb-on-mac)