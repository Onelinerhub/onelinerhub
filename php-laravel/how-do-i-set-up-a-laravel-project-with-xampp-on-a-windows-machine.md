# How do I set up a Laravel project with XAMPP on a Windows machine?
// plain

1. Download and install XAMPP from [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html)
2. Install Composer from [https://getcomposer.org/download/](https://getcomposer.org/download/)
3. Open XAMPP control panel and start Apache and MySQL
4. Create a new folder in the XAMPP/htdocs directory and open a command prompt in the folder
5. Run the following command to create a new Laravel project:
```
composer create-project --prefer-dist laravel/laravel projectname
```
6. Go to the projectname/config/ folder and open the database.php file
7. Update the MySQL connection details in the file to connect to the XAMPP MySQL server.

## Code explanation
**

- composer create-project --prefer-dist laravel/laravel projectname: This command will create a new Laravel project in the specified directory.

**## Helpful links**

- [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html): Download link for XAMPP
- [https://getcomposer.org/download/](https://getcomposer.org/download/): Download link for Composer

onelinerhub: [How do I set up a Laravel project with XAMPP on a Windows machine?](https://onelinerhub.com/php-laravel/how-do-i-set-up-a-laravel-project-with-xampp-on-a-windows-machine)