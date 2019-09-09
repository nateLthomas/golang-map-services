# golang-map-services

Server for quantized mesh tiles, xyz tile, and static files. Created with golang. 

The server can be https or http, for https the server needs a cert.pem and key.pem to create this you will need to do the following comand:

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout key.pem -out cert.pem

when creatng the certs the "Name (e.g. server FQDN or YOUR name)" you need to enter your server ip e.g. coolmaps.com, or 127.0.0.1:2000

### how to use
```
 ./https -h
```

returns:

```
Usage of ./https:
  -credits string
        Built by Nate T (default "Nate")
  -dir string
        Pick dir to serve static files (default "static")
  -https
        true/false for server to be https, need cert.pem and key.pem in root directory (default true)
  -image_type string
        Pick the type of image jpg or png (default "jpg")
  -mbtiles string
        Path to sqlite mbtiles dataset (default "./control-room.mbtiles")
  -port int
        Pick port to listen on (default 2000)
  -tr_tiles string
        Path to sqlite terrain dataset (default "none")
```

Example usage:

```
./https -https=true -dir="static" -tr_tiles=3dtiles.db
```
