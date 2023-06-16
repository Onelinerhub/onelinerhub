# How do I use an Elasticsearch keystore?
// plain

To use an Elasticsearch keystore, you need to create a new keystore first. You can do this by running the following command:
```
bin/elasticsearch-keystore create
```
This will create a new keystore in the `config/` directory, which you can then use to store secure settings.

You can then add settings to the keystore using the `add` command:
```
bin/elasticsearch-keystore add mysetting.secure
```
This will prompt you to enter a value for the setting, which will be securely stored in the keystore.

You can also view the settings stored in the keystore using the `list` command:
```
bin/elasticsearch-keystore list
```
This will output a list of all the settings stored in the keystore.

You can also remove settings from the keystore using the `remove` command:
```
bin/elasticsearch-keystore remove mysetting.secure
```
This will remove the setting from the keystore.

Finally, you can also update the settings stored in the keystore using the `update` command:
```
bin/elasticsearch-keystore update mysetting.secure
```
This will prompt you to enter a new value for the setting, which will be securely stored in the keystore.

## Code explanation
**

* `bin/elasticsearch-keystore create` - creates a new keystore in the config/ directory
* `bin/elasticsearch-keystore add mysetting.secure` - adds a setting to the keystore
* `bin/elasticsearch-keystore list` - lists all the settings stored in the keystore
* `bin/elasticsearch-keystore remove mysetting.secure` - removes a setting from the keystore
* `bin/elasticsearch-keystore update mysetting.secure` - updates a setting stored in the keystore

**## Helpful links**

* [Elasticsearch Keystore Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/keystore.html)

onelinerhub: [How do I use an Elasticsearch keystore?](https://onelinerhub.com/elasticsearch/how-do-i-use-an-elasticsearch-keystore)