import streamlit as st

st.set_page_config(page_title="คำนวณค่าดัชนีมวลกาย BMI", page_icon="💪")

st.title("💪 คำนวณค่าดัชนีมวลกาย BMI")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=1.0, max_value=300.0, value=55.0, step=0.5)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", min_value=50.0, max_value=250.0, value=158.0, step=0.5)

if st.button("คำนวณค่า BMI 🎯"):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    st.divider()
    st.subheader(f"ค่า BMI ของคุณคือ: {bmi:.2f}")

    if bmi < 18.5:
        st.warning("⚠️ คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
    elif 18.5 <= bmi < 23.0:
        st.success("🎉 คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
    elif 23.0 <= bmi < 25.0:
        st.info("💡 คุณเริ่มมีน้ำหนักเกินเกณฑ์ (ท้วม)")
    else:
        st.error("🚨 คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")

    st.divider()
    st.write("นายนันท์มนัส แก้วทอง เลขที่ 8 ม.4/5")
