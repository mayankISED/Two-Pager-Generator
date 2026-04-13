import sys
import os
sys.path.append(os.path.abspath(".."))  # goes up from Controller/ to project root
import pandas as pd
from Config.db import get_db_connection
from Model import visual_data as vd

conn = get_db_connection()

result = vd.get_ip_in_force(conn, "United Kingdom", 2010, 2020)