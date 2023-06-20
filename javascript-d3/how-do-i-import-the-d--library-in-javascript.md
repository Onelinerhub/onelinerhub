# How do I import the D3 library in JavaScript?
// plain

The D3 library can be imported into a JavaScript project in a few different ways.

1. **Using a CDN**

A Content Delivery Network (CDN) is a network of servers that can serve files to a user's browser. The D3 library can be imported using a CDN by adding the following code to the `<head>` of an HTML document:

```
<script src="https://d3js.org/d3.v5.min.js"></script>
```

2. **Using npm**

If the project is using a package manager such as npm, the D3 library can be imported by running the following command in the terminal:

```
npm install d3
```

This will install the D3 library in the project's `node_modules` folder.

3. **Using a local file**

If the project is not using a package manager, the D3 library can be imported by downloading the library from the [D3 website](https://d3js.org/) and adding the following code to the `<head>` of an HTML document:

```
<script src="path/to/d3.min.js"></script>
```

Where `path/to/d3.min.js` is the path to the downloaded D3 library file.

Once the D3 library has been imported, it can be used in the project by referencing the `d3` object. For example:

```
console.log(d3.version);
```

## Output example

```
5.16.0
```

onelinerhub: [How do I import the D3 library in JavaScript?](https://onelinerhub.com/javascript-d3/how-do-i-import-the-d--library-in-javascript)