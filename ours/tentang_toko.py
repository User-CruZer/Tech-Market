import streamlit as st
from data_deskrip import *

left, mid, right = st.columns(3)

with mid:
    st.image("ours/kumpulan gambar/Store.png", use_container_width=True)

st.title("About Us!")

st.write("Salah satu alasan utama mengapa merakit PC adalah pilihan terbaik untuk jangka\
          panjang adalah kemudahannya untuk di-upgrade sesuai kebutuhan di masa depan.")
st.write(" ".join(deskrip_Home))