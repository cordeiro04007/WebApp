from pathlib import Path
import streamlit as st
import pandas as pd

from utilidades import leitura_tabelas

leitura_tabelas()

df_vendas = st.session_state['dados']['df_vendas']
df_filiais= st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']
df_vendas
df_filiais
df_produtos