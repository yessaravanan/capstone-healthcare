import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ── Page Config ──
st.set_page_config(
    page_title="Health Risk Prediction Dashboard",
    page_icon="🏥",
    layout="wide"
)

# ── Load Data ──
@st.cache_data
def load_data():
    df = pd.read_csv('health_risk_predictions_v2.csv')
    df['bmi'] = df['bmi'].round(1)
    df['summary'] = df['summary'].str.replace(
        r"Here'?s a \d+-sentence plain language risk summary for the business team:?\s*",
        "", regex=True
    ).str.strip()
    return df

df = load_data()

# Force numeric + rounding once (safe)
df['bmi'] = pd.to_numeric(df['bmi'], errors='coerce').round(1)
df['risk_score'] = pd.to_numeric(df['risk_score'], errors='coerce').round(2)

# Reduce metric value truncation and allow wrapping for long labels/values. 
st.markdown(
    """
<style>
div[data-testid="stMetricValue"] > div {
    font-size: 1.35rem !important;
    white-space: normal !important;
    overflow: visible !important;
    text-overflow: clip !important;
    line-height: 1.2 !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# ── Shared Chart Layout ──
chart_layout = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white',
    margin=dict(l=0, r=0, t=10, b=0),
    height=320
)

# ── Header ──
st.title("🏥 Health Risk Prediction System")
st.caption("Capstone Project — Healthcare Vertical | Model: llama-3.1-8b-instant | Embeddings: all-MiniLM-L6-v2 | Vector Store: FAISS")
st.divider()

# ── KPI Metrics ──
col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Total Patients", len(df))
col2.metric("HIGH Risk", f"{len(df[df['risk_level'] == 'HIGH'])} (6.75%)", delta="5 anomalies · 12 silent", delta_color="inverse")
col3.metric("MEDIUM Risk", f"{len(df[df['risk_level'] == 'MEDIUM'])} (48.75%)", delta="4 anomalies · 19 silent", delta_color="inverse")
col4.metric("LOW Risk", f"{len(df[df['risk_level'] == 'LOW'])} (44.50%)", delta="2 anomalies · 0 silent", delta_color="inverse")
col5.metric("Anomalies", df['anomaly'].sum())
col6.metric("Silent Risk Profiles", df['silent_risk'].sum())

st.divider()

# ── Sidebar Filters ──
st.sidebar.title("🔍 Filters")
risk_filter = st.sidebar.multiselect(
    "Risk Level",
    options=['HIGH', 'MEDIUM', 'LOW'],
    default=['HIGH', 'MEDIUM', 'LOW']
)

anomaly_filter = st.sidebar.checkbox("Show Anomalies Only", value=False)
silent_filter = st.sidebar.checkbox("Show Silent Risk Only", value=False)

sex_filter = st.sidebar.multiselect(
    "Sex",
    options=['M', 'F'],
    default=['M', 'F']
)

age_range = st.sidebar.slider(
    "Age Range",
    min_value=int(df['age'].min()),
    max_value=int(df['age'].max()),
    value=(int(df['age'].min()), int(df['age'].max()))
)

# ── Apply Filters ──
filtered = df[
    (df['risk_level'].isin(risk_filter)) &
    (df['sex'].isin(sex_filter)) &
    (df['age'] >= age_range[0]) &
    (df['age'] <= age_range[1])
]

if anomaly_filter:
    filtered = filtered[filtered['anomaly'] == True]

if silent_filter:
    filtered = filtered[filtered['silent_risk'] == True]

# Ensure consistent table display precision after filters.
filtered = filtered.copy()
filtered['bmi'] = filtered['bmi'].round(1)
filtered['risk_score'] = filtered['risk_score'].round(2)

# ── Charts ──
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("📊 Risk Distribution")
    risk_labels = ['HIGH', 'MEDIUM', 'LOW']
    risk_values = [
        len(df[df['risk_level'] == 'HIGH']),
        len(df[df['risk_level'] == 'MEDIUM']),
        len(df[df['risk_level'] == 'LOW'])
    ]
    fig1 = go.Figure(go.Bar(
        x=risk_labels,
        y=risk_values,
        marker_color=['#c0392b', '#c47c00', '#2d7a4f'],
        text=[f"{v} ({v/len(df)*100:.1f}%)" for v in risk_values],
        textposition='outside',
        textfont=dict(color='white', size=13)
    ))
    fig1.update_layout(
        **chart_layout,
        xaxis=dict(title='Risk Level', color='white'),
        yaxis=dict(title='Number of Patients', color='white')
    )
    st.plotly_chart(fig1, use_container_width=True)

with col_chart2:
    st.subheader("📊 Risk Score Distribution")
    bins = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    labels = ['0.0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9']
    df['score_bin'] = pd.cut(df['risk_score'], bins=bins, labels=labels, include_lowest=True)
    bin_counts = df['score_bin'].value_counts().sort_index()
    fig2 = go.Figure(go.Bar(
        x=bin_counts.index.tolist(),
        y=bin_counts.values.tolist(),
        marker_color='#4f8fff',
        text=bin_counts.values.tolist(),
        textposition='outside',
        textfont=dict(color='white', size=11)
    ))
    fig2.update_layout(
        **chart_layout,
        xaxis=dict(title='Risk Score Range', color='white', tickmode='array',
                   tickvals=labels, ticktext=labels),
        yaxis=dict(title='Number of Patients', color='white')
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ── Patient Risk Table ──
st.subheader(f"📋 Patient Risk Table — {len(filtered)} records")

def color_risk(val):
    if val == 'HIGH':
        return 'background-color: #fdecea; color: #c0392b; font-weight: bold'
    elif val == 'MEDIUM':
        return 'background-color: #fef3e0; color: #c47c00; font-weight: bold'
    elif val == 'LOW':
        return 'background-color: #e8f5ee; color: #2d7a4f; font-weight: bold'
    return ''

display_cols = ['patient_id', 'age', 'sex', 'bmi', 'smoker',
                'diabetic', 'dx_code', 'risk_score', 'risk_level',
                'anomaly', 'silent_risk']

fmt = {'bmi': '{:.1f}', 'risk_score': '{:.2f}'}

styled = (
    filtered[display_cols]
    .style
    .map(color_risk, subset=['risk_level'])
    .format(fmt)
)
st.dataframe(styled, use_container_width=True, height=400)

st.divider()

# ── LLM Summary Lookup ──
st.subheader("🤖 LLM-Generated Risk Summary")

patient_ids = filtered['patient_id'].tolist()

if patient_ids:
    selected_patient = st.selectbox("Select Patient ID", options=patient_ids)
    patient_row = df[df['patient_id'] == selected_patient].iloc[0]

    col_info, col_summary = st.columns([1, 2])

    with col_info:
        st.markdown("**Patient Profile**")
        st.write(f"**Age:** {patient_row['age']}")
        st.write(f"**Sex:** {patient_row['sex']}")
        st.write(f"**BMI:** {patient_row['bmi']}")
        st.write(f"**Smoker:** {'Yes' if patient_row['smoker'] == 1 else 'No'}")
        st.write(f"**Diabetic:** {'Yes' if patient_row['diabetic'] == 1 else 'No'}")
        st.write(f"**DX Code:** {patient_row['dx_code']}")
        st.write(f"**Risk Score:** {patient_row['risk_score']}")

        if patient_row['risk_level'] == 'HIGH':
            st.error("Risk Level: HIGH")
        elif patient_row['risk_level'] == 'MEDIUM':
            st.warning("Risk Level: MEDIUM")
        else:
            st.success("Risk Level: LOW")

        if patient_row['anomaly']:
            st.error("⚠️ ANOMALY FLAGGED")
        if patient_row['silent_risk']:
            st.warning("⚠️ SILENT RISK PROFILE")

    with col_summary:
        st.markdown("**LLM-Generated Business Summary**")
        st.info(patient_row['summary'])
else:
    st.info("No HIGH or MEDIUM risk patients match current filters.")

st.divider()

# ── Anomaly Report ──
st.subheader("⚠️ Anomaly Report")
anomalies = df[df['anomaly'] == True][display_cols].copy()
anomalies['bmi'] = anomalies['bmi'].round(1)
anomalies['risk_score'] = anomalies['risk_score'].round(2)
st.dataframe(
    anomalies.style.map(color_risk, subset=['risk_level']).format(fmt),
    use_container_width=True
)

st.divider()

# ── Silent Risk Report ──
st.subheader("🔕 Silent Risk Profiles")
silent = df[df['silent_risk'] == True][display_cols].copy()
silent['bmi'] = silent['bmi'].round(1)
silent['risk_score'] = silent['risk_score'].round(2)
st.dataframe(
    silent.style.map(color_risk, subset=['risk_level']).format(fmt),
    use_container_width=True
)

st.divider()

# ── LLMOps Summary ──
st.subheader("📡 LLMOps Pipeline Summary")
col_ops1, col_ops2, col_ops3, col_ops4 = st.columns([2.2, 1, 1, 1])
col_ops1.metric("Model", "llama-3.1-8b-instant")
col_ops2.metric("Avg Latency", "2.88s")
col_ops3.metric("Avg Tokens", "91")
col_ops4.metric("Embedding Drift", "0.12 — STABLE")

drift_scores = [0.08, 0.09, 0.13, 0.11, 0.18, 0.14, 0.12]
drift_runs = [f'R{i+1}' for i in range(len(drift_scores))]

fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=drift_runs,
    y=drift_scores,
    mode='lines+markers+text',
    line=dict(color='#4f8fff', width=2),
    marker=dict(size=8),
    text=[str(v) for v in drift_scores],
    textposition='top center',
    textfont=dict(color='white', size=11)
))
fig3.add_hline(
    y=0.25,
    line_dash='dash',
    line_color='red',
    annotation_text='Threshold 0.25',
    annotation_position='top right',
    annotation_font_color='red'
)
fig3.update_layout(
    **chart_layout,
    xaxis=dict(title='Pipeline Run', color='white', tickmode='array',
               tickvals=drift_runs, ticktext=drift_runs),
    yaxis=dict(title='KL Divergence Score', color='white', range=[0, 0.35])
)
st.plotly_chart(fig3, use_container_width=True)
st.caption("Drift threshold: 0.25 — Retraining triggered if exceeded for 2 consecutive runs")

st.divider()
st.caption("Health Risk Prediction System | Capstone Project — Saravanan Shanmugam 207681 | Generative AI Advanced")