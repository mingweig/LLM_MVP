import streamlit as st
import json
import openai
import logging
import copy
from openai import OpenAI


patient_base = {}
def add_patient(patient_data):
  if patient_data['patient_id'] not in patient_base:
    patient_base[patient_data['patient_id']] = patient_data
    print(f"Add {patient_data['patient_id']} into the patient database.")
    return "Added Successfully!"
  else:
    return "Patient ID is already esist! Pelease double check your data!"

file_path = 'data.json'
file_path_2 = 'data_2.json'
file_path_3 = 'data_3.json'

with open(file_path, 'r') as file:
    patient_data_1 = json.load(file)
    add_patient(patient_data_1)
with open(file_path_2, 'r') as file:
    patient_data_2 = json.load(file)
    add_patient(patient_data_2)
with open(file_path_3, 'r') as file:
    patient_data_3 = json.load(file)
    add_patient(patient_data_3)



credentials_path = 'credentials.json'

with open(credentials_path, 'r') as file:
    credentials = json.load(file)

openai_api_key = credentials['openai_api_key']

# Use the API key as needed, for example, to configure OpenAI's API client
openai.api_key = openai_api_key
client = OpenAI(api_key=openai_api_key)


def safety_check(patient_data, additional_prompts=''):
    """
    Generates safety check result using OpenAI's GPT-3.5.

    Parameters:
    - patient_data (str): The patient data to generate the summary from.
    - additional_prompts (str): Try prompt engineering here.

    Returns:
    - str: The generated patient summary.
    """

    # Initialize the OpenAI client with your API key
    client = OpenAI(api_key=openai_api_key)

    # Create the chat completion request with the patient data
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""
                              You are a doctor writing a discharge letter for a patient. Use patient data from context only. Decide if the patient is feasible to discharge or not.
                              {additional_prompts}
                              Data: {patient_data}
                Output should strictly be a boolean variable: True/False

                """,
            }
        ],
        #model="gpt-4-turbo-preview",
        model="gpt-3.5-turbo",
    )

    # Return the content of the generated message
    return chat_completion.choices[0].message.content

# Set up basic configuration for logging
log_filename = './app_logs.log'
logging.basicConfig(filename=log_filename, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

def generate_patient_summary(patient_data, additional_prompts=''):
    """
    Generates a patient summary using OpenAI's GPT-3.5.

    Parameters:
    - patient_data (str): The patient data to generate the summary from.
    - additional_prompts (str): Try prompt engineering here.

    Returns:
    - str: The generated patient summary.
    """
    try:
      # Initialize the OpenAI client with your API key
      client = OpenAI(api_key=openai_api_key)

      # Create the chat completion request with the patient data
      chat_completion = client.chat.completions.create(
          messages=[
              {
                  "role": "user",
                  "content": f"""
                                You are a doctor writing a discharge letter for a patient. Use patient data from context only. If this patient is not safe for discharge, do not recommend discharge. Minimize hallucinations.
                                {additional_prompts}
                                Data: {patient_data}

                  """,
              }
          ],
          #model="gpt-4-turbo-preview",
          model="gpt-3.5-turbo",
      )

      # Return the content of the generated message
      # Log successful generation
      logging.info("Successfully generated patient summary.")
      return chat_completion.choices[0].message.content
    except Exception as e:
        # Log the exception
      logging.error("Error in generating patient summary", exc_info=True)
      return f"An error occurred: {str(e)}"

def privacy_handler(patient_data):
  patient = copy.deepcopy(patient_data)
  if 'name' in patient['patient_demographics']:
    p_name =  patient['patient_demographics']['name']
    del patient['patient_demographics']['name']
  else: p_name = None
  if 'patient_id' in patient:
    p_id = patient['patient_id']
    del patient['patient_id']
  else: p_id = None
  return p_name, p_id, patient

# Streamlit UI components
st.title("🧭 Healthcare Compass: Patient Journey Facilitator")
disclaimer = (
    "⚠️ This discharge summary is generated with the assistance of AI. "
    "Please review carefully before sharing with patients to ensure accuracy "
    "and completeness. Always verify with medical records and professional judgement."
)

st.warning(disclaimer)

# Input fields for patient data
patient_id = st.text_input("Patient ID", "Enter patient ID")
Staff_name = st.text_input("Staff Name", "Enter Staff Name")
Title      = st.text_input("Staff Title", "Enter Staff Title")


# Button to generate the summary
if st.button("Generate Discharge Summary"):
    if patient_id in patient_base:
        p_name, p_id, patient_data = privacy_handler(patient_base[patient_id])
        if safety_check(patient_data) == "True":
            summary = f"Patient Name: {p_name}\n\nPatient_ID: {p_id}\n\n" + generate_patient_summary(patient_data, additional_prompts=f"Your name is {Staff_name}, Title: {Title}. Do not require patient name / id / or DoB, starting from Dear patient,")
            st.text_area("Generated Summary", value=summary, height=300)

            filename = f"/content/LLM_MVP/Patient_summary_{p_id}.txt"
            try:
                with open(filename, 'w') as file:
                    file.write(summary)
                st.success("✅ Summary saved successfully!")
            except Exception as e:
                st.error(f"❗️ Fail to save the summary: {e}")
        else:
            st.error(f"❗️ Patient {p_name} is not safe for discharge.")
    else:
        st.error("❗️ Patient ID not found.")
        # Add code here to save the edited summary, such as writing to a file or database
