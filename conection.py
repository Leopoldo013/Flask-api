import snowflake
from snowflake import connector


# Gets the version
def connect(query):
    global content
    ctx = snowflake.connector.connect(
        user='xxxxxxx',
        password='xxxxxxx,
        account='xxxxxx',
        warehouse='xxxxxxx',
        database='xxxxxx',
        schema='xxxxxxx'
    )
    cs = ctx.cursor()
    try:
        dado = cs.execute(query).fetchall()

    finally:
        cs.close()
    ctx.close()
    return dado
