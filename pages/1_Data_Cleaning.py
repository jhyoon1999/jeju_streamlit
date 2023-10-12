import streamlit as st
from streamlit_mermaid import st_mermaid
import pandas as pd

st.set_page_config(
    page_title="데이터클리닝",
    page_icon=":shark:",
    layout="wide"
)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(['데이터 클리닝', 
                                                '여행', '스포츠,레저', '카페',
                                                '서비스, 산업', '문화, 예술', '시장', '교통,수송'])

#%%데이터 불러오기
@st.cache_data
def get_item_list() :
    data = pd.read_excel('Data/item_features_show_cleaning.xlsx')
    return data

items = get_item_list()

@st.cache_data
def get_travel(items) :
    travel = items[items['category_name'].str.contains("여행 >")]
    return travel

@st.cache_data
def get_sports(items) :
    sports = items[items['category_name'].str.contains("스포츠,레저")]
    return sports

@st.cache_data
def get_cafe(items) :
    cafe = items[items['category_name'].str.contains("음식점 > 카페")]
    return cafe

@st.cache_data
def get_service(items) :
    service = items[items['category_name'].str.contains("서비스,산업")]
    return service

@st.cache_data
def get_art(items) :
    art = items[items['category_name'].str.contains("문화,예술 >")]
    return art

@st.cache_data
def get_market(items) :
    market = items[items['category_name'].str.contains("가정,생활 > 시장")]
    return market

@st.cache_data
def get_transport(items) :
    transport = items[items['category_name'].str.contains("교통,수송 >")]
    return transport

travel = get_travel(items)
sports = get_sports(items)
cafe = get_cafe(items)
service = get_service(items)
art = get_art(items)
market = get_market(items)
transport = get_transport(items)


#%% 데이터 클리닝
with tab1 : 
    st.subheader("Data Cleaning Process")

    cleaning_process = """
    classDiagram
        여행 --|> USER_FEATURES : Aggregation
        여행객Master --|> USER_FEATURES : Aggregation
        방문지 --|> ITEM_RATINGS : Filtering
        방문지  --|> Not_Searched_SPOT : Filtering
        방문지  --|> Not_JEJU : Filtering
        USER_FEATURES --|> Cleaning Data : Aggregation
        ITEM_RATINGS --|> Cleaning Data : Aggregation
        Cleaning Data --|> 추천대상선정 : Filtering
        추천대상선정 --|> Train Data : Filtering
        
        class 여행
        여행 : -주요변수-
        여행 : 1. 여행ID
        여행 : 2. 여행객ID
        여행 : 3. 여행미션
        
        여행 : (구성)
        여행 : (3600개의 개별적인 여행 SET)
        
        class 여행객Master
        여행객Master : -주요변수-
        여행객Master : 1. 여행객ID
        여행객Master : 2. 성별
        여행객Master : 3. 연령대
        여행객Master : 4. 여행스타일
        여행객Master : 5. 여행동기
        여행객Master : 6. 동반현황
        
        여행객Master : (구성)
        여행객Master : (3600개의 개별적인 여행 SET)
        
        class 방문지
        방문지 : -주요변수-
        방문지 : 1. 여행ID
        방문지 : 2. 방문지명
        방문지 : 3. 체류시간
        방문지 : 4. 방문지유형코드
        방문지 : 5. 방문석택이유
        방문지 : 6. 만족도
        방문지 : 7. 재방문의향
        방문지 : 8. 추천의향
        
        방문지 : (구성)
        방문지 : (4243개 여행방문지 SET)
        
        class USER_FEATURES
        USER_FEATURES : 여행정보와 여행객MASTER 정보를 모두 갖는 3238개 여행 SET
        
        class ITEM_RATINGS
        ITEM_RATINGS : 카카오지도에서 검색된 제주도 방문지 2315개
        
        class Not_Searched_SPOT
        Not_Searched_SPOT : 카카오지도에서 검색되지 않은 방문지 365개
        
        class Not_JEJU 
        Not_JEJU : 제주도가 아닌 방문지 1563개
        
        class Cleaning Data
        Cleaning Data : USER_FEATURES과 ITEM_RATINGS를 join한 데이터
        Cleaning Data : (구성)
        Cleaning Data : (1. 2504개 TRAVEL_ID)
        Cleaning Data : (2. 2004개의 SPOT_ID --> 통합과정을 통한 New Spot_ID 1684개)
        Cleaning Data : (3. 13540개의 RATING)
        
        class 추천대상선정
        추천대상선정 : 카카오지도 API 업종 분류
        추천대상선정 : 1. 여행
        추천대상선정 : 2. 스포츠, 레저
        추천대상선정 : 3. 음식점 > 카페
        추천대상선정 : 4. 서비스, 산업
        추천대상선정 : 5. 문화, 예술
        추천대상선정 : 6. 가정, 생활 > 시장
        추천대상선정 : 7. 교통, 수송
        
        class Train Data
        Train Data : 여행지 1318곳
        Train Data : 여행객 2457명
        Train Data : rating 12587개
    """

    st_mermaid(cleaning_process, height = "3000px")

#%% show data
with tab2 : #여행
    st.dataframe(data = travel)
    st.write("데이터 크기:",travel.shape[0], "개 방문지")
    st.write("평균 만족도 점수:",  travel['평균 만족도 점수'].mean(), "점")
    st.write("평균 재방문의향 점수:",  travel['평균 재방문의향 점수'].mean(), "점")
    st.write("평균 추천의향 점수:",  travel['평균 추천의향 점수'].mean(), "점")

with tab3 : #sports
    st.dataframe(data = sports)
    st.write("데이터 크기:",sports.shape[0], "개 방문지")
    st.write("평균 만족도 점수:",  sports['평균 만족도 점수'].mean(), "점")
    st.write("평균 재방문의향 점수:",  sports['평균 재방문의향 점수'].mean(), "점")
    st.write("평균 추천의향 점수:",  sports['평균 추천의향 점수'].mean(), "점")

with tab4 : #cafe
    st.dataframe(data = cafe)
    st.write("데이터 크기:",cafe.shape[0], "개 방문지")
    st.write("평균 만족도 점수:",  cafe['평균 만족도 점수'].mean(), "점")
    st.write("평균 재방문의향 점수:",  cafe['평균 재방문의향 점수'].mean(), "점")
    st.write("평균 추천의향 점수:",  cafe['평균 추천의향 점수'].mean(), "점")

with tab5 : #service
    st.dataframe(data = service)
    st.write("데이터 크기:",service.shape[0], "개 방문지")
    st.write("평균 만족도 점수:",  service['평균 만족도 점수'].mean(), "점")
    st.write("평균 재방문의향 점수:",  service['평균 재방문의향 점수'].mean(), "점")
    st.write("평균 추천의향 점수:",  service['평균 추천의향 점수'].mean(), "점")

with tab6 : #art
    st.dataframe(data = art)
    st.write("데이터 크기:",art.shape[0], "개 방문지")
    st.write("평균 만족도 점수:",  art['평균 만족도 점수'].mean(), "점")
    st.write("평균 재방문의향 점수:",  art['평균 재방문의향 점수'].mean(), "점")
    st.write("평균 추천의향 점수:",  art['평균 추천의향 점수'].mean(), "점")

with tab7 : #market
    st.dataframe(data = market)
    st.write("데이터 크기:",market.shape[0], "개 방문지")
    st.write("평균 만족도 점수:",  market['평균 만족도 점수'].mean(), "점")
    st.write("평균 재방문의향 점수:",  market['평균 재방문의향 점수'].mean(), "점")
    st.write("평균 추천의향 점수:",  market['평균 추천의향 점수'].mean(), "점")

with tab8 : #transport
    st.dataframe(data = transport)
    st.write("데이터 크기:",transport.shape[0], "개 방문지")
    st.write("평균 만족도 점수:",  transport['평균 만족도 점수'].mean(), "점")
    st.write("평균 재방문의향 점수:",  transport['평균 재방문의향 점수'].mean(), "점")
    st.write("평균 추천의향 점수:",  transport['평균 추천의향 점수'].mean(), "점")