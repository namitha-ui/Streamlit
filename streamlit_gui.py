import streamlit as st
import requests

# Set page configuration
st.set_page_config(
    page_title="Model Deployment Interface",
    page_icon="🚀",
    layout="wide",
)

# Use relative path for the logo
logo_path = "logo.png"  # Ensure this file is in the same directory as your app script
st.image(logo_path, use_container_width=False, width=150)

# Sidebar Menu
st.sidebar.title("Menu")
st.sidebar.markdown("Configuration")
st.sidebar.markdown("Playground")

st.sidebar.subheader("MANAGEMENT")
menu_option = st.sidebar.radio(
    "",
    [
        "Service Deployment",
        "Service Information",
        "Service Evaluation",
        "Service Monitor"
    ]
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)

# Main Content
if menu_option == "Service Deployment":
    st.markdown("<h2 style='font-size: 24px;'>Model Deployment Interface</h2>", unsafe_allow_html=True)
    st.header("You can deploy models here")
    
    model_type = st.selectbox(
        "Select Type:",
        ["Chatbot", "RAG (Retrieval-Augmented Generation)"]
    )

    model = st.selectbox(
        "Select Model:",
        ["Databricks Meta Bane 3-70-Instruction", "Other Models"]
    )

    retriever = st.selectbox(
        "Select Retriever:",
        ["Retriever Simple", "Vector Search Endpoint 1"]
    )

    index = st.selectbox(
        "Select Index:",
        [
            "Databricks Tag Sync Index - 167629883cd9dce > 1504cdcd147482",
            "Other Indexes"
        ]
    )

    index_endpoint = st.selectbox(
        "Select Index End Points:",
        [
            "Endpoint 1 - http://example.com/endpoint1",
            "Endpoint 2 - http://example.com/endpoint2",
            "Other Endpoints"
        ]
    )

    thematic_prompt = st.text_area(
        "Thematic Prompt:",
        placeholder="Enhance your prompt here if any..."
    )

    if st.button("Deploy"):
        payload = {
            "model_type": model_type,
            "model": model,
            "retriever": retriever,
            "index": index,
            "index_endpoint": index_endpoint,
            "prompt": thematic_prompt
        }
        
        API_ENDPOINT = "https://your-api-endpoint.com/deploy"

        try:
            response = requests.post(API_ENDPOINT, json=payload)

            if response.status_code == 200:
                st.success("Deployment Successful!")
                st.write(f"Response: {response.json()}")
            else:
                st.error(f"Deployment Failed! Status Code: {response.status_code}")
                st.write(f"Error Details: {response.text}")

        except Exception as e:
            st.error(f"An error occurred: {e}")

elif menu_option == "Service Information":
    st.title("Service Information")
    st.write("This section provides details about deployed services.")

elif menu_option == "Service Evaluation":
    st.title("Service Evaluation")
    st.write("This section helps you evaluate your services.")

elif menu_option == "Service Monitor":
    st.title("Service Monitor")
    st.write("This section provides monitoring tools for your services.")
