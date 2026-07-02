import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
from app import run_elite_ranking_engine_stream

# Premium light mode config matching premium enterprise standards
st.set_page_config(page_title="Redrob Quantum AI Recruiting Platform", page_icon="⚡", layout="wide")

# Custom Light Palette Premium CSS Inject Injection
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Core Framework Light Reset */
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #1F2937; }
    .main { background-color: #F8FAFC; }
    
    /* Premium Button Frameworks */
    .stButton>button {
        background: linear-gradient(135deg, #0EA5E9 0%, #2563EB 100%);
        color: white !important; border: none; padding: 12px 24px; border-radius: 10px;
        font-weight: 600; transition: all 0.2s ease-in-out;
        box-shadow: 0 4px 14px rgba(14, 165, 233, 0.25); width: 100%;
    }
    .stButton>button:hover { transform: translateY(-1px); box-shadow: 0 6px 20deg rgba(14, 165, 233, 0.4); }
    
    /* Enterprise Component Panels */
    .card-shell {
        background: #FFFFFF; border: 1px solid #E2E8F0;
        border-radius: 16px; padding: 26px; margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }
    
    .metric-badge {
        background: linear-gradient(135deg, #0D9488 0%, #115E59 100%);
        color: white; padding: 6px 14px; border-radius: 9999px; font-weight: 700; font-size: 13px;
    }
    
    .stage-card {
        background: #F1F5F9; border-left: 4px solid #0EA5E9; padding: 14px;
        margin: 8px 0; border-radius: 4px 12px 12px 4px;
        animation: cardSlide 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    @keyframes cardSlide { from { opacity: 0; transform: translateX(-8px); } to { opacity: 1; transform: translateX(0); } }
</style>
""", unsafe_allow_html=True)

# --- MODERN LIGHT HEADER BAR COMPONENT ---
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center; padding: 16px 32px; background: #FFFFFF; border-bottom: 1px solid #E2E8F0; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 1px 2px 0 rgba(0,0,0,0.05);">
    <div style="display: flex; align-items: center; gap: 14px;">
        <div style="background: linear-gradient(135deg, #0EA5E9 0%, #2563EB 100%); width: 38px; height: 38px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight:800; color:white; font-size:18px; box-shadow: 0 2px 8px rgba(14,165,233,0.3);">Q</div>
        <span style="font-size: 20px; font-weight: 700; color: #1E293B; letter-spacing: -0.5px;">Redrob <span style="color:#0EA5E9; font-weight:500;">QuantumAI</span></span>
    </div>
    <div style="display: flex; align-items: center; gap: 24px;">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="width: 8px; height: 8px; background-color: #10B981; border-radius: 50%; display: inline-block;"></span>
            <span style="font-size: 14px; color: #64748B; font-weight:500;">Cluster Node: Active</span>
        </div>
        <div style="width: 36px; height: 36px; border-radius: 50%; background: #F1F5F9; border: 1px solid #E2E8F0; display:flex; align-items:center; justify-content:center; font-size:13px; font-weight:600; color:#475569;">PX</div>
    </div>
</div>
""", unsafe_allow_html=True)

left_panel, right_panel = st.columns([1, 2])

with left_panel:
    st.markdown('<div class="card-shell">', unsafe_allow_html=True)
    st.subheader("🎯 Job Requirements Schema")
    DATASET_PATH = "candidates.jsonl"
    
    job_desc_input = st.text_area(
        "Target Workspace Position Parameter:",
        value="Looking for a Senior Software Engineer with expertise in Python, FastAPI, and Postgres backend architectures. Should have experience building scalable APIs, deploying microservices, and orchestrating cloud vector layers.",
        height=220
    )
    
    top_k_select = st.slider("Target Pipeline Shortlist Count (Top-K):", 3, 15, 5)
    trigger_pipeline = st.button("⚡ Run Elite Match & Analytics Pipeline")
    st.markdown('</div>', unsafe_allow_html=True)

# Dynamic Processing Experience Handling
if trigger_pipeline:
    with right_panel:
        st.markdown('<div class="card-shell">', unsafe_allow_html=True)
        st.markdown("<h3 style='margin-top:0;'>⚙️ Quantum AI Pipeline Orchestration Mesh</h3>", unsafe_allow_html=True)
        
        # Interactive Synchronous Progress Placeholders
        progress_bar = st.progress(0)
        metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
        
        with metrics_col1:
            ui_stage = st.empty()
        with metrics_col2:
            ui_pct = st.empty()
        with metrics_col3:
            ui_eta = st.empty()
            
        st.markdown("<h4 style='margin-bottom:8px; color:#475569;'>🪵 Live Pipeline Activity Feed</h4>", unsafe_allow_html=True)
        log_container = st.empty()
        st.markdown('</div>', unsafe_allow_html=True)
        
        running_logs = []
        final_payload = None
        
        # Pull live values from generator pipeline loop execution
        for stage_idx, status_msg, detail, data_payload in run_elite_ranking_engine_stream(DATASET_PATH, job_desc_input):
            calculated_pct = int((stage_idx / 8) * 100)
            calculated_eta = int((8 - stage_idx) * 1.2)
            
            # Explicit real-time updates to UI fields
            ui_stage.metric("Stages Completed", f"{stage_idx}/8")
            ui_pct.metric("Completion", f"{calculated_pct}%")
            ui_eta.metric("ETA", f"{calculated_eta}s")
            
            progress_bar.progress(calculated_pct)
            
            running_logs.append(f"""
            <div class="stage-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="color:#0F172A; font-weight:600; font-size:14px;">✨ {status_msg}</span>
                    <span style="color:#0EA5E9; font-size:11px; font-weight:700; background:rgba(14,165,233,0.1); padding:2px 8px; border-radius:4px;">STAGE {stage_idx}</span>
                </div>
                <div style="color: #64748B; font-size: 13px; margin-top: 4px;">{detail}</div>
            </div>
            """)
            log_container.markdown("".join(running_logs), unsafe_allow_html=True)
            
            if data_payload is not None:
                final_payload = data_payload

        if final_payload is not None:
            st.session_state['processed_data'] = final_payload[0]
            st.session_state['text_column'] = final_payload[1]
            st.session_state['top_k'] = top_k_select
            st.session_state['pipeline_executed'] = True
            st.rerun()

# --- INTERACTIVE ANALYTICS & RECOGNITION DASHBOARD ---
if st.session_state.get('pipeline_executed', False):
    df = st.session_state['processed_data']
    text_col = st.session_state['text_column']
    top_k = st.session_state['top_k']
    
    top_records = df.head(top_k)
    
    # Locate data attributes safely
    name_col = 'anonymized_name' if 'anonymized_name' in df.columns else ('name' if 'name' in df.columns else df.columns[0])
    headline_col = 'headline' if 'headline' in df.columns else ('professional_headline' if 'professional_headline' in df.columns else text_col)
    summary_col = 'summary' if 'summary' in df.columns else ('professional_summary' if 'professional_summary' in df.columns else text_col)
    id_col = 'candidate_id' if 'candidate_id' in df.columns else ('id' if 'id' in df.columns else df.columns[0])

    st.markdown("## 📊 Strategic Talent Distribution Insights")
    analytics_col1, analytics_col2 = st.columns(2)
    
    with analytics_col1:
        st.markdown('<div class="card-shell">', unsafe_allow_html=True)
        st.markdown("### Match Accuracy Spectrum", unsafe_allow_html=True)
        fig_hist = px.histogram(df, x="final_match_score", nbins=12, color_discrete_sequence=['#0EA5E9'])
        fig_hist.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#1E293B", margin=dict(t=10,b=10,l=10,r=10))
        st.plotly_chart(fig_hist, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with analytics_col2:
        st.markdown('<div class="card-shell">', unsafe_allow_html=True)
        st.markdown("### Skill Vector Coordinates Matrix", unsafe_allow_html=True)
        fig_scatter = px.scatter(df, x="semantic_score", y="velocity_score", size="keyword_score", color_discrete_sequence=['#2563EB'])
        fig_scatter.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#1E293B", margin=dict(t=10,b=10,l=10,r=10))
        st.plotly_chart(fig_scatter, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"## 🏆 Top {top_k} Elite Selection Standings")
    
    for rank, (idx, row) in enumerate(top_records.iterrows(), 1):
        # Graceful fallbacks for string processing slices
        display_headline = str(row[headline_col]) if headline_col in row else "Senior Professional Contributor"
        if len(display_headline) > 100: display_headline = display_headline[:97] + "..."
            
        display_summary = str(row[summary_col]) if summary_col in row else str(row[text_col])
        if len(display_summary) > 300: display_summary = display_summary[:297] + "..."

        with st.container():
            st.markdown(f"""
            <div class="card-shell">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 20px;">
                    <div style="flex: 1; min-width: 300px;">
                        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                            <span style="background: #E0F2FE; color: #0369A1; padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 700; uppercase;">RANK {rank}</span>
                            <span style="color: #64748B; font-size: 12px; font-weight: 500;">🆔 ID: {row[id_col]}</span>
                        </div>
                        <h3 style="margin: 0 0 4px 0; color: #0F172A; font-size: 20px; font-weight:700;">👤 {row[name_col]}</h3>
                        <h4 style="margin: 0 0 12px 0; color: #0EA5E9; font-size: 15px; font-weight: 600;">💼 {display_headline}</h4>
                        <p style="color: #475569; font-size: 14px; line-height: 1.5; margin: 0;"><b>Professional Summary:</b> {display_summary}</p>
                    </div>
                    <div style="text-align: right; min-width: 140px; display:flex; flex-direction:column; align-items:flex-end; justify-content:space-between;">
                        <span class="metric-badge">Match Score: {row['final_match_score']*100:.1f}%</span>
                        <div style="margin-top: 40px; font-size:12px; color:#64748B;">
                            <div>🤖 Semantics: <b>{row['semantic_score']*100:.0f}%</b></div>
                            <div>🛠️ Keywords: <b>{row['keyword_score']*100:.0f}%</b></div>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    csv_report = top_records.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Export Elite Standings Data Report Matrix",
        data=csv_report,
        file_name="quantum_ai_shortlist_report.csv",
        mime="text/csv"
    )

# --- ENTERPRISE RECRUITMENT BRAND LINE FOOTER ---
st.markdown("""
<div style="margin-top: 80px; padding: 32px 20px; border-top: 1px solid #E2E8F0; text-align: center; background: #FFFFFF; border-radius:12px;">
    <p style="color: #64748B; font-size: 14px; margin: 0;">© 2026 Parthiban. All Rights Reserved. Designed & Developed by Parthiban to Premium Enterprise Specifications.</p>
    <div style="display: flex; justify-content: center; gap: 24px; margin-top: 12px;">
        <a href="#" style="color: #94A3B8; text-decoration: none; font-size: 13px;">Privacy Protocol</a>
        <a href="#" style="color: #94A3B8; text-decoration: none; font-size: 13px;">Terms of Platform Use</a>
        <a href="#" style="color: #94A3B8; text-decoration: none; font-size: 13px;">Pipeline Analytics Node Registry</a>
    </div>
</div>
""", unsafe_allow_html=True)