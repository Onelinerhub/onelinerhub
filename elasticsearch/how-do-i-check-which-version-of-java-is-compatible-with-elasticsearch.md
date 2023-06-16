# How do I check which version of Java is compatible with Elasticsearch?
// plain

To check which version of Java is compatible with Elasticsearch, you can use the `java -version` command. This command will display the version of the Java Runtime Environment (JRE) installed on your system.

## Example


```
$ java -version
openjdk version "1.8.0_242"
OpenJDK Runtime Environment (build 1.8.0_242-b08)
OpenJDK 64-Bit Server VM (build 25.242-b08, mixed mode)
```

The output of this command displays the version of the JRE installed on the system. The version must be 8 or higher in order to be compatible with Elasticsearch.

Elasticsearch also requires that the Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8 be installed. To check if this is installed, you can use the `java -fullversion` command.

## Example


```
$ java -fullversion
openjdk full version "1.8.0_242-b08"
```

The output of this command will display the version of the JRE installed on the system, as well as the JCE Unlimited Strength Jurisdiction Policy Files 8.

To ensure compatibility with Elasticsearch, you should have the following installed:

* Java Runtime Environment (JRE) version 8 or higher
* Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8

## Helpful links

* [Java SE 8 Documentation](https://docs.oracle.com/javase/8/docs/)
* [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)

onelinerhub: [How do I check which version of Java is compatible with Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-check-which-version-of-java-is-compatible-with-elasticsearch)