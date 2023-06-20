# How do I tar and gzip a file in Java?
// plain

To tar and gzip a file in Java, you can use the `java.util.zip` package. Here's an example of how to create a tar.gz file from a file:

```java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.zip.GZIPOutputStream;
import java.util.zip.TarEntry;
import java.util.zip.TarOutputStream;

public class TarGzExample {
  public static void main(String[] args) throws IOException {
    // Create a tar.gz file from the file
    File inputFile = new File("test.txt");
    File outputFile = new File("test.tar.gz");
    FileOutputStream fos = new FileOutputStream(outputFile);
    GZIPOutputStream gzos = new GZIPOutputStream(fos);
    TarOutputStream tos = new TarOutputStream(gzos);

    // Create the tar entry
    TarEntry tarEntry = new TarEntry(inputFile, inputFile.getName());
    tos.putNextEntry(tarEntry);

    // Write the file content
    FileInputStream fis = new FileInputStream(inputFile);
    byte[] buffer = new byte[1024];
    int length;
    while ((length = fis.read(buffer)) > 0) {
      tos.write(buffer, 0, length);
    }

    // Close the streams
    tos.close();
    fis.close();
    gzos.close();
    fos.close();
  }
}
```

This code does the following:

1. Creates a `File` object for the file that needs to be tarred and gzipped (`test.txt` in this case).
2. Creates a `FileOutputStream` object for the tar.gz file (`test.tar.gz` in this case).
3. Creates a `GZIPOutputStream` object, which compresses the contents of the tar file.
4. Creates a `TarOutputStream` object, which is used to write the tar file.
5. Creates a `TarEntry` object for the file that needs to be tarred and gzipped.
6. Writes the content of the file to the tar file.
7. Closes all the streams.

After running this code, a tar.gz file (`test.tar.gz`) will be created.

## Helpful links

- [JavaDoc for java.util.zip](https://docs.oracle.com/javase/8/docs/api/java/util/zip/package-summary.html)
- [JavaDoc for TarOutputStream](https://docs.oracle.com/javase/8/docs/api/java/util/zip/TarOutputStream.html)
- [JavaDoc for GZIPOutputStream](https://docs.oracle.com/javase/8/docs/api/java/util/zip/GZIPOutputStream.html)

onelinerhub: [How do I tar and gzip a file in Java?](https://onelinerhub.com/cli-tar/how-do-i-tar-and-gzip-a-file-in-java)