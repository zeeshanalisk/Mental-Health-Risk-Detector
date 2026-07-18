# ===================================================================
# Importing Necessary Libraries and Packages
# ===================================================================
import os
import time
import pickle
import requests
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_lottie import st_lottie

# ===================================================================
# Page / Meta Layout
# ===================================================================
st.set_page_config(
    page_title="Mental Health Risk in Tech — Assessment",
    page_icon="🧠",
    layout="wide"
)

# ===================================================================
# Background + Global Styles
# ===================================================================
def set_background_and_styles():
    st.markdown(
        """
        <style>
.stApp {
    background:
      linear-gradient( to bottom right, rgba(098,5,675,1.345), rgba(249,947,090,1.980) ),
      url('https://thumbs.dreamstime.com/z/lightbox-motivation-words-self-care-positive-thinking-mental-health-emotional-wellness-top-view-185218285.jpg?ct=jpeg');
    background-size: cover;
    background-attachment: fixed;
    color: #ffffff;  /* main text color changed to white */
    font-family: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
    animation: fadeBg 2.2s ease-in-out;
}
.glass {
    background: rgba(255,255,255,0.08);
    -webkit-backdrop-filter: blur(12px);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 18px;
    padding: 22px 20px 18px 20px;
    box-shadow: 0 14px 36px rgba(0,0,0,25);
    animation: fadeInUp 0.8s ease both;
    color: #ffffff;  /* glass box text color */
}
.hero-title { font-size: 42px; font-weight: 900; color: #ffffff; text-shadow: 0 10px 28px rgba(0,0,0,.45); animation: fadeInDown 1.1s ease both; }
.hero-sub { font-size: 17px; color: #f1f5f9; margin-top: -4px; animation: fadeIn 1.4s ease both; }
label, .stSelectbox label, .stRadio label, .stSlider label {
    font-size: 18px !important; font-weight: 700 !important;
    color: #ffffff !important;  /* changed label text color */
    text-shadow: 0 0 16px rgba(59,130,246,.48);
    animation: glowFade 2.4s ease-in-out infinite alternate, fadeIn 0.6s ease-in-out;
}
div.stButton > button:first-child {
    background: linear-gradient(90deg, #22d3ee, #3b82f6);
    border: none !important;
    border-radius: 16px !important;
    color: #061028 !important;
    font-weight: 900 !important;
    letter-spacing: .3px;
    padding: 13px 22px;
    box-shadow: 0 12px 28px rgba(37,99,235,.45);
    transition: transform .2s ease, box-shadow .2s ease;
    animation: pulse 2.4s infinite;
}
div.stButton > button:first-child:hover { transform: translateY(-2px) scale(1.03); box-shadow: 0 18px 34px rgba(37,99,235,.65); }
.risk-bar-frame{ width:100%; background: rgba(255,255,255,0.08); border-radius: 12px; padding: 6px; border: 1px solid rgba(255,255,255,0.12); margin-top: 10px; }
.risk-bar-fill{ height: 34px; border-radius: 8px; width: 0%; display:flex; align-items:center; justify-content:center; color:#ffffff; font-weight: 900; background: linear-gradient(90deg, #22d3ee 0%, #60a5fa 50%, #ef4444 100%); box-shadow: inset 0 0 8px rgba(255,255,255,.25), 0 6px 15px rgba(0,0,0,.18); transition: width .18s ease-out; }
.section-title { font-size: 22px; font-weight: 900; color: #ffffff; margin-bottom: 4px; }
.muted { color:#cbd5e1; }
@keyframes fadeIn { from {opacity:0;} to {opacity:1;} }
@keyframes fadeInUp { from {opacity:0; transform: translateY(20px);} to {opacity:1; transform:none;} }
@keyframes fadeInDown { from {opacity:0; transform: translateY(-20px);} to {opacity:1; transform:none;} }
@keyframes pulse { 0% { box-shadow: 0 0 0px rgba(34,211,238,.2); } 50% { box-shadow: 0 0 26px rgba(59,130,246,.55); } 100% { box-shadow: 0 0 0px rgba(34,211,238,.2); } }
@keyframes glowFade { from { text-shadow: 0 0 12px rgba(59,130,246,.3); } to   { text-shadow: 0 0 22px rgba(34,211,238,.65); } }
@keyframes fadeBg { from {opacity:0;} to {opacity:1;} }
</style>
<style>
/* Make all labels, radio buttons, and select text visible */
.stRadio label, .stSelectbox label, .stSlider label, label {
    color: #f4f5f34 !important;       /* bright white-ish */
    font-weight: 700 !important;     /* bold */
}

.stRadio > div, .stRadio input[type="radio"] {
    accent-color: #22d3ee !important;  /* bright blue selection */
}

.stSelectbox select, .stSlider input {
    color: #f1f5f9 !important;
    background-color: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
}

/* Optional: improve spacing for readability */
.stRadio, .stSelectbox, .stSlider {
    margin-bottom: 14px;
}
</style>


        """,
        unsafe_allow_html=True
    )

set_background_and_styles()

# ===================================================================
# Lottie Loader Block
# ===================================================================
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_brain = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")

# ===================================================================
# About Section
# ===================================================================
with st.sidebar:
    st.markdown("<div class='color#ffff'><b>💡 Motivation</b></div>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif", use_container_width=True)
    st.caption("Small steps matter. Awareness and Mental well-being are as vital as your work/job itself.💙")
    st.caption("Your HR Partner for Mental Well-being Insight;")
    st.caption("[1]Early Risk Detection: Helps HR identify employees who may be at risk of mental health challenges")
    st.caption("[2]Preventive Action: Provides insights so HR can plan wellness programs before issues escalate.")
    st.caption("[3]Workload Management: Supports balancing workload to reduce stress and burnout")

# ===================================================================
# Header of the Interface
# ===================================================================
st.markdown("<div class='hero-title'>🧠 Mental Health Risk Prediction in Tech Industry</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-sub'>Short, respectful check-in → risk estimate → practical guidance. Educational only.</div>", unsafe_allow_html=True)
if lottie_brain:
    st_lottie(lottie_brain, height=200, key="brain", loop=True)

# ===================================================================
# Loading the Trained AIML Model
# ===================================================================
MODEL_PATH = "osmi_mental_health_trained_model.pkl"
SCALER_PATH = "trained_model_scaler.pkl"

def try_load(path):
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except Exception:
        return None

model = try_load(MODEL_PATH)
scaler = try_load(SCALER_PATH)

# ===================================================================
# Questionnaire Survey
# ===================================================================
st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>📋 Questionnaire</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    age = st.slider("👤 What is your Age?", 18, 70, 28)
    gender = st.radio("⚧ State your Gender:", ["Male", "Female", "Other"])
    self_employed = st.radio("💼 Are you Self-employed?", ["Yes", "No"])
    family_history = st.radio("🏥 Do you have a Family history of Mental-illness?", ["Yes", "No"])
    work_interfere = st.selectbox("📊 How often does work interferes with Mental health?", ["Never", "Rarely", "Sometimes", "Often"])
    no_employees = st.selectbox("👥 How many employees work at your company?", ["1-5", "6-25", "26-100", "100-500", "500-1000", "1000+"])
    remote_work = st.radio("🌍 Do you work remotely?", ["Yes", "No"])
    tech_company = st.radio("💻 Are you employed in a Company related to Tech Industry ?", ["Yes", "No"])
with col2:
    benefits = st.radio("🎁 Does your Employer provides Mental health benefits?", ["Yes", "No", "Don't know"])
    care_options = st.radio("🆘 Are Care options provided by Employer?", ["Yes", "No"])
    wellness_program = st.radio("💡 Presence of Wellness programs?", ["Yes", "No"])
    seek_help = st.radio("🔎 Do you seek help for Mental health concerns when needed?", ["Yes", "No"])
    anonymity = st.radio("🙈 Is your anonymity protected when seeking help?", ["Yes", "No"])
    leave = st.radio("🛑 Ease of taking Medical leave?", ["Easy", "Neutral", "Difficult"])
    mental_health_consequence = st.radio("😟 Consequences for discussing mental health with employer?", ["Yes", "No"])
    phys_health_consequence = st.radio("🤕 Consequences for discussing physical health with employer?", ["Yes", "No"])
with col3:
    coworkers = st.radio("🧑‍🤝‍🧑 Willingness to discuss mental health with coworkers?", ["Yes", "No"])
    supervisor = st.radio("👨‍💼 Willingness to discuss mental health with supervisor?", ["Yes", "No"])
    mental_health_interview = st.radio("🗣️ Discuss mental health in job interview?", ["Yes", "No"])
    phys_health_interview = st.radio("🩺 Discuss physical health in job interview?", ["Yes", "No"])
    mental_vs_physical = st.radio("⚖️ Employer gives equal importance to mental and physical health?", ["Yes", "No"])
    obs_consequence = st.radio("👀 Have you noticed any negative consequences for people discussing mental health at work?", ["Yes", "No"])
    work_hours = st.slider("⏱️ Work hours per day", 4, 16, 9)
    sleep_hours = st.slider("😴 Average sleep per night (hours)", 3, 12, 7)
    stress = st.slider("🔥 Perceived stress (1–10)", 1, 10, 6)

st.markdown("</div>", unsafe_allow_html=True)

# ===================================================================
# Encoding the Inputs 
# ===================================================================
def yesno(v): return 1 if v == "Yes" else 0
def gender_enc(g): return {"Male":0,"Female":1,"Other":2}.get(g,2)
def map_idx(val,lst): return lst.index(val) if val in lst else 0

feat_order = [
    "Age","Gender","SelfEmployed","FamilyHistory","WorkInterfere","NoEmployees",
    "RemoteWork","TechCompany","Benefits","CareOptions","WellnessProgram","SeekHelp",
    "Anonymity","Leave","MHConsequence","PHConsequence","Coworkers","Supervisor",
    "MHInterview","PHInterview","MHvsPH","ObsConsequence"
]

feat = {
    "Age": age,
    "Gender": gender_enc(gender),
    "SelfEmployed": yesno(self_employed),
    "FamilyHistory": yesno(family_history),
    "WorkInterfere": map_idx(work_interfere, ["Never","Rarely","Sometimes","Often"]),
    "NoEmployees": map_idx(no_employees, ["1-5","6-25","26-100","100-500","500-1000","1000+"]),
    "RemoteWork": yesno(remote_work),
    "TechCompany": yesno(tech_company),
    "Benefits": map_idx(benefits, ["Yes","No","Don't know"]),
    "CareOptions": yesno(care_options),
    "WellnessProgram": yesno(wellness_program),
    "SeekHelp": yesno(seek_help),
    "Anonymity": yesno(anonymity),
    "Leave": map_idx(leave, ["Easy","Neutral","Difficult"]),
    "MHConsequence": yesno(mental_health_consequence),
    "PHConsequence": yesno(phys_health_consequence),
    "Coworkers": yesno(coworkers),
    "Supervisor": yesno(supervisor),
    "MHInterview": yesno(mental_health_interview),
    "PHInterview": yesno(phys_health_interview),
    "MHvsPH": yesno(mental_vs_physical),
    "ObsConsequence": yesno(obs_consequence)
}

X = np.array([feat[k] for k in feat_order], dtype=float).reshape(1,-1)

if scaler is not None:
    try: X_scaled = scaler.transform(X)
    except Exception: X_scaled = X
else: X_scaled = X

# ===================================================================
# Prediction button
# ===================================================================
st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>🔮 Prediction</div>", unsafe_allow_html=True)
left, right = st.columns([1,2])
with left:
    predict = st.button("GET RISK ESTIMATION", use_container_width=True)

risk_percent = None
model_used = False

if predict and model is not None:
    try:
        if hasattr(model,"predict_proba"):
            proba = model.predict_proba(X_scaled)[0]
            idx = int(np.where(model.classes_==1)[0][0]) if 1 in list(model.classes_) else 1
            risk_percent = float(np.clip(proba[idx]*100.0,0,100))
        else:
            pred = model.predict(X_scaled)[0]
            risk_percent = 70.0 if int(pred)==1 else 20.0
        model_used = True
    except Exception:
        st.error("Prediction failed. Ensure the model is compatible.")

# ===================================================================
# Risk display + Gauge + Charts 
# ===================================================================
if risk_percent is not None:
    num_ph = st.empty()
    bar_ph = st.empty()
    target = int(round(risk_percent))
    step = max(1,target//50 or 1)
    for i in range(0,target+1,step):
        num_ph.markdown(
            f"<h3 style='margin:0'>Risk Probability: "
            f"<span style='background:linear-gradient(90deg,#22d3ee,#60a5fa);padding:6px 12px;"
            f"border-radius:10px;color:#061028;font-weight:900'>{i}%</span></h3>",
            unsafe_allow_html=True
        )
        bar_html = f"""
        <div class="risk-bar-frame">
            <div class="risk-bar-fill" style="width:{i}%;"><div style="width:100%; text-align:center; color: white; font-weight:800;">{i}%</div></div>
        </div>
        """
        bar_ph.markdown(bar_html, unsafe_allow_html=True)
        time.sleep(0.012)

    # Gauge
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=target,
        title={'text': "Risk Probability (%)"},
        gauge={
            'axis': {'range': [0,100]},
            'bar': {'color': "rgba(0,0,0,0)"},
            'steps':[{'range':[0,40],'color':"#10b981"},{'range':[40,70],'color':"#fbbf24"},{'range':[70,100],'color':"#ef4444"}],
            'threshold':{'line':{'color':"white",'width':4}, 'thickness':0.75,'value':target}
        }
    ))
    gauge.update_layout(height=250, margin=dict(t=10,b=0,l=0,r=0))
    st.plotly_chart(gauge, use_container_width=True)

    # Animated Graph + Bar + Pie
    st.markdown("#### 📊 Probability Breakdown")
    bar_placeholder = st.empty()
    pie_placeholder = st.empty()
    frames = np.linspace(0,risk_percent/100.0,12)
    for f in frames:
        bar_fig = go.Figure(data=[go.Bar(
            x=["Low Risk","High Risk"],
            y=[1.0-f,f],
            text=[f"{(1.0-f)*100:.1f}%", f"{f*100:.1f}%"],
            textposition="auto"
        )])
        bar_fig.update_yaxes(range=[0,1])
        bar_fig.update_layout(height=320, margin=dict(t=30,b=0,l=0,r=0))
        bar_placeholder.plotly_chart(bar_fig, use_container_width=True)
        time.sleep(0.05)

    pie_fig = px.pie(values=[100-risk_percent,risk_percent],
                     names=["Low Risk","High Risk"], hole=0.35, title="Distribution")
    pie_fig.update_traces(textinfo="percent+label")
    pie_placeholder.plotly_chart(pie_fig, use_container_width=True)

    # Guidance
    st.markdown("#### 🧭 Suggested next steps")
    tips = []
    if target<30: st.success("Low risk — keep protective habits strong."); tips+=["Protect 7–9h sleep window.","Micro-breaks every 60–90 minutes."]
    elif target<60: st.warning("Moderate risk — small changes will help."); tips+=["Reduce late-night screens.","Schedule 2–3 movement breaks/day.","Add low-intensity exercise (walks)."]
    else: st.error("High risk — consider structured support."); tips+=["Talk with a counselor/EAP.","Calendar 15-min recovery breaks.","Renegotiate scope/timelines early."]
    if sleep_hours<7: tips.append("Add +30 minutes sleep for the next week.")
    if work_hours>10: tips.append("Try a hard ‘shutdown’ ritual to end the day.")
    if work_interfere in ["Sometimes","Often"]: tips.append("Set focus blocks with do-not-disturb.")
    if benefits in ["No","Don't know"]: tips.append("Ask HR about benefits and care options.")
    if coworkers=="No": tips.append("Find 1 trusted peer for check-ins.")
    if supervisor=="No": tips.append("Schedule a 1:1 to align expectations.")
    if stress>=7: tips.append("Try 5 minutes of guided breathing twice a day.")
    st.markdown("\n".join([f"- {t}" for t in tips]))
    st.caption("✅ Prediction used the trained model.")

st.markdown("</div>", unsafe_allow_html=True)

#====================================================================
# Records
#====================================================================
# Path for storing survey history data
HISTORY_PATH = "survey_history.csv"

if predict and risk_percent is not None:
    response_record = {
        "Age": age,
        "Gender": gender,
        "SelfEmployed": self_employed,
        "FamilyHistory": family_history,
        "WorkInterfere": work_interfere,
        "No_of_Employees": no_employees,
        "RemoteWork": remote_work,
        "TechCompany": tech_company,
        "Benefits": benefits,
        "CareOptions": care_options,
        "WellnessProgram": wellness_program,
        "SeekHelp": seek_help,
        "Anonymity": anonymity,
        "Leave": leave,
        "MHConsequence": mental_health_consequence,
        "PHConsequence": phys_health_consequence,
        "Coworkers": coworkers,
        "Supervisor": supervisor,
        "MHInterview": mental_health_interview,
        "PHInterview": phys_health_interview,
        "MHvsPH": mental_vs_physical,
        "ObsConsequence": obs_consequence,
        "WorkHours": work_hours,
        "SleepHours": sleep_hours,
        "StressLevel": stress,
        "model_used": "LogisticRegression" if model_used else "Unknown",
        "RiskProbability": round(risk_percent, 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Append to CSV
    if os.path.exists(HISTORY_PATH):
        old_df = pd.read_csv(HISTORY_PATH)
        new_df = pd.concat([old_df, pd.DataFrame([response_record])], ignore_index=True)
    else:
        new_df = pd.DataFrame([response_record])

    new_df.to_csv(HISTORY_PATH, index=False)
    st.success("✅ Your response has been saved!")

# Display Stored Records
if os.path.exists(HISTORY_PATH):
    st.markdown("### 📜 Survey History")
    history_df = pd.read_csv(HISTORY_PATH)
    st.dataframe(history_df.tail(10))  

# ===================================================================
# Footer Note
# ===================================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='glass' 
         style='color:#ffffff; font-weight:600; text-align:center;'>
        🧾 <span>This tool is used for project testing, not for medical advice.<br>
        If you’re in distress, please reach out to a qualified professional.</span>
    </div>
    """,
    unsafe_allow_html=True
)