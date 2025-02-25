import streamlit as st

def run():
    st.title("❓ 자주 묻는 질문 FAQ")
    st.header("브랜드 선택")

    brands = ["현대", "기아"]
    categories = ["전체","차량구매", "차량옵션", "차량정비", "할부", "보증 및 A/S", "할인 및 프로모션", "전기차"]

    selected_brand = st.selectbox("브랜드를 선택하세요:", brands)
    selected_category = st.radio("카테고리를 선택하세요:", categories, horizontal=True)


#FAQ data 저장 
    faq_data = {
        "현대" : {
            "차량구매" : [("현대-차량구매-질문","현대-차량구매-답변")],
            "차량옵션" : [("현대-차량옵션-질문","현대-차량옵션-답변")],
            "차량정비" : [("현대-차량정비질문","현대-차량정비-답변")],
            "할부" : [("현대-할부-질문","현대-할부-답변")],
            "보증 및 A/S" : [("현대-보증 및 A/S-질문","현대-보증 및 A/S-답변")],
            "할인 및 프로모션" : [("현대-할인 및 프로모션-질문","현대-할인 및 프로모션-답변")],
            "전기차" : [("현대-전기차-질문","현대-전기차-답변")]
        },
        "기아" : {
            "차량구매" : [("기아-차량구매-질문","기아-차량구매-답변")],
            "차량옵션" : [("기아-차량옵션-질문","기아-차량옵션-답변")],
            "차량정비" : [("기아-차량정비질문","기아-차량정비-답변")],
            "할부" : [("기아-할부-질문","기아-할부-답변")],
            "보증 및 A/S" : [("기아-보증 및 A/S-질문","기아-보증 및 A/S-답변")],
            "할인 및 프로모션" : [("기아-할인 및 프로모션-질문","기아-할인 및 프로모션-답변")],
            "전기차" : [("기아-전기차-질문","기아-전기차-답변")]
        }
    }
    if selected_category == "전체":
        for category, faqs in faq_data[selected_brand].items():
            for question, answer in faqs:
                with st.expander(question):
                    st.write(answer)
    else:
        # 현대&기아&카테고리
        if selected_category in faq_data[selected_brand]:
            for question, answer in faq_data[selected_brand][selected_category]:
                with st.expander(question):  
                    st.write(answer)
        else:
            st.write("📌 해당 브랜드의 FAQ가 없습니다.")