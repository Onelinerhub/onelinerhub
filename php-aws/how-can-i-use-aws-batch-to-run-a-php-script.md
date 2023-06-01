# How can I use AWS Batch to run a PHP script?
// plain

AWS Batch can be used to run a PHP script in the following way:

1. Create a job definition in the AWS Management Console, specifying the container image, memory requirements, and other parameters for the job.

2. Upload the PHP script to an Amazon S3 bucket.

3. Create a job queue, and add the job definition to the queue.

4. Submit the job to the queue with the Amazon S3 bucket location of the PHP script as a parameter.

5. Monitor the job progress in the AWS Management Console.

6. When the job is complete, the output of the PHP script will be available in the Amazon S3 bucket.

7. To run the script again, simply repeat steps 4-6.

## Example code

```
aws batch submit-job --job-name my-php-job --job-queue my-job-queue --job-definition my-job-definition --parameters bucket="my-s3-bucket",key="my-php-script.php"
```

## Output example

```
{
    "jobId": "12345678-abcd-efgh-ijkl-123456789012"
}
```

## Code explanation

- `aws batch submit-job` - command to submit a job to AWS Batch
- `--job-name my-php-job` - name of the job
- `--job-queue my-job-queue` - name of the job queue
- `--job-definition my-job-definition` - name of the job definition
- `--parameters bucket="my-s3-bucket"` - Amazon S3 bucket where the PHP script is located
- `key="my-php-script.php"` - file name of the PHP script

## Helpful links
- [AWS Batch](https://aws.amazon.com/batch/)
- [Submitting Jobs to AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/submit-jobs.html)
- [AWS CLI Reference for AWS Batch](https://docs.aws.amazon.com/cli/latest/reference/batch/index.html)

onelinerhub: [How can I use AWS Batch to run a PHP script?](https://onelinerhub.com/php-aws/how-can-i-use-aws-batch-to-run-a-php-script)