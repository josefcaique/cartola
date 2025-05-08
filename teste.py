from config.db import getConnection
import pandas as pd





conn = getConnection()
cursor = conn.cursor()


conn.commit()
cursor.close()
conn.close()