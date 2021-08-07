import streamlit as st

# Custom imports
from multipage import MultiPage
import home
from pages import amazon, nykaa, tatacliq
# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Khadija's Closet")

# Add all your applications (pages) here
app.add_page("Home",home.app)
app.add_page("Nykaa", nykaa.app)
app.add_page("Amazon", amazon.app)
app.add_page("TataCliq", tatacliq.app)

# The main app
app.run()