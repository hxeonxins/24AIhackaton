import streamlit as st

st.title('My Favorit Subject is.. Web! 😆')
st.header('what your favorit subject?')

text = st.text_input('Can I have your name')
if st.button('이름 저장'):
    if 'name' not in st.session_state:
        st.session_state.name = text
    else:
        st.session_state.name = text

number = st.text_input('Can I have your number?')
if st.button('번호 저장'):
    if 'number' not in st.session_state:
        st.session_state.number = number
    else:
        st.session_state.number = number
