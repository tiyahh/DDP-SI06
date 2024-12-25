import streamlit as st

# st.title("hellow kawand")
# st.write("hallo")
# st.markdown("selamat datang")
# st.video("http://33.media.tumblr.com/3ea4be126abfa7a36da0a51bcc7b061c/tumblr_n9wwqq3htN1trhk44o1_500.gif")

st.image("sp.jpeg")
dashboard = st.Page("./fitur/dashboard.py", title="dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")

pg = st.navigation(
    {
        "Menu utama" : [dashboard],
        "Transaksi" : [nabung],
    }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()