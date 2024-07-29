import streamlit as st
from utils import generate_script
import os

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

st.title("视频脚本生成器")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAi的API密钥：",type="password")
    st.markdown("[获取openAI API密钥](https://platform.openai.com/account/api-keys)")
    base_url = st.text_input("请输入base_url")

subject = st.text_input("请输入视频的主题")
video_length = st.number_input("请输入视频的大致上时长(分钟)",min_value=0.1,step=0.1)
creativity = st.slider("请输入视频脚本的创造力(数字小说明更严谨,数字大说明更加多样性)",min_value=0.0,max_value=1.0,value=0.2,step=0.1)

submit = st.button("生成脚本")
if submit and not openai_api_key:
    st.info("请输入你的Open AI API密钥")
    st.stop()
if submit and not subject:
    st.info("请输入视频的标题")
    st.stop()
if submit and not video_length >=0.1:
    st.info("视频的长度需要大于等于0.1")
    st.stop()
if submit:
    with st.spinner("Ai正在思考中,请稍后..."):
        search_result,title,scrip = generate_script(subject,video_length,creativity,openai_api_key,base_url)
    st.success("视频脚本已生成!")
    st.subheader("标题:")
    st.write(title)
    st.subheader("视频脚本")
    st.write(scrip)
    with st.expander("维基百科搜索结果"):
        st.info(search_result)

#https://api.chatanywhere.tech/v1
