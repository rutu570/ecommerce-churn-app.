import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- CONFIG & THEME ---
st.set_page_config(
    page_title="CommerceIntel Pro",
    page_icon="💎",
    layout="wide"
)

# Custom Professional Styling
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e1e4e8; }
    .hero-text { font-size: 42px; font-weight: 700; color: #1a1c23; margin-bottom: 0px; }
    .sub-text { font-size: 18px; color: #586069; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3039/3039434.png", width=80) # Logo
    st.title("Admin Console")
    page = st.selectbox("Switch Workspace", ["🏠 Overview", "📈 Intelligence Lab", "🔮 Risk Predictor"])
    st.divider()
    st.caption("Active Session: Secure ✅")

# --- 1. HOME (OVERVIEW) ---
if page == "🏠 Overview":
    # HERO SECTION
    col_img, col_txt = st.columns([1.5, 1])
    
    with col_img:
        # Professional E-commerce/Analytics Image
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop", 
                 use_container_width=True)
    
    with col_txt:
        st.markdown('<p class="hero-text">Predictive Analytics</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-text">Stop churn before it happens. Scale your revenue with AI-driven customer insights.</p>', unsafe_allow_html=True)
        st.button("Launch New Analysis", type="primary")

    st.divider()
    
    # KPI SECTION
    st.subheader("System Highlights")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Revenue Growth", "+24.5%", "High")
    k2.metric("Customer Churn", "2.1%", "-0.4%", delta_color="inverse")
    k3.metric("Retention Cost", "$12.40", "Optimal")
    k4.metric("AI Accuracy", "94.2%", "Stable")

# --- 2. INTELLIGENCE LAB ---
elif page == "📈 Intelligence Lab":
    st.title("Customer Intelligence Lab")
    st.write("Upload your dataset to visualize complex purchase patterns.")
    
    file = st.file_uploader("Upload CSV File", type="csv")
    if file:
        df = pd.read_csv(file)
        tab_v, tab_d = st.tabs(["📊 Visual Explorer", "📂 Raw Dataset"])
        
        with tab_v:
            c1, c2 = st.columns([1, 2])
            with c1:
                st.write("### Chart Controls")
                target = st.selectbox("Category Column", df.columns)
                value = st.selectbox("Metric Column", df.select_dtypes(include='number').columns)
            with c2:
                fig = px.bar(df, x=target, y=value, color=target, template="plotly_white", barmode="group")
                st.plotly_chart(fig, use_container_width=True)
        
        with tab_d:
            st.dataframe(df, use_container_width=True)

# --- 3. RISK PREDICTOR ---
elif page == "🔮 Risk Predictor":
    st.title("Retention Risk Engine")
    
    with st.container(border=True):
        st.write("### User Behavior Input")
        r, f, m = st.columns(3)
        recency = r.slider("Recency (Days)", 0, 365, 30)
        freq = f.number_input("Frequency (Orders)", 1, 100, 10)
        spend = m.number_input("Monetary ($)", 0, 5000, 500)
        
        if st.button("Generate Risk Profile", use_container_width=True):
            score = (recency * 0.4) - (freq * 1.2)
            
            # GAUGE METER
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = max(0, min(score, 100)),
                title = {'text': "Churn Risk Score"},
                gauge = {'axis': {'range': [0, 100]},
                         'bar': {'color': "#ff4b4b" if score > 30 else "#00cc96"},
                         'steps': [{'range': [0, 30], 'color': "#e8f5e9"}, 
                                   {'range': [30, 70], 'color': "#fff3e0"},
                                   {'range': [70, 100], 'color': "#ffebee"}]}))
            st.plotly_chart(fig, use_container_width=True)

