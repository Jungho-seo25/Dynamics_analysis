import requests
import streamlit as st

# Google Drive '다운로드 URL'
url = "https://drive.google.com/uc?export=download&id=1FfVRXnEIwcjssh-56DJWPJNZd4mfMkQt"

site_url = requests.get(url).text.strip()

st.set_page_config(
    layout="wide"
)
st.markdown(f"[🔗 사이트 바로가기]({site_url})")
st.components.v1.iframe(site_url, width=1000 ,height=1200, scrolling=True)



#response = requests.get(url)
#text = response.text
#st.write(text)
