import streamlit as st
from streamlit_mermaid import st_mermaid

st.set_page_config(
    page_title="홈페이지",
    page_icon=":shark:",
    layout="wide"
)

st.title("요약")

st.subheader("**최종 목표 : AI 기반 개인 맞춤 여행지 추천 웹서비스 개발**")

st.write("**1차 목표 : 최소기능제품(Minimum Viable Product) 개발**")
st.write("1. 최소기능 : AI 기반 개인 맞춤형 여행지 추천")
st.write("2. 개발완료 예정일 : 9월 31일")
st.write("3. 프로세스")

processing = """flowchart LR
    데이터클리닝 --> 데이터분석
    데이터분석 --> AI개발
    AI개발 --> API개발
    API개발 --> 최소기능제품개발
    프론트엔드개발 --> 최소기능제품개발
"""

st_mermaid(processing)

st.write("**이슈 논의**")
st.write("""1. 여행지에 대해 카카오지도 API 기반 데이터 필터링 작업을 거침 &rarr;
        카카오지도 내에서 검색 되지 않은 여행지 우선 제외 &rarr;
        네이버지도를 통해 검수 과정 필요""", unsafe_allow_html=True)
st.write("""2. 추천 대상 기준 확립을 통한 여행지 데이터에 대한 전수검수 필요""")