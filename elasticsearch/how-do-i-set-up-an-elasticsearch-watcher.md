# How do I set up an Elasticsearch watcher?
// plain

Setting up an Elasticsearch watcher is a 3-step process:

1. Create a watch: A watch is a JSON document that defines the conditions that must be met for the watch to be triggered. For example:
```
PUT _watcher/watch/my_watch
{
  "trigger" : {
    "schedule" : {
      "interval" : "10m"
    }
  },
  "input" : {
    "search" : {
      "request" : {
        "indices" : [
          "my_index"
        ],
        "body" : {
          "query" : {
            "match_all" : {}
          }
        }
      }
    }
  },
  "actions" : {
    "log_something" : {
      "logging" : {
        "text" : "{{ctx.payload}}"
      }
    }
  }
}
```

2. Activate the watch:
```
PUT _watcher/watch/my_watch/_activate
```

3. Check the watch's status:
```
GET _watcher/watch/my_watch
```

The output should look something like this:
```
{
  "my_watch" : {
    "metadata" : {
      "xpack" : {
        "version" : 1
      },
      "modified_date" : "2020-07-13T13:25:19.639Z",
      "created_date" : "2020-07-13T13:25:19.639Z",
      "version" : 1,
      "type" : "json",
      "status" : {
        "state" : "active"
      }
    },
    "watch" : {
      "trigger" : {
        "schedule" : {
          "interval" : "10m"
        }
      },
      "input" : {
        "search" : {
          "request" : {
            "indices" : [
              "my_index"
            ],
            "body" : {
              "query" : {
                "match_all" : {}
              }
            }
          }
        }
      },
      "actions" : {
        "log_something" : {
          "logging" : {
            "text" : "{{ctx.payload}}"
          }
        }
      }
    }
  }
}
```

For more information, see the [Elasticsearch Watcher documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/watcher.html).

onelinerhub: [How do I set up an Elasticsearch watcher?](https://onelinerhub.com/elasticsearch/how-do-i-set-up-an-elasticsearch-watcher)