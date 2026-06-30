import streamlit as st
import pandas as pd

st.markdown('## Bem-vindo ao Analisador de Vendas ##')
st.divider()
st.sidebar.markdown('Desenvolvido por: [Alex Cordeiro](https://github.com/cordeiro04007)')

st.markdown(
    f"""
    Esse projeto foi desenvolvido como projeto final do curso *Python para Usuários de Excel*.
    Utilizaremos três principais bibliotecas para o seu desenvolvimento:

    - **`Pandas`**: para manipulação de dados e tabelas;
    - **`Plotly`**: para geração de gráficos;
    - **`Streamlit`**: para criação desse WebApp interativo que você encontra nesse projeto.

    Os dados utilziados foram gerados pelo script "gerador_de_vendas.py" que se encontra junto ao código
    fonte do projeto. Os dados podem ser visualizados na aba de tabelas!

    Sugestões podem ser enviadas para o email alexcordeiro58@gmail.com ou diretamente pelo [GitHub](https://github.com/cordeiro04007).
    """
)