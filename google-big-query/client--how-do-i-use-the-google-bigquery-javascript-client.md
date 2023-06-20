# client

How do I use the Google BigQuery JavaScript client?
// plain

The Google BigQuery JavaScript client is a library that allows JavaScript applications to access the Google BigQuery API. It can be used to query data from BigQuery, upload and download data, and manage datasets and tables.

To use the Google BigQuery JavaScript client, you first need to install the library:

```
npm install @google-cloud/bigquery
```

Once installed, you can import the library into your JavaScript application:

```
const {BigQuery} = require('@google-cloud/bigquery');
```

You can then create a BigQuery client object, which can be used to interact with the BigQuery API:

```
const bigquery = new BigQuery();
```

You can then use the client object to query data from BigQuery, upload and download data, and manage datasets and tables. For example, you can use the `query` method to execute a query and get the results:

```
const [rows] = await bigquery.query(`
  SELECT name
  FROM \`bigquery-public-data.usa_names.usa_1910_current\`
  WHERE gender = 'M'
  LIMIT 10
`);

console.log('Names:');
rows.forEach(row => console.log(row.name));
```

## Output example


```
Names:
William
John
Robert
Joseph
Charles
George
Edward
Frank
Thomas
Henry
```

## Code explanation


1. `npm install @google-cloud/bigquery`: This command installs the Google BigQuery JavaScript library.
2. `const {BigQuery} = require('@google-cloud/bigquery');`: This line imports the BigQuery library into the JavaScript application.
3. `const bigquery = new BigQuery();`: This line creates a BigQuery client object.
4. `const [rows] = await bigquery.query(`: This line executes a query and gets the results.

For more information, see the [Google BigQuery JavaScript Client Library documentation](https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-nodejs).

onelinerhub: [client

How do I use the Google BigQuery JavaScript client?](https://onelinerhub.com/google-big-query/client--how-do-i-use-the-google-bigquery-javascript-client)