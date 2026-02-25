import streamlit as st
import google.generativeai as genai

# 1. Konfigurasie van die bladsy
st.set_page_config(page_title="Bybelstudie Jan de Beer", page_icon="📖")

# 2. Sleutel Invoer (Vervang die teks tussen die aanhalings met u regte sleutel)
API_KEY = "AIzaSyBGCBgMjr3Vl-2efOtRUiCzc4FWgVhtx9s"
genai.configure(api_key=API_KEY)

# 3. Teologiese Instruksies
SYSTEM_PROMPT = """
Tree op as 'n Protestantse Teoloog. 
Fokus: Afrikaanse 2020-vertaling, Nestle-Aland Grieks, Biblia Hebraica.
Teoloë: Karl Barth, John MacArthur, Calvyn en Ben Engelbrecht.
Verskaf altyd woordverklarings uit die grondtale.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    system_instruction=SYSTEM_PROMPT
)

# 4. Die Koppelvlak vir die S25 Ultra
st.title("📖 Bybelstudie-Assistent")
st.subheader("Vir Ds. Jan de Beer")

query = st.text_input("Voer 'n teksgedeelte of vraag in:", placeholder="Bv. Romeine 5:1")

if query:
    with st.spinner("Besig met eksegese..."):
        try:
            response = model.generate_content(query)
            st.markdown("---")
            st.write(response.text)
        except Exception as e:
            st.error(f"Fout: {e}")
