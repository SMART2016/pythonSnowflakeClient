import os

import snowflake.connector
import config


print ('user is ', os.getenv('SNOWSQL_USER'))
conn = snowflake.connector.connect(
    user=config.USER,
    password=config.PASSWORD,
    account=config.ACCOUNT,
    warehouse='COMPUTE_WH',
    database='demo_db',
    schema='public'
)

#create cursor
curs=conn.cursor()
#execute SQL statement
curs.execute("select * from demo_db.public.S3ACCCESSLOG;")
#fetch result

print (curs.fetchone())
