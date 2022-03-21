# How to use geoip module

### **Warning.** This module is deprecated, use [geoip2 module](/nginx/how-to-use-geoip2-module) instead.

```nginx
geoip_country /var/geoip.dat;

server {
  if ($geoip_city_country_code = "RU") {
    return 403 'no';
  }
}
```

- `geoip_country` - set path to [geoip country database](https://dev.maxmind.com/geoip/legacy/databases?lang=en) file
- `/var/geoip.dat` - path to geoip database file
- `$geoip_city_country_code` - variable with detected country code
- `"RU"` - sample value to check upon
- `return 403 'no';` - return `403` header if request is detected as `RU`

group: geoip_1


