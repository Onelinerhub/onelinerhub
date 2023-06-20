# How do I determine which version of Vue.js I am using?
// plain

To determine which version of Vue.js you are using, you can use the `Vue.version` property. This property returns an object containing the version number, build date, and other information.

## Example code

```
console.log(Vue.version);
```

Example output:
```
{
  full: "2.6.10",
  major: 2,
  minor: 6,
  patch: 10,
  date: "2019-08-13"
}
```

The `Vue.version` property returns an object containing the following properties:

- `full`: The full version string, e.g. "2.6.10".
- `major`: The major version number, e.g. 2.
- `minor`: The minor version number, e.g. 6.
- `patch`: The patch version number, e.g. 10.
- `date`: The release date, e.g. "2019-08-13".

## Helpful links
- [Vue.js Version](https://vuejs.org/v2/guide/releases.html)
- [Vue.version API Documentation](https://vuejs.org/v2/api/#Vue-version)

onelinerhub: [How do I determine which version of Vue.js I am using?](https://onelinerhub.com/vue.js/how-do-i-determine-which-version-of-vue-js-i-am-using)