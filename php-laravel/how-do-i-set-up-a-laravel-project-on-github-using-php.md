# How do I set up a Laravel project on GitHub using PHP?
// plain

1. Create a repository on GitHub and clone it to your local machine.
2. Install [Laravel](https://laravel.com/docs/7.x/installation) and its dependencies on your machine.
3. Create your Laravel project using the `laravel new` command.
4. Add all the files from your Laravel project to the local repository.
5. Commit the changes and push it to the remote repository.
6. Set up the webhooks in GitHub to trigger builds when changes are pushed.
7. You can now use PHP to make changes to your Laravel project on GitHub.

## Example code

```
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>
laravel new
git add .
git commit -m "Initial commit"
git push origin master
```

Output of example code:
```
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 4 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (11/11), 1.17 KiB | 1.17 MiB/s, done.
Total 11 (delta 0), reused 0 (delta 0)
To https://github.com/<username>/<repo-name>.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

## Code explanation

- `git clone https://github.com/<username>/<repo-name>.git`: This command clones the repository from GitHub to your local machine.
- `cd <repo-name>`: This command changes the current directory to the cloned repository.
- `laravel new`: This command creates a new Laravel project in the current directory.
- `git add .`: This command adds all the files from the Laravel project to the local repository.
- `git commit -m "Initial commit"`: This command commits the changes to the local repository.
- `git push origin master`: This command pushes the changes to the remote repository.

## Helpful links
- [Laravel Documentation](https://laravel.com/docs/7.x/installation)
- [GitHub Documentation](https://docs.github.com/)

onelinerhub: [How do I set up a Laravel project on GitHub using PHP?](https://onelinerhub.com/php-laravel/how-do-i-set-up-a-laravel-project-on-github-using-php)