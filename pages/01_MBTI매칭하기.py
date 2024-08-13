import streamlit as st

# 타이틀과 설명
st.title('MBTI 유형 분석기 🔍✨')
st.write('당신의 MBTI 유형을 선택하고, 나의 특성과 잘 맞는 유형, 그렇지 않은 유형을 알아보세요!')

# MBTI 유형 선택
mbti = st.selectbox(
    '당신의 MBTI 유형을 선택해주세요!',
    ['ISTJ', 'ISFJ', 'INFJ', 'INTJ',
     'ISTP', 'ISFP', 'INFP', 'INTP',
     'ESTP', 'ESFP', 'ENFP', 'ENTP',
     'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
)

# MBTI 유형에 따른 특성 설명 및 추천
def get_mbti_info(mbti):
    descriptions = {
        'ISTJ': '📋 ISTJ: 책임감이 강하고 신뢰할 수 있는 사람으로, 조직적이며 규칙을 중시합니다.',
        'ISFJ': '🛡️ ISFJ: 친절하고 배려심이 깊으며, 안정적이고 실용적인 접근 방식을 선호합니다.',
        'INFJ': '🌟 INFJ: 직관적이며 이상주의적인 성향을 가진 사람으로, 깊은 통찰력과 공감 능력을 지니고 있습니다.',
        'INTJ': '🧠 INTJ: 분석적이며 전략적 사고를 중요시하며, 독립적이고 목표 지향적인 성향을 가지고 있습니다.',
        'ISTP': '🛠️ ISTP: 현실적이고 실용적인 문제 해결 능력을 지니며, 혼자서 작업하는 것을 선호합니다.',
        'ISFP': '🎨 ISFP: 감성적이며 예술적 재능을 가지고 있고, 자유롭고 편안한 환경을 선호합니다.',
        'INFP': '💭 INFP: 이상주의적이고 내향적인 성향을 가지며, 자신의 가치와 신념을 중시합니다.',
        'INTP': '🔍 INTP: 창의적이고 분석적인 사고를 지니며, 복잡한 문제를 해결하는 
