import argparse
import os
import time

import geopandas as gpd

# set up cli args
parser = argparse.ArgumentParser()
parser.add_argument("geojson", type=str, help="path to geojson file")
parser.add_argument('-gp', "--geoparquet", type=str,
                    help="path to save geoparquet file, defaults to same folder as geojson", default=None)
parser.add_argument('-o', '--overwrite', action='store_true',
                    help="overwrite any existing file with the same name")
parser.add_argument('-a', '--analytics', action='store_true',
                    help="generate and print analytics")
parser.add_argument('-c', '--compression', default='gzip',
                    choices=['snappy', 'gzip', 'brotli', 'None'], help="geoparquet compression type (default: gzip)")

if __name__ == '__main__':
    #timing
    t0 = time.perf_counter()

    # get cli args
    args = parser.parse_args()

    # check if output path was supplied
    if not args.geoparquet:
        # set default output path if one was not supplied
        # this seems a bit shit, probs need to do this a better way eventually
        args.geoparquet = args.geojson.replace('.geojson', '.parquet')

    # check if geojson file exists
    if not os.path.exists(args.geojson):
        raise FileNotFoundError('Check your geojson file path')
    else:

        # check geoparquet path is empty if not overwriting
        if not args.overwrite:
            if os.path.exists(args.geoparquet):
                raise FileExistsError('Check your geoparquet path isnt already in use, or use the --overwrite flag')

        # reading in geojson
        gdf = gpd.read_file(args.geojson)

        # using gzip compression now as brotli is not widely supported
        # https://cloudnativegeo.org/blog/2023/08/performance-explorations-of-geoparquet-and-duckdb/
        gdf.to_parquet(args.geoparquet, compression=args.compression)

        # generate analytics
        if args.analytics:
            time_taken = time.perf_counter()-t0
            storage_saving = 100 * os.path.getsize(args.geoparquet)/os.path.getsize(args.geojson)

            # printing analytics
            print(f'Converted {args.geojson} into {args.geoparquet}')
            print(f'\t Conversion took {time_taken:.2f}s and parquet is only {storage_saving:.2f}% the size of the original geojson')
