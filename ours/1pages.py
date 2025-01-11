import streamlit as st

st.logo("ours/kumpulan gambar/Logo1.png",size="large")

pages = {
    "🖥️-🦖": [
        st.Page("beranda.py", title="Beranda"),
        st.Page("Rekomendasi.py", title="ChatBot"),
        st.Page("simulasi.py", title="Simulasi"),
        st.Page("order_now.py", title="CheckOut"),
        st.Page("tentang_toko.py", title="about us")
    ]
}

pg = st.navigation(pages)
pg.run()