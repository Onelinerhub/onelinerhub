# How do I use Vue.js Forge to create a new project?
// plain

Vue.js Forge is a command-line tool for quickly scaffolding Vue.js projects. To use Vue.js Forge to create a new project, you can run the following command in your terminal:

```
vue-forge init <project-name>
```

This command will create a new project in the current directory with the given project name. It will also install all the necessary dependencies and set up the configuration files.

The command will output the following:

```
Creating project in current directory...
  Installing dependencies...
  Setting up configuration files...
Done!
```

The command will create the following files and directories:

* `package.json` - contains the project's dependencies and scripts.
* `.babelrc` - contains the configuration for Babel.
* `.eslintrc` - contains the configuration for ESLint.
* `public/` - contains the static assets.
* `src/` - contains the source code.

You can then start developing your application by running:

```
npm run serve
```

This command will start a development server and open a browser window pointing to the application.

## Helpful links
* [Vue.js Forge](https://vue-forge.github.io/)
* [Vue.js CLI](https://cli.vuejs.org/)

onelinerhub: [How do I use Vue.js Forge to create a new project?](https://onelinerhub.com/vue.js/how-do-i-use-vue-js-forge-to-create-a-new-project)