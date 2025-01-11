import streamlit as st
import pandas as pd
from comP import parts

def choose_component(component_name, options):
    """
    nampilin daftar komponen dan meminta pengguna memilih komponennya
    mengembalikan (return) nama dan harga komponen yang dipilih
    """
    # Menambahkan pilihan kosong (placeholder) di awal daftar
    options_list = ["Pilih komponen"] + list(options.keys())
    
    selected_component = st.selectbox(f"Pilih {component_name}:", options_list)
    if selected_component != "Pilih komponen":
        return selected_component, options[selected_component]
    else:
        return None, 0

def matching(cpu_choice, mobo_choice, ram_choice,):
    """
    memeriksa kecocokan komponen
    """
    # Matching cpu dan mobo
    if "LGA 1700" in cpu_choice and "LGA 1700" in mobo_choice:
        return True
    if "LGA 1151" in cpu_choice and "LGA 1151" in mobo_choice:
        return True
    if "LGA 1150" in cpu_choice and "LGA 1150" in mobo_choice:
        return True
    if "LGA 1200" in cpu_choice and "LGA 1200" in mobo_choice:
        return True
    if "AM4" in cpu_choice and "AM4" in mobo_choice:
        return True
    
    # Matching mobo dan ram
    if "DDR5" in mobo_choice and "DDR5" in ram_choice:
        return True
    if "DDR4" in mobo_choice and "DDR4" in ram_choice:
        return True
    if "DDR3" in mobo_choice and "DDR3" in ram_choice:
        return True
    return False

def main():
    components = parts()
    selected_components = []
    st.title("Simulasi Perakitan Komputer")
    st.divider()
    st.subheader("Pengecekan Kompatibilitas")

    # on/off cek dengan compabilitas
    check_compatibility = st.selectbox(
        "Aktifkan pengecekan kompatibilitas?",
        ["Ya, periksa kompatibilitas", "Tidak, bebas memilih"]
    )
    st.divider()

    # CPU
    cpu_name, cpu_price = choose_component("Processor", components["CPU"])
    if cpu_name:
        selected_components.append(("Processor", cpu_name, cpu_price))

    # MOBO
    mobo_name, mobo_price = choose_component("Motherboard", components["Motherboard"])
    if mobo_name:
        selected_components.append(("Motherboard", mobo_name, mobo_price))

    if check_compatibility == "Ya, periksa kompatibilitas" and cpu_name and mobo_name:
        if cpu_name and mobo_name and not matching(cpu_name, mobo_name, ""):
            st.warning("Socket CPU dan Motherboard tidak cocok!")

    # RAM
    ram_name, ram_price = choose_component("RAM", components["RAM"])
    if ram_name:
        selected_components.append(("RAM", ram_name, ram_price))
    if check_compatibility == "Ya, periksa kompatibilitas" and mobo_name and ram_name:
        if mobo_name and ram_name and not matching("", mobo_name, ram_name):
            st.warning("Socket RAM dan Motherboard tidak cocok!")
    
    st.divider()
    st.subheader("Main Components")

    # CASING
    casing_name, casing_price = choose_component("Casing", components["Casing"])
    if casing_name:
        selected_components.append(("Casing", casing_name, casing_price))

    # VGA
    vga_name, vga_price = choose_component("Graphic Card 1", components["Graphic Card"])
    if vga_name:
        selected_components.append(("Graphic Card", vga_name, vga_price))

    vga_name, vga_price = choose_component("Graphic Card 2", components["Graphic Card"])
    if vga_name:
        selected_components.append(("Graphic Card", vga_name, vga_price))

    # STORAGE
    storage_name, storage_price = choose_component("Storage 1", components["Storage"])
    if storage_name:
        selected_components.append(("Storage", storage_name, storage_price))
    
    storage_name, storage_price = choose_component("Storage 2", components["Storage"])
    if storage_name:
        selected_components.append(("Storage", storage_name, storage_price))

    storage_name, storage_price = choose_component("Storage 3", components["Storage"])
    if storage_name:
        selected_components.append(("Storage", storage_name, storage_price))
    
    storage_name, storage_price = choose_component("Storage 4", components["Storage"])
    if storage_name:
        selected_components.append(("Storage", storage_name, storage_price))

    # PSU
    psu_name, psu_price = choose_component("Power Supply", components["Power Supply"])
    if psu_name:
        selected_components.append(("Power Supply", psu_name, psu_price))

    st.divider()
    st.subheader("Additional Components")

    # FAN COOLER
    fan_cooler_name, fan_cooler_price = choose_component("Fan Cooler", components["Fan Cooler"])
    if fan_cooler_name:
        selected_components.append(("Fan Cooler", fan_cooler_name, fan_cooler_price))

    # AIO COOLER
    aio_cooler_name, aio_cooler_price = choose_component("AIO Cooler", components["AIO Cooler"])
    if aio_cooler_name:
        selected_components.append(("AIO Cooler", aio_cooler_name, aio_cooler_price))

    # PC COOLER
    pc_cooler_name, pc_cooler_price = choose_component("PC Cooler 1", components["PC Cooler"])
    if pc_cooler_name:
        selected_components.append(("PC Cooler", pc_cooler_name, pc_cooler_price))
    
    pc_cooler_name, pc_cooler_price = choose_component("PC Cooler 2", components["PC Cooler"])
    if pc_cooler_name:
        selected_components.append(("PC Cooler", pc_cooler_name, pc_cooler_price))

    pc_cooler_name, pc_cooler_price = choose_component("PC Cooler 3", components["PC Cooler"])
    if pc_cooler_name:
        selected_components.append(("PC Cooler", pc_cooler_name, pc_cooler_price))

    # menampilkan tabel komponen yang dipilih dan total harga
    if selected_components:
        st.divider()
        st.title("Komponen yang dipilih:")
        df = pd.DataFrame(selected_components, columns=["Komponen", "Nama", "Harga"])
        df["Jumlah Beli"] = [st.number_input(f"Jumlah {row.Komponen} ({row.Nama}):", min_value=1, step=1, key=f"jumlah_{index}") for index, row in df.iterrows()]
        df["Total Harga"] = df["Harga"] * df["Jumlah Beli"]
        df.index = pd.RangeIndex(start=1, stop=len(df) + 1, step=1)
        st.table(df)

        # total harga
        st.write(f"\n**Total Harga**: Rp {df["Total Harga"].sum():,}")
    
    st.write("Terima kasih telah menggunakan simulasi ini!")

main()