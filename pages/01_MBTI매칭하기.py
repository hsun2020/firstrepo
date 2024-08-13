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
        'INTP': '🔍 INTP: 창의적이고 분석적인 사고를 지니며, 복잡한 문제를 해결하는 것을 즐깁니다.',
        'ESTP': '🏎️ ESTP: 활발하고 모험을 즐기며, 즉각적인 반응과 행동을 중시하는 성향을 가집니다.',
        'ESFP': '🎉 ESFP: 외향적이고 사교적이며, 현재의 순간을 즐기고 다른 사람들과의 관계를 중시합니다.',
        'ENFP': '🌈 ENFP: 창의적이고 열정적이며, 사람들과의 깊은 연결과 가능성을 추구합니다.',
        'ENTP': '💡 ENTP: 창의적이고 혁신적인 사고를 지니며, 새로운 아이디어와 도전을 좋아합니다.',
        'ESTJ': '📊 ESTJ: 실용적이고 조직적인 성향을 가지며, 명확한 규칙과 절차를 선호합니다.',
        'ESFJ': '👩‍⚕️ ESFJ: 타인을 돕고 배려하는 것을 중요시하며, 친근하고 조화를 중시하는 성향을 가집니다.',
        'ENFJ': '💖 ENFJ: 강한 공감 능력을 가지며, 타인의 성장과 발전을 지원하는 것을 중요시합니다.',
        'ENTJ': '🚀 ENTJ: 전략적이고 목표 지향적이며, 자연스럽게 리더십을 발휘하는 성향을 가지고 있습니다.',
    }

    best_match = {
        'ISTJ': 'ESTJ 🤝',
        'ISFJ': 'ESFJ 🤝',
        'INFJ': 'ENFJ 🤝',
        'INTJ': 'ENTJ 🤝',
        'ISTP': 'ESTP 🤝',
        'ISFP': 'ESFP 🤝',
        'INFP': 'ENFP 🤝',
        'INTP': 'ENTP 🤝',
        'ESTP': 'ISTP 🤝',
        'ESFP': 'ISFP 🤝',
        'ENFP': 'INFP 🤝',
        'ENTP': 'INTP 🤝',
        'ESTJ': 'ISTJ 🤝',
        'ESFJ': 'ISFJ 🤝',
        'ENFJ': 'INFJ 🤝',
        'ENTJ': 'INTJ 🤝',
    }
    
    worst_match = {
        'ISTJ': 'INFP 💔',
        'ISFJ': 'ENTP 💔',
        'INFJ': 'ESTP 💔',
        'INTJ': 'ESFP 💔',
        'ISTP': 'ENFJ 💔',
        'ISFP': 'ENTJ 💔',
        'INFP': 'ESTJ 💔',
        'INTP': 'ESFJ 💔',
        'ESTP': 'INFJ 💔',
        'ESFP': 'INTJ 💔',
        'ENFP': 'ISTJ 💔',
        'ENTP': 'ISFJ 💔',
        'ESTJ': 'INFP 💔',
        'ESFJ': 'INTP 💔',
        'ENFJ': 'ISTP 💔',
        'ENTJ': 'ISFP 💔',
    }

    description = descriptions.get(mbti, '해당 MBTI 유형에 대한 정보가 없습니다.')
    best_match_type = best_match.get(mbti, '정보 없음')
    worst_match_type = worst_match.get(mbti, '정보 없음')

    return description, best_match_type, worst_match_type

# MBTI 정보를 가져오기
description, best_match, worst_match = get_mbti_info(mbti)

# 결과를 화면에 표시
st.write(f'🔍 **{mbti}** 유형의 특성:')
st.write(description)
st.write(f'🤝 **가장 잘 맞는 유형:** {best_match}')
st.write(f'💔 **가장 안 맞는 유형:** {worst_match}')
