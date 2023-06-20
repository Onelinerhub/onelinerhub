# How can I use the command line to edit text using Qt?
// plain

The command line can be used to edit text using Qt, a cross-platform application framework. Qt provides a command line tool called `qdbusviewer` that can be used to view and edit the properties of a Qt application.

To use `qdbusviewer` to edit text, first you need to get the application's DBus address. This can be done by running the following command:

```
qdbus <application-name>
```

For example, if you want to edit text in the `kate` application, you can run the following command:

```
qdbus org.kde.kate
```

This will output the DBus address of the application, which can be used to view and edit the properties of the application.

To view the properties of the application, you can run the following command:

```
qdbusviewer <dbus-address>
```

For example, if the DBus address of the `kate` application is `org.kde.kate`, you can run the following command to view the properties of the application:

```
qdbusviewer org.kde.kate
```

Once the properties of the application are visible, you can select the `Text` property and edit the text as required.

## Helpful links
- [Qt Documentation - qdbusviewer](https://doc.qt.io/qt-5/qdbusviewer.html)
- [Qt Documentation - DBus](https://doc.qt.io/qt-5/qdbus.html)

onelinerhub: [How can I use the command line to edit text using Qt?](https://onelinerhub.com/cli-sed/how-can-i-use-the-command-line-to-edit-text-using-qt)