# How do I install the Redis version compatible with PHP 8?
// plain

1. Install Redis compatible with PHP 8 by downloading the source code from [Redis.io](https://redis.io/download).
2. Extract the downloaded files and navigate to the directory in the terminal.
3. Run the following command to compile the source code: ```$ make distclean```
4. Run the following command to configure and compile the source code: ```$ make MALLOC=libc```
5. Run the following command to install the compiled source code: ```$ sudo make install```
6. To check if Redis is installed correctly, run the following command: ```$ redis-server -v```
7. The output should be something similar to the following: ```Redis server v=5.0.7 sha=00000000:0 malloc=libc bits=64 build=c7a2b8e6f7f2a6f0```

## Helpful links
- [Redis.io](https://redis.io/download)
- [Redis Quick Start](https://redis.io/topics/quickstart)

onelinerhub: [How do I install the Redis version compatible with PHP 8?](https://onelinerhub.com/predis/how-do-i-install-the-redis-version-compatible-with-php--)