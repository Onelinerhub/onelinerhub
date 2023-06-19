# How can I view the history of changes made to an AngularJS project?
// plain

To view the history of changes made to an AngularJS project, you can use the `git log` command. This command will list all of the commits that have been made to the project. For example, to view the last 10 commits, you can run the following command:

```
git log -n 10
```

The output of this command will look something like this:

```
commit 8f4a2b0d4d27f9f4b3f9c5f2b7f6d6a2f8f5a2b3
Author: John Smith <john@example.com>
Date:   Wed Jan 9 17:19:02 2019 -0500

    Fix bug #123

commit f3c2b2d2d3f7f8f3b2f1d4f2b7f6d6a2f8f5a2b3
Author: John Smith <john@example.com>
Date:   Tue Jan 8 17:19:02 2019 -0500

    Add feature #456

commit 8f4a2b0d4d27f9f4b3f9c5f2b7f6d6a2f8f5a2b3
Author: Jane Doe <jane@example.com>
Date:   Mon Jan 7 17:19:02 2019 -0500

    Refactor code
```

You can also use the `git show` command to view the details of a specific commit. For example, to view the details of the last commit, you can run the following command:

```
git show
```

The output of this command will look something like this:

```
commit 8f4a2b0d4d27f9f4b3f9c5f2b7f6d6a2f8f5a2b3
Author: John Smith <john@example.com>
Date:   Wed Jan 9 17:19:02 2019 -0500

    Fix bug #123

diff --git a/src/app.js b/src/app.js
index f8f5a2b..f2b7f6d 100644
--- a/src/app.js
+++ b/src/app.js
@@ -1,7 +1,7 @@
 var app = angular.module('myApp', []);

 app.controller('MainCtrl', function($scope) {
-    $scope.message = 'Hello world!';
+    $scope.message = 'Hello Angular!';
 });
```

In addition to the `git log` and `git show` commands, there are a number of other useful tools and commands for viewing the history of changes made to an AngularJS project. For more information, see the following links:

- [Git Documentation](https://git-scm.com/documentation)
- [Git Tutorials](https://www.atlassian.com/git/tutorials)
- [GitHub Guides](https://guides.github.com/activities/hello-world)

onelinerhub: [How can I view the history of changes made to an AngularJS project?](https://onelinerhub.com/angularjs/how-can-i-view-the-history-of-changes-made-to-an-angularjs-project)