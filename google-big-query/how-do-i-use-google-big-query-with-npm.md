# How do I use Google Big Query with npm?
// plain

Google BigQuery is a serverless, highly scalable data warehouse that enables you to run analytics over massive datasets. It can be used with npm (Node Package Manager) to access BigQuery from Node.js applications.

Using BigQuery with npm requires the installation of the `@google-cloud/bigquery` package. This can be done with the following command:

```
npm install --save @google-cloud/bigquery
```

Once the package is installed, you can access BigQuery from your Node.js application. Here is an example of how to list the datasets in your BigQuery project:

```
const {BigQuery} = require('@google-cloud/bigquery');

// Create a BigQuery client
const bigquery = new BigQuery();

async function listDatasets() {
  // Lists all datasets in the current project
  const [datasets] = await bigquery.getDatasets();

  console.log('Datasets:');
  datasets.forEach(dataset => console.log(dataset.id));
}

listDatasets();
```

The output of this code would be a list of all the datasets in the current project:

```
Datasets:
my_dataset_1
my_dataset_2
...
```

For more information on using BigQuery with npm, see the [Google Cloud Node.js documentation](https://cloud.google.com/nodejs/docs/reference/bigquery/2.4.x/).

onelinerhub: [How do I use Google Big Query with npm?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-with-npm)