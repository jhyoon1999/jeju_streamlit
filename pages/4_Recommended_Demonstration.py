import streamlit as st
import pandas as pd
import requests

#import os
#print(os.getcwd())
#os.chdir(r'c:\Users\gardp\OneDrive\바탕 화면\업무\여행지_추천_웹서비스_업무\추천시스템_0920\09_Streamlit')

@st.cache_data
def get_item_value_list() :
    data = pd.read_excel(r'item_value_list.xlsx')
    return data

#item_value_list = pd.read_excel('item_value_list.xlsx')
item_value_list = get_item_value_list()

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(['추천 요청서 작성', 
                                                '여행', '스포츠,레저', '카페',
                                                '서비스', '아트', '시장', '교통,수송'])



with tab1 :
    with st.form(key = 'Request', clear_on_submit=False) :
        request_body = None
        response = None
        user_features = {}
        filtering = {}
        
        #1. 성별
        gender_list = list(item_value_list['GENDER'].dropna().unique())
        gender = st.selectbox('귀하의 성별을 선택해주세요.', gender_list)
        
        if gender :
            user_features['GENDER'] = gender
        st.write(" ")

        #2. 나이대
        age_list = list(item_value_list['AGE_GRP'].dropna().unique())
        age = st.selectbox('귀하의 연령대를 선택해주세요', age_list)
        
        if age : 
            user_features['AGE_GRP'] = age
        st.write(" ")

        #3. 동반현황
        accompany_list = list(item_value_list['TRAVEL_STATUS_ACCOMPANY'].dropna().unique())
        accompany = st.selectbox('이번 여행의 동반현황은 무엇인가요?', accompany_list)
        
        if accompany :
            user_features['TRAVEL_STATUS_ACCOMPANY'] = accompany
        st.write(" ")

        #4. 자연 vs. 도시
        style1_list = list(item_value_list['TRAVEL_STYL_1'].dropna().unique())

        style1 = st.select_slider("자연과 도시 중 선호하는 방향을 정해주세요.", style1_list, value=('중립'))
        
        if style1 :
            user_features['TRAVEL_STYL_1'] = style1
        st.write(" ")

        #5. 새로운지역 vs. 익숙한 지역
        style3_list = list(item_value_list['TRAVEL_STYL_3'].dropna().unique())
        
        style3 = st.select_slider("여행지역으로 새로운지역과 익숙한지역 중 선호하는 방향을 정해주세요.", style3_list, value=('중립'))
        
        if style3 :
            user_features['TRAVEL_STYL_3'] = style3
        
        #6. 휴양 vs. 체험활동
        style5_list = list(item_value_list['TRAVEL_STYL_5'].dropna().unique())
        
        style5 = st.select_slider("휴양과 체험활동 중 선호하는 방향을 정해주세요.", style5_list, value=('중립'))
        
        if style5 :
            user_features['TRAVEL_STYL_5'] = style5
        st.write(" ")

        #7. 잘알려지지 않은 곳 vs. 알려진 방문지
        style6_list = list(item_value_list['TRAVEL_STYL_6'].dropna().unique())
        
        style6 = st.select_slider("잘 알려지지 않은 곳과 알려진 방문지 중 선호하는 방향을 정해주세요.", style6_list, value=('중립'))
        
        if style6 :
            user_features['TRAVEL_STYL_6'] = style6
        st.write(" ")

        #8. 여행 미션
        mission_list = list(item_value_list['modified mission value'].dropna().unique())
        mission_value_list = list(item_value_list['mission_value'].dropna().unique())
        st.write("이번 여행의 미션을 선택해주세요.")
        
        sns = st.checkbox(mission_list[0])
        if sns :
            user_features[mission_value_list[0]] = 1
        else :
            user_features[mission_value_list[0]] = 0
        
        wellness = st.checkbox(mission_list[1])
        if wellness :
            user_features[mission_value_list[1]] = 1
        else :
            user_features[mission_value_list[1]] = 0
        
        education = st.checkbox(mission_list[2])
        if education :
            user_features[mission_value_list[2]] = 1
        else :
            user_features[mission_value_list[2]] = 0
        
        drama = st.checkbox(mission_list[3])
        if drama :
            user_features[mission_value_list[3]] = 1
        else :
            user_features[mission_value_list[3]] = 0
        
        climb = st.checkbox(mission_list[4])
        if climb :
            user_features[mission_value_list[4]] = 1
        else :
            user_features[mission_value_list[4]] = 0

        cat = st.checkbox(mission_list[5])
        if cat :
            user_features[mission_value_list[5]] = 1
        else :
            user_features[mission_value_list[5]] = 0
        
        shopping = st.checkbox(mission_list[6])
        if shopping :
            user_features[mission_value_list[6]] = 1
        else :
            user_features[mission_value_list[6]] = 0
        
        city = st.checkbox(mission_list[7])
        if city :
            user_features[mission_value_list[7]] = 1
        else :
            user_features[mission_value_list[7]] = 0
        
        new_spot = st.checkbox(mission_list[8])
        if new_spot :
            user_features[mission_value_list[8]] = 1
        else :
            user_features[mission_value_list[8]] = 0
        
        sports = st.checkbox(mission_list[9])
        if sports :
            user_features[mission_value_list[9]] = 1
        else :
            user_features[mission_value_list[9]] = 0
        
        history = st.checkbox(mission_list[10])
        if history :
            user_features[mission_value_list[10]] = 1
        else :
            user_features[mission_value_list[10]] = 0
        
        spa = st.checkbox(mission_list[11])
        if spa :
            user_features[mission_value_list[11]] = 1
        else :
            user_features[mission_value_list[11]] = 0
        
        game = st.checkbox(mission_list[12])
        if game :
            user_features[mission_value_list[12]] = 1
        else :
            user_features[mission_value_list[12]] = 0
        
        influence = st.checkbox(mission_list[13])
        if influence :
            user_features[mission_value_list[13]] = 1
        else :
            user_features[mission_value_list[13]] = 0
        
        church = st.checkbox(mission_list[14])
        if church :
            user_features[mission_value_list[14]] = 1
        else :
            user_features[mission_value_list[14]] = 0
        
        art = st.checkbox(mission_list[15])
        if art :
            user_features[mission_value_list[15]] = 1
        else :
            user_features[mission_value_list[15]] = 0
        
        event = st.checkbox(mission_list[16])
        if event :
            user_features[mission_value_list[16]] = 1
        else :
            user_features[mission_value_list[16]] = 0
        
        environ = st.checkbox(mission_list[17])
        if environ :
            user_features[mission_value_list[17]] = 1
        else :
            user_features[mission_value_list[17]] = 0
        
        campping = st.checkbox(mission_list[18])
        if campping :
            user_features[mission_value_list[18]] = 1
        else :
            user_features[mission_value_list[18]] = 0
        
        tema = st.checkbox(mission_list[19])
        if tema :
            user_features[mission_value_list[19]] = 1
        else :
            user_features[mission_value_list[19]] = 0
        
        hokang = st.checkbox(mission_list[20])
        if hokang :
            user_features[mission_value_list[20]] = 1
        else :
            user_features[mission_value_list[20]] = 0
        
        st.write(" ")
        
        #9. 여행동기
        motive_list = list(item_value_list['modified motive value'].dropna().unique())
        motive_value_list = list(item_value_list['motive_value'].dropna().unique())
        st.write("이번 여행의 동기를 선택해주세요.")
        
        picture = st.checkbox(motive_list[0])
        if picture :
            user_features[motive_value_list[0]] = 1
        else :
            user_features[motive_value_list[0]] = 0
        
        new_activity = st.checkbox(motive_list[1])
        if new_activity :
            user_features[motive_value_list[1]] = 1
        else :
            user_features[motive_value_list[1]] = 0
        
        stay = st.checkbox(motive_list[2])
        if stay :
            user_features[motive_value_list[2]] = 1
        else :
            user_features[motive_value_list[2]] = 0
        
        love = st.checkbox(motive_list[3])
        if love :
            user_features[motive_value_list[3]] = 1
        else :
            user_features[motive_value_list[3]] = 0
        
        edu = st.checkbox(motive_list[4])
        if edu :
            user_features[motive_value_list[4]] = 1
        else :
            user_features[motive_value_list[4]] = 0
        
        exercise = st.checkbox(motive_list[5])
        if exercise :
            user_features[motive_value_list[5]] = 1
        else :
            user_features[motive_value_list[5]] = 0
        
        lazy = st.checkbox(motive_list[6])
        if lazy :
            user_features[motive_value_list[6]] = 1
        else :
            user_features[motive_value_list[6]] = 0
        
        self_esteem = st.checkbox(motive_list[7])
        if self_esteem :
            user_features[motive_value_list[7]] = 1
        else :
            user_features[motive_value_list[7]] = 0
        
        special = st.checkbox(motive_list[8])
        if special :
            user_features[motive_value_list[8]] = 1
        else :
            user_features[motive_value_list[8]] = 0
        
        anything = st.checkbox(motive_list[9])
        if anything :
            user_features[motive_value_list[9]] = 1
        else :
            user_features[motive_value_list[9]] = 0
        st.write(" ")
        st.write(" ")
        
        #Filter
        st.write("추천대상을 선택해주세요.")
        
        travel = st.radio("여행: 일반적으로 말하는 관광명소(ex. 테마파크, 자연관광지, 문화유적, 드라이브코스) 또는 숙박시설을 포함합니다.",
                        options= ["포함", "미포함"])
        if travel == "포함" : 
            filtering["travel"] = 1
        else :
            filtering['travel'] = 0
        
        transport = st.radio("교통,수송: 각종 항만, 방파제, 유람선, 등대 등을 포함합니다.",
                            options= ["포함", "미포함"])
        if transport == "포함" :
            filtering["transport"] = 1
        else :
            filtering['transport'] = 0
        
        sporting = st.radio("스포츠,레저", options= ["포함", "미포함"])
        if sporting == "포함" :
            filtering["sports"] = 1
        else :
            filtering['sports'] = 0
        
        service = st.radio("서비스", options= ["포함", "미포함"])
        if service == "포함" :
            filtering['service'] = 1
        else :
            filtering['service'] = 0
        
        market = st.radio("시장", options= ["포함", "미포함"])
        if market == "포함" :
            filtering['market'] = 1
        else :
            filtering['market'] = 0
        
        cafe = st.radio("카페", options= ["포함", "미포함"])
        if cafe == "포함" :
            filtering['cafe'] = 1
        else :
            filtering['cafe'] = 0
        
        arting = st.radio("미술, 공연",options= ["포함", "미포함"])
        if arting == "포함" :
            filtering['art'] = 1
        else :
            filtering['art'] = 0
            
        submit_button = st.form_submit_button(label = '추천요청')
        
        if submit_button :    
            request_body = {"new_user_data" : user_features, "filter_item" : filtering}
        
        if request_body :
            st.write(request_body)
        
        if request_body :
            url = 'https://o5as6un2knzd5sl6ldr2gnn3ba0mbgdy.lambda-url.ap-northeast-2.on.aws/recommend/recommendation'
            response = requests.post(url, json=request_body)
            if response.status_code == 200 :
                st.write("성공적으로 추천아이템을 받아왔어요.")
                recommended_item = response.json()
            else :
                st.write(response.status_code)
                st.write(response.text)


with tab2 : #여행
    if response :
        if response.status_code == 200 :
            if 'travel' in recommended_item.keys() :
                travel_item = recommended_item['travel']
                travel_item_df = pd.DataFrame(travel_item)
                st.write(travel_item_df)
            else :
                st.write("여행은 추천대상이 아니에요.")

with tab3 : #스포츠레저
    if response :
        if response.status_code == 200 :
            if 'sports' in recommended_item.keys() :
                sports_item = recommended_item['sports']
                sports_item_df = pd.DataFrame(sports_item)
                st.write(sports_item_df)
            else :
                st.write("스포츠는 추천대상이 아니에요.")

with tab4 : #카페페
    if response :
        if response.status_code == 200 :
            if 'café' in recommended_item.keys() :
                cafe_item = recommended_item['café']
                cafe_item_df = pd.DataFrame(cafe_item)
                st.write(cafe_item_df)
            else :
                st.write("카페는 추천대상이 아니에요.")
                
with tab5 : #서비스
    if response :
        if response.status_code == 200 :
            if 'service' in recommended_item.keys() :
                service_item = recommended_item['service']
                service_item_df = pd.DataFrame(service_item)
                st.write(service_item_df)
            else :
                st.write("서비스는 추천대상이 아니에요.")

with tab6 : #아트
    if response :
        if response.status_code == 200 :
            if 'art' in recommended_item.keys() :
                art_item = recommended_item['art']
                art_item_df = pd.DataFrame(art_item)
                st.write(art_item_df)
            else :
                st.write("아트는 추천대상이 아니에요.")

with tab7 : #시장
    if response :
        if response.status_code == 200 :
            if 'market' in recommended_item.keys() :
                market_item = recommended_item['market']
                market_item_df = pd.DataFrame(market_item)
                st.write(market_item_df)
            else :
                st.write("시장은 추천대상이 아니에요.")

with tab8 : #교통, 수송
    if response :
        if response.status_code == 200 :
            if 'transport' in recommended_item.keys() :
                transport_item = recommended_item['transport']
                transport_item_df = pd.DataFrame(transport_item)
                st.write(transport_item_df)
            else :
                st.write("교통은 추천대상이 아니에요.")




































































































































