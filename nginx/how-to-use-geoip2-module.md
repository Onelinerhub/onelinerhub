# How to use geoip2 module

```nginx
geoip2 /etc/country.mmdb {
  auto_reload 5m;
  $geoip2_data_country_code default=US source=$variable_with_ip country iso_code;
}

server {
  if ( $geoip2_data_country_code = "RU" ) {
    return 403 'no no';
  }
}
```

- `/etc/country.mmdb` - maxmind [geoip database](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data?lang=en) file
- `auto_reload 5m` - check for DB updates every 5 minutes
- `$geoip2_data_country_code` - this variable will store detected country code
- `return 403 'no no';` - forbidden access if country code is `RU`

group: geoip2


