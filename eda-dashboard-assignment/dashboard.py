import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Title
st.title("📊 Simple Data Dashboard")

# Fetch data
url = "https://jsonplaceholder.typicode.com/posts"
data = requests.get(url).json()

# Convert to DataFrame
df = pd.DataFrame(data)

# Show raw data
st.subheader("Raw Data")
st.write(df)

# -------------------------------
# STEP 4: Data Cleaning
# -------------------------------

# Rename column
df.rename(columns={"userId": "user_id"}, inplace=True)

# Drop null values
df.dropna(inplace=True)

# -------------------------------
# STEP 5: Exploratory Analysis
# -------------------------------

# Count posts per user
posts_per_user = df.groupby("user_id").size()

st.subheader("Posts per User")
st.write(posts_per_user)

# -------------------------------
# STEP 6: Feature Engineering
# -------------------------------

# Add post length column
df["post_length"] = df["body"].apply(len)

st.subheader("Post Length Data")
st.write(df[["user_id", "post_length"]])

# -------------------------------
# STEP 7: Visualizations
# -------------------------------

# Bar Chart
st.subheader("Bar Chart - Posts per User")
st.bar_chart(posts_per_user)

# Histogram
st.subheader("Histogram - Post Length")

fig, ax = plt.subplots()
ax.hist(df["post_length"], bins=20)
st.pyplot(fig)