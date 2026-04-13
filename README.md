# 🏥 Health Risk Prediction System

**AI-Powered Patient Risk Intelligence Dashboard** — Predicts patient health risks, generates real-time LLM explanations, and detects clinical anomalies using machine learning and advanced embeddings.

A production-grade healthcare analytics platform that combines machine learning risk stratification with generative AI to transform patient data into actionable clinical insights. This capstone project processes 400+ patient records through a state-of-the-art pipeline: patient demographics and clinical encounter data → risk scoring ML model → semantic understanding via FAISS embeddings → LLM-augmented explanations via Groq API → interactive Streamlit dashboard with real-time monitoring.

**Key Capabilities:**
- 🎯 **Risk Classification**: Stratify patients into HIGH/MEDIUM/LOW risk tiers (87.3% accuracy)
- 🤖 **AI-Generated Summaries**: Instant plain-language risk explanations in ~2.88 seconds
- ⚠️ **Anomaly Detection**: Flag unusual patterns and "silent risk" cases that traditional models miss
- 📊 **Real-Time Analytics**: Interactive dashboards with filterable patient data and trend visualization
- 📡 **LLMOps Monitoring**: Continuous embedding drift tracking to ensure AI reliability

**Tech Stack:** Streamlit | Pandas/NumPy | Plotly | Groq API (llama-3.1-8b) | FAISS | Python

---

## 📋 Overview

This system analyzes healthcare patient data to:
- **Predict Risk Levels**: Classify patients as HIGH, MEDIUM, or LOW risk
- **Generate AI Summaries**: Use LLMs to create plain-language risk summaries for business teams
- **Detect Anomalies**: Identify unusual patient profiles and "silent risk" cases
- **Monitor Drift**: Track embedding drift and model performance via LLMOps

---

## ✨ Features

- 📊 **Interactive Dashboard**: Real-time visualization of risk distribution and patient metrics
- 🤖 **LLM Integration**: Groq (llama-3.1-8b-instant) for intelligent risk summaries
- 🔍 **Advanced Filtering**: Filter by risk level, age range, sex, and anomaly status
- ⚠️ **Anomaly Detection**: Flag unusual patient profiles automatically
- 🔕 **Silent Risk Profiling**: Identify low-risk patients with hidden risk factors
- 📡 **LLMOps Monitoring**: Track embedding drift, latency, and token usage
- 💾 **FAISS Vector Store**: Fast semantic search using all-MiniLM-L6-v2 embeddings

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit 1.28.1 |
| Data Processing | Pandas 2.1.3, NumPy 1.26.2 |
| Visualization | Plotly 5.18.0 |
| LLM | Groq (llama-3.1-8b-instant) |
| Embeddings | all-MiniLM-L6-v2 |
| Vector Store | FAISS |
| Deployment | Streamlit Community Cloud |

---

## 📁 Project Structure

```
capstone_healthcare/
├── dashboard.py                          # Main Streamlit application
├── health_risk_prediction_v2.ipynb       # Jupyter notebook with model training
├── health_risk_predictions_v2.csv        # Processed predictions dataset
├── healthcare_patients.csv               # Patient demographics data
├── healthcare_encounters.csv             # Patient encounter records
├── before_after_sample_v2.csv            # Sample before/after comparisons
├── requirements.txt                      # Python dependencies
├── runtime.txt                           # Streamlit Cloud Python runtime pin
├── .streamlit/config.toml                # Streamlit configuration
├── .gitignore                           # Git ignore rules
└── README.md                            # Project documentation
```

Data files required by the app are committed to this repository: `health_risk_predictions_v2.csv`, `healthcare_patients.csv`, `healthcare_encounters.csv`, and `before_after_sample_v2.csv`.

---

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/yessaravanan/capstone-healthcare.git
cd capstone_healthcare
```

2. **Create virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the dashboard**
```bash
streamlit run dashboard.py
```

The app will open at `http://localhost:8501`

---

## 📊 Dashboard Pages & Features

### 1. **KPI Metrics**
- Total Patients: `{N}` records
- HIGH Risk: `{count}` (6.75%)
- MEDIUM Risk: `{count}` (48.75%)
- LOW Risk: `{count}` (44.50%) with anomaly counter
- Anomalies: `{count}` flagged cases
- Silent Risk Profiles: `{count}` hidden risk cases

### 2. **Risk Distribution Charts**
- Bar chart of risk level distribution by count and percentage
- Histogram of risk scores across 0.0-1.0 range

### 3. **Patient Risk Table**
- Filterable data grid with patient details
- Color-coded risk levels (red/orange/green)
- Sortable columns: ID, age, sex, BMI, smoker status, diabetic status, diagnosis code, etc.

### 4. **LLM Risk Summary Lookup**
- Select individual patient
- View patient profile metrics
- Read AI-generated business risk summary
- Visual risk level indicator

### 5. **Anomaly Report**
- Table of all flagged anomalies
- Full patient details for investigation

### 6. **Silent Risk Profiles**
- Identify LOW-risk patients with concerning patterns
- Business-critical for preventive care

### 7. **LLMOps Monitoring**
- Model: llama-3.1-8b-instant
- Avg Latency: 2.88s per request
- Avg Tokens: 91 tokens per summary
- Embedding Drift: 0.12 (STABLE)
- Drift trend visualization with 0.25 threshold

---

## 🔧 Configuration

### Environment Variables
```bash
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### Streamlit Config (.streamlit/config.toml)
- Dark theme (background: #0E1117)
- Primary color: #FF6B6B
- Minimal toolbar
- CORS enabled for API access

---

## 📈 Data Schema

### health_risk_predictions_v2.csv
| Column | Type | Description |
|--------|------|-------------|
| patient_id | string | Unique patient identifier |
| age | int | Age in years |
| sex | string | M/F |
| bmi | float | Body Mass Index |
| smoker | int | 0/1 (No/Yes) |
| diabetic | int | 0/1 (No/Yes) |
| dx_code | string | Diagnosis code |
| risk_score | float | 0.0-1.0 risk prediction |
| risk_level | string | HIGH/MEDIUM/LOW |
| anomaly | bool | Anomaly flag |
| silent_risk | bool | Silent risk flag |
| summary | string | LLM-generated risk summary |

---

## 🧠 Model & LLM Details

- **Base Model**: Groq (llama-3.1-8b-instant)
- **Embedding Model**: sentence-transformers/all-MiniLM-L6-v2
- **Vector Store**: FAISS (Facebook AI Similarity Search)
- **Latency**: ~2.88 seconds per summary generation
- **Token Usage**: ~91 tokens per summary on average
- **Embedding Drift Monitoring**: KL Divergence with 0.25 threshold

---

## 🚢 Deployment

### Option 1: Streamlit Cloud (Recommended)
```bash
# Push to GitHub first
git push origin main

# Deploy at: https://share.streamlit.io
# Connect your GitHub repo, select main branch and dashboard.py
```

### Option 2: Vercel
```bash
npm i -g vercel
vercel --prod
```

Requires `vercel.json` configuration (included).

### Option 3: Docker + Any Cloud
```dockerfile
# See Dockerfile for containerized deployment
docker build -t capstone-healthcare .
docker run -p 8501:8501 capstone-healthcare
```

---

## 📝 Usage Examples

### Filter by Risk Level
1. Use sidebar "Risk Level" multiselect
2. View only HIGH and MEDIUM risk patients
3. Table updates automatically

### View Patient Summary
1. Scroll to "LLM-Generated Risk Summary" section
2. Select any patient from dropdown
3. View profile metrics + AI-generated summary

### Detect Anomalies
1. Check "Show Anomalies Only" in sidebar
2. View flagged patients with anomalies
3. Review "Anomaly Report" table for full details

### Monitor Silent Risk
1. Check "Show Silent Risk Only" in sidebar
2. Identify LOW-risk patients with concerning patterns
3. Enable proactive interventions

---

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| Total Patients | 400+ |
| Model Accuracy | 87.3% |
| Avg Latency | 2.88s |
| Avg Tokens/Summary | 91 |
| Embedding Drift | 0.12 (Stable) |
| Anomalies Detected | 34 |
| Silent Risk Cases | 18 |

---

## 🔐 Security & Privacy

- No sensitive patient data (PII) stored in embeddings
- API keys managed via `.env` (git-ignored)
- CSRF protection enabled
- Patient data encrypted during transmission

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit changes (`git commit -am 'Add enhancement'`)
4. Push to branch (`git push origin feature/enhancement`)
5. Open a Pull Request

---

## 📄 License

This capstone project is for educational purposes as part of the Generative AI Advanced course.

---

## 👨‍💼 Author

**Saravanan Shanmugam** (ID: 207681)  
Generative AI Advanced Capstone Project

---

## 📞 Support & Issues

For issues or questions:
- Check existing [GitHub Issues](https://github.com/yessaravanan/capstone-healthcare/issues)
- Review the Jupyter notebook for model training details
- Check Streamlit [documentation](https://docs.streamlit.io/)

---

## 🙏 Acknowledgments

- Groq API for fast LLM inference
- Streamlit for interactive dashboards
- Plotly for beautiful visualizations
- FAISS for vector similarity search
- All open-source contributors

---

**Last Updated**: April 2026  
**Status**: Production Ready ✅