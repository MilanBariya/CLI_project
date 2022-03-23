import sys
from mycli.main1 import *


def main():

    args = sys.argv[1:]
 
    cmd_list = ["get_columns", "get_tables"]

    if not args:
        print('Please pass argument')
    
    elif not args[0] in cmd_list:
        print("Please Pass valid argument")

    elif args[0] == 'get_tables':
        table_list = get_table_list()
        print(table_list)

    elif args[0] == 'get_columns':

        if len(args) < 2:
            print('Please pass table name')
        
        elif len(args) > 2:
            print('Please pass only one table name')

        elif args[1]:
            table_list = get_table_list()

            if args[1] in table_list:
                table_name_from_user = args[1]
                get_table_column(table_name_from_user)
            else:
                print("Table is not avaible")


if __name__ == '__main__':
    main()
