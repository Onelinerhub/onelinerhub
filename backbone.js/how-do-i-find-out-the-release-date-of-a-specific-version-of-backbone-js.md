# How do I find out the release date of a specific version of Backbone.js?
// plain

The best way to find out the release date of a specific version of Backbone.js is to check the [GitHub repository](https://github.com/jashkenas/backbone).

You can look at the [Releases](https://github.com/jashkenas/backbone/releases) page to find out the exact date of a release. For example, the release date of version 1.3.3 can be found in the [release notes](https://github.com/jashkenas/backbone/releases/tag/1.3.3):

```
Backbone 1.3.3

Release Date: 2016-02-09
```

Alternatively, you can also use the [GitHub API](https://developer.github.com/v3/) to programmatically query the release date. For example, the following code snippet uses `curl` to query the API:

```
curl -H "Accept: application/vnd.github.v3+json" "https://api.github.com/repos/jashkenas/backbone/releases/tags/1.3.3"
```

The output of the command will contain the release date:

```
{
  "url": "https://api.github.com/repos/jashkenas/backbone/releases/992933",
  "assets_url": "https://api.github.com/repos/jashkenas/backbone/releases/992933/assets",
  "upload_url": "https://uploads.github.com/repos/jashkenas/backbone/releases/992933/assets{?name,label}",
  "html_url": "https://github.com/jashkenas/backbone/releases/tag/1.3.3",
  "id": 992933,
  "tag_name": "1.3.3",
  "target_commitish": "master",
  "name": "Backbone 1.3.3",
  "draft": false,
  "author": {
    "login": "jashkenas",
    "id": 47,
    "avatar_url": "https://avatars1.githubusercontent.com/u/47?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/jashkenas",
    "html_url": "https://github.com/jashkenas",
    "followers_url": "https://api.github.com/users/jashkenas/followers",
    "following_url": "https://api.github.com/users/jashkenas/following{/other_user}",
    "gists_url": "https://api.github.com/users/jashkenas/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/jashkenas/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/jashkenas/subscriptions",
    "organizations_url": "https://api.github.com/users/jashkenas/orgs",
    "repos_url": "https://api.github.com/users/jashkenas/repos",
    "events_url": "https://api.github.com/users/jashkenas/events{/privacy}",
    "received_events_url": "https://api.github.com/users/jashkenas/received_events",
    "type": "User",
    "site_admin": false
  },
  "prerelease": false,
  "created_at": "2016-02-09T14:17:06Z",
  "published_at": "2016-02-09T14:17:06Z",
  "assets": [],
  "tarball_url": "https://api.github.com/repos/jashkenas/backbone/tarball/1.3.3",
  "zipball_url": "https://api.github.com/repos/jashkenas/backbone/zipball/1.3.3",
  "body": ""
}
```

The `created_at` field contains the release date of the version. In this case, `2016-02-09T14:17:06Z` indicates that the release date of version 1.3.3 is February 9, 2016.

onelinerhub: [How do I find out the release date of a specific version of Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-find-out-the-release-date-of-a-specific-version-of-backbone-js)