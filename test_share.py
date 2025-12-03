import requests
import streamlit as st

# Google Drive '다운로드 URL'
url = "https://drive.google.com/uc?export=download&id=1FfVRXnEIwcjssh-56DJWPJNZd4mfMkQt"


site_url = requests.get(url).text.strip()

enableXsrfProtection = False
enableCORS = False

st.set_page_config(
    layout="wide"
)
st.markdown(f"[🔗 사이트 바로가기]({site_url})")
st.warning('미리보기가 아닌 사이트 링크에서 해석을 진행해 주세요!', icon="🚨")
st.components.v1.iframe(site_url,height=2000,scrolling=True)



#response = requests.get(url)
#text = response.text
#st.write(text)






