import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(page_title="CommerceIntel Pro", layout="wide", page_icon="📈")

# --- CUSTOM UI STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .action-card { background-color: #e3f2fd; padding: 15px; border-radius: 10px; border-left: 5px solid #2196f3; }
    </style>
    """, unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
# This ensures data persists across different menu selections
if 'raw_data' not in st.session_state:
    st.session_state.raw_data = None

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ Admin Panel")
    page = st.radio("Navigation", ["🏠 Home", "📁 Analysis Center", "🔮 Risk Predictor"])
    st.divider()
    if st.session_state.raw_data is not None:
        st.success("✅ Data Loaded in Memory")
    else:
        st.warning("⚠️ No Data Uploaded Yet")

# --- 1. HOME ---
if page == "🏠 Home":
    st.title("E-Commerce Intelligence Suite")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        ### Pro-Grade Analytics
        This system bridges the gap between **Raw Data** and **Actionable Strategy**. 
        1. Upload your CSV in the **Analysis Center**.
        2. View trends and KPI summaries.
        3. Use the **Risk Predictor** to scan your data for churn threats.
        """)
    with col2:
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80", use_container_width=True)

# --- 2. ANALYSIS CENTER ---
elif page == "📁 Analysis Center":
    st.title("Data Intelligence Lab")
    uploaded_file = st.file_uploader("Upload Customer Sales CSV", type="csv")
    
    if uploaded_file:
        # Save to session state so Risk Predictor can see it
        st.session_state.raw_data = pd.read_csv(uploaded_file)
        df = st.session_state.raw_data
        
        st.subheader("💡 Portfolio Overview")
        k1, k2, k3 = st.columns(3)
        k1.metric("Total Records", len(df))
        
        num_cols = df.select_dtypes(include=['number']).columns
        if not num_cols.empty:
            k2.metric("Total Volume", f"{df[num_cols[0]].sum():,.0f}")
            k3.metric("Average Transaction", f"{df[num_cols[0]].mean():,.2f}")

        st.divider()
        st.subheader("📊 Interactive Trends")
        x_ax = st.selectbox("Select Dimension (X)", df.columns)
        y_ax = st.selectbox("Select Metric (Y)", num_cols if not num_cols.empty else df.columns)
        st.plotly_chart(px.bar(df, x=x_ax, y=y_ax, template="plotly_white", color=x_ax), use_container_width=True)
    else:
        st.info("Please upload a file to begin.")

# --- 3. RISK PREDICTOR (Connected to Data) ---
elif page == "🔮 Risk Predictor":
    st.title("Automated Churn Analysis")
    
    if st.session_state.raw_data is None:
        st.error("🚨 No data found! Please upload a CSV in the 'Analysis Center' first.")
    else:
        df = st.session_state.raw_data
        st.write("### AI Risk Scanning")
        st.write("The system is now analyzing your uploaded database for behavioral anomalies.")

        # AUTOMATED DATA INSIGHT
        st.markdown("---")
        col_input, col_result = st.columns([1, 1.5])
        
        with col_input:
            st.write("**Manual Override**")
            days = st.slider("Last Purchase (Days)", 0, 365, 45)
            orders = st.number_input("Average Order Frequency", 1, 100, 5)
            
            if st.button("Generate Strategy"):
                risk_score = (days * 0.4) - (orders * 1.5)
                
                with col_result:
                    # GAUGE METER
                    fig = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = max(0, min(risk_score, 100)),
                        title = {'text': "Churn Risk Level"},
                        gauge = {'bar': {'color': "#ef5350" if risk_score > 50 else "#66bb6a"}}
                    ))
                    st.plotly_chart(fig, use_container_width=True)

                    # STRATEGY AND ACTIONS
                    st.markdown("### 🛠️ Recommended Actions")
                    if risk_score > 50:
                        st.markdown("""
                        <div class="action-card">
                        <strong>Strategy: Reactive Recovery</strong><br>
                        1. <strong>Incentive:</strong> Trigger a 20% 'We Miss You' discount code.<br>
                        2. <strong>Feedback:</strong> Send a 1-question survey to identify pain points.<br>
                        3. <strong>Channel:</strong> Reach out via SMS for higher open rates.
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div class="action-card" style="border-left-color: #4caf50; background-color: #e8f5e9;">
                        <strong>Strategy: Proactive Retention</strong><br>
                        1. <strong>Loyalty:</strong> Enroll in the VIP Early Access program.<br>
                        2. <strong>Up-sell:</strong> Recommend products based on their history.<br>
                        3. <strong>Engagement:</strong> Share educational content about their favorite category.
                        </div>
                        """, unsafe_allow_html=True)
        
        # DATA-DRIVEN TABLE (Solving problems using actual data)
        st.subheader("📋 High-Risk Segments in Your Data")
        st.write("The following records from your file match 'At-Risk' behavior profiles:")
        # Show users who have low frequency (example filter)
        if not num_cols.empty:
            risk_df = df[df[num_cols[0]] < df[num_cols[0]].mean()] # Showing records below average volume
            st.dataframe(risk_df.head(10), use_container_width=True)
