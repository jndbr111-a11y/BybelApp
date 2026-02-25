import streamlit as st
import google.generativeai as genai

# 1. Bladsy-instellings
st.set_page_config(page_title="Bybelstudie Jan de Beer", page_icon="📖")

# 2. Sleutel Invoer (Maak seker u regte sleutel is hier tussen die aanhalings)
API_KEY = "AIzaSyBGCBgMjr3Vl-2efOtRUiCzc4FWgVhtx9s"
genai.configure(api_key=API_KEY)

# 3. Teologiese Instruksies
SYSTEM_PROMPT = """
Tree op as 'n Protestantse Teoloog. 
Fokus: Afrikaanse 2020-vertaling, Nestle-Aland Grieks, Biblia Hebraica.
Teoloë: Karl Barth, John MacArthur, Calvyn en Ben Engelbrecht.
Verskaf altyd woordverklarings uit die grondtale.
"""

# HIER IS DIE BELANGRIKE VERANDERING:
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest"
)

# 4. Die Koppelvlak
st.title("📖 Bybelstudie-Assistent")
st.subheader("Vir Ds. Jan de Beer")

query = st.text_input("Voer 'n teksgedeelte of vraag in:")

if query:
    with st.spinner("Besig met eksegese..."):
        try:
            # Ons stuur die instruksie saam met die vraag vir stabiliteit
            response = model.generate_content(f"{SYSTEM_PROMPT}\n\nVraag: {query}")
            st.markdown("---")
            st.write(response.text)
        except Exception as e:
            st.error(f"Fout: {e}")
