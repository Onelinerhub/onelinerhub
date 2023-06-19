# How can I use Amazon EC2 to host a YouTube video?
// plain

Amazon EC2 can be used to host YouTube videos by creating an EC2 instance and setting up a web server.

The following example code can be used to create an EC2 instance:

```
aws ec2 run-instances --image-id ami-12345678 --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-12345678 --subnet-id subnet-12345678
```

The output of the command would be the Instance ID of the newly created instance.

The web server can then be set up on the EC2 instance. This can be done by connecting to the instance using SSH and then following the relevant instructions for setting up the web server.

Once the web server is set up, the YouTube video can be uploaded to the web server and made available to viewers.

## Helpful links
- [Amazon EC2](https://aws.amazon.com/ec2/)
- [Setting up a web server](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-16-04)

onelinerhub: [How can I use Amazon EC2 to host a YouTube video?](https://onelinerhub.com/amazon-redshift/how-can-i-use-amazon-ec--to-host-a-youtube-video)