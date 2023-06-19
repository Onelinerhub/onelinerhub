# How do I use the Amazon/AWS X-Ray Daemon Docker?
// plain

The Amazon/AWS X-Ray Daemon Docker is a tool used to collect and relay data from applications to the X-Ray service. To use the Docker, you must first install the Docker and the X-Ray SDK.

Once the Docker and SDK are installed, you can run the X-Ray Daemon with the following command:

```
$ docker run -d -e AWS_XRAY_DAEMON_ADDRESS=<IP_ADDRESS> -v /var/run/docker.sock:/var/run/docker.sock amazon/aws-xray-daemon
```

The command above will run the X-Ray Daemon in a Docker container, with the IP address of the X-Ray service set as an environment variable.

The `-d` flag tells the Docker to run the container in the background. The `-v` flag mounts the Docker socket, which allows the X-Ray Daemon to capture data from other containers running on the same host.

In order for the X-Ray Daemon to capture data from other containers, the `AWS_XRAY_DAEMON_ADDRESS` environment variable must be set to the IP address of the X-Ray service.

Once the X-Ray Daemon is running, it will begin collecting data from other containers running on the same host. This data can then be viewed in the X-Ray console.

For more information, see the [X-Ray Daemon Docker Documentation](https://docs.aws.amazon.com/xray-daemon/latest/devguide/xray-daemon-docker.html).

onelinerhub: [How do I use the Amazon/AWS X-Ray Daemon Docker?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-amazon-aws-x-ray-daemon-docker)