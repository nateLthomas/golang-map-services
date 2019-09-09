# Terrain-Server
Server for quantized mesh tiles, xyz tile, and static files. Created with golang. 

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
