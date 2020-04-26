# Nginx configuration

This is the cconfiguration file for nginx reverse proxy server. Port for incoming connection is cconfigurable via `listen` option. The destination is configurable via `proxy_pass` option:

```
http://<destination_host>:<destination_port>
```

## Configuration file sould be placed to

```
/etc/nginx/conf.d/default.conf
```
