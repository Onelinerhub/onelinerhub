# How can I use SQLite with Kotlin in Android Studio?
// plain

SQLite is an open source SQL database that is widely used in Android apps. It can be used with Kotlin in Android Studio by using the Room Persistence Library.

The Room Persistence Library provides an abstraction layer over SQLite to allow for more robust database access while harnessing the full power of SQLite.

To use SQLite with Kotlin, you first need to include the Room Persistence Library in your app/build.gradle file.

```
dependencies {
    implementation "androidx.room:room-runtime:2.2.5"
    annotationProcessor "androidx.room:room-compiler:2.2.5"
}
```

Once the Room Persistence Library is included, you can create a Room database class. This class will define the entities that will be stored in the database, the version of the database, and the list of migrations.

```
@Database(entities = [User::class], version = 1, exportSchema = false)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

You can then create a DAO (Data Access Object) class which will define the methods that you can use to access and manipulate the data in the database.

```
@Dao
interface UserDao {

    @Query("SELECT * FROM user")
    fun getAll(): List<User>

    @Insert
    fun insertAll(vararg users: User)

    @Delete
    fun delete(user: User)
}
```

Finally, you can create an instance of the database and use the DAO methods to access and manipulate the data.

```
val database = Room.databaseBuilder(
        context.applicationContext,
        AppDatabase::class.java, "database-name"
).build()

val users = database.userDao().getAll()
```

## Helpful links
- [Room Persistence Library](https://developer.android.com/topic/libraries/architecture/room)
- [SQLite](https://www.sqlite.org/index.html)

onelinerhub: [How can I use SQLite with Kotlin in Android Studio?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-kotlin-in-android-studio)