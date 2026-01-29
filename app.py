import streamlit as st
import pandas as pd
import plotly.express as px

# --- MODERN PAGE CONFIG ---
st.set_page_config(
    page_title="InsightCommerce Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS FOR BETTER LOOKS ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ ChurnAnalytica")
    st.info("The Ultimate E-commerce Intelligence Suite")
    page = st.radio("Menu", ["🏠 Dashboard Home", "📈 Analysis Lab", "🔮 AI Predictor"])
    st.divider()
    st.caption("v2.0 - Research Edition")

# --- 1. HOME DASHBOARD ---
if page == "🏠 Dashboard Home":
    st.title("Project Overview")
    
    # Hero Metric Row
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg. Retention", "84%", "+2.5%")
    col2.metric("Churn Risk", "12%", "-1.2%", delta_color="inverse")
    col3.metric("Avg. Order", "$142", "+$12")

    st.markdown("---")
    st.subheader("Why this Research Matters")
    st.write("""
    Retaining an existing customer is **5x cheaper** than acquiring a new one. 
    This platform uses data to identify 'At-Risk' users before they leave.
    """)
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1000&q=80")

# --- 2. ANALYSIS LAB ---
elif page == "📈 Analysis Lab":
    st.title("Data Intelligence Lab")
    uploaded_file = st.file_uploader("Drop your CSV here", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        tab1, tab2 = st.tabs(["📊 Visuals", "📋 Raw Data"])
        
        with tab1:
            st.subheader("Interactive Insights")
            c1, c2 = st.columns([1, 2])
            with c1:
                x_col = st.selectbox("X-Axis", df.columns)
                y_col = st.selectbox("Y-Axis", df.columns)
                color_col = st.selectbox("Color by", df.columns)
            
            with c2:
                fig = px.histogram(df, x=x_col, y=y_col, color=color_col, 
                                 template="plotly_white", barmode="group")
                st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.dataframe(df, use_container_width=True)

# --- 3. AI PREDICTOR ---
elif page == "🔮 AI Predictor":
    st.title("Churn Prediction Engine")
    st.write("Simulate customer behavior to test the model.")
    
    with st.expander("Configure Customer Parameters", expanded=True):
        c1, c2 = st.columns(2)
        days = c1.slider("Recency (Days since last buy)", 0, 365, 45)
        freq = c2.slider("Frequency (Total Orders)", 1, 50, 5)
    
    if st.button("Calculate Churn Probability"):
        # Research-based Logic Simulation
        risk = (days * 0.4) - (freq * 1.5)
        if risk > 15:
            st.error(f"High Risk Detected: {risk:.1f}% probability")
            st.warning("Action: Trigger 'Win-back' email sequence immediately.")
        else:
            st.success(f"Loyalty Confirmed: {risk:.1f}% probability")
            st.balloons()
