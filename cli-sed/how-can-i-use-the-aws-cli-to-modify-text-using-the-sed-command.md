# How can I use the AWS CLI to modify text using the sed command?
// plain

The AWS CLI can be used to modify text using the sed command. To do this, the command should be written as follows:

```
aws s3 cp s3://<bucket-name>/<object-name> - | sed -e '<sed-command>' | aws s3 cp - s3://<bucket-name>/<object-name>

```

For example, to replace the string "hello" with "goodbye" in an S3 object, the command would look like this:

```
aws s3 cp s3://my-bucket/my-object.txt - | sed -e 's/hello/goodbye/g' | aws s3 cp - s3://my-bucket/my-object.txt

```

## Code explanation

- `aws s3 cp`: This is the AWS CLI command to copy an object from an S3 bucket.
- `s3://<bucket-name>/<object-name>`: This is the location of the S3 object to be copied.
- `-`: This is a special character meaning "standard input".
- `sed -e '<sed-command>'`: This is the sed command used to modify the text.
- `aws s3 cp - s3://<bucket-name>/<object-name>`: This is the AWS CLI command to copy an object to an S3 bucket.

## Helpful links
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html)
- [GNU sed Manual](https://www.gnu.org/software/sed/manual/sed.html)

onelinerhub: [How can I use the AWS CLI to modify text using the sed command?](https://onelinerhub.com/cli-sed/how-can-i-use-the-aws-cli-to-modify-text-using-the-sed-command)