# Reset Auto Increment field in mysql table

```mysql
ALTER TABLE `table_name` DROP `column_name`;
ALTER TABLE `table_name` ADD `column_name` int not null auto_increment primary key first;
```