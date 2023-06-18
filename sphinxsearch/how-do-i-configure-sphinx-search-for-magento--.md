# How do I configure Sphinx search for Magento 2?
// plain

Sphinx Search can be configured for Magento 2 using the following steps:

1. Install the Sphinx Search Extension for Magento 2. This can be done by downloading the extension from https://github.com/Smile-SA/elasticsuite/releases and then copying the extension files to the `app/code` directory of your Magento installation.

2. Enable the extension by running the following command from the Magento root directory:

```
php bin/magento module:enable Smile_ElasticsuiteCore Smile_ElasticsuiteCatalog Smile_ElasticsuiteSwatches Smile_ElasticsuiteVirtualCategory
```

3. Run the following command to install the extension:

```
php bin/magento setup:upgrade
```

4. Configure the Sphinx Search extension in the Magento Admin Panel. Navigate to Stores > Configuration > Smile Elastic Suite > Elastic Suite Configuration > Sphinx Search. Here you can configure the settings for Sphinx Search.

5. Generate the Sphinx configuration file by running the following command from the Magento root directory:

```
php bin/magento dev:urn-catalog-generate-sphinx-config
```

6. Start the Sphinx Search service by running the following command from the Magento root directory:

```
php bin/magento search:sphinx:start
```

7. Test the Sphinx Search service by running the following command from the Magento root directory:

```
php bin/magento search:sphinx:test
```

The output should be:

```
Sphinx Search is running.
```

Once these steps are completed, Sphinx Search should be successfully configured for Magento 2.

onelinerhub: [How do I configure Sphinx search for Magento 2?](https://onelinerhub.com/sphinxsearch/how-do-i-configure-sphinx-search-for-magento--)