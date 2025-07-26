# dinner_health_app.py
import streamlit as st
import openai
import os

# 使用新版 OpenAI 客户端
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🍱 晚餐健康评估小助手")

# 输入
dinner = st.text_area("请输入你今天的晚餐内容：", height=150, placeholder="如：一碗白米饭 + 一块红烧肉 + 一碗青菜")

# 按钮
if st.button("评估我的晚餐"):
    if not dinner.strip():
        st.warning("请输入晚餐内容")
    else:
        with st.spinner("GPT 正在分析中..."):
            prompt = f"""
我今天晚餐吃了：{dinner}。
请你根据常见食物热量，帮我估算这顿饭的总热量（单位：大卡 kcal）。
再根据营养搭配原则，判断这顿饭是否健康，并给出简要建议。
"""
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "你是一个专业的营养师助手。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            result = response.choices[0].message.content
            st.success("分析结果：")
            st.markdown(result)