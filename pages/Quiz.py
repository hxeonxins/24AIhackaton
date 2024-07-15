import streamlit as st

st.header('Try this Quize!!')
ansswer = st.text_input('REST API의 개념을 설명하시오. (단, 다음 단어가 반드시 포함 될 것->GET, POST, PUT/PATCH, DELETE)')
if st.button('주관식 제출'):
    if 'ansswer' not in st.session_state:
        st.session_state.ansswer = ansswer
    else:
        st.session_state.ansswer = ansswer

picOne = st.radio(
    "다음 http 프로토콜 통신 중 옳은 것은?",
    ["200 - 요청이 성공적으로 처리됨", "300 - 서버 문제로 요청 오류", "500 - 클라이언트 문제로 요청 오류", "100 - 요청이 성공적으로 처리 됨", "400 - 클라이언트 요청이 성공적으로 처리됨"],
    index=None,
)
st.write("You selected:", picOne)

if st.button('객관식 제출'):
    if 'picOne' not in st.session_state:
        st.session_state.picOne = picOne
    else:
        st.session_state.picOne = picOne