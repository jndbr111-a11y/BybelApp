import streamlit as st
import google.generativeai as genai

# 1. Konfigurasie van die App se Voorkoms op die S25 Ultra
st.set_page_config(page_title="Bybelstudie Assistent", page_icon="📖", layout="centered")

# 2. Stel jou API-sleutel in (Vervang met jou eie sleutel)
genai.configure(api_key="AIzaSyBGCBgMjr3Vl-2efOtRUiCzc4FWgVhtx9s")

# 3. Die Teologiese Instruksies (Die "Brein")
SYSTEM_INSTRUCTION = """
Tree op as 'n Bybels-Protestantse teoloog. 
Jou doel is diepgaande eksegese en woordverklarings vir Jan de Beer.
BRONNE: Afrikaanse 2020-vertaling, Nestle-Aland Grieks, Biblia Hebraica.
TEOLOË: Karl Barth, John MacArthur, Johannes Calvyn, Ben Engelbrecht.
FORMAAT: 
1. Skrifteks (2020).
2. Grondteks met morfologiese ontleding.
3. Teologiese kommentaar vanuit die spesifieke Protestantse tradisie.
"""

# Initaliseer die Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    system_instruction=SYSTEM_INSTRUCTION
)

# 4. Gebruikerskoppelvlak (UI)
st.title("📖 Bybelstudie & Teologie App")
st.markdown("Verken die Skrif deur die lens van die Protestantse tradisie.")

# 'n Kantbalk vir instellings of ekstra inligting
with st.sidebar:
    st.header("Konteks-instellings")
    st.info("Hierdie App fokus op die Bybels-Protestantse teologie van Barth, MacArthur, Calvyn en Engelbrecht.")

# Die invoerblok vir die teksgedeelte
user_input = st.text_input("Voer 'n Bybelvers of teologiese vraag in:", placeholder="Bv. Romeine 1:16 of 'Wat sê Barth oor uitverkiesing?'")

if user_input:
    with st.spinner("Besig met teologiese ontleding..."):
        try:
            # Genereer die antwoord
            response = model.generate_content(user_input)
            
            # Vertoon die resultaat in 'n mooi formaat
            st.markdown("---")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Oeps, daar was 'n fout: {e}")

# Voeg 'n voetnota by
st.markdown("---")
st.caption("Ontwikkel vir Jan de Beer | Aangedryf deur Gemini 1.5 Pro")
