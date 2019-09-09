# Terrain to SQLite

Convert a directory of quantized mesh terrain tiles to a sqlite database.

### How to use

```
python terrain_to_sql.cpython-37.pyc -h
```

return:

```
usage: terrain_to_sql.cpython-37.pyc [-h] [-d TILE_DIRECTORY] [-o OUTFILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -d TILE_DIRECTORY, --tile_directory TILE_DIRECTORY
                        Specify the directory of terrain files.
  -o OUTFILENAME, --outfilename OUTFILENAME
                        Specify name and location of sqlite database.
```

usage example:

```
python terrain_to_sql.cpython-37.pyc -d terrain -o test.db
```

### Things to do

Update the tile spec to copy mbtiles currently just a x, y, z , image(blob) with a index called xyz on the x,y,z fields.
