# How do I use AngularJS with GitHub?
// plain

Using AngularJS with GitHub is relatively easy. First, you need to create an AngularJS project. You can do this by running the following command in the terminal:
```
ng new my-angular-app
```
Once the project is created, you can push it to GitHub by running the following commands:
```
cd my-angular-app
git init
git add .
git commit -m "First commit"
git remote add origin <your-github-repo-url>
git push -u origin master
```

The above commands will create a new repository on GitHub and push the code from your local repository to the remote repository.

Once the code is pushed to GitHub, you can make changes and push them to the repository. For example, if you want to add a new component to your project, you can run the following command:
```
ng generate component my-component
```
You can then commit the changes and push them to GitHub:
```
git add .
git commit -m "Added my-component"
git push
```

This will push the changes to your GitHub repository.

To learn more about using AngularJS with GitHub, please refer to the [AngularJS documentation](https://angular.io/guide/github).

onelinerhub: [How do I use AngularJS with GitHub?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-with-github)