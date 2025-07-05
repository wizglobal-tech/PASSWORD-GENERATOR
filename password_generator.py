import streamlit as st
import secrets
import string

st.set_page_config(page_title="Password Generator", layout="centered")

if "password" not in st.session_state:
    st.session_state.password = ""

st.title("🔑 Password Generator")

length = st.slider("Password Length", min_value=8, max_value=64, value=12)

if st.button("Generate Password"):
    char_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(secrets.choice(char_set) for _ in range(length))
    st.session_state.password = password

if st.session_state.password:
    st.subheader("Your Generated Password")
    st.code(st.session_state.password, language=None)
    st.markdown("*Select the password above and copy it manually.*")

st.markdown("*Click 'Generate Password' again to create a new password with the same settings.*")