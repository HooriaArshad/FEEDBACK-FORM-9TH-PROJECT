import streamlit as st
import pandas as pd


if 'feedback_list' not in st.session_state:
    st.session_state.feedback_list = []


st.title("📝 Customer Feedback App")


st.sidebar.header("🧑 Enter Your Feedback")
name = st.sidebar.text_input("Your Name")
email = st.sidebar.text_input("Email Address")
rating = st.sidebar.slider("Rate Us", 1, 5, 3)
feedback = st.sidebar.text_area("Your Feedback")

if st.sidebar.button("Submit"):
    if name and email and feedback:
        st.session_state.feedback_list.append({
            "Name": name,
            "Email": email,
            "Rating": rating,
            "Feedback": feedback
        })
        st.sidebar.success("Thanks for your feedback!")
    else:
        st.sidebar.warning("Please fill all fields.")

st.write("## 💬 Feedback Received")

if st.session_state.feedback_list:
    df = pd.DataFrame(st.session_state.feedback_list)
    st.dataframe(df)

    st.write("### 📊 Average Rating")
    avg_rating = df['Rating'].mean()
    st.metric("Average User Rating", f"{avg_rating:.2f} ⭐")
else:
    st.info("No feedback yet. Submit yours using the form on the left.")

