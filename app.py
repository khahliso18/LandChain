import streamlit as st

st.set_page_config(page_title="LandChain", layout="wide")

st.title("🏡 LandChain Startup App")

st.header("Problem")
st.write("Land fraud and slow manual verification")

st.header("Solution")
st.write("Blockchain-based land registry system")

st.header("Actors")
st.write("Government, Buyer, Seller, Registrar")

st.header("Token")
st.write("LandCoin rewards users")

st.header("Simulation")

if st.button("Add Block"):
    st.write("New block added to blockchain")
