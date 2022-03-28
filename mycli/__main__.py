from re import S
import sys
from mycli.main import *
import logging

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')


def main():

    args = sys.argv[1:]

    cmd_list = ["get_columns", "get_tables", "set_engine"]
    engine_list = ["mysql", "clickhouse"]

    if not args:
        logging.error('Please pass argument')

    elif not args[0] in cmd_list:
        logging.error('Please pass valid argument')

    # set engine
    elif args[0] == 'set_engine':

        if len(args) < 2:
            logging.error('Please pass the engine parameter')

        elif len(args) > 2:
            logging.error('Please pass only one engine name')

        elif not args[1] in engine_list:
            logging.error('Please pass valid engine name')

        elif args[1]:
            set_engine(args[1])
            logging.info(f"{args[1]} connected")
            f = open("temp.txt", "w")
            f.write(args[1])

    # get tables
    elif args[0] == 'get_tables':
        table_list = get_table_list()
        for table in table_list:
            logging.info(f"Table name: {table}")

    # get columns
    elif args[0] == 'get_columns':

        if len(args) < 2:
            logging.error('Please pass table name in argument')

        elif len(args) > 2:
            logging.error('Please pass only one table name')

        elif args[1]:
            table_list = get_table_list()

            if args[1] in table_list:
                table_name_from_user = args[1]
                columns_list = get_table_column(table_name_from_user)
                for column in columns_list:
                    logging.info(f"Column name: {column}")
            else:
                logging.error('Table is not avaible in database')


if __name__ == '__main__':
    main()
