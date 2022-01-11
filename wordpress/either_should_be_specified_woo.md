# Fix Either should be specified Error in Woocommerce

```php
function wc_remove_product_schema_product_archive() {
   remove_action( 'woocommerce_shop_loop', array( WC()->structured_data, 'generate_product_data' ), 10, 0 );
}
add_action( 'woocommerce_init', 'wc_remove_product_schema_product_archive' );
```

add this code in function.php current active theme