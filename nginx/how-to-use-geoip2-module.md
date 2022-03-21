# How to use geoip2 module

```nginx
geoip2 /etc/country.mmdb {
  auto_reload 5m;
  $geoip2_metadata_country_build metadata build_epoch;
  $geoip2_data_country_code default=US source=$variable_with_ip country iso_code;
  $geoip2_data_country_name country names en;
}
```

- `/etc/country.mmdb` - maxmind [geoip database file

group: geoip2


