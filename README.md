﻿# Caso de uso do DBT & Streamlit

## Conceito

Este projeto teve como ideia acompanhar e aplicar a aula aberta do Workshop do Luciano Galvão.
A ideia era desenvolver uma breve solução que busca informação de 3 tickers diferentes, armazenar em postgres, documentar com dbt e levantar essas informações em um B.I. simples no streamlit.

Link da aula aberta: https://www.youtube.com/watch?v=n3R0c2ZB6BQ&t=10549s&ab_channel=LucianoGalv%C3%A3oFilho

# Passos do desenvolvimento

1. Inicialmente fazemos a busca dos valores de suas cotações ao longo de 3 meses.
2. Lançamos essa informação a um banco postgree, de preferencia numa solução open source ou nuvem. No caso utilizamos um banco de dados free hospedado no NEON
3. Criamos 2 tabelas, a commodities e a de movimentações financeiras.
4. Com elas em mão usamos o dbt para transformação e para documentar o processo aplicado nelas para chegar na solução final que é o datamart.
5. Ao fim do processo do dbt, geramos a documentação por ele e temos nosso MVP finalizado.
