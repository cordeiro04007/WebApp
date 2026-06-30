from pathlib import Path
import streamlit as st
import pandas as pd

def leitura_tabelas():
    if not 'dados' in st.session_state: 
        pasta_datasets = Path(__file__).parents[1] / 'datasets' 
        df_filiais = pd.read_csv(pasta_datasets/'filiais.csv',decimal= ',', sep=';', index_col=0)
        df_vendas = pd.read_csv(pasta_datasets/'vendas.csv', decimal= ',', sep=';', index_col=0, parse_dates=True)
        df_produtos = pd.read_csv(pasta_datasets/'produtos.csv',decimal= ',', sep=';', index_col=0)
        dados = {'df_vendas': df_vendas,
                'df_filiais': df_filiais,
                'df_produtos': df_produtos,
                }
        st.session_state['dados'] = dados