import streamlit as st

st.title("My Streanlit App")
with st.form(key="my_form"):
    name = st.text_input("Nama Lengkap")
    jenis_kelamin = st.radio("Jenis Kelamin", ("Laki-Laki" ,"Perempuan"))
    submit = st.form_submit_button(label="Kirim")