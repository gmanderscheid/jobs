
from pandas import read_csv
from os import environ 
from logging import info, basicConfig, DEBUG, error
from sys import stdout

basicConfig(format='%(message)s', level=DEBUG, stream=stdout)

def main():
    info("Running main")
    try :
        df = read_csv(environ.get('FILEPATH'))
        df[~df.image.isna()].to_parquet('./data/valid_product_catalog.parquet')
        df[~df.image.isna()].drop_duplicates('image').to_parquet('./data/valid_product_catalog_no_duplicates.parquet')
        info("Files written")
    except Exception as e :
        error(str(e))

if __name__ == '__main__':
    main()
