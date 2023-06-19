# How do I create and use Amazon EC2 key pairs?
// plain

1. Create an Amazon EC2 key pair:
   - Log in to the [AWS Management Console](https://console.aws.amazon.com/) and select EC2.
   - In the navigation pane, choose **Key Pairs** under **NETWORK & SECURITY**.
   - Choose **Create Key Pair**.
   - Enter a name for the key pair and choose **Create**.
   - The private key file is automatically downloaded by your browser.
   - The base file name is the name you specified as the name of your key pair, and the file name extension is .pem.

2. Use the key pair:
   - When you launch an instance, you specify the key pair that you want to use.
   - When you connect to the instance, you must provide the corresponding private key.
   - For example, the following command connects to an instance using SSH:
   ```
   ssh -i /path/my-key-pair.pem ec2-user@ec2-198-51-100-1.compute-1.amazonaws.com
   ```
   - The `-i` option specifies the private key to use for authentication.

## Helpful links
- [Create a Key Pair Using Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair)
- [Connect to Your Linux Instance Using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

onelinerhub: [How do I create and use Amazon EC2 key pairs?](https://onelinerhub.com/amazon-redshift/how-do-i-create-and-use-amazon-ec--key-pairs)