# How can I use Sphinx Search with Golang?
// plain

Sphinx Search is a full-text search engine written in C++ and can be used with Golang. It provides fast and relevant search results and can be integrated with Golang applications.

To use Sphinx Search with Golang, you need to install the [Go Sphinx API](https://github.com/sphinx-contrib/go-sphinx) library.

```go
package main

import (
	"fmt"
	sphinx "github.com/sphinx-contrib/go-sphinx"
)

func main() {
	client := sphinx.NewClient("localhost", 9312)

	// Set the search query
	query := sphinx.Query{
		Query: "golang",
	}

	// Execute the search query
	res, err := client.Query(query)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Print the search results
	fmt.Println(res)
}
```

## Output example


```
{Total:1 Matches:[{DocID:1 Weight:1 Attrs:[{Name:title Value:"Golang"}]}]}
```

The code above demonstrates how to use Sphinx Search with Golang. It creates a new Sphinx client and sets the search query. Then, it executes the query and prints the search results.

The Go Sphinx API library provides a rich set of features for integrating Sphinx Search with Golang applications. It supports indexing, searching, and highlighting of search results. It also provides support for advanced search features such as filtering, sorting, and grouping.

onelinerhub: [How can I use Sphinx Search with Golang?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinx-search-with-golang)