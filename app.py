import streamlit as st
from deep_translator import GoogleTranslator

# 페이지 설정
st.set_page_config(page_title="다국어 번역기", page_icon="🌐", layout="centered")

st.title("🌐 다국어 동시 번역기")
st.markdown("한국어를 입력하면 **영어, 일본어, 중국어(간체), 프랑스어**로 동시에 번역됩니다.")

# 텍스트 입력 창
text_to_translate = st.text_area("번역할 한국어를 입력하세요:", height=150, placeholder="여기에 텍스트를 입력해 주세요...")

# 번역 버튼
if st.button("번역하기", type="primary"):
    if text_to_translate.strip() == "":
        st.warning("번역할 텍스트를 먼저 입력해주세요!")
    else:
        with st.spinner("번역 중입니다. 잠시만 기다려주세요..."):
            try:
                # 번역기 인스턴스 생성 및 번역 수행
                # source='ko' (한국어)에서 각각의 타겟 언어로 번역
                en_text = GoogleTranslator(source='ko', target='en').translate(text_to_translate)
                ja_text = GoogleTranslator(source='ko', target='ja').translate(text_to_translate)
                zh_text = GoogleTranslator(source='ko', target='zh-CN').translate(text_to_translate)
                fr_text = GoogleTranslator(source='ko', target='fr').translate(text_to_translate)

                st.success("번역이 완료되었습니다!")

                # 화면을 2단으로 나누어 깔끔하게 배치
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("🇺🇸 영어 (English)")
                    st.info(en_text)
                    
                    st.subheader("🇨🇳 중국어 (Chinese)")
                    st.info(zh_text)
                    
                with col2:
                    st.subheader("🇯🇵 일본어 (Japanese)")
                    st.info(ja_text)
                    
                    st.subheader("🇫🇷 프랑스어 (French)")
                    st.info(fr_text)
                    
            except Exception as e:
                st.error(f"오류가 발생했습니다. 다시 시도해주세요. (에러 내용: {e})")
