# How can I use Amazon Redshift to power my Power BI dashboard?
// plain

You can use Amazon Redshift to power your Power BI dashboard by connecting it to the Power BI service. To do this, you need to create an ODBC connection in the Power BI Service.

Once you have created the ODBC connection, you can use the following code to connect to your Amazon Redshift cluster from the Power BI Service:

```
connectionString = "DRIVER={Amazon Redshift (x64)};SERVER=<cluster_endpoint>;PORT=<port>;DATABASE=<database_name>;UID=<username>;PWD=<password>"
```

You can then use this connection string to access your data in Amazon Redshift from the Power BI service. Once you have connected to your data, you can use the Power BI Desktop to create your dashboard.

To create a dashboard, you can use the Power BI Desktop to create visuals, such as charts, tables, and other visualizations. You can also create filters and slicers to further refine your data.

Once you have created your dashboard, you can publish it to the Power BI Service. This will allow you to share your dashboard with other users and view it on any device.

You can find more information about using Amazon Redshift with Power BI [here](https://docs.microsoft.com/en-us/power-bi/connect-data/service-amazon-redshift).

onelinerhub: [How can I use Amazon Redshift to power my Power BI dashboard?](https://onelinerhub.com/amazon-redshift/how-can-i-use-amazon-redshift-to-power-my-power-bi-dashboard)