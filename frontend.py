import streamlit as st
import requests 
import config


def compute_probability(payload):

    r = requests.post(url="http://127.0.0.1:8080/compute_probability", json=payload)
    return r.json()

st.set_page_config(page_title="A web Page",layout="centered")
st.title("Determine Placement Probability")
st.caption("Frontend:Streamlit | Backend: REST API")
st.subheader(body="Please enter  your details below", text_alignment="center")


iq = st.number_input(label="Enter Your Iq here",min_value=40,max_value=160,step=1)
previous_semester_result = st.number_input(label="Enter Your previous semester result here",min_value=0.0,max_value=10.0,step=0.01)
cgpa = st.number_input(label="Enter Your cgpa here",min_value=0.0,max_value=10.0,step=0.01)
communication_skills = st.number_input(label="Enter Your communication skills Rating  here",min_value=0,max_value=10,step=1)
project_completed = st.number_input(label="Enter number of project completed by you",min_value=0,max_value=10,step=1)

payload = {"iq":iq,"previous_semester_result":previous_semester_result,"cgpa":cgpa,"communication_skills":communication_skills,"projects_completed":project_completed}


text_area_placeholder = st.empty()
if st.button("Calculate Probability"):
    response = compute_probability(payload)
    print(response)
    text_area_placeholder.text_area(label="Your Placement Probability",value=response["result"])


