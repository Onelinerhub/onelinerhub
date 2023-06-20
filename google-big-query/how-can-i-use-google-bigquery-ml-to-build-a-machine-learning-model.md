# How can I use Google BigQuery ML to build a machine learning model?
// plain

Google BigQuery ML (BQML) is a machine learning tool that enables data scientists to build and deploy machine learning models directly within BigQuery. To use BQML to build a machine learning model, you need to:

1. Create a BigQuery dataset - this is where you will store the data and the model.
2. Load the data into BigQuery - you can use a CSV file, or query data from another table.
3. Create a model - you can use the CREATE MODEL statement to create a model in BigQuery.
4. Train the model - you can use the TRAIN MODEL statement to train the model using your data.
5. Evaluate the model - you can use the EVALUATE MODEL statement to evaluate the performance of the model.
6. Deploy the model - you can use the CREATE MODEL statement to deploy the model in BigQuery.
7. Use the model - you can use the PREDICT statement to make predictions using the model.

## Example code

```
CREATE MODEL my_model
OPTIONS
  (model_type='linear_reg',
  input_label_cols=['label']) AS
SELECT
  x,
  y,
  label
FROM
  my_dataset.my_table;

TRAIN MODEL my_model
  WITH OPTIONS
    (epochs=10);

EVALUATE MODEL my_model;

CREATE OR REPLACE MODEL my_model
  OPTIONS
    (model_type='linear_reg',
    input_label_cols=['label']) AS
SELECT
  x,
  y,
  label
FROM
  my_dataset.my_table;

PREDICT
  my_model.predicted_label
FROM
  my_dataset.my_table;
```

## Output example

```
predicted_label
----------------
0.5
0.7
0.3
```

## Helpful links
- [BigQuery ML Documentation](https://cloud.google.com/bigquery/docs/bigqueryml-intro)
- [BigQuery ML Tutorial](https://cloud.google.com/bigquery/docs/bigqueryml-tutorial)

onelinerhub: [How can I use Google BigQuery ML to build a machine learning model?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-ml-to-build-a-machine-learning-model)