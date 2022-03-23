from sqlalchemy import create_engine, MetaData, Table, inspect
from sys import argv


engine = create_engine('mysql+pymysql://root:1222412224@127.0.0.1/sql_hr')

connection = engine.connect()
metadata = MetaData()


# This Function will give columns name
def get_table_column(tb_name):

    tb = Table(tb_name, metadata, autoload=True, autoload_with=engine)
    columns = tb.columns.keys()
    return columns


# This functin will give tables list
def get_table_list():
    inspector = inspect(engine)
    table_list = engine.table_names()
    return table_list
