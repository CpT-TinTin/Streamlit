import streamlit as st

st.title("User Feedback Form")

with st.form("feedback_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    feedback = st.text_area("Your feedback")
    rating = st.slider("Rate your experience", 1, 5, 3)
    subscribe = st.checkbox("Subscribe to newsletter")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Thank you for your feedback!")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Age:** {age}")
    st.write(f"**Feedback:** {feedback}")
    st.write(f"**Rating:** {rating} / 5")
    st.write(f"**Subscribed to newsletter:** {'Yes' if subscribe else 'No'}")