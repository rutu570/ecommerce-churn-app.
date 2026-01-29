import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- SETTINGS & THEME ---
st.set_page_config(page_title="CommerceIntel Pro", layout="wide", page_icon="📈")

# Custom UI Styling
st.markdown("""
    <style>
    .main { background-color: #f4f7f9; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #eef0f2; }
    .hero-title { font-size: 50px; font-weight: 800; color: #1e293b; margin-bottom: 0px; }
    .hero-subtitle { font-size: 20px; color: #64748b; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3039/3039434.png", width=60) # Small Logo
    st.title("🛡️ CommerceIntel")
    st.caption("Advanced Retail Analytics v3.0")
    st.divider()
    page = st.radio("Navigation", ["🏠 Home", "📊 Dashboard", "📁 Data Lab", "🔮 Risk Engine"])
    st.divider()
    st.success("System: Connected")

# --- 1. HOME PAGE (New Premium UI) ---
if page == "🏠 Home":
    col_text, col_img = st.columns([1, 1.2], gap="large")
    
    with col_text:
        st.markdown('<p class="hero-title">Predictive Intelligence</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Transform raw retail data into actionable growth strategies with AI-driven insights.</p>', unsafe_allow_html=True)
        
        st.info("📊 **Active Modules:** Churn Prediction, Trend Discovery, and Revenue Optimization.")
        st.button("Explore Analytics Lab", type="primary", use_container_width=True)

    with col_img:
        # High-quality professional analytics image
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop", 
                 caption="Real-time Data Processing Hub", use_container_width=True)

    st.divider()
    
    # Quick Snapshot Metrics
    st.subheader("System Highlights")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Revenue Growth", "+24.5%", "High")
    k2.metric("Customer Churn", "3.2%", "-0.4%", delta_color="inverse")
    k3.metric("Retention Cost", "$12.40", "Optimal")
    k4.metric("AI Accuracy", "94.2%", "Stable")

# --- 2. DASHBOARD ---
elif page == "📊 Dashboard":
    st.title("Business Snapshot")
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📦 Category Performance")
        mock_data = pd.DataFrame({"Category": ["Electronics", "Home", "Apparel", "Beauty"], "Sales": [4500, 3200, 2800, 1500]})
        fig_pie = px.pie(mock_data, values='Sales', names='Category', hole=0.6)
        st.plotly_chart(fig_pie, use_container_width=True)
    with col_r:
        st.subheader("📈 Sales Velocity")
        line_data = pd.DataFrame({"Day": range(1,11), "Orders": [10, 12, 18, 15, 22, 25, 21, 28, 32, 35]})
        fig_line = px.area(line_data, x="Day", y="Orders", color_discrete_sequence=['#00CC96'])
        st.plotly_chart(fig_line, use_container_width=True)

# --- 3. DATA LAB ---
elif page == "📁 Data Lab":
    st.title("Intelligence Center")
    file = st.file_uploader("Import Sales Data (CSV)", type="csv")
    if file:
        df = pd.read_csv(file)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Upload a retail CSV to unlock deep-dive analysis.")

# --- 4. RISK ENGINE ---
elif page == "🔮 Risk Engine":
    st.title("AI Churn Prediction")
    days_ago = st.slider("Days Since Last Purchase", 0, 365, 45)
    if st.button("Generate Risk Assessment"):
        risk_score = (days_ago * 0.3)
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = min(risk_score, 100),
            title = {'text': "Churn Probability %"},
            gauge = {'bar': {'color': "#1f77b4"}}))
        st.plotly_chart(fig_gauge, use_container_width=True)
