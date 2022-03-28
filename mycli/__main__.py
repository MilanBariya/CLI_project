from re import S
import sys
from mycli.main import *
import logging
import click

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')


@click.group()
def cli():
    pass

@click.command()
@click.option('--engine', type=click.Choice(['mysql', 'clickhouse']), help='Engine name to connect with that')
@click.argument('fname')
def seteng(engine, fname):
    """This function will set the engine"""
    set_engine(engine, fname)
    logging.info(f"{engine} connected")
    f = open("temp.txt", "w")
    f.write(engine + "\n")
    f.write(fname)

@click.command()
def gettables():
    """This function will return a list of tables"""
    table_list = get_table_list()
    for table in table_list:
        logging.info(f"Table name: {table}")

@click.command()
@click.option('--table')
def getcolumn(table):
    """This function will return the columns of the given table"""
    table_list = get_table_list()
    if table in table_list:
        table_name_from_user = table
        columns_list = get_table_column(table_name_from_user)
        for column in columns_list:
            logging.info(f"Column name: {column}")
    else:
        logging.error('Table is not avaible in database')



cli.add_command(seteng)
cli.add_command(gettables)
cli.add_command(getcolumn)

if __name__ == '__main__':
    cli()
