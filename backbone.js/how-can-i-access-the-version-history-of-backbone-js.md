# How can I access the version history of Backbone.js?
// plain

You can access the version history of Backbone.js on the [GitHub Releases page](https://github.com/jashkenas/backbone/releases).

The page contains all the releases of Backbone.js from the initial release in 2010 to the current version. You can view the release notes for each version, as well as download the source code for each release.

You can also use the [GitHub API](https://developer.github.com/v3/repos/releases/) to access the version history programmatically. For example, the following code snippet will list the version history of Backbone.js:

```
curl -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/jashkenas/backbone/releases
```

The output of the command will be a list of release objects containing the version number, release notes, download URLs, and other information about each version.

You can also use the [GitHub GraphQL API](https://developer.github.com/v4/guides/forming-calls/#list-releases) to access the version history of Backbone.js. For example, the following GraphQL query will list the version history of Backbone.js:

```
query {
  repository(owner:"jashkenas", name:"backbone") {
    releases(first:100) {
      nodes {
        tagName
        name
        publishedAt
        url
      }
    }
  }
}
```

The output of the query will be a list of release objects containing the version number, release notes, download URLs, and other information about each version.

onelinerhub: [How can I access the version history of Backbone.js?](https://onelinerhub.com/backbone.js/how-can-i-access-the-version-history-of-backbone-js)