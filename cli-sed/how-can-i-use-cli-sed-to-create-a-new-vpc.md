# How can I use CLI sed to create a new VPC?
// plain

Using the sed command line interface (CLI) you can create a new Virtual Private Network (VPC). The following example will create a VPC with the name "myVPC" in the us-east-1 region:

```
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --region us-east-1 --output text | sed -n -e 's/^VPCID\t//p'
```

The output of this command will be the VPC ID of the newly created VPC.

The code consists of 4 parts:
1. `aws ec2 create-vpc`: This command creates a new VPC.
2. `--cidr-block 10.0.0.0/16`: This specifies the IP range for the VPC.
3. `--region us-east-1`: This specifies the region in which to create the VPC.
4. `--output text`: This specifies the output format.
5. `sed -n -e 's/^VPCID\t//p'`: This command parses the output of the create-vpc command to get the VPC ID.

## Helpful links
- [AWS Documentation - Creating a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario1.html)
- [Linux Sed Command Tutorial](https://www.tutorialspoint.com/unix_commands/sed.htm)

onelinerhub: [How can I use CLI sed to create a new VPC?](https://onelinerhub.com/cli-sed/how-can-i-use-cli-sed-to-create-a-new-vpc)