import sys
from mycli.main1 import *


def main():

    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    print('passed argument :: {}'.format(args))

    table_name_from_user = args[0]
    get_table_column(table_name_from_user)

    get_table_list()


if __name__ == '__main__':
    main()
