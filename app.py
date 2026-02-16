import streamlit as st
from model import predict_result, accuracy

st.title("📈 Campus Performance Intelligence System " )

st.write("Enter student details below:")

#input fields for the user to enter student details
hours = st.slider("Study Hours per Day", 0, 12, 4)
attendance = st.slider("Attendance Percentage", 0, 100, 75)
previous_marks = st.slider("Previous Marks (%)", 0, 100, 60)
assignment_score = st.slider("Assignment Score (%)", 0, 100, 60)

if st.button("Predict Result"):

    result, probability = predict_result(
        hours, attendance, previous_marks, assignment_score
    )

    if result == 0:
        st.error("🚫 Detained due to low attendance.")
    elif result == 1:
        st.warning("❌ Fail. Improve your study strategy, attendance, and assignment scores. You can do better!")
    else:
        st.success("✅ Pass! Keep up the good work.")

    st.write("### Prediction Probabilities:")
    st.write("Detained:", round(probability[0][0]*100, 2), "%")
    st.write("Fail:", round(probability[0][1]*100, 2), "%")
    st.write("Pass:", round(probability[0][2]*100, 2), "%")

st.write("---")
st.write("📊 Model Accuracy:", round(accuracy*100, 2), "%")
st.sidebar.header("About This Project")
st.sidebar.write(
    "Hello and welcome to the Campus Performance Intelligence System!"
    "This system predicts student academic outcomes by taking attendance , study hours and marks as input and analyzing them "
    "using Machine Learning based on performance indicators."
    "The goa is very simple, I want to help students identifying risks and improving their academic performance through data-driven insights."
)
st.write("### Performance Analysis")

if attendance < 70:
    st.write("Low attendance is major issue, becuase of low attendance you can't give exams and you can't get good marks.")
elif hours < 3:
    st.write("Low study hours are affecting performance.")
elif previous_marks < 50:
    st.write("Weak academic foundation detected.")
else:
    st.write("Overall academic indicators are strong.")

