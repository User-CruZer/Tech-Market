import streamlit as st
import pandas as pd
import time
# Contoh penggunaan fungsi
st.title("Pembelian")
if "orders" not in st.session_state:
    st.session_state.orders = []
    st.subheader("Anda belum memasukkan barang ke keranjang")

# Tampilkan data sebagai DataFrame Pandas
if st.session_state.orders:
    df = pd.DataFrame(st.session_state.orders)
    st.write("Tabel Pesanan:")
    df.index = pd.RangeIndex(start=1, stop=len(df) + 1, step=1)
    st.table(df)  # Menampilkan tabel pandas di Streamlit
if st.session_state.orders != []:
    if st.button("buy", use_container_width=True):
        st.session_state.orders = []
        st.success("pesanan anda telah dibuat")
        time.sleep(2)
        st.rerun()