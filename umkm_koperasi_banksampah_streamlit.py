import streamlit as st

st.title("Bank Sampah")
text_input = st.text_input("Nama Anggota")

st.info(text_input)
st.info(st.number_input("Jumlah ", 0, 50000000))