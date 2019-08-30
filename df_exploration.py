# #!/usr/bin/python3
#!/home/jcz/anaconda3/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy
import numpy as np

# engine = sqlalchemy.create_engine('mysql+pymysql://jcz:yub.miha@localhost:3306/weather')
engine = sqlalchemy.create_engine('mysql+pymysql://jcz:yub.miha@localhost:3306/weather')
df = pd.read_sql_table("v_KPWM_daily",engine)
print(df.dtypes)
df.tail()

