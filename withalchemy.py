from sqlalchemy import create_engine
import config

engine = create_engine(
    'snowflake://{user}:{password}@{account}/'.format(
        user=config.USER,
        password=config.PASSWORD,
        account=config.ACCOUNT,
    )
)
try:
    connection = engine.connect()
    results = connection.execute('select * from demo_db.public.S3ACCCESSLOG').fetchone()
    print(results)
finally:
    connection.close()
    engine.dispose()