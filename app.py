import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="InsightCommerce", layout="centered")

# --- NAVIGATION ---
page = st.sidebar.selectbox("Go to:", ["🏠 Home", "📁 Data Upload & Analysis", "🔮 Predictor"])

# --- 1. HOME ---
if page == "🏠 Home":
    st.title("E-Commerce Analytics")
    st.write("Upload your customer data to identify churn risk and purchase patterns.")
    st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80")

# --- 2. DATA UPLOAD & ANALYSIS ---
elif page == "📁 Data Upload & Analysis":
    st.header("Upload Customer CSV")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        
        st.subheader("Data Preview")
        st.write(df.head(5)) # Shows first 5 rows
        
        # Simple Logic to find Columns for Charting
        columns = df.columns.tolist()
        st.subheader("Visual Analysis")
        x_axis = st.selectbox("Select X-axis (e.g., Category or Date)", columns)
        y_axis = st.selectbox("Select Y-axis (e.g., Sales or Quantity)", columns)
        
        fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Please upload a CSV file to see the analysis.")

# --- 3. PREDICTOR ---
elif page == "🔮 Predictor":
    st.header("Churn Risk Calculator")
    # (Same predictor code as before or enhanced with your ML model)
    days = st.slider("Days since last purchase", 0, 365, 30)
    if st.button("Analyze Risk"):
        if days > 90:
            st.error("🚨 HIGH RISK")
        else:
            st.success("✅ LOW RISK")
