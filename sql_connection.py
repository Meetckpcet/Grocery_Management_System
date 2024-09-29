import datetime
import mysql.connector

__cnx = None

def get_sql_connection(): 
  global __cnx
  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='Meet@3110', database='grocesary_store')

  return __cnx