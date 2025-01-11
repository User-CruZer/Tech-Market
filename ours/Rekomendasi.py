import streamlit as st
import json
import pandas as pd
from chatbot import get_pc_recommendation
from chatbot import get_bot_response
st.title("Recomendation Product Merapi")

# Inisialisasi riwayat chat
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.caption("type 'help' to see what bot can do!")

user_question = st.text_input("Asking Something About our Products:")

if st.button("ASK", use_container_width=True):
    if user_question:
        response = get_bot_response(user_question)
        
        st.session_state.chat_history.append({"user": user_question, "bot": response})

if st.button("RECOMEND", use_container_width=True):
    pc_recommendations = get_pc_recommendation()  # Mengambil data rekomendasi dari chatbot.py

    if pc_recommendations:
        st.write("🤖 Bot: here is the ready-made pc we recommend🫡")
        # Memastikan data "recomend_me_a_pc" ada di dalam file JSON
        pc_data = []
        for pc, specs in pc_recommendations["recomend_me_a_pc"].items():

            pc_info = {
                "PC": pc,
                "PRICE": specs["PRICE"],
                "CPU": specs["CPU"],
                "Fan Cooler": specs["Fan Cooler"],
                "MOBO": specs["MOBO"],
                "RAM": specs["RAM"],
                "STORAGE": specs["STORAGE"],
                "GPU": specs["GPU"],
                "PSU": specs["PSU"],
                "CASING": specs["CASING"]
            }

            # pc_info = {
            #     "PC": pc,
            #     "PRICE": specs.get("PRICE"),
            #     "CPU": specs.ge("CPU"),
            #     "Fan Cooler": specs.get("Fan Cooler"),
            #     "MOBO": specs.get("MOBO"),
            #     "RAM": specs.get("RAM"),
            #     "STORAGE": specs.get("STORAGE"),
            #     "GPU": specs.get("GPU"),
            #     "PSU": specs.get("PSU"),
            #     "CASING": specs.get("CASING")
            # }
            pc_data.append(pc_info)

        # Konversi ke DataFrame Pandas
        df = pd.DataFrame(pc_data)
        #agar memulai dari index 1
        df.index = pd.RangeIndex(start=1, stop=len(df) + 1, step=1)


        st.write(df)
    else:
        st.error("No PC recommendations found.")


# Tampilkan riwayat chat
st.subheader("Chat History:")
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(f"Anda: {chat['user']}")

    with st.chat_message("assistant"):
        st.write(f"Bot: {chat['bot']}")
if st.button("Delete Chat History",use_container_width=True):
    st.session_state.chat_history = []
    st.rerun()