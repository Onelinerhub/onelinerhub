# How do I use Elasticsearch ILM to manage my indices?
// plain

Elasticsearch Index Lifecycle Management (ILM) is a feature that allows you to manage the lifecycle of your indices. It enables you to define an index lifecycle policy that automates the management of your indices.

For example, you can define a policy that will move an index from warm to cold after a certain period of time. You can also specify how many replicas and shards should be used for each index.

To use ILM, you need to first enable it by setting the `xpack.ilm.enabled` setting to `true` in your `elasticsearch.yml` file.

Once ILM is enabled, you can create an ILM policy by using the `PUT _ilm/policy` API. Here is an example of a policy that moves an index from warm to cold after 7 days:

```
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "warm": {
        "min_age": "7d",
        "actions": {
          "set_priority": {
            "priority": 50
          }
        }
      },
      "cold": {
        "min_age": "14d",
        "actions": {
          "freeze": {}
        }
      }
    }
  }
}
```

Once the policy is created, you can apply it to an index by using the `PUT _ilm/policy/my_policy` API. Here is an example of applying the policy to an index named `my_index`:

```
PUT my_index/_settings
{
  "index.lifecycle.name": "my_policy"
}
```

The index will then be managed according to the policy you specified.

## Helpful links
- [Elasticsearch Index Lifecycle Management Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/ilm.html)
- [Elasticsearch ILM API Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/ilm-api.html)

onelinerhub: [How do I use Elasticsearch ILM to manage my indices?](https://onelinerhub.com/elasticsearch/how-do-i-use-elasticsearch-ilm-to-manage-my-indices)