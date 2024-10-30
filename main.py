print("Hello World!")
import streamlit as st
st.write("hello World!!")
st.write("내 이름은 이동건")
st.write("Nice to meet you!")

이동건 = st.button("이동건")
학교 = st.button("학교")

if 이동건:
    st.write("어서오세요")
else:
    st.write("반가워요")


check = st.checkbox("공부했나요")

agree = st.checkbox("동의.")

if agree:
    st.write("동의합니다!!")

st.title("😍Ph.D.")
st.header("✌Curriculum studies")
st.subheader("at the University of Virginia")
st.markdown("우리 함께 **교육학**을 :red[배워]봅시다!!!")
st.write("우리 함께 **Curricululm studies**을 :blue[배워]봅시다!!!")

짜장면 = st.checkbox("짜장면(5000원)")
짬뽕 = st.checkbox("짬뽕(7000원)")
탕수육 = st.checkbox("탕수육(15000원)")
가격 = 0
if 짜장면:
    가격 +=5000
if 짬뽕:
    가격 +=7000
if 탕수육:
    가격 +=15000
st.subheader(f"선택한 음식의 가격은 {가격}원입니다.")

result = st.radio("Streamlit으로 웹 :rainbow[어플리케이션]을 개발할 수 있다?", ["O", "X"])

if result == "O":
    st.success("정답!!")
else:
    st.error("오답!!")

기분 = st.selectbox("오늘 나의 기분은?",
                    ["Very good!",
                     "Good :)",
                     "SO SO", 
                     "Not bad.",
                     "Bad day!"])
st.subheader(f"I'm {기분}.")

전공 = st.text_input("당신의 전공 과목을 입력하세요.")

st.write(f"{전공} 학생이시군요! 대단합니다.")

