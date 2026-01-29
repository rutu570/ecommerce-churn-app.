import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="CommerceIntel Pro", layout="wide", page_icon="📈")

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("🕹️ Control Panel")
page = st.sidebar.selectbox("Go to:", ["🏠 Home", "📁 Analysis Center", "🔮 Risk Predictor"])

# --- 1. HOME ---
if page == "🏠 Home":
    st.title("E-Commerce Intelligence Suite")
    st.markdown("""
    ### Transform your raw data into strategy.
    Use this tool to:
    * **Upload** sales CSVs and see instant summaries.
    * **Analyze** product performance with interactive visuals.
    * **Predict** customer churn using behavioral sliders.
    """)
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80")

# --- 2. ANALYSIS CENTER ---
elif page == "📁 Analysis Center":
    st.title("Data Intelligence Lab")
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success(f"Successfully loaded {len(df)} rows.")

        # --- FEATURE: AUTO-KPI CARDS ---
        st.subheader("💡 Quick Stats")
        kpi1, kpi2, kpi3 = st.columns(3)
        
        # Checking for common column names (Sales, Price, etc.)
        num_cols = df.select_dtypes(include=['number']).columns
        if not num_cols.empty:
            kpi1.metric("Total Volume", f"{df[num_cols[0]].sum():,.0f}")
            kpi2.metric("Avg Value", f"{df[num_cols[0]].mean():,.2f}")
            kpi3.metric("Unique Records", len(df))

        st.divider()

        # --- FEATURE: INTERACTIVE FILTERING ---
        st.subheader("📊 Visual Explorer")
        all_cols = df.columns.tolist()
        
        col_a, col_b, col_c = st.columns(3)
        x_ax = col_a.selectbox("Horizontal (X) Axis", all_cols)
        y_ax = col_b.selectbox("Vertical (Y) Axis", num_cols if not num_cols.empty else all_cols)
        chart_type = col_c.selectbox("Chart Style", ["Bar", "Line", "Scatter", "Pie"])

        # --- FEATURE: DYNAMIC CHARTING ---
        if chart_type == "Bar":
            fig = px.bar(df, x=x_ax, y=y_ax, color=x_ax, template="plotly_white")
        elif chart_type == "Line":
            fig = px.line(df, x=x_ax, y=y_ax, template="plotly_white")
        elif chart_type == "Scatter":
            fig = px.scatter(df, x=x_ax, y=y_ax, color=x_ax)
        else:
            fig = px.pie(df, names=x_ax, values=y_ax)

        st.plotly_chart(fig, use_container_width=True)

        # --- FEATURE: DATA EXPORT ---
        st.download_button("📥 Download Analysis as CSV", df.to_csv().encode('utf-8'), "analysis.csv", "text/csv")
    else:
        st.info("Waiting for data... Please upload a CSV to begin.")

# --- 3. RISK PREDICTOR ---
elif page == "🔮 Risk Predictor":
    st.title("Churn Probability Engine")
    st.write("Determine how likely a customer is to leave.")
    
    with st.container():
        c1, c2 = st.columns(2)
        days = c1.slider("Last Purchase (Days Ago)", 0, 365, 30)
        orders = c2.number_input("Lifetime Orders", 1, 100, 5)
        
        if st.button("Generate Risk Profile"):
            # Simple logical feature: Risk Scoring
            score = (days * 0.5) - (orders * 2)
            if score > 20:
                st.error(f"High Churn Risk (Score: {score:.1f})")
                st.warning("Action Needed: Send a retention discount coupon.")
            else:
                st.success(f"Healthy Relationship (Score: {score:.1f})")
                st.balloons()
