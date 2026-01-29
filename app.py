import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- SETTINGS & THEME ---
st.set_page_config(page_title="CommerceIntel Ultimate", layout="wide", page_icon="📈")

st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .stAlert { border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🛡️ CommerceIntel")
    st.caption("Advanced Retail Analytics v3.0")
    st.divider()
    page = st.radio("Navigation", ["Dashboard", "Data Lab", "Risk Engine", "Settings"])
    st.divider()
    st.success("System: Connected")

# --- 1. DASHBOARD (Visual Summaries) ---
if page == "Dashboard":
    st.title("Business Snapshot")
    
    # KPI Row
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Gross Revenue", "$542K", "+14%")
    c2.metric("Active Users", "1,284", "+5%")
    c3.metric("Churn Rate", "3.2%", "-0.4%", delta_color="inverse")
    c4.metric("Avg. Ticket", "$124", "+$8")

    st.divider()

    # Dynamic Charts
    col_l, col_r = st.columns(2)
    
    with col_l:
        st.subheader("📦 Category Performance")
        mock_data = pd.DataFrame({"Category": ["Electronics", "Home", "Apparel", "Beauty"], "Sales": [4500, 3200, 2800, 1500]})
        fig_pie = px.pie(mock_data, values='Sales', names='Category', hole=0.6, color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_r:
        st.subheader("📈 Sales Velocity")
        line_data = pd.DataFrame({"Day": range(1,11), "Orders": [10, 12, 18, 15, 22, 25, 21, 28, 32, 35]})
        fig_line = px.area(line_data, x="Day", y="Orders", line_shape="spline", color_discrete_sequence=['#00CC96'])
        st.plotly_chart(fig_line, use_container_width=True)

# --- 2. DATA LAB (Upload & Smart Filtering) ---
elif page == "Data Lab":
    st.title("Intelligence Center")
    file = st.file_uploader("Import Sales Data (CSV)", type="csv")

    if file:
        df = pd.read_csv(file)
        
        # --- FEATURE: SMART SEARCH & FILTER ---
        st.subheader("🔍 Smart Filter")
        search_query = st.text_input("Search records (e.g., Customer Name or Product)")
        if search_query:
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]

        # --- FEATURE: DATA TABS ---
        tab1, tab2, tab3 = st.tabs(["📋 Data Grid", "📊 Trend Discovery", "📥 Export"])
        
        with tab1:
            st.dataframe(df, use_container_width=True, height=400)
            
        with tab2:
            num_cols = df.select_dtypes(include=['number']).columns
            if len(num_cols) >= 2:
                col_x = st.selectbox("Select Trend X", df.columns)
                col_y = st.selectbox("Select Trend Y", num_cols)
                fig_trend = px.histogram(df, x=col_x, y=col_y, color_discrete_sequence=['#636EFA'])
                st.plotly_chart(fig_trend, use_container_width=True)
            else:
                st.warning("Upload data with numeric columns to see trends.")
        
        with tab3:
            st.write("Download your filtered dataset below:")
            st.download_button("Export as CSV", df.to_csv().encode('utf-8'), "filtered_data.csv", "text/csv")
    else:
        st.info("Upload your retail CSV to unlock analysis.")

# --- 3. RISK ENGINE (Interactive Predictor) ---
elif page == "Risk Engine":
    st.title("AI Churn Prediction")
    st.write("Simulate customer behavior to identify potential revenue loss.")

    with st.expander("Customer Profile Settings", expanded=True):
        col1, col2 = st.columns(2)
        days_ago = col1.slider("Days Since Last Purchase", 0, 365, 45)
        total_spent = col2.number_input("Total Lifetime Spend ($)", 1, 10000, 500)
        satisfaction = st.select_slider("Customer Feedback Level", options=["Very Dissatisfied", "Neutral", "Happy", "Loyalist"])

    if st.button("Generate Risk Assessment"):
        # Simulated Logic for Feature Richness
        risk_score = (days_ago * 0.3)
        if satisfaction == "Very Dissatisfied": risk_score += 40
        
        # --- FEATURE: GAUGE METER ---
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = min(risk_score, 100),
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Churn Probability %", 'font': {'size': 24}},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "#1f77b4"},
                'steps': [
                    {'range': [0, 40], 'color': "#e8f5e9"},
                    {'range': [40, 70], 'color': "#fff3e0"},
                    {'range': [70, 100], 'color': "#ffebee"}],
            }
        ))
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        # --- FEATURE: ACTIONABLE RECOMMENDATIONS ---
        if risk_score > 60:
            st.error("🚨 CRITICAL RISK: This customer is likely to churn.")
            st.info("💡 **Next Action:** Issue a 20% discount code and trigger a personalized check-in email.")
        else:
            st.success("✅ STABLE: Customer shows healthy engagement levels.")

# --- 4. SETTINGS ---
elif page == "Settings":
    st.title("System Settings")
    st.toggle("Enable Real-time Notifications")
    st.toggle("Dark Mode UI (Beta)")
    st.color_picker("Brand Primary Color", "#007bff")
    st.button("Clear Cache & Data")
