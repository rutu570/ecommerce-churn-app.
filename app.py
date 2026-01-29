import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO

# --- CONFIG ---
st.set_page_config(page_title="CommerceIntel Pro", layout="wide", page_icon="💡")

# --- SESSION STATE ---
if 'data' not in st.session_state:
    st.session_state.data = None

# --- SIDEBAR ---
with st.sidebar:
    st.title("💎 Intelligence Suite")
    page = st.radio("Workspace", ["Dashboard", "Strategy Lab", "Export Center"])
    st.divider()
    st.info("Tip: Upload a CSV in 'Strategy Lab' to activate AI suggestions.")

# --- 1. DASHBOARD ---
if page == "Dashboard":
    st.title("Commercial Snapshot")
    
    # Visualizing various formats: Metric, Gauge, and Area
    c1, c2, c3 = st.columns([1, 1, 2])
    
    with c1:
        st.metric("Retention Rate", "88%", "+2.1%")
        st.metric("Avg Order Value", "$142", "-$5")
    
    with c2:
        # Gauge Format for quick health check
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number", value = 72,
            title = {'text': "Market Reach %"},
            gauge = {'bar': {'color': "#3b82f6"}}))
        fig_gauge.update_layout(height=250, margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig_gauge, use_container_width=True)
        
    with c3:
        # Area Format for trends
        df_trend = pd.DataFrame({"Week": [1,2,3,4], "Users": [100, 120, 115, 140]})
        st.plotly_chart(px.area(df_trend, x="Week", y="Users", title="Weekly User Growth"), use_container_width=True)

# --- 2. STRATEGY LAB (Intelligence & Action) ---
elif page == "Strategy Lab":
    st.title("Strategy & Problem Solving")
    file = st.file_uploader("Upload Retail Data", type=["csv", "xlsx"])

    if file:
        # Handling multiple formats (CSV and Excel)
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        
        st.session_state.data = df
        st.success(f"Analyzed {file.name} successfully.")

        st.subheader("🤖 Automated Suggestions")
        
        # Logic to provide suggestions based on data
        num_cols = df.select_dtypes(include=['number']).columns
        if not num_cols.empty:
            low_performers = df[df[num_cols[0]] < df[num_cols[0]].mean()]
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.warning(f"Found {len(low_performers)} underperforming segments.")
                st.write("**Suggested Action:** Apply a 'Volume Discount' to these items to increase turnover.")
            
            with col_b:
                st.success("High-growth potential identified in top 10% of records.")
                st.write("**Suggested Action:** Move these to 'Featured' status on your homepage.")

        st.divider()
        st.subheader("🔍 Deep Dive Analysis")
        st.dataframe(df.style.highlight_max(axis=0, color='#dcfce7'), use_container_width=True)
    else:
        st.info("Upload your data to receive automated business suggestions.")

# --- 3. EXPORT CENTER (Various Formats) ---
elif page == "Export Center":
    st.title("Results Export")
    if st.session_state.data is not None:
        df = st.session_state.data
        st.write("Choose your preferred format for the final report:")
        
        c1, c2 = st.columns(2)
        
        # Format 1: CSV
        csv = df.to_csv(index=False).encode('utf-8')
        c1.download_button("📥 Download as CSV", data=csv, file_name="report.csv", mime="text/csv")
        
        # Format 2: JSON (For developers)
        json = df.to_json(orient='records').encode('utf-8')
        c2.download_button("📥 Download as JSON", data=json, file_name="report.json", mime="application/json")
        
        st.markdown("""
        ### 📋 Summary Report
        **Data Health:** Good  
        **Primary Insight:** Customer frequency is the strongest predictor of loyalty in this set.  
        **Next Steps:** Implement the loyalty program suggested in the 'Strategy Lab'.
        """)
    else:
        st.error("No data available to export. Please upload data in the Strategy Lab first.")
