from pathlib import Path
import streamlit as st
import pandas as pd

from utilidades import leitura_tabelas

leitura_tabelas()

df_vendas = st.session_state['dados']['df_vendas']
df_filiais= st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']

def mostra_tabela_produtos():
    st.markdown('# Tabela de Produtos')
    st.dataframe(df_produtos)

def mostra_tabela_filiais():
    st.markdown('# Tabela de Filiais')
    st.dataframe(df_filiais)

def mostra_tabela_vendas():
    st.markdown('# Tabela de Vendas')
    st.sidebar.divider()
    st.sidebar.markdown('## Filtrar Tabela')
    colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas da Tabela:', 
                                                  list(df_vendas.columns),list(df_vendas.columns))
    col1,col2 = st.sidebar.columns(2)
    filtro_selecionado = col1.selectbox('Filtrar coluna', list(df_vendas.columns))
    valor_unico_selecionado = list(df_vendas[filtro_selecionado].unique())
    valor_selecionado = col2.selectbox('Valor do filtro', valor_unico_selecionado)
    filtrar = col1.button('Filtrar')
    limpar = col2.button('Limpar')

    if filtrar:
        st.dataframe(df_vendas.loc[df_vendas[filtro_selecionado] == valor_selecionado, colunas_selecionadas],height = 800)
    elif limpar:
       st.dataframe(df_vendas[colunas_selecionadas],height = 800)
    else:
       st.dataframe(df_vendas[colunas_selecionadas],height = 800)
       

st.sidebar.markdown('**Seleção de Tabelas**')
opcao_tabelas = st.sidebar.selectbox('Selecione a tabela que você deseja ver:',['Vendas', 'Filiais', 'Produtos'])

if opcao_tabelas == 'Produtos':
    mostra_tabela_produtos()
elif opcao_tabelas == 'Vendas':
    mostra_tabela_vendas()
elif opcao_tabelas == 'Filiais':
    mostra_tabela_filiais()

