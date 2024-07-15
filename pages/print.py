import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

sum = 0

if st.button('불러오기'):
    sum=0;
    st.subheader("객관식 답안 : " + st.session_state.picOne)
    if (st.session_state.picOne == "200 - 요청이 성공적으로 처리됨") :
        sum += 50
        st.text("맞음")
    else :
        st.text("이걸 틀리네....🤣🤣🤣🤣🤣🤣")

    st.subheader("주관식 답안 : " + st.session_state.ansswer)
    if (st.session_state.ansswer == "REST API는 기존 API체계를 GET, POST, PUT/PATCH, DLELETE를 사용해서 하나의 주소로 관리한다.") :
        sum += 50
        st.text("맞음")
    else :
        st.text("이걸 틀리네….🤣🤣🤣🤣🤣🤣")

    st.subheader(f"총 점수 : {sum}")

    cred = credentials.Certificate('secret.json')

    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://aihackaton-253aa-default-rtdb.firebaseio.com/'
    })

    ref = db.reference('score')
    ref.set({'sum': sum})
    print(sum)