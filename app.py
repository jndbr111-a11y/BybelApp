import streamlit as st
import google.generativeai as genai

# 1. Basiese App Opstelling
st.set_page_config(page_title="Bybelstudie Assistent", page_icon="📖")

# 2. Sleutel Konfigurasie (Maak seker u sleutel is tussen die aanhalings)
genai.configure(api_key="AIzaSyBGCBgMjr3Vl-2efOtRUiCzc4FWgVhtx9s")

# 3. Koppelvlak
st.title("📖 Bybelstudie-Assistent")
st.subheader("Vir Ds. Jan de Beer")

query = st.text_input("Voer 'n teksgedeelte of teologiese vraag in:")

if query:
    with st.spinner("Besig met eksegese..."):
        try:
            # ONS GEBRUIK NOU DIE MEES STABIELE MODELNAAM
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            Tree op as 'n Protestantse Teoloog. 
            Onderwerp: {query}
            
            Riglyne:
            1. Gebruik die Afrikaanse 2020-vertaling.
            2. Ontleed die grondteks (Nestle-Aland Grieks of Biblia Hebraica).
            3. Verskaf perspektiewe van Karl Barth, John MacArthur, Johannes Calvyn en Ben Engelbrecht.
            4. Verskaf volledige woordverklarings uit die grondtale.
            """
            
            response = model.generate_content(prompt)
            st.markdown("---")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Verbindingsfout: {e}")
