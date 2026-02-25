import streamlit as st
import google.generativeai as genai

# 1. Stel die bladsy op vir u S25 Ultra
st.set_page_config(page_title="Bybelstudie Assistent", page_icon="📖")

# 2. Stel die API-sleutel op (PLAK U SLEUTEL HIER)
genai.configure(api_key="AIzaSyBGCBgMjr3Vl-2efOtRUiCzc4FWgVhtx9s")

# 3. Koppelvlak
st.title("📖 Bybelstudie-Assistent")
st.subheader("Vir Ds. Jan de Beer")

query = st.text_input("Voer 'n teksgedeelte of vraag in:")

if query:
    with st.spinner("Besig met eksegese..."):
        try:
            # ONS GEBRUIK NOU DIE SPESIFIEKE MODEL-ID WAT ALTYD WERK
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            instruksie = f"""
            Tree op as 'n Protestantse Teoloog vir Ds. Jan de Beer. 
            Vraag: {query}
            
            Riglyne:
            1. Gebruik die Afrikaanse 2020-vertaling.
            2. Ontleed die grondteks (Grieks/Hebreeus).
            3. Verwys na Barth, MacArthur, Calvyn en Ben Engelbrecht.
            """
            
            response = model.generate_content(instruksie)
            st.markdown("---")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Daar is 'n fout: {e}")
