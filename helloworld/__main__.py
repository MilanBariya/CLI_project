import sys
from sqlalchemy import create_engine, MetaData, Table, inspect
from sys import argv


engine = create_engine('mysql+pymysql://root:1222412224@127.0.0.1/sql_hr')

connection = engine.connect()
metadata = MetaData()


def main():

    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    print('passed argument :: {}'.format(args))

    table_name_from_user = args[0]
    get_table_column(table_name_from_user)

    get_table_list()


# This Function will give columns names
def get_table_column(tb_name):

    tb = Table(tb_name, metadata, autoload=True, autoload_with=engine)
    columns = tb.columns.keys()
    print(f"#### columns in {tb_name} table ####")
    for column in columns:
        print(column)


# This functin will give tables list
def get_table_list():
    inspector = inspect(engine)
    print("#### Table List ####")
    print(engine.table_names())


if __name__ == '__main__':
    main()
