# How can I use Amazon Redshift ML to build machine learning models?
// plain

Amazon Redshift ML allows users to build machine learning models using SQL. This is done by using the CREATE MODEL command.

For example, the following code block creates a linear regression model using the `tbl_sales` table:
```sql
CREATE MODEL sales_model
LINEAR REGRESSOR
USING price, quantity, discount
FROM tbl_sales;
```

The code consists of the following parts:
1. `CREATE MODEL`: This is the command used to create a model.
2. `sales_model`: This is the name of the model being created.
3. `LINEAR REGRESSOR`: This specifies the type of model being created.
4. `USING price, quantity, discount`: This is the list of columns used as input features for the model.
5. `FROM tbl_sales`: This is the table from which the data will be used to train the model.

Once the model is created, it can be used to make predictions using the PREDICT command. For example, the following code can be used to make predictions using the `sales_model` model:
```sql
SELECT
  price,
  quantity,
  discount,
  PREDICT(sales_model USING price, quantity, discount)
  AS predicted_sales
FROM tbl_sales;
```

## Helpful links
- [Amazon Redshift ML](https://aws.amazon.com/redshift/machine-learning/)
- [CREATE MODEL Command](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_MODEL.html)
- [PREDICT Command](https://docs.aws.amazon.com/redshift/latest/dg/r_PREDICT.html)

onelinerhub: [How can I use Amazon Redshift ML to build machine learning models?](https://onelinerhub.com/amazon-redshift/how-can-i-use-amazon-redshift-ml-to-build-machine-learning-models)