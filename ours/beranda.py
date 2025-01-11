import streamlit as st
from PIL import Image
from data_deskrip import *

# Fungsi untuk mengubah ukuran gambar
def resize_image(image_path, size=(300, 300)):
    img = Image.open(image_path)
    img_resized = img.resize(size)
    return img_resized

# Inisialisasi session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Fungsi untuk navigasi
def switch_page(page_name):
    st.session_state.page = page_name

# fungsi untuk mengambil data dari button yg di click
if "orders" not in st.session_state:
    st.session_state.orders = []

def add_order(item_name):
    st.success(f"{item_name}\
        \nberhasil ditambahkan ke pesanan!")

# Sidebar atau navigasi
st.sidebar.title("Menu")
if st.sidebar.button("Home", use_container_width=True):
    switch_page("Home")
if st.sidebar.button("Motherboard", use_container_width=True):
    switch_page("Motherboard")
if st.sidebar.button("CPU", use_container_width=True):
    switch_page("CPU")
if st.sidebar.button("GPU", use_container_width=True):
    switch_page("GPU")
if st.sidebar.button("SSD", use_container_width=True):
    switch_page("SSD")
if st.sidebar.button("RAM", use_container_width=True):
    switch_page("RAM")
if st.sidebar.button("PSU", use_container_width=True):
    switch_page("PSU")
if st.sidebar.button("Cooler", use_container_width=True):
    switch_page("Cooler")
if st.sidebar.button("Casing", use_container_width=True):
    switch_page("Casing")


# Menampilkan konten berdasarkan halaman
if st.session_state.page == "Home":
    st.title("Selamat datang di Merapi")
    st.subheader("(Mending Rakit PC)")
    st.write("**Solusi Lengkap untuk Merakit dan Meng-upgrade PC Impian Anda, Tanpa Ribet.**")
    st.caption(
    """
    <div style="text-align: center;">
        <p>Gunakan menu dibagian kiri untuk Menjelajahi lebih banyak produk lainnya.</p>
    </div>
    """,
    unsafe_allow_html=True
)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Cpu")
        st.image("ours/kumpulan gambar/intel core i9 gen 14.jpg", caption="Intel core i9 14900K Box")
        st.button("Go to CPU page", key="switch_button_1", on_click=switch_page, args=("CPU",))
    
    with col2:
        st.header("Gpu")
        st.image(resize_image("ours/kumpulan gambar/Rtx4090.jpg"), caption="MSI GeForce RTX 4090 GAMING X TRIO 24GB GDDR6X")
        st.button("Go to GPU page", key="switch_button_2", on_click=switch_page, args=("GPU",))

    with col3:
        st.header("Casing")
        st.image("ours/kumpulan gambar/casing techware.jpg", caption="TECWARE FLATLINE TG MK2")
        st.button("Go to Casing page", key="switch_button_3", on_click=switch_page, args=("Casing",))


elif st.session_state.page == "Motherboard":
    st.title("Motherboard")
    st.write((" ".join(deskrip_Motherboard)))
    
    col4, col5, col6, col7 = st.columns(4)
    with col4:
        st.subheader("Asrock")
        st.image("ours/kumpulan gambar/mobo b550m pro4.jpg", caption="ASROCK B550M PRO4 AMD")
        with st.popover("Press"):
            st.markdown("**Rp. 1.548.000**")
            st.markdown("Spesifikasi:")
            st.markdown((" ".join(asrock_b550m)))
            if st.button("Order now", key="mobo_1"):
                item_name = "ASROCK B550M PRO4 AMD"
                price = "Rp. 1.548.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)



    with col5:
        st.subheader("Srock")
        st.image("ours/kumpulan gambar/mobo b560m-hdv.jpg", caption="ASROCK MOTHERBOARD B560M HDV M.2 R2.0 (INTEL)")
        with st.popover("Press"):
            st.markdown("**Rp. 1.250.000**")
            st.markdown("Spesifikasi:")
            st.markdown((" ".join(asrock_b560m)))
            if st.button("Order now", key= "mobo_2") :
                item_name = "ASROCK MOTHERBOARD B560M HDV M.2 R2.0 (INTEL)"
                price = "Rp. 1.250.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)




    with col6:
        st.subheader("Asrock")
        st.image("ours/kumpulan gambar/mobo a520m-hvs.jpg", caption="ASROCK MOTHERBOARD A520M-HVS (AMD)")
        with st.popover("Press"):
            st.markdown("**Rp. 989.000**")
            st.markdown("Spesifikasi:")
            st.markdown((" ".join(asrock_a520m)))
            if st.button("Order now", key="mobo_3") :
                item_name = "ASROCK MOTHERBOARD A520M-HVS (AMD)"
                price = "Rp. 989.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)


    with col7:
        st.subheader("Asus")
        st.image("ours/kumpulan gambar/mobo rog strix.jpg", caption="ASUS Motherbord ROG STRIX B460-F GAMING")
        with st.popover("Press"):
            st.markdown("**Rp.3.300.000**")
            st.markdown("Spesifikasi:")
            st.markdown((" ".join(rog_strix)))
            if st.button("Order now", key="mobo_4") :
                item_name = "ASUS Motherbord ROG STRIX B460-F GAMING"
                price = "Rp.3.300.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)



elif st.session_state.page == "CPU":
    st.title("CPU")
    st.write("**Central processing unit**")
    st.write((" ".join(deskrip_CPU)))

    cpu1, cpu2, cpu3, cpu4 = st.columns(4)
    with cpu1:
        st.subheader("Amd ryzen 5000 series")
        st.image(resize_image("ours/kumpulan gambar/Cpu ryzen 5000 series.jpg"), caption="AMD Ryzen 9 5900X")
        with st.popover("Press"):
            st.markdown("**Rp. 5.730.000**")
            st.markdown((" ".join(ryzen_5_5000s)))
            if st.button("Order now", key="cpu1") :
                item_name = "AMD Ryzen 9 5900X"
                price = "Rp.5.730.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)



    with cpu2:
        st.subheader("Intel pentium Gold")
        st.image("ours/kumpulan gambar/cpu pentium gold.jpg", caption="intel pentium G5420")
        with st.popover("Press"):
            st.markdown("**Rp.840.000**")
            st.markdown((" ".join(intel_pentium)))
            if st.button("Order now", key="cpu2") :
                item_name = "Intel pentium G5420"
                price = "Rp.840.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)



    with cpu3:
        st.subheader("Amd ryzen 3000 series")
        st.image(resize_image("ours/kumpulan gambar/cpu ryzen 3000 series.jpg"), caption="Ryzen 5 3600")
        with st.popover("Press"):
            st.markdown("**Rp.2.020.000**")
            st.markdown((" ".join(ryzen_3_3000s)))
            if st.button("Order now", key="cpu3") :
                item_name = "Ryzen 5 3600"
                price = "Rp.2.020.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)




    with cpu4:
        st.subheader("Intel gen 10 series")
        st.image("ours/kumpulan gambar/cpu intel gen 10.jpg", caption="Intel I5 10400F")
        with st.popover("Press"):
            st.markdown("**Rp.1.635.000**")
            st.markdown((" ".join(intel_i5_gen10)))
            if st.button("Order now", key="cpu4") :
                item_name = "Intel I5 10400F"
                price = "Rp.1.635.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)




elif st.session_state.page == "GPU":
    st.title("GPU")
    st.write((" ".join(deskrip_GPU)))
    
    gpu1, gpu2, gpu3, gpu4 = st.columns(4)

    with gpu1:
        st.subheader("Amd Rx series")
        st.image(resize_image("ours/kumpulan gambar/gpu rx580.png"), caption="Radeon RX 580 8G")
        with st.popover("Press"):
            st.markdown("**Rp. 1.650.000**")
            st.markdown((" ".join(amd_rx580)))
            if st.button("Order now", key="gpu1") :
                item_name = "Radeon RX 580 8G"
                price = "Rp. 1.650.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)


    with gpu2:
        st.subheader("Nvidia G series")
        st.image(resize_image("ours/kumpulan gambar/gpu gtx 1660.png"), caption="GTX 1660 Gaming X 6G")
        with st.popover("Press"):
            st.markdown("**Rp. 1.679.000**")
            st.markdown((" ".join(gtx_1660)))
            if st.button("Order now", key="gpu2") :
                item_name = "GTX 1660 Gaming X 6G"
                price = "Rp. 1.679.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)



    with gpu3:
        st.subheader("Intel arc series")
        st.image(resize_image("ours/kumpulan gambar/gpu intel arc 750.png"), caption="Intel ARC 750")
        with st.popover("Press"):
            st.markdown("**Rp. 3.499.000**")
            st.markdown((" ".join(intel_arc_750)))
            if st.button("Order now", key="gpu3") :
                item_name = "Intel ARC 750"
                price = "Rp. 3.499.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

    with gpu4:
        st.subheader("Amd Radeon RX")
        st.image("ours/kumpulan gambar/amd radeon RX 6700xt.png", caption="Amd radeon RX 6700xt")
        with st.popover("Press"):
            st.markdown("**Rp. 3.821.000**")
            st.markdown((" ".join(amd_rx6700xt)))
            if st.button("Order now", key="gpu4") :
                item_name = "Amd radeon RX 6700xt"
                price = "Rp. 3.821.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

elif st.session_state.page == "SSD":
    st.title("SSD")
    st.write((" ".join(deskrip_SSD)))

    ssd1, ssd2, ssd3, ssd4 = st.columns(4)

    with ssd1:
        st.subheader("SSD Sata")
        st.image(resize_image("ours/kumpulan gambar/ssd sata samsung.jpg"), caption="Samsung SSD 870 EVO 500GB Sata 3")
        with st.popover("Press"):
            st.markdown("**Rp.821.000**")
            st.markdown(" ".join(samsung_500gb_sata_870evo))
            if st.button("Order now", key="ssd1") :
                item_name = "Samsung SSD 870 EVO 500GB Sata 3"
                price = "Rp.821.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

    with ssd2:
        st.subheader("SSD NVMe")
        st.image("ours/kumpulan gambar/ssd nvme crucial.png", caption="Crucial SSD P3 Plus PCIe Gen4 M.2 NVMe")
        with st.popover("Press"):
            st.markdown("**Rp.690.000**")
            st.markdown("Size : 500GB, Read/write: 4700/1900Mb/s, TBW 110")
            if st.button("Order now", key="ssd2") :
                item_name = "Crucial SSD P3 Plus PCIe Gen4 M.2 NVMe"
                price = "Rp.690.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

    with ssd3:
        st.subheader("SSD SATA")
        st.image("ours/kumpulan gambar/ssd sata kyo kaizen.jpg", caption="SSD KYO KAIZEN 128GB SATA III 2.5 6GB/S SSD SATA 3")
        with st.popover("Press"):
            st.markdown("**Rp.145.000**")
            st.markdown(" ".join(kyo_sata))
            if st.button("Order now", key="ssd3") :
                item_name = "SSD KYO KAIZEN 128GB SATA III 2.5 6GB/S SSD SATA 3"
                price = "Rp.145.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

    with ssd4:
        st.subheader("SSD NVMe")
        st.image("ours/kumpulan gambar/ssd nvme acer fa100.jpg", caption="ACER FA100 M.2 NVMe PCIe Gen3 x4 SSD - 1TB")
        with st.popover("Press"):
            st.markdown("**Rp.919.000**")
            st.markdown(" ".join(acer_fa100))
            if st.button("Order now", key="ssd4") :
                item_name = "ACER FA100 M.2 NVMe PCIe Gen3 x4 SSD - 1TB"
                price = "Rp.919.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)


elif st.session_state.page == "RAM":
    st.title("RAM")
    st.write((" ".join(deskrip_RAM)))
    
    ram1, ram2, ram3, ram4 = st.columns(4)

    with ram1:
        st.subheader("Ram DDR4")
        st.image("ours/kumpulan gambar/ram ddr4 kingston fury.png", caption="RAM Kingston Fury Beast RGB DDR4 3200MHz (PC25600) 8GB (1x8GB)")
        with st.popover("Press"):
            st.markdown("**Rp.375.000**")
            st.markdown(" ".join(ram_fury_kingston))
            if st.button("Order now", key="ram1") :
                item_name = "RAM Kingston Fury Beast RGB DDR4 3200MHz (PC25600) 8GB (1x8GB)"
                price = "Rp.375.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

    with ram2:
        st.subheader("Ram DDR3")
        st.image("ours/kumpulan gambar/ram ddr3 enpc.jpg", caption="RAM EnPC LONGDIMM DDR3 8GB 1600Mhz")
        with st.popover("Press"):
            st.markdown("**Rp.92.000**")
            st.markdown(" ".join(ram_enpc_longdimm))
            if st.button("Order now", key="ram2") :
                item_name = "RAM EnPC LONGDIMM DDR3 8GB 1600Mhz"
                price = "Rp.92.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

    with ram3:
        st.subheader("Ram DDR4")
        st.image("ours/kumpulan gambar/ram ddr4 teamgroup.jpg", caption="Team Ram T-Create Expert 16GB Kit (8GBX2) DDR 4 PC3600")
        with st.popover("Press"):
            st.markdown("**Rp. 495.000**")
            st.markdown(" ".join(ram_team_expert))
            if st.button("Order now", key="ram3") :
                item_name = "Team Ram T-Create Expert 16GB Kit (8GBX2) DDR 4 PC3600"
                price = "Rp. 495.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)
    
    with ram4:
        st.subheader("Ram DDR5")
        st.image("ours/kumpulan gambar/ram ddr 5 predator vesta.png", caption="PREDATOR VESTA II DDR5 6000 MHz RGB U-DIMM [Desktop RAM] - 32GB KIT")
        with st.popover("Press"):
            st.markdown("**Rp.1.899.000**")
            st.markdown(" ".join(ram_predator_vista))
            if st.button("Order now", key="ram4") :
                item_name = "PREDATOR VESTA II DDR5 6000 MHz RGB U-DIMM [Desktop RAM] - 32GB KIT"
                price = "Rp.1.899.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)


elif st.session_state.page == "PSU":
    st.title("PSU")
    st.write(" ".join(deskrip_PSU))
    
    psu1, psu2, psu3 = st.columns(3)

    with psu1:
        st.subheader("PSU 550W")
        st.image("ours/kumpulan gambar/psu coolermaster 550w.jpg", caption="Cooler Master MWE 550 V2 - 550W")
        with st.popover("Press"):
            st.markdown("**Rp. 770.000**")
            st.markdown(" ".join(psu_coolermaster))
            if st.button("Order now", key="psu1") :
                item_name = "Cooler Master MWE 550 V2 - 550W"
                price = "Rp. 770.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

    
    with psu2:
        st.subheader("PSU 650W")
        st.image("ours/kumpulan gambar/psu aerocool lux 650w.jpg", caption="Aerocool LUX 650W 80+ Bronze ATX PSU")
        with st.popover("Press"):
            st.markdown("**RP. 649.000**")
            st.markdown(" ".join(psu_lux))
            if st.button("Order now", key="psu2") :
                item_name = "Aerocool LUX 650W 80+ Bronze ATX PSU"
                price = "Rp. 649.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)


    with psu3:
        st.subheader("PSU 750W")
        st.image("ours/kumpulan gambar/psu corsair cv 750w.jpg",  caption="CV Series CV750 750 Watt 80 Plus Bronze")
        with st.popover("Press"):
            st.markdown("**Rp. 939.000**")
            st.markdown(" ".join(psu_cv_series))
            if st.button("Order now", key="psu3") :
                item_name = "CV Series CV750 750 Watt 80 Plus Bronze"
                price = "Rp. 939.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

elif st.session_state.page == "Cooler":
    st.title("Cooler")
    st.write(" ".join(deskrip_COOLER))


    with st.expander("**Air cooler**"):
        cpu_cooler1, cpu_cooler2 = st.columns(2)
        with cpu_cooler1:
            st.subheader("Armaggedon CPU Cooler")
            st.image("ours/kumpulan gambar/air cooler armaggedon.png", caption="Armaggeddon Air Cooler Blizzard 3 ARGB PC Cooler 6 Heat Pipes Direct Contact Technology")
            with st.popover("Press"):
                st.markdown("**Rp. 270.000**")
                st.markdown(" ".join(cooler_cpu_armageddon))
                if st.button("Order now", key="cooler1") :
                    item_name = "Armaggeddon Air Cooler Blizzard 3 ARGB PC Cooler 6 Heat Pipes Direct Contact Technology"
                    price = "Rp. 270.000"
                    st.session_state.orders.append({"Item": item_name, "Price": price})
                    add_order(item_name)
                    

    with cpu_cooler2:
        st.subheader("PcCooler CPU Cooler")
        st.image("ours/kumpulan gambar/air cooler pccooler.jpg", caption="PCCOOLER Air Cooler / PC COOLER R200")
        with st.popover("Press"):
            st.markdown("**Rp. 145.000**")
            st.markdown(" ".join(cooler_pccooler))
            if st.button("Order now", key="cooler2") :
                item_name = "PCCOOLER Air Cooler / PC COOLER R200"
                price = "Rp. 145.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

    with st.expander("**AIO Cooler**"):
        aio_cooler1, aio_cooler2 = st.columns(2)

    with aio_cooler1:
          st.subheader("KYO Liquid Cooler")
          st.image("ours/kumpulan gambar/liquid cooler kyo sama.jpg", caption="KYO SAMA PI240B ARGB AIO Liquid Cooling 240mm AIO 240")
          with st.popover("Press"):
               st.markdown("**Rp. 770.000**")
               st.markdown(" ".join(liquid_kyo_cooling))
               if st.button("Order now", key="cooler3") :
                    item_name = "KYO SAMA PI240B ARGB AIO Liquid Cooling 240mm AIO 240"
                    price = "Rp. 770.000"
                    st.session_state.orders.append({"Item": item_name, "Price": price})
                    add_order(item_name)
    
    with aio_cooler2:
        st.subheader("DeepCool Liquid Cooler")
        st.image("ours/kumpulan gambar/liquid cooler deepcool.jpg", caption="DeepCool LE720 ARGB - 360mm AIO Liquid")
        with st.popover("Press"):
                st.markdown("**Rp. 1.079.000**")
                st.markdown(" ".join(liquid_deepcool))
                if st.button("Order now", key="cooler4") :
                    item_name = "DeepCool LE720 ARGB - 360mm AIO Liquid"
                    price = "Rp. 1.079.000"
                    st.session_state.orders.append({"Item": item_name, "Price": price})
                    add_order(item_name)

    with st.expander("Pc cooler"):
     pc_cooler1, pc_cooler2 = st.columns(2)
    
     with pc_cooler1:
        st.subheader("KYO Fan Cooler")
        st.image(resize_image("ours/kumpulan gambar/pc cooler kyo1.png"), caption="KYO InfinitiX Fan ARGB 120mm ARGB Sync")
        with st.popover("Press"):
             st.markdown("**Rp. 69.000**")
             st.markdown(" ".join(kyo_ifinitix_120mm))
             if st.button("Order now", key="cooler5") :
                item_name = "KYO InfinitiX Fan ARGB 120mm ARGB Sync"
                price = "Rp. 69.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

     with pc_cooler2:
        st.subheader("KYO Fan Cooler")
        st.image(resize_image("ours/kumpulan gambar/pc cooler kyo2.jpg"), caption="KYO InfinitiX PL120 Fan ARGB 120mm ARGB")
        with st.popover("Press"):
             st.markdown("**Rp. 125.000**")
             st.markdown(" ".join(kyo_ifinitix_pl120))
             if st.button("Order now", key="cooler6") :
                item_name = "KYO InfinitiX PL120 Fan ARGB 120mm ARGB"
                price = "Rp. 125.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)



elif st.session_state.page == "Casing":
    st.title("Casing")
    st.write("Casing PC adalah komponen penting dalam sistem komputer yang sering dianggap hanya sebagai\
              pelindung fisik. Namun, casing memiliki peran lebih besar daripada itu.")
    
    case1, case2, case3 = st.columns(3)

    with case1:
        st.subheader("Case sades")
        st.image("ours/kumpulan gambar/case sades.jpg", caption="Case Sades Seth")
        with st.popover("Press"):
            st.markdown("**Rp. 450.000**")
            st.markdown(" ".join(case_sades_seth))
            if st.button("Order now", key="case1") :
                item_name = "Case Sades Seth"
                price = "Rp. 450.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

    with case2:
        st.subheader("Case sades")
        st.image("ours/kumpulan gambar/case sades2.jpg", caption="Case Sades Sphinx White")
        with st.popover("Press"):
            st.markdown("**Rp. 455.000**")
            st.markdown(" ".join(case_sades_sphinx))
            if st.button("Order now", key="case2") :
                item_name = "Case Sades Sphinx White"
                price = "Rp. 455.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)

    with case3:
        st.subheader("Case Da")
        st.image("ours/kumpulan gambar/case digial alliance.jpg", caption="Casing Digital Alliance 335B")
        with st.popover("Press"):
            st.markdown("**Rp. 395.000**")
            st.markdown(" ".join(case_digital_alliance_old))
            if st.button("Order now", key="case3") :
                item_name = "Casing Digital Alliance 335B"
                price = "Rp. 395.000"
                st.session_state.orders.append({"Item": item_name, "Price": price})
                add_order(item_name)