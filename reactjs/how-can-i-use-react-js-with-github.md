# How can I use React.js with Github?
// plain

React.js is a popular JavaScript library used for building user interfaces. It can be used with Github in a variety of ways.

One way to use React.js with Github is to create a React.js app and host it on Github Pages. To do this, you'll need to create a new repository on Github and add your React.js app files to it. Then, you'll need to enable Github Pages for the repository and configure it to serve your app.

For example, the following code will create a React.js app with Create React App and deploy it to Github Pages:

```
# Create a new React.js app
npx create-react-app my-app

# Add the app files to the repository
git add .

# Commit the changes
git commit -m "Initial commit"

# Push the changes to Github
git push origin master

# Enable Github Pages for the repository
# and configure it to serve your app
```

Once you've enabled Github Pages for the repository, you'll be able to view your app at a URL like `https://<username>.github.io/<repository-name>`.

Another way to use React.js with Github is to use Github Actions to build and deploy your React.js app. You can set up a workflow in your Github repository that will build and deploy your React.js app to a hosting provider like Netlify or Vercel.

For example, the following code will create a workflow that will build and deploy a React.js app to Netlify:

```yaml
name: Deploy

on:
  push:
    branches: [master]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Install and build
      run: |
        npm install
        npm run build
    - name: Deploy to Netlify
      uses: nwtgck/actions-netlify@v1
      with:
        site_id: <site_id>
        auth_token: ${{ secrets.NETLIFY_AUTH_TOKEN }}
        dir: 'build'
```

Once the workflow is set up, Github Actions will build and deploy your React.js app to Netlify every time you push changes to the `master` branch.

These are just two examples of how you can use React.js with Github. There are many more possibilities, so feel free to explore and experiment.

## Helpful links
- [Create React App](https://create-react-app.dev/)
- [Github Pages](https://pages.github.com/)
- [Github Actions](https://github.com/features/actions)
- [Netlify](https://www.netlify.com/)
- [Vercel](https://vercel.com/)

onelinerhub: [How can I use React.js with Github?](https://onelinerhub.com/reactjs/how-can-i-use-react-js-with-github)