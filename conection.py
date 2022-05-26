import snowflake
from snowflake import connector


# Gets the version
def connect(query):
    global content
    ctx = snowflake.connector.connect(
        user='SVC_BLACKBOARD_DATA',
        password='9TW3t31U0Ne#',
        account='jcxbjjc-prod_5f28363662504_sf',
        warehouse='BLACKBOARD_DATA_WH',
        database='BLACKBOARD_DATA_2D3D65372DD04D7291A3E70BEF3A2F5C',
        schema='CMD_LMS'
    )
    cs = ctx.cursor()
    try:
        dado = cs.execute(query).fetchall()

    finally:
        cs.close()
    ctx.close()
    return dado