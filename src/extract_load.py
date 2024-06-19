import pandas as pd
from sqlalchemy import create_engine

# import psycopg2-binary
import yfinance as yf

#Bibliotecas necessárias para pegar as variaveis de ambiente
from dotenv import load_dotenv
import os

#import das minhas variaveis de ambiente
load_dotenv()

commodities=['CL=F','GC=F','SI=F']

DB_PORT=os.getenv('DB_PORT_PROD')
DB_HOST=os.getenv('DB_HOST_PROD')
DB_NAME=os.getenv('DB_NAME_PROD')
DB_USER=os.getenv('DB_USER_PROD')
DB_PASS=os.getenv('DB_PASS_PROD')
DB_SCHEMA=os.getenv('DB_SCHEMA_PROD')

DATABASE_URL=f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine=create_engine(DATABASE_URL)

def buscar_dados_commodities(simbolo,periodo='5d',intervalo='1d'):
  ticker=yf.Ticker(simbolo)
  dados=ticker.history(period=periodo,interval=intervalo)[['Close']]
  dados['simbolo']=simbolo
  return dados

def buscar_todos_dados_commodities(commodities):
  todos_dados=[]
  for simbolo in commodities:
    dados = buscar_dados_commodities(simbolo)
    todos_dados.append(dados)

  return pd.concat(todos_dados)

def salva_no_postgres(df,schema='public'):
  df.to_sql('commodities',engine,if_exists='replace',index=True,index_label='Date',schema=schema)

if __name__=="__main__":
  dados_concatenados=buscar_todos_dados_commodities(commodities)
  print(dados_concatenados[dados_concatenados.simbolo=='SI=F'])
  salva_no_postgres(dados_concatenados,schema='public')
# pegar a cotacao dos meus ativos

# concatenar os meus ativos

# salvar no banco de dados