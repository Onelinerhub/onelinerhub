# How can I integrate Amazon Redshift with Hadoop?
// plain

Integrating Amazon Redshift with Hadoop requires the use of the Amazon Redshift JDBC driver. This driver allows you to connect to Redshift clusters from Java applications running on Hadoop clusters.

The following example code demonstrates how to connect to a Redshift cluster from a Java application running on Hadoop:

```
import java.sql.Connection;
import java.sql.DriverManager;

public class RedshiftConnection {
  public static void main(String[] args) {
    try {
      // Load the Redshift JDBC Driver
      Class.forName("com.amazon.redshift.jdbc.Driver");

      // Create a connection to the Redshift cluster
      Connection con = DriverManager.getConnection(
        "jdbc:redshift://example-cluster.123456789012.us-east-1.redshift.amazonaws.com:5439/dev",
        "username",
        "password"
      );

      System.out.println("Connected to Redshift.");
    } catch (Exception e) {
      System.err.println("Error connecting to Redshift.");
      e.printStackTrace();
    }
  }
}
```

## Output example
 `Connected to Redshift.`

The code consists of the following parts:

1. `Class.forName("com.amazon.redshift.jdbc.Driver")` - Loads the Redshift JDBC driver.
2. `DriverManager.getConnection()` - Establishes a connection to the Redshift cluster. This method requires the cluster endpoint, username and password as parameters.
3. `System.out.println("Connected to Redshift.")` - Prints a message indicating that the connection was successful.

For more information, see the [Amazon Redshift JDBC Driver Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html).

onelinerhub: [How can I integrate Amazon Redshift with Hadoop?](https://onelinerhub.com/amazon-redshift/how-can-i-integrate-amazon-redshift-with-hadoop)