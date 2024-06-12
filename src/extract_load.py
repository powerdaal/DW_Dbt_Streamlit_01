import pandas as pd
import sqlalchemy
from dotenv import load_dotenv
# import psycopg2-binary
import yfinance as yf
import os

#import das minhas variaveis de ambiente
commodities=['CL=F','GC=F','SI=F']

def buscar_dados_commodities(simbolo,periodo='5d',intervalo='1d'):
  ticker=yf.Ticker('CL=F')
  dados=ticker.history(period=periodo,interval=intervalo)[['Close']]
  dados['simbolo']=simbolo
  return dados

def buscar_todos_dados_commodities(commodities):
  todos_dados=[]
  for simbolo in commodities:
    dados = buscar_dados_commodities(simbolo)
    todos_dados.append(dados)

  return pd.concat(todos_dados)

if __name__=="__main__":
  dados_concatenados=buscar_todos_dados_commodities(commodities)
  print(dados_concatenados[dados_concatenados.simbolo=='SI=F'])

# pegar a cotacao dos meus ativos

# concatenar os meus ativos

# salvar no banco de dados