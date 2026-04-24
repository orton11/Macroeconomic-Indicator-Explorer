import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Macro Tool", layout="wide")
st.title("📊 Macroeconomic Comparison Tool")

# 加载数据
df = pd.read_csv('macro_data.csv')
df['year'] = df['year'].astype(int)

# 获取列表
countries = sorted(df['country'].unique())
year_min, year_max = df['year'].min(), df['year'].max()

st.success(f"✅ Loaded {df.shape[0]} rows, {len(countries)} countries")

# ========== 侧边栏 ==========
st.sidebar.header("⚙️ Settings")

selected_countries = st.sidebar.multiselect(
    "Select countries",
    countries,
    default=['China', 'United States']
)

indicator = st.sidebar.selectbox(
    "Select indicator",
    ['GDP Growth (%)', 'Inflation (%)', 'Unemployment Rate (%)', 
     'Trade (% of GDP)', 'Government Debt (% of GDP)']
)

year_range = st.sidebar.slider(
    "Year range",
    year_min, year_max,
    (2000, 2024)
)

# ========== 过滤数据 ==========
filtered = df[
    (df['country'].isin(selected_countries)) &
    (df['year'] >= year_range[0]) &
    (df['year'] <= year_range[1])
]

# ========== 图表 ==========
if not filtered.empty:
    st.subheader(f"📈 {indicator}")
    fig = px.line(
        filtered,
        x='year',
        y=indicator,
        color='country',
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # 统计
    st.subheader("📊 Summary")
    stats = filtered.groupby('country')[indicator].agg(['mean', 'min', 'max']).round(2)
    st.dataframe(stats)
else:
    st.warning("No data")

# ========== 原始数据 ==========
with st.expander("📋 Raw Data"):
    st.dataframe(filtered)