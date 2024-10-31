import pandas as pd
import psycopg2
import warnings
from dotenv import load_dotenv
import os
warnings.filterwarnings('ignore')

df = pd.read_csv('./facts_table.csv')

df['type_sales'] = df['amount'].apply(lambda x: 'high sales' if x > 100.000 else 'low sales')
df['discount'] = df['amount'] * df['discount']
df['discount_percentage'] = (df['discount'] / df['amount']) * 100
df['profit'] = df['amount'] - df['freight']
df['profit_margin'] = (df['profit'] / df['amount']) * 100

df.to_csv('Finaldf.csv', sep = '|', index = False)

load_dotenv()

host = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

connection = psycopg2.connect(host=host, database=database, 
                              user=user, password=password, port=port)
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS facts_table (facts_id SMALLINT, order_id SMALLINT, freight REAL, order_date DATE, unit_price REAL, quantity SMALLINT, discount REAL, amount REAL, product_id SMALLINT, supplier_id SMALLINT, category_id SMALLINT, employee_id SMALLINT, customer_id CHARACTER VARYING(5), type_sales CHARACTER VARYING(20), discount_percentage REAL, profit REAL, profit_margin REAL);')
connection.commit()
cursor.execute("""ALTER TABLE ONLY facts_table ADD CONSTRAINT pk_facts_id PRIMARY KEY (facts_id)""")

with open('Finaldf.csv', 'r') as f:
    next(f)
    cursor.copy_from(f, 'facts_table', sep='|')

connection.commit()
