import streamlit as st

home=st.Page('pages/home.py', title='Home', icon=':material/home:')
conn=st.Page('pages/wifi_connecter.py',title='Wifi Connecter',icon=':material/wifi:')
dashboard=st.Page('pages/dashboard.py',title='Dashboard',icon=':material/dashboard:')


pg=st.navigation(
    {
        "Home Page":[home],
        "Connect":[conn],
    "Dashboard":[dashboard]
    }
)


pg.run()