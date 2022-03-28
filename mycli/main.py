from sqlalchemy import create_engine, MetaData, Table, inspect
from sys import argv
import json
from clickhouse_driver import Client


# This function will set engine
def set_engine(eng, fname=None):
    global data, engine, connection, metadata
 
    details = open(fname)
    data = json.load(details)
    username = data.get("username")
    password = data.get("password", "")
    host = data.get("host")
    db = data.get("db")
    engine_name = data.get("engine_name")
    

    engine = create_engine(
        f"{engine_name}://{username}:{password}@{host}/{db}")
    connection = engine.connect()
    metadata = MetaData()

try:
    f = open("temp.txt", "r")
    val = f.readline()
    filename = f.readline()
    set_engine(val.strip(), filename.strip())
except Exception as e:
    print(e)

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
