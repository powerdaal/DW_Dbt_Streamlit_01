import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError

import streamlit as st

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


def get_data():
    query=f""" SELECT * FROM public.dm_commodities """
    df=pd.read_sql(query,engine)

    try:
        df = pd.read_sql(query, engine)
        return df
    except ProgrammingError as e:
        st.error(f"Erro ao acessar a tabela 'dm_commodities' no schema '{DB_SCHEMA}': {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

# Configurar a página do Streamlit
st.set_page_config(page_title='Dashboard de Commodities', layout='wide')

# Título do Dashboard
st.title('Dashboard de Commodities')

# Descrição
st.write("""
Este dashboard mostra os dados de commodities e suas transações.
""")

# Obter os dados
df = get_data()

# Verificar se o DataFrame está vazio
if df.empty:
    st.write("Não foi possível carregar os dados. Verifique se a tabela 'dm_commodities' existe no schema especificado.")
else:
    # Exibir os dados
    st.write("### Dados das Commodities")
    st.dataframe(df)

    # Resumo estatístico
    st.write("### Resumo Estatístico")
    st.write(df.describe())

    # Gráficos
    st.write("### Gráficos")

    # Gráfico de barras para ganhos e perdas
    st.bar_chart(df[['data', 'ganho']].set_index('data'))

    # Gráfico de linha para valores de fechamento
    st.line_chart(df[['data', 'valor_fechamento']].set_index('data'))