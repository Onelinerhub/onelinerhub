# How can I create and manage Amazon Redshift jobs?
// plain

Creating and managing Amazon Redshift jobs is accomplished by using SQL queries and the AWS Management Console.

1. Create a SQL query to define the job:

```
CREATE TABLE my_table (
  id INTEGER NOT NULL,
  name VARCHAR(50)
);
```

2. Schedule the job using the AWS Management Console:

- Log in to the AWS Management Console.
- Select the Amazon Redshift service.
- Select the “Scheduled Jobs” tab.
- Click the “Create Job” button.
- Enter the SQL query in the “Job Definition” field.
- Enter a schedule for the job.
- Click the “Create Job” button.

3. Monitor the job:

- Log in to the AWS Management Console.
- Select the Amazon Redshift service.
- Select the “Scheduled Jobs” tab.
- Select the job from the list.
- Click the “Run Now” button to manually run the job.
- Check the “Job Status” to see the job's progress.

## Helpful links

- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)
- [Creating and Managing Amazon Redshift Jobs](https://aws.amazon.com/redshift/creating-managing-jobs/)

onelinerhub: [How can I create and manage Amazon Redshift jobs?](https://onelinerhub.com/amazon-redshift/how-can-i-create-and-manage-amazon-redshift-jobs)