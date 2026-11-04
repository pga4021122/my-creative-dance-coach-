# Role-based Creative Chatbot (OpenAI version)
# Step 3 starting point: one question, one answer, with a creative role.

import streamlit as st
from openai import OpenAI

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(page_title="💃 Creative Dance Coach", layout="wide")
st.title("💃 Creative Dance Coach")
st.write("AI 창작무용 코치에게 안무와 움직임에 대해 질문해 보세요!")

# -----------------------
# Sidebar: API Key + Role Selection
# -----------------------
st.sidebar.header("🔑 API & Role Settings")

api_key = st.sidebar.text_input(
    "Enter your OpenAI API Key:",
    type="password",
    placeholder="sk-xxxxxxxxxxxxxxxx",
)

# Each role is a "system prompt": it tells the AI who it is and how to think.
roles = {
    "🎥 Video Director":
    "You are a professional film director. Always analyze ideas in terms of visual storytelling — use camera movement, lighting, framing, and emotional tone to explain your thoughts. Describe concepts as if you are planning a film scene.",

    "💃 Creative Dance Coach":
    "You are a professional creative dance and choreography coach. Help students develop original choreography through movement exploration, emotion, rhythm, space, dynamics, and storytelling. Provide practical step-by-step movement ideas and choreography structures. Encourage creativity and offer examples inspired by Korean dance when appropriate. Always respond in Korean with clear, supportive, and specific advice.",

    "👗 Fashion Stylist":
    "You are a fashion stylist. Explain every idea using the language of color, texture, and silhouette. Think visually — how something would appear, feel, and harmonize.",

    "🎭 Acting Coach":
    "You are an acting coach. Speak as if guiding an actor through emotion and timing. Use scene examples, emotional layering, and body language descriptions.",

    "🎨 Art Curator":
    "You are an art curator. Reflect in an analytical yet poetic tone. Compare artistic elements, styles, and their emotional effects as if curating an exhibition.",
}

role_name = st.sidebar.selectbox("전문가 역할 선택:", list(roles.keys()), index=1)
role_description = roles[role_name]
st.sidebar.info(role_description)

# -----------------------
# User Input Area
# -----------------------
user_input = st.text_area(
    "💬 창작무용에 관한 질문이나 아이디어를 입력하세요:",
    height=100,
    placeholder="예: 슬픔에서 희망으로 변화하는 감정을 춤으로 어떻게 표현할 수 있을까?",
)

# -----------------------
# Generate Response
# -----------------------
if st.button("AI 코치에게 질문하기"):
    if not api_key:
        st.warning("⚠️ 왼쪽 메뉴에 OpenAI API 키를 입력하세요.")
    elif not user_input:
        st.warning("질문을 먼저 입력하세요!")
    else:
        try:
            client = OpenAI(api_key=api_key)
            with st.spinner("AI 코치가 답변을 준비하고 있어요..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": role_description},
                        {"role": "user", "content": user_input},
                    ],
                )
                answer = response.choices[0].message.content
                st.success(f"{role_name}의 답변")
                st.write(answer)
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.caption("Built for 'Art & Advanced Big Data' • Prof. Jahwan Koo (SKKU)")
