# GeoJSON to GeoParquet Converter

This Python project provides a command-line interface (CLI) tool to convert GeoJSON files into GeoParquet format. GeoParquet is an optimized columnar storage format for geospatial data, which can be beneficial for analytics and storage efficiency.

## Features

- Convert GeoJSON files to GeoParquet format.
- Option to specify the output path for the GeoParquet file.
- Overwrite existing files with the same name.
- Generate and print analytics of the GeoJSON data.
- Choose from various compression types for the GeoParquet file.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Bonsa11/geojson-to-geoparquet.git
   ```

2. Navigate to the project directory:
   ```bash
   cd geojson-to-geoparquet
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
usage: main.py [-h] [-gp GEOPARQUET] [-o] [-a] [-c {snappy,gzip,brotli,None}] geojson
```

### Positional Arguments:

- `geojson`: Path to the GeoJSON file you want to convert.

### Options:

- `-h`, `--help`: Show the help message and exit.
  
- `-gp GEOPARQUET`, `--geoparquet GEOPARQUET`: Specify the path to save the GeoParquet file. If not provided, it defaults to the same folder as the input GeoJSON file.
  
- `-o`, `--overwrite`: Overwrite any existing file with the same name.
  
- `-a`, `--analytics`: Generate and print analytics of the GeoJSON data.
  
- `-c {snappy,gzip,brotli,None}`, `--compression {snappy,gzip,brotli,None}`: Choose the compression type for the GeoParquet file. Available options are `snappy`, `gzip`, `brotli`, and `None`. Default: gzip

## Examples

1. Convert a GeoJSON file to GeoParquet with default settings:
   ```bash
   python main.py data.geojson
   ```

2. Convert a GeoJSON file to GeoParquet and specify the output path:
   ```bash
   python main.py data.geojson -gp /path/to/output/data.parquet
   ```

3. Convert a GeoJSON file to GeoParquet with gzip compression and overwrite existing files:
   ```bash
   python main.py -c gzip -o data.geojson 
   ```

4. Convert a GeoJSON file to GeoParquet and generate analytics:
   ```bash
   python main.py -a data.geojson
   
   Converted ./examples/output.geojson into ./examples/output.parquet
       Conversion took 9.24s and parquet is only 5.44% the size of the original geojson
   ```

## Dependencies

- This project requires Python 3.x.
- Dependencies are listed in the `requirements.txt` file.
