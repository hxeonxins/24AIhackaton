import streamlit as st
text = st.text_input('Can I have your name?')
if st.button('저장'):
    if 'name' not in st.session_state:
        st.session_state.name = text
    else:
        st.session_state.name = text