from sqlalchemy import create_engine, MetaData, Table
from sys import argv

engine = create_engine('mysql+pymysql://root:1222412224@127.0.0.1/sql_hr')

connection = engine.connect()
metadata = MetaData()


   
# Print full table metadata
# print(repr(metadata.tables['offices']))
# ensus = Table('offices', metadata, autoload=True, autoload_with=engine)


# This Function will give columns name
def get_table_column(tb_name):
    
    tb = Table(tb_name, metadata, autoload=True, autoload_with=engine)
    columns = tb.columns.keys()
    print("#### columns ####")
    for column in columns:
        print(column)

table_name_from_user = argv[1]
print("table name given by you:",table_name_from_user)

get_table_column(table_name_from_user)