import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy
import numpy as np

# engine = sqlalchemy.create_engine('mysql+pymysql://jcz:yub.miha@localhost:3306/weather')
engine = sqlalchemy.create_engine('mysql+pymysql://jcz:yub.miha@localhost:3306/weather')

query = '''show tables'''
df = pd.read_sql_query(query,engine)
df1 = pd.read_sql_table("v_monthly_gas",engine)

print(df1.dtypes)
df1.tail()
print("----------")


plt.figure(figsize=(15,10))
width = 0.35
plt.bar('YEARMONTH','gas_usage',width, color="red", data=df1, label="Gas Usage (cu ft)")

plt.xlabel("Year and Month")
plt.ylabel("Gas usage (cu ft) and Electric Usage (kwh)")
plt.title("Monthly Heat Utility Usage")
plt.xticks(rotation='vertical')

plt.legend()

plt.tight_layout() # optional to fix certain layout issues.

plt.savefig('gas_usage_simple.png')
plt.show()