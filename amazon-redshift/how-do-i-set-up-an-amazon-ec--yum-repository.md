# How do I set up an Amazon EC2 YUM repository?
// plain

1. First, create an Amazon EC2 instance.
2. Connect to the instance using SSH.
3. Install the `yum-utils` package using the command `sudo yum install yum-utils`.
4. Create a `.repo` file in `/etc/yum.repos.d/` directory using the command `sudo vi /etc/yum.repos.d/amazon-ec2.repo`.
5. Add the following lines to the `.repo` file:
```
[ec2-yumrepo]
name=Amazon EC2 YUM Repo
baseurl=http://ec2-downloads.s3.amazonaws.com/ec2-yumrepo/
enabled=1
gpgcheck=0
```
6. Save and exit the `.repo` file.
7. Refresh the YUM repository using the command `sudo yum repolist`.

## Helpful links
- [Amazon EC2 Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
- [YUM Documentation](https://yum.baseurl.org/wiki/YumRepositories)

onelinerhub: [How do I set up an Amazon EC2 YUM repository?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-an-amazon-ec--yum-repository)