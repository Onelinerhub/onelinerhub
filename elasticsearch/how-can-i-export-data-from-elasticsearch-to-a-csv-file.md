# How can I export data from Elasticsearch to a CSV file?
// plain

Exporting data from Elasticsearch to a CSV file can be done using the [Elasticsearch-CSV library](https://github.com/elastic/elasticsearch-csv).

The library provides a command line tool called `es2csv` that can be used to export data from an Elasticsearch index to a CSV file.

For example, the following command can be used to export data from the `my_index` index to the `my_data.csv` file:
```
es2csv -u http://localhost:9200 -i my_index -f my_data.csv
```

The command above will export all fields from the `my_index` index to the `my_data.csv` file. If you want to export only specific fields, you can use the `-f` option to specify the fields to be exported.

For example, the following command will export only the `title` and `date` fields from the `my_index` index to the `my_data.csv` file:
```
es2csv -u http://localhost:9200 -i my_index -f my_data.csv -f title,date
```

If you need to export data from multiple indices, you can use the `-i` option to specify the indices to be exported.

For example, the following command will export all fields from the `my_index_1` and `my_index_2` indices to the `my_data.csv` file:
```
es2csv -u http://localhost:9200 -i my_index_1,my_index_2 -f my_data.csv
```

The library also provides a Python API that can be used to export data from Elasticsearch to a CSV file programmatically.

onelinerhub: [How can I export data from Elasticsearch to a CSV file?](https://onelinerhub.com/elasticsearch/how-can-i-export-data-from-elasticsearch-to-a-csv-file)