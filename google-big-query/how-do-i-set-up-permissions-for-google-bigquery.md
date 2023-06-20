# How do I set up permissions for Google BigQuery?
// plain

To set up permissions for Google BigQuery, you can use the [Cloud IAM](https://cloud.google.com/iam/) service. This service allows you to control access to Google Cloud Platform resources.

For example, to grant a user access to a BigQuery dataset, you can use the following command:

```
gcloud projects add-iam-policy-binding <project-id> \
    --member user:<user-email> \
    --role roles/bigquery.dataViewer
```

This command will add the user with the specified email address to the project with the specified ID, and grant them the role of BigQuery Data Viewer. This will allow them to view datasets in the project.

You can also use the Cloud IAM service to grant other roles, such as BigQuery Job User, BigQuery Data Editor, and BigQuery User.

Below is a list of the parts of the code and their explanation:

* `gcloud projects add-iam-policy-binding` - this command adds a user to a project and grants them a role
* `<project-id>` - this is the ID of the project to which the user should be added
* `--member user:<user-email>` - this specifies the user to be added to the project, using their email address
* `--role roles/bigquery.dataViewer` - this specifies the role to be granted to the user, in this case BigQuery Data Viewer

## Helpful links

* [Cloud IAM Documentation](https://cloud.google.com/iam/docs/)
* [BigQuery IAM Roles](https://cloud.google.com/bigquery/docs/access-control#bigquery-roles)

onelinerhub: [How do I set up permissions for Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-set-up-permissions-for-google-bigquery)