import streamlit as st
import pandas as pd

#===================== Beranda ============================
st.logo("th.png", size='large')
st.set_page_config(page_title="Aplikasi Rumah Idaman", page_icon="🏡", layout="wide") #judul apk
st.title("Aplikasi Rumah Idaman🏡")

Beranda, ReferensiRumah, UkuranBangunan, Harga, TentangKami = st.tabs([
    "Beranda", "Referensi Rumah", "Ukuran Bangunan", "Harga", "Tentang Kami"])

#========== SIDEBAR BERANDA ==========

with Beranda:
    # ---- Judul aplikasi BERANDA ----
    st.header("Selamat Datang Di Aplikasi Menghitung Rumah Impian!")

    # Contoh gambar rumah impian beranda
    col1, col2, col3 = st.columns(3, gap="small")
    col2.image("rumah1.webp", width=700)

    # Tentang aplikasi beranda
    st.write("""
    Aplikasi ini dapat menemukan rumah yang 
    rumah yang sempurna sesuai kebutuhan dan keinginan Anda.
    Temukan, rencanakan, dan wujudkan Rumah Idaman Anda dengan Mudah dan Praktis.
    Kami hadir untuk membantu Anda mengeksplorasi Inspirasi Desain, Mengelola Perencanaan,
    hingga Mewujudkan Hunian yang sesuai dengan gaya hidup dan kebutuhan Anda.

    ### Apa yang Anda Cari?
    - **Ukuran Bangunan**: Pilih rumah dengan ukuran yang sesuai untuk keluarga Anda.  
    - **Luas Garasi**: Pastikan kendaraan Anda memiliki ruang yang aman dan nyaman.  
    - **Desain dan Volume Ruangan**: Temukan rumah dengan tata ruang yang fungsional dan modern.  
    - **Kapasitas**: Tentukan jumlah orang yang ideal untuk rumah impian.
    - **Harga Yang Pas**: Kami akan memberikan harga sesuai dengan kualitas yang anda inginkan.
             
    ### Tujuan Kami
    - Memberikan platform yang mempermudah Anda dalam mencari Inspirasi desain rumah.
    - Menyediakan alat untuk mengatur perencanaan pembangunan rumah secara efisien.
    - Menghubungkan Anda dengan Arsitek, Desainer, dan Penyedia jasa terpercaya.
             
    ### Manfaat Yang Anda Dapatkan
    - Perencanaan yang Mudah
      Gunakan fitur kami untuk Menghitung Lebar bangunan yang ideal, Menghitung anggaran, dan Jadwal pembangunan secara sistematis.
    - Hemat Waktu dan Biaya
      Dengan fitur perencanaan Cerdas, Anda dapat menghindari kesalahan yang berpotensi merugikan dan Memastikan proyek berjalan sesuai anggaran.
             

    **Mari memulai perjalanan Anda untuk mewujudkan rumah impian dengan mudah. Masukkan preferensi Anda, dan kami akan membantu mencarikan rumah terbaik untuk Anda!**
    """)

#========== SIDEBAR REFERENSI RUMAH ==========
with ReferensiRumah:
    st.header("Referensi Rumah")
    # ******** Gambar referensi *********
    for i in range(1, 2): #---- looping ---
        st.write(f"### Rumah 20 x 50")
        col1, col2 = st.columns(2, gap="small")
        col1.image(f"rumah1.webp", caption="20 x 50")
        col2.write(f"""
            Rumah mewah dengan lebar tanah 1000 M ini sangat ideal untuk keluarga Anda.
            Rumah 3 lantai ini sudah dilengkapi dengan halaman depan untuk bersantai dan kolam renang yang luas.
            Berikut fasilitas rumah:
            - **AC**
            - **2 Kamar Tidur**
            - **2 Kamar Mandi**
            - **Halaman Belakang**
            - **Rooftop**
            - **Kolam Renang**
            """)
        st.write("**Luas 1000 Meter, RP. 6.000.000.000**")

    for i in range(1, 2):
        st.write(f"## Rumah 15 x 20")
        col1, col2 = st.columns(2, gap="small")
        col1.image(f"rumah2.webp", caption="15 x 20")
        col2.write(f"""
            Rumah ini sangat ideal untuk keluarga Anda.
            Rumah 2 lantai ini dilengkapi dengan halaman depan yang luas untuk bersantai, disertai dengan kolam ikan.
            Berikut fasilitas rumah:
            - **AC**
            - **1 Kamar Tidur**
            - **1 Kamar Mandi**
            - **Halaman Belakang**
            - **Kolam Ikan**
        """)
        st.write("**Luas 300 Meter, RP. 2.046.000.000**")

    for i in range(1, 2):
        st.write(f"## Rumah 13 x 19")
        col1, col2 = st.columns(2, gap="small")
        col1.image(f"rumah3.webp", caption="13 x 19")
        col2.write(f"""
            Rumah ini sangat ideal untuk keluarga kecil Anda.
            Rumah 2 lantai ini dilengkapi dengan ruang tengah yang luas yang berhadapan langsung dengan halaman depan dan belakang.
            Berikut fasilitas rumah:
            - **AC**
            - **1 Kamar Tidur**
            - **1 Kamar Mandi**
            - **Halaman Belakang**
            - **Kolam Renang**
        """)
        st.write("**Luas 247 Meter, RP. 1,363.000.000**")

    for i in range(1, 2):
        st.write(f"## Rumah 11 x 14")
        col1, col2 = st.columns(2, gap="small")
        col1.image(f"rumah4.webp" , caption="13 x 19")
        col2.write(f"""
            Rumah ini sederhana nan elegan yang sangat ideal untuk keluarga Anda.
            Rumah 2 lantai ini dilengkapi dengan halaman yang luas serta garasi untuk mobil Anda.
            Berikut fasilitas rumah:
            - **AC**
            - **2 Kamar Tidur**
            - **1 Kamar Mandi**
            - **Garasi**
            - **Gudang**
        """)
        st.write("**Luas 154 Meter, RP. 1.097.000.000**")

    for i in range(1, 2):
        st.write(f"## Rumah 10 x 5")
        col1, col2 = st.columns(2, gap="small")
        col1.image(f"1.jpg", caption="10 x 5")
        col2.write(f"""
            Rumah ini sangat ideal untuk keluarga Anda.
            Berikut fasilitas rumah:
            - **AC**
            - **2 Kamar Tidur**
            - **1 Kamar Mandi**
            - **Halaman Belakang**
            - **Garasi**
            - **Kolam Renang**
                   """)
        st.write("**Luas 50 Meter, RP. 421.000.000**")



#=================== SIDEBAR HARGA ====================
#harga kerja kuli 6- 12 jt per meter
#harga elektrikal dan mekanikal 600rb per meter
#biaya material bangunan 1.5 jt per meter
    

# ********** harga properti ************
with Harga:
   
    st.header("Harga Properti")

    class HargaProperti: #------ class ------
        def __init__(self, harga_per_meterpersegi, biaya_jasa_per_bulan, biaya_elektrikal_mekanik_per_meter, biaya_material_bangunan_per_meter):
            self.harga_per_meterpersegi = harga_per_meterpersegi
            self.biaya_jasa_per_bulan = biaya_jasa_per_bulan
            self.biaya_elektrikal_mekanik_per_meter = biaya_elektrikal_mekanik_per_meter
            self.biaya_material_bangunan_per_meter = biaya_material_bangunan_per_meter

        def hitung_harga_properti(self, luas_bangunan):
            """
            Menghitung total harga bangunan per berdasarkan:
            - Harga per meter persegi
            - Biaya jasa kuli
            - Biaya elektrikal dan mekanik
            - Biaya material bangunan
            """
            #*** total ***
            harga_per_luas = luas_bangunan * self.harga_per_meterpersegi
            total_biaya_jasa_per_24bulan = self.biaya_jasa_per_bulan * 7 * 23  # 2 tahun dikurang 1 bln libur 
            total_biaya_elektrikal_mekanik = self.biaya_elektrikal_mekanik_per_meter * luas_bangunan
            total_biaya_material_bangunan = self.biaya_material_bangunan_per_meter * luas_bangunan
            total_harga = harga_per_luas + total_biaya_jasa_per_24bulan + total_biaya_elektrikal_mekanik + total_biaya_material_bangunan
            return harga_per_luas, total_harga, total_biaya_jasa_per_24bulan, total_biaya_elektrikal_mekanik, total_biaya_material_bangunan

    harga_per_m2 = 4000000  # Harga per meter
    biaya_jasa_per_bulan = 4000000 #per orang & bulan
    biaya_elektrikal_mekanik_per_meter = 1500000# per meter
    biaya_material_bangunan_per_meter = 6000000 #per meter
    total_biaya_per_meter = harga_per_m2 + biaya_jasa_per_bulan + biaya_elektrikal_mekanik_per_meter + biaya_material_bangunan_per_meter


    harga_properti = HargaProperti(harga_per_m2, biaya_jasa_per_bulan, biaya_elektrikal_mekanik_per_meter, biaya_material_bangunan_per_meter)

    # Input luas bangunan
    luas = st.number_input("Masukkan luas bangunan (m²):", min_value=0, step=1)
    # t_harga = None
    # menghitung total harga

    if st.button("Total Harga"):
        if luas >= 9:
            harga_per_luas, total_harga, total_biaya_jasa_24bulan, total_biaya_elektrikal_mekanik, total_biaya_material_bangunan = harga_properti.hitung_harga_properti(luas)
            if 't_harga' not in st.session_state:
                st.session_state.t_harga = total_harga
            # print("Ini dari tombol", t_harga)
            data_hasil = {
                "Keterangan": [
                "harga (per meter persegi) ",
                "biaya jasa (per orang dalam 1 bulan)",
                "biaya elektrikal dan mekanik (per meter)",
                "biaya material bangunan (per meter)",
                "total harga properti"
                    ],
                "Biaya per meter ": [
                    f"Rp {harga_per_m2:,.0f}",
                    f"Rp {biaya_jasa_per_bulan:,.0f}",
                    f"Rp {biaya_elektrikal_mekanik_per_meter:,.2f}",
                    f"Rp {biaya_material_bangunan_per_meter:,.2f}",
                    f"Rp {total_biaya_per_meter:,.2f}"
                    ],
                "Total biaya (24 bulan) ": [
                    f"Rp {harga_per_luas:,.0f}",
                    f"Rp {total_biaya_jasa_24bulan:,.0f}",
                    f"Rp {total_biaya_elektrikal_mekanik:,.2f}",
                    f"Rp {total_biaya_material_bangunan:,.2f}",
                    f"Rp {total_harga:,.2f}"
                    ]
                }
            df = pd.DataFrame(data_hasil)
            st.subheader("Rincian Biaya Properti")
            st.dataframe(df)
            st.success(f"Total harga properti: Rp {total_harga:,.0f}")#:,.0f untuk koma ribuan
            st.balloons()
        else:
            st.error("Nilai yang Anda masukkan tidak valid")

    st.markdown("---")



    #************ cicilan perbulan ***********
    st.header("Metode Pembayaran")
    def cicilan_pokok(pinjaman, tenor_bulan):
        return pinjaman / tenor_bulan

    def cicilan_bunga_per_bulan(pinjaman, tenor_tahun, tenor_bulan):
        return pinjaman * (5  / 100) * tenor_tahun / tenor_bulan #bunga 5%

    def total_cicilan_kpr_per_bulan(cicilan_pokok, cicilan_bunga_per_bulan):
        return cicilan_pokok + cicilan_bunga_per_bulan

         # Pilihan metode pembayaran
    option = st.selectbox(
        "Apa metode pembayaran yang Anda pilih?",
        ("Cash", "Cicilan KPR"),
        index=0,
        help="Pilih metode pembayaran yang sesuai",
    )

    st.write("Anda memilih metode pembayaran:", option)

    pinjaman = st.number_input("Masukkan jumlah pinjaman:", min_value=0.0, value=0.0, step=100000.0)

    # Pilihan tenor menggunakan selectbox
    tenor_tahun = st.selectbox(
        "Pilih tenor (dalam tahun):",
        (5, 10, 15),
        index=0,
        help="Pilih tenor pembayaran KPR"
    )

    # Konversi tenor ke bulan
    tenor_bulan = tenor_tahun * 12

    if st.button('Hitung Total'):
        # print("Ini dari bawah", t_harga)
        # if t_harga is not None:
            # Hitung jika metode pembayaran adalah "Cicilan KPR"
        if option.lower() == "cicilan kpr":
            if pinjaman > 0:
                cicilan_per_bulan = cicilan_pokok(pinjaman, tenor_bulan)
                bunga_per_bulan = cicilan_bunga_per_bulan(pinjaman, tenor_tahun, tenor_bulan)
                total_per_bulan = total_cicilan_kpr_per_bulan(cicilan_per_bulan, bunga_per_bulan)
                total_pinjaman_dilunasi = cicilan_per_bulan * tenor_bulan
                sisa_pinjaman = pinjaman - st.session_state.t_harga

                data_hasil = {
                    "Keterangan": [
                    "Cicilan Per Bulan",
                    "Bunga Per Bulan",
                    "Total Cicilan Per Bulan",
                    "Pinjaman Pokok(KPR)",
                    "Total Harga Properti",
                    "Sisa Pinjaman Bank"
                            ],

                    "Biaya (Rp)": [
                    f"Rp {cicilan_per_bulan:,.2f}",
                    f"Rp {bunga_per_bulan:,.2f}",
                    f"Rp {total_per_bulan:,.2f}",
                    f"Rp {pinjaman:,.0f}",
                    f"Rp {st.session_state.t_harga:,.0f}",
                    f"Rp {sisa_pinjaman:,.2f}"
                    ]
                }
                            
                df = pd.DataFrame(data_hasil)
                st.subheader("Rincian Biaya Properti")
                st.dataframe(df)
                        
                st.write("Pinjaman Bank:", f"Rp {pinjaman:,.2f}")
                st.write("Total Harga Properti:", f"Rp {st.session_state.t_harga:,.2f}")
                st.write("Sisa Pinjaman Bank:", f"Rp {sisa_pinjaman:,.0f}")
                st.balloons()

        elif option.lower() == "cash":
            if 'total_harga' in locals():
                st.info("Metode pembayaran Cash: Anda harus membayar seluruh pinjaman langsung.")
                st.write("Total yang harus dibayar:", f"Rp {st.session_state.t_harga:,.0f}")
                st.balloons()
            else:
                st.write("Total yang harus dibayar:", f"Rp {st.session_state.t_harga:,.0f}")
                st.balloons()
           
        else:
                st.warning("Hitung total harga terlebih dahulu")

       

#====================== SIDEBAR UKURAN BANGUNAN ====================
with UkuranBangunan:
    st.header("Menghitung Ukuran Bangunan")
    st.write("Menghitung ukuran bangunan ini mencangkup luas, tinggi, panjang, lebar, volume bangunan sesuai keinginan Anda.")

    def hitung_luas_bangunan(lebar_lahan, panjang_bangunan):
        return lebar_lahan * panjang_bangunan

    def hitung_jumlah_penghuni(luas_bangunan, luas_per_orang=9):
        return int(luas_bangunan // luas_per_orang)
    
    def hitung_volume_bangunan(panjang_bangunan, lebar_bangunan, tinggi_bangunan):
        return panjang_bangunan * lebar_bangunan * tinggi_bangunan
     
    # Streamlit input luas lahan dan panjang bangunan
    lebar_bangunan = st.number_input("Masukkan lebar lahan (m):", min_value=0, step=5)
    panjang_bangunan = st.number_input("Masukkan panjang bangunan (m):", min_value=0, step=5)
    tinggi_bangunan = st.number_input("Masukkan tinggi bangunan (m)", min_value=0, step=1)

    # Pastikan kedua input diberikan sebelum menghitung
    if tinggi_bangunan > 0 and panjang_bangunan > 0 and lebar_bangunan > 0:
        
    #************** Memanggil modul **************
        # Rumus luas bangunan
        luas_bangunan = hitung_luas_bangunan(panjang_bangunan, lebar_bangunan)

        #Rumus volume bangunan
        volume_bangunan = hitung_volume_bangunan(panjang_bangunan, lebar_bangunan, tinggi_bangunan)
 
        # Menghitung jumlah orang yang dapat tinggal
        jumlah_penghuni = hitung_jumlah_penghuni(luas_bangunan, luas_per_orang=9)
   
        # Hasil
    if st.button("Hasil Perhitungan"):
        if jumlah_penghuni > 0:
                st.success(f"Bangunan Ideal")
                st.write(f"Luas bangunan: {luas_bangunan:.2f} m²")
                st.write(f"Volume bangunan: {volume_bangunan} m²")
                st.write(f"Jumlah orang yang dapat tinggal: {jumlah_penghuni} orang")
        else:
            st.error("Nilai yang Anda masukkan tidak valid")


#=================== Tentang Kami =====================
with TentangKami:
    st.header("Tentang Kami")
    st.write("Aplikasi ini dibuat oleh kelompok 4, yang terdiri dari Fathiyah, Farhan, April, Najwa")
    
    col1, col2, col3, col4 = st.columns(4, gap="small")
    col1.image("tiyah.jpg", caption="Fathiyah SI06")
    col2.image("nayla.jpg", caption="Nayla SI06")
    col3.image("parhan.jpg", caption="Farhan SI06")
    col4.image("najwa.jpg", caption="Najwa SI06")
    st.markdown("---")

#*********** feedback *************
    st.subheader("Rating Kami")
    selected = st.feedback("faces")

    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    if selected is not None:
        st.markdown()
  

    sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
    selected = st.feedback("thumbs")
    if selected is not None:
        st.markdown()
  
  # ============= CSS untuk Streamlit ================
st.markdown(
    """
    <style>

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #8D0B41;
        color:  #ffe2ec;
        padding: 5px;
    }

    /* background */ 
    .stApp{
    background-image: url("https://images.unsplash.com/photo-1511389026070-a14ae610a1be?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }

    [data-testid="stHeader"] {
    background: rgba(0,0,0,0);
    }

    [data-testid="stToolbar"] {
    right: 2rem;
    }


    </style>
    """,
    unsafe_allow_html=True
)

# [theme]
# base="light"
# backgroundColor="#bfbebe"
# secondaryBackgroundColor="#f3f0f0"

