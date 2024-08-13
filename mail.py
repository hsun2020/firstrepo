import streamlit as st

st.title('나의 첫 웹 서비스 만들기!✌️')

# 사용자로부터 이름을 입력받기
name = st.text_input('이름을 입력해주세요!')

# 사용자로부터 좋아하는 음식을 선택받기
menu = st.selectbox(
    '좋아하는 음식을 선택해주세요!',
    ['망고빙수', '아몬드봉봉', '요아정', '민초']
)

# 버튼을 눌렀을 때 인사말 출력
if st.button('인사말 생성하기'):
    st.write(name + '님! 당신이 좋아하는 음식은 ' + menu + '이군요! 저도 좋아요!')

  
