import requests
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Contact App Project",
    page_icon="📞"
)

# App title
st.title("📞 Contact App")

st.write("Click the button below to fetch user data.")

# Button
if st.button("Fetch Contacts"):

    # API request
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:
        users = response.json()

        users_data = []

        for user in users:
            users_data.append({
                "Name": user["name"],
                "Username": user["username"],
                "Email": user["email"],
                "Phone": user["phone"],
                "Website": user["website"]
            })

        # Create DataFrame
        df = pd.DataFrame(users_data)

        # Display table
        st.success("Contacts fetched successfully!")
        st.dataframe(df)

    else:
        st.error("Failed to fetch data from API.")