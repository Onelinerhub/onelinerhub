# How do I enable X11 forwarding on an Ubuntu instance in Amazon EC2?
// plain

To enable X11 forwarding on an Ubuntu instance in Amazon EC2, you need to:

1. Log in to your EC2 instance with SSH.
2. Install an X11 server on the instance. For example:
```
sudo apt-get install xorg
```
3. Install an X11 forwarding package. For example:
```
sudo apt-get install xauth
```
4. Edit the sshd_config file to enable X11 forwarding. For example:
```
sudo nano /etc/ssh/sshd_config
```
Add the following line to the file:
```
X11Forwarding yes
```
5. Save the file and exit.
6. Restart the ssh service. For example:
```
sudo service ssh restart
```
7. Connect to the instance with SSH and add the -X flag to enable X11 forwarding. For example:
```
ssh -X ubuntu@ec2-xx-xxx-xxx-xxx.compute-1.amazonaws.com
```

## Helpful links
- [How to Connect to Your Amazon EC2 Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html)
- [How to Set Up X11 Forwarding](https://www.digitalocean.com/community/tutorials/how-to-set-up-x11-forwarding-on-ubuntu-18-04)

onelinerhub: [How do I enable X11 forwarding on an Ubuntu instance in Amazon EC2?](https://onelinerhub.com/amazon-redshift/how-do-i-enable-x---forwarding-on-an-ubuntu-instance-in-amazon-ec-)