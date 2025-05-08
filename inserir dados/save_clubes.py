import requests
import json
from config.db import getConnection





conn = getConnection()
cursor = conn.cursor()
conn.commit()
cursor.close()
conn.close()

