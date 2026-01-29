import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE SETUP ---
st.set_page_config(page_title="CommerceIntel Pro", layout="wide")

# --- CUSTOM INTERFACE STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; border: 1px solid #e0e0e0; padding: 20px; border-radius: 12px; }
    div[data-testid="stExpander"] { border: none; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🚀 CommerceIntel")
    st.write("Commercial Intelligence & Retention Suite")
    menu = st.selectbox("Select Workspace", ["Snapshot", "Data Explorer", "Predictive Engine"])
    st.divider()
    st.caption("System Status: Online")

# --- 1. SNAPSHOT (High-Level Metrics) ---
if menu == "Snapshot":
    st.title("Business Performance Snapshot")
    
    # KPIs in different formats
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Total Revenue", "$428,500", "+12%")
    with c2:
        st.metric("Retention Rate", "91.2%", "2.4%")
    with c3:
        st.metric("Churn Risk", "4.8%", "-0.5%", delta_color="inverse")

    st.divider()
    
    # Multi-format charts
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("Sales Distribution")
        pie_data = pd.DataFrame({"Cat": ["Electronics", "Fashion", "Home"], "Val": [40, 35, 25]})
        st.plotly_chart(px.pie(pie_data, values='Val', names='Cat', hole=0.5), use_container_width=True)

    with col_right:
        st.subheader("Monthly Growth")
        line_data = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr"], "Sales": [10, 15, 13, 19]})
        st.plotly_chart(px.line(line_data, x="Month", y="Sales", markers=True), use_container_width=True)

# --- 2. DATA EXPLORER (Table Formats) ---
elif menu == "Data Explorer":
    st.title("Customer Intelligence Lab")
    uploaded_file = st.file_uploader("Import Customer Dataset (CSV)", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        # Display data in various formats
        st.subheader("Interactive Data Grid")
        st.dataframe(df, use_container_width=True)
        
        st.subheader("Statistical Summary")
        st.table(df.describe().head(5)) # Static table for key stats
    else:
        st.info("Upload a file to unlock advanced data grids.")

# --- 3. PREDICTIVE ENGINE ---
elif menu == "Predictive Engine":
    st.title("Customer Retention AI")
    
    with st.container():
        st.write("Adjust parameters to calculate churn probability.")
        col1, col2 = st.columns(2)
        recency = col1.slider("Last Purchase (Days)", 0, 180, 20)
        freq = col2.number_input("Total Orders", 1, 100, 5)
        
        if st.button("Generate Risk Profile"):
            # Calculation logic
            risk_score = (recency * 0.5) / freq
            
            # Visual Gauge Format
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = risk_score,
                title = {'text': "Churn Probability %"},
                gauge = {'axis': {'range': [None, 100]},
                         'bar': {'color': "darkblue"},
                         'steps' : [
                             {'range': [0, 30], 'color': "lightgreen"},
                             {'range': [30, 70], 'color': "yellow"},
                             {'range': [70, 100], 'color': "red"}]}))
            st.plotly_chart(fig, use_container_width=True)
