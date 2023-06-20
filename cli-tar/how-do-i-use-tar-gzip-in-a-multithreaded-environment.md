# How do I use tar gzip in a multithreaded environment?
// plain

Tar Gzip can be used in a multithreaded environment to compress and decompress files in parallel. It uses a combination of tar and gzip to speed up the process. The following example code shows how to use tar gzip in a multithreaded environment:

```
#include <stdio.h>
#include <pthread.h>
#include <zlib.h>
#include <tar.h>

int main(int argc, char** argv)
{
	// Create a thread for each file to be compressed
	pthread_t threads[argc-1];
	for (int i = 1; i < argc; i++) {
		pthread_create(&threads[i-1], NULL, tar_gzip, argv[i]);
	}

	// Wait for all threads to finish
	for (int i = 0; i < argc-1; i++) {
		pthread_join(threads[i], NULL);
	}

	return 0;
}

void* tar_gzip(void* filename)
{
	// Open the file
	FILE* fp = fopen((char*)filename, "rb");

	// Create a buffer to store the compressed data
	char buffer[BUFSIZ];

	// Setup the tar header
	struct tar_header header;
	strncpy(header.name, (char*)filename, 100);
	header.typeflag = REGTYPE;
	header.size = get_file_size(fp);

	// Compress the data
	gzFile gzf = gzopen(buffer, "wb");
	gzwrite(gzf, fp, header.size);
	gzclose(gzf);

	// Write the tar header and compressed data to the file
	fwrite(&header, sizeof(struct tar_header), 1, fp);
	fwrite(buffer, sizeof(char), get_compressed_size(buffer), fp);

	// Close the file
	fclose(fp);
}
```

The code above demonstrates how to use tar gzip in a multithreaded environment:

1. Create a thread for each file to be compressed.
2. Wait for all threads to finish.
3. Open the file.
4. Create a buffer to store the compressed data.
5. Setup the tar header.
6. Compress the data.
7. Write the tar header and compressed data to the file.
8. Close the file.

## Helpful links

- [zlib](https://zlib.net/)
- [tar.h](https://www.gnu.org/software/libc/manual/html_node/tar_002eh.html)

onelinerhub: [How do I use tar gzip in a multithreaded environment?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-gzip-in-a-multithreaded-environment)