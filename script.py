#Se hacen las importaciones necesarias para el desarrollo del script
import pandas as pd
import psycopg2
import warnings
from dotenv import load_dotenv
import os
warnings.filterwarnings('ignore')

#Se sube el archivo facts_table.csv para leerlo y extraer los datos desde ahí
df = pd.read_csv('./facts_table.csv')

#Se crean las columnas type_sales, discount, discount_percentage, profit y profit_margin, 
#para luego ser agregadas al archivo Finaldf.csv. Estas columnas se crean a partir de las columnas 
# ya existentes con el fin de que sean de utilidad dentro de análisis de los datos.
df['type_sales'] = df['amount'].apply(lambda x: 'high sales' if x > 100.000 else 'low sales')
df['discount'] = df['amount'] * df['discount']
df['discount_percentage'] = (df['discount'] / df['amount']) * 100
df['profit'] = df['amount'] - df['freight']
df['profit_margin'] = (df['profit'] / df['amount']) * 100

#Se guarda el archivo Finaldf.csv con las columnas creadas
df.to_csv('Finaldf.csv', sep = '|', index = False)

#Se establece la conexión con la base de datos
load_dotenv()

host = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

connection = psycopg2.connect(host=host, database=database, 
                              user=user, password=password, port=port)
cursor = connection.cursor()

#Se crea la tabla facts_table en la base de datos
cursor.execute('CREATE TABLE IF NOT EXISTS facts_table (facts_id SMALLINT, order_id SMALLINT, freight REAL, order_date DATE, unit_price REAL, quantity SMALLINT, discount REAL, amount REAL, product_id SMALLINT, supplier_id SMALLINT, category_id SMALLINT, employee_id SMALLINT, customer_id CHARACTER VARYING(5), type_sales CHARACTER VARYING(20), discount_percentage REAL, profit REAL, profit_margin REAL);')
connection.commit()
#Se establece la columna facts_id como llave primaria
cursor.execute("""ALTER TABLE ONLY facts_table ADD CONSTRAINT pk_facts_id PRIMARY KEY (facts_id)""")

#Se copian los datos del archivo Finaldf.csv a la tabla facts_table para poblarla. 

with open('Finaldf.csv', 'r') as f:
    next(f)
    cursor.copy_from(f, 'facts_table', sep='|')

connection.commit()
