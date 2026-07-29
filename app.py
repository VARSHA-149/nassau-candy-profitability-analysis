import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Nassau Candy Dashboard",
    page_icon="🍬",
    layout="wide"
)

# -----------------------------
# Custom CSS Styling
# -----------------------------
st.markdown("""
<style>
    /* Typography & Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Light Theme Background */
    .stApp {
        background-color: #F8FAFC;
        color: #1F2937;
    }

    /* Reduce unnecessary top/bottom padding */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    /* Requirement 5 & 12: Minimal Executive Sidebar (230px width, Navy #0F3D91 background) */
    section[data-testid="stSidebar"] {
        width: 230px !important;
        min-width: 230px !important;
        max-width: 230px !important;
        background-color: #0F3D91 !important;
        padding-top: 1.5rem !important;
    }
    
    /* Sidebar Headers */
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4 {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        margin-top: 0.5rem !important;
        margin-bottom: 0.75rem !important;
        letter-spacing: 0.02em;
    }

    /* Sidebar Labels */
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] label p {
        color: #E2E8F0 !important;
        font-weight: 500 !important;
        font-size: 0.82rem !important;
        margin-bottom: 3px !important;
    }

    /* Requirement 4, 10, 11: Clean, uniform input controls with white background, #E5E7EB borders, 8px rounded corners */
    section[data-testid="stSidebar"] .stSelectbox > div > div, 
    section[data-testid="stSidebar"] .stMultiSelect > div > div,
    section[data-testid="stSidebar"] .stTextInput input,
    section[data-testid="stSidebar"] .stDateInput input {
        background-color: #FFFFFF !important;
        color: #1F2937 !important;
        border-radius: 8px !important;
        border: 1px solid #E5E7EB !important;
        font-size: 0.82rem !important;
        padding: 4px 10px !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
    }

    /* Style selectbox/multiselect placeholder & text color */
    section[data-testid="stSidebar"] div[role="button"] *,
    section[data-testid="stSidebar"] input {
        color: #1F2937 !important;
    }

    /* Requirement 3: Hide large multiselect tags/chips via CSS */
    div[data-baseweb="tag"] {
        display: none !important;
    }

    /* Requirement 8, 9: Equal vertical spacing and alignment between sidebar controls */
    section[data-testid="stSidebar"] .element-container {
        margin-bottom: 0.65rem !important;
    }

    /* Sidebar Divider */
    section[data-testid="stSidebar"] hr {
        border-color: rgba(255, 255, 255, 0.15) !important;
        margin: 1.2rem 0 !important;
    }

    /* Download Button at Bottom */
    .stDownloadButton button {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100% !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        padding: 8px 12px !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1) !important;
        transition: background-color 0.2s ease !important;
    }
    .stDownloadButton button:hover {
        background-color: #1D4ED8 !important;
    }
    .stDownloadButton button p {
        color: #FFFFFF !important;
    }

    /* Header Bar */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 0 10px 0;
    }
    .header-title {
        font-size: 2.1rem;
        font-weight: 700;
        color: #0F3D91;
        margin: 0;
        line-height: 1.2;
    }
    .header-subtitle {
        font-size: 1rem;
        font-weight: 500;
        color: #4B5563;
        margin-top: 2px;
    }
    .header-right {
        text-align: right;
        font-size: 0.85rem;
        color: #6B7280;
        background-color: #FFFFFF;
        padding: 6px 14px;
        border-radius: 8px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }

    /* Custom Divider */
    .header-divider {
        height: 1px;
        background-color: #E5E7EB;
        margin-bottom: 18px;
    }

    /* KPI Custom Cards */
    .kpi-card {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        padding: 24px 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        display: flex;
        align-items: center;
        gap: 18px;
        min-height: 135px;
        height: 100%;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
    }
    .kpi-icon-circle {
        width: 58px;
        height: 58px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.75rem;
        background-color: #EFF6FF;
        color: #2563EB;
        flex-shrink: 0;
    }
    .kpi-content {
        display: flex;
        flex-direction: column;
    }
    .kpi-title {
        font-size: 0.85rem;
        font-weight: 600;
        color: #6B7280;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 700;
        color: #0F3D91;
        margin: 3px 0;
        line-height: 1.1;
    }
    .kpi-trend {
        font-size: 0.8rem;
        font-weight: 600;
        color: #16A34A;
        display: flex;
        align-items: center;
        gap: 4px;
    }

    /* Business Insights Panel */
    .insights-card {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .insights-header {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0F3D91;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .insight-item {
        font-size: 0.82rem;
        color: #374151;
        margin-bottom: 6px;
        display: flex;
        align-items: flex-start;
        gap: 6px;
        line-height: 1.35;
    }
    .insight-icon {
        color: #16A34A;
        font-weight: bold;
        flex-shrink: 0;
    }

    /* Chart Container Styling */
    .chart-card {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 16px;
        height: 100%;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6B7280;
        font-size: 0.85rem;
        font-weight: 500;
        padding: 20px 0 10px 0;
        border-top: 1px solid #E5E7EB;
        margin-top: 25px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Dataset & Calculate Metrics
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/Nassau Candy Distributor.csv")
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)
    df["Month"] = df["Order Date"].dt.strftime("%b")
    df["Gross Margin (%)"] = (df["Gross Profit"] / df["Sales"]) * 100
    df["Profit per Unit"] = df["Gross Profit"] / df["Units"]
    return df

df_raw = load_data()

# -----------------------------
# Executive Clean Sidebar (~230px Width)
# -----------------------------
# Requirement 6: Simple Section Heading "Filters"
st.sidebar.markdown("<h3 style='font-size: 1.1rem; border-bottom: 1px solid rgba(255,255,255,0.15); padding-bottom: 6px; margin-bottom: 12px;'>Filters</h3>", unsafe_allow_html=True)

# Requirement 13: Exact Filter Order (Division, Region, Ship Mode, Product Search, Date Range)
# 1. Division Filter
division_options = df_raw["Division"].unique().tolist()
division = st.sidebar.multiselect(
    "Division",
    options=division_options,
    default=division_options
)

# 2. Region Filter
region_options = df_raw["Region"].unique().tolist()
selected_regions = st.sidebar.multiselect(
    "Region",
    options=region_options,
    default=region_options
)

# 3. Ship Mode Filter
ship_mode_options = df_raw["Ship Mode"].unique().tolist() if "Ship Mode" in df_raw.columns else []
if ship_mode_options:
    selected_ship_modes = st.sidebar.multiselect(
        "Ship Mode",
        options=ship_mode_options,
        default=ship_mode_options
    )
else:
    selected_ship_modes = []

# 4. Product Search
product_search = st.sidebar.text_input("Product Search", "")

# 5. Date Range
min_date = df_raw["Order Date"].min().date()
max_date = df_raw["Order Date"].max().date()
selected_date_range = st.sidebar.date_input(
    "Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# 6. Margin Threshold
margin_threshold = st.sidebar.slider(
    "Minimum Gross Margin (%)",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=1.0
)
# Apply All Filters while retaining original variable bindings
df = df_raw[
    (df_raw["Division"].isin(division)) &
    (df_raw["Region"].isin(selected_regions))
]

if ship_mode_options and selected_ship_modes:
    df = df[df["Ship Mode"].isin(selected_ship_modes)]

if len(selected_date_range) == 2:
    start_date, end_date = selected_date_range
    df = df[
        (df["Order Date"].dt.date >= start_date) &
        (df["Order Date"].dt.date <= end_date)
    ]

if product_search:
    df = df[df["Product Name"].str.contains(product_search, case=False, na=False)]

    df = df[df["Gross Margin (%)"] >= margin_threshold]

st.sidebar.markdown("---")

# Requirement 6: Simple Section Heading "Export"
st.sidebar.markdown("<h3 style='font-size: 1.1rem; border-bottom: 1px solid rgba(255,255,255,0.15); padding-bottom: 6px; margin-bottom: 12px;'>Export</h3>", unsafe_allow_html=True)

# Requirement 14: Download CSV Button at bottom
st.sidebar.download_button(
    label="Download Filtered CSV",
    data=df.to_csv(index=False),
    file_name="filtered_nassau_candy_data.csv",
    mime="text/csv"
)

# -----------------------------
# Page Header
# -----------------------------
latest_date_str = df_raw["Order Date"].max().strftime("%B %d, %Y")

st.markdown(f"""
<div class="header-container">
    <div>
        <h1 class="header-title">Nassau Candy Distributor</h1>
        <div class="header-subtitle">Product Line Profitability & Margin Performance Analysis</div>
    </div>
    <div class="header-right">
        📅 <strong>Last Updated:</strong> {latest_date_str}
    </div>
</div>
<div class="header-divider"></div>
""", unsafe_allow_html=True)

if df.empty:
    st.warning("⚠️ No data available matching the selected sidebar filters.")
else:
    # KPI Calculations
    total_sales = df["Sales"].sum()
    total_profit = df["Gross Profit"].sum()
    avg_margin = df["Gross Margin (%)"].mean()
    total_units = df["Units"].sum()

    # Dynamic Insights Calculations
    top_div = df.groupby("Division")["Gross Profit"].sum().idxmax() if not df.empty else "N/A"
    top_prod = df.groupby("Product Name")["Gross Profit"].sum().idxmax() if not df.empty else "N/A"

    # -----------------------------
    # KPI Section & Business Insights Panel
    # -----------------------------
    kpi_col, insight_col = st.columns([3.6, 1.0])

    with kpi_col:
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-icon-circle">💰</div>
                <div class="kpi-content">
                    <div class="kpi-title">Total Sales</div>
                    <div class="kpi-value">${total_sales:,.2f}</div>
                    <div class="kpi-trend">▲ Target Achieved</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-icon-circle">💵</div>
                <div class="kpi-content">
                    <div class="kpi-title">Gross Profit</div>
                    <div class="kpi-value">${total_profit:,.2f}</div>
                    <div class="kpi-trend">▲ Positive Returns</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-icon-circle">📈</div>
                <div class="kpi-content">
                    <div class="kpi-title">Average Margin</div>
                    <div class="kpi-value">{avg_margin:.2f}%</div>
                    <div class="kpi-trend">▲ Healthy Margin</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-icon-circle">📦</div>
                <div class="kpi-content">
                    <div class="kpi-title">Units Sold</div>
                    <div class="kpi-value">{int(total_units):,}</div>
                    <div class="kpi-trend">▲ High Demand</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with insight_col:
        st.markdown(f"""
        <div class="insights-card">
            <div class="insights-header">💡 Business Insights</div>
            <div class="insight-item"><span class="insight-icon">✔</span> <strong>Top Division:</strong> {top_div}</div>
            <div class="insight-item"><span class="insight-icon">✔</span> <strong>Top Product:</strong> {top_prod}</div>
            <div class="insight-item"><span class="insight-icon">✔</span> <strong>Avg Margin:</strong> {avg_margin:.2f}%</div>
            <div class="insight-item"><span class="insight-icon">✔</span> <strong>Pareto Rule:</strong> 80/20 profit split</div>
            <div class="insight-item"><span class="insight-icon">✔</span> <strong>Correlation:</strong> Sales & Margin link</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # -----------------------------
    # Chart Row 1
    # -----------------------------
    row1_c1, row1_c2, row1_c3 = st.columns(3)

    with row1_c1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        top_products = (
            df.groupby("Product Name")["Gross Profit"]
              .sum()
              .sort_values(ascending=False)
              .head(10)
              .reset_index()
        )
        fig_top_prod = px.bar(
            top_products,
            x="Product Name",
            y="Gross Profit",
            color="Gross Profit",
            title="Top 10 Most Profitable Products",
            template="plotly_white",
            color_continuous_scale="Blues"
        )
        fig_top_prod.update_layout(margin=dict(l=10, r=10, t=35, b=10), height=340, xaxis_tickangle=-45)
        st.plotly_chart(fig_top_prod, width="stretch")
        st.markdown('</div>', unsafe_allow_html=True)

    with row1_c2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        fig_scatter = px.scatter(
            df,
            x="Sales",
            y="Gross Margin (%)",
            color="Division",
            hover_data=["Product Name"],
            title="Sales vs Gross Margin",
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig_scatter.update_layout(margin=dict(l=10, r=10, t=35, b=10), height=340)
        st.plotly_chart(fig_scatter, width="stretch")
        st.markdown('</div>', unsafe_allow_html=True)

    with row1_c3:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        region_summary = (
            df.groupby("Region")
              .agg({
                  "Sales": "sum",
                  "Gross Profit": "sum"
              })
              .reset_index()
        )
        fig_region = px.bar(
            region_summary,
            x="Region",
            y="Gross Profit",
            color="Region",
            title="Gross Profit by Region",
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig_region.update_layout(margin=dict(l=10, r=10, t=35, b=10), height=340)
        st.plotly_chart(fig_region, width="stretch")
        st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------
    # Chart Row 2
    # -----------------------------
    row2_c1, row2_c2, row2_c3 = st.columns(3)

    with row2_c1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        division_summary = (
            df.groupby("Division")
              .agg({
                  "Sales": "sum",
                  "Gross Profit": "sum"
              })
              .reset_index()
        )
        
        col1, col2 = st.columns(2)
        with col1:
            fig_sales = px.bar(
                division_summary,
                x="Division",
                y="Sales",
                color="Division",
                title="Sales by Division",
                template="plotly_white"
            )
            fig_sales.update_layout(margin=dict(l=5, r=5, t=30, b=5), height=310)
            st.plotly_chart(fig_sales, width="stretch")

        with col2:
            fig_profit = px.bar(
                division_summary,
                x="Division",
                y="Gross Profit",
                color="Division",
                title="Gross Profit by Division",
                template="plotly_white"
            )
            fig_profit.update_layout(margin=dict(l=5, r=5, t=30, b=5), height=310)
            st.plotly_chart(fig_profit, width="stretch")
            
        st.markdown('</div>', unsafe_allow_html=True)

    with row2_c2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        monthly = (
            df.groupby("Month")["Sales"]
              .sum()
              .reindex([m for m in month_order if m in df["Month"].unique()])
              .reset_index()
        )
        fig_monthly = px.line(
            monthly,
            x="Month",
            y="Sales",
            markers=True,
            title="Monthly Sales Trend",
            template="plotly_white",
            color_discrete_sequence=["#2563EB"]
        )
        fig_monthly.update_layout(margin=dict(l=10, r=10, t=35, b=10), height=340)
        st.plotly_chart(fig_monthly, width="stretch")
        st.markdown('</div>', unsafe_allow_html=True)

    with row2_c3:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        pareto = (
            df.groupby("Product Name")["Gross Profit"]
              .sum()
              .sort_values(ascending=False)
              .reset_index()
        )
        pareto["Cumulative %"] = (
            pareto["Gross Profit"].cumsum() /
            pareto["Gross Profit"].sum()
        ) * 100

        fig_pareto = px.bar(
            pareto.head(15),
            x="Product Name",
            y="Gross Profit",
            title="Pareto Analysis",
            template="plotly_white",
            color="Gross Profit",
            color_continuous_scale="Teal"
        )
        fig_pareto.update_layout(margin=dict(l=10, r=10, t=35, b=10), height=340, xaxis_tickangle=-45)
        st.plotly_chart(fig_pareto, width="stretch")
        st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------
    # Row 3: Filtered Dataset Preview
    # -----------------------------
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.subheader(" Dataset Preview")
    st.dataframe(df.head(10), width="stretch", height=280)
    st.markdown('</div>', unsafe_allow_html=True)

