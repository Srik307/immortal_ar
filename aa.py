import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('medicines.csv')
    return data

# Extract unique symptoms
@st.cache
def get_unique_symptoms(data):
    symptoms = data['Symptom'].dropna().unique()
    return sorted(symptoms)

# Streamlit app
def main():
    st.title("Medicine Finder Based on Symptoms")
    
    # Load data
    data = load_data()
    
    # Get unique symptoms
    symptoms = get_unique_symptoms(data)
    
    # User input for symptom
    user_input = st.text_input("Enter a symptom:", "")
    
    # Filter symptoms based on user input
    filtered_symptoms = sorted([symptom for symptom in symptoms if user_input.lower() in symptom.lower()])
    
    # Dropdown for symptoms
    selected_symptom = st.selectbox("Select a symptom:", options=filtered_symptoms)
    
    if selected_symptom:
        # Filter the dataset based on the selected symptom
        filtered_data = data[data['Symptom'].str.contains(selected_symptom, case=False, na=False)]
        
        if not filtered_data.empty:
            st.write("Medicines matching the symptom:")
            st.dataframe(filtered_data)
        else:
            st.write("No medicines found for the selected symptom.")
    
if __name__ == '__main__':
    main()