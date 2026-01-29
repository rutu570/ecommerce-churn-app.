import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="ChurnAnalytica", 
    page_icon="🛍️",
    layout="centered" # Best for mobile screens
)

# --- NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to:", ["🏠 Home", "📊 Dashboard", "🔮 Churn Predictor", "📑 Project Report"])

# --- 1. HOME PAGE ---
if page == "🏠 Home":
    st.title("E-Commerce Purchase Prediction")
    st.image("https://images.unsplash.com/photo-1556742044-3c52d6e88c62?auto=format&fit=crop&w=800&q=80")
    st.markdown("""
    ### Welcome!
    This project uses **Machine Learning** to help e-commerce businesses:
    * **Predict** if a customer will buy again.
    * **Detect** customers likely to stop using the service (Churn).
    * **Analyze** purchase patterns to improve strategy.
    
    👈 **Use the sidebar menu to explore the data!**
    """)

# --- 2. DASHBOARD PAGE ---
elif page == "📊 Dashboard":
    st.header("Exploratory Data Analysis")
    
    # Mock data for visualization
    chart_data = pd.DataFrame({
        'Status': ['Loyal', 'At Risk', 'Lost'],
        'Customers': [450, 180, 75]
    })
    
    # Interactive Bar Chart
    fig = px.bar(chart_data, x='Status', y='Customers', color='Status', 
                 title="Current Customer Segmentation")
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **Insight:** 180 customers are 'At Risk'. Targeting them now could prevent revenue loss.")

# --- 3. PREDICTOR PAGE ---
elif page == "🔮 Churn Predictor":
    st.header("Predict Churn Risk")
    st.write("Enter customer details to see the prediction.")

    with st.container():
        recency = st.number_input("Days since last purchase", min_value=0, value=30)
        frequency = st.number_input("Total number of orders", min_value=1, value=5)
        monetary = st.number_input("Total spent ($)", min_value=0, value=100)
        
        if st.button("Run Prediction"):
            # Simple logic for demo (Will be replaced by ML Model later)
            if recency > 90:
                st.error("Result: **HIGH CHURN RISK** 🚨")
                st.write("Recommendation: Send a discount email immediately.")
            else:
                st.success("Result: **LOYAL CUSTOMER** ✅")
                st.write("Recommendation: Keep engaging with new product arrivals.")

# --- 4. REPORT PAGE ---
elif page == "📑 Project Report":
    st.header("Project Methodology")
    st.markdown("""
    ### 1. Problem Statement
    In e-commerce, it is 5x cheaper to retain an existing customer than to find a new one. This project predicts churn to save costs.
    
    ### 2. Dataset
    Using the **Online Retail Dataset** (Kaggle), focusing on:
    * **Recency:** Time since last order.
    * **Frequency:** Total number of orders.
    * **Monetary:** Total revenue per customer.
    
    ### 3. Tools Used
    * **Python:** Data processing
    * **Streamlit:** Web interface
    * **Plotly:** Interactive charts
    """)
