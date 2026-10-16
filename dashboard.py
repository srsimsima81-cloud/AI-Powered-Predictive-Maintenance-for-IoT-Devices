
"""Premium futuristic dashboard for AI-powered predictive maintenance."""

from pathlib import Path

import streamlit as st
from src.predict import predict_one
from src.train import ROOT


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="PREMAINT | Predictive Intelligence",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# FUTURISTIC UI THEME
# --------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    :root {
        --bg: #070B12;
        --panel: #0D1420;
        --panel-2: #111C2B;
        --line: rgba(107, 194, 255, 0.17);
        --cyan: #62E8FF;
        --blue: #6595FF;
        --text: #EDF6FF;
        --muted: #8498AF;
        --green: #53F0B0;
        --amber: #FFC66D;
        --red: #FF6685;
    }

    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 15% 0%, rgba(25, 90, 145, 0.18), transparent 35%),
            radial-gradient(ellipse at 90% 15%, rgba(76, 48, 150, 0.12), transparent 32%),
            var(--bg);
        color: var(--text);
    }

    [data-testid="stHeader"] {
        background: rgba(7, 11, 18, 0.75);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0D1522 0%, #090E17 100%);
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] > div {
        padding-top: 1.6rem;
    }

    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] p {
        color: #C7D7E8 !important;
    }

    h1, h2, h3 {
        color: var(--text) !important;
        letter-spacing: -0.035em;
    }

    p, label {
        color: #C0D0E2;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .brand-row {
        display: flex;
        align-items: center;
        gap: 13px;
        margin-bottom: 7px;
    }

    .brand-icon {
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid rgba(98, 232, 255, 0.45);
        border-radius: 14px;
        background: linear-gradient(135deg, rgba(98,232,255,0.15), rgba(101,149,255,0.07));
        color: var(--cyan);
        font-size: 25px;
        box-shadow: 0 0 28px rgba(98,232,255,0.08);
    }

    .brand-name {
        font-size: 1.85rem;
        font-weight: 700;
        line-height: 1.05;
        color: #F1F8FF;
        letter-spacing: -0.055em;
    }

    .brand-name span {
        color: var(--cyan);
    }

    .eyebrow {
        font-family: 'DM Mono', monospace;
        text-transform: uppercase;
        font-size: 0.68rem;
        letter-spacing: 0.17em;
        color: var(--cyan);
    }

    .subtitle {
        color: var(--muted);
        font-size: 0.92rem;
        margin: 10px 0 25px;
    }

    .top-status {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        border: 1px solid rgba(83,240,176,0.23);
        border-radius: 999px;
        padding: 8px 12px;
        background: rgba(83,240,176,0.055);
        color: var(--green);
        font-family: 'DM Mono', monospace;
        font-size: 0.69rem;
        letter-spacing: 0.06em;
    }

    .status-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: var(--green);
        box-shadow: 0 0 10px rgba(83,240,176,0.8);
    }

    .section-label {
        font-family: 'DM Mono', monospace;
        color: var(--cyan);
        font-size: 0.72rem;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        margin: 1.1rem 0 0.8rem;
    }

    .panel {
        background: linear-gradient(145deg, rgba(17,28,43,0.96), rgba(10,17,28,0.96));
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 22px 23px;
        min-height: 142px;
        box-shadow: 0 12px 38px rgba(0,0,0,0.12);
    }

    .metric-label {
        color: var(--muted);
        font-size: 0.77rem;
        letter-spacing: 0.035em;
        margin-bottom: 15px;
    }

    .metric-value {
        font-family: 'DM Mono', monospace;
        font-size: clamp(1.6rem, 2.8vw, 2.35rem);
        font-weight: 500;
        line-height: 1.15;
        color: var(--text);
        overflow-wrap: anywhere;
    }

    .metric-foot {
        margin-top: 12px;
        color: #8096AD;
        font-size: 0.72rem;
    }

    .risk-panel {
        background: linear-gradient(130deg, rgba(19,37,55,0.97), rgba(11,17,28,0.98));
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: 25px;
        margin-top: 12px;
    }

    .risk-heading {
        font-size: 1.08rem;
        font-weight: 600;
        color: #F0F7FF;
    }

    .risk-number {
        font-family: 'DM Mono', monospace;
        font-size: clamp(2.5rem, 5vw, 4rem);
        line-height: 1.2;
        font-weight: 500;
        margin: 12px 0;
    }

    .risk-track {
        width: 100%;
        height: 8px;
        border-radius: 99px;
        background: #263548;
        overflow: hidden;
        margin: 15px 0;
    }

    .risk-fill {
        height: 100%;
        border-radius: 99px;
    }

    .risk-caption {
        color: var(--muted);
        font-size: 0.81rem;
        line-height: 1.65;
    }

    .alert-banner {
        border-radius: 14px;
        padding: 17px 19px;
        margin-top: 16px;
        border: 1px solid;
        font-weight: 600;
        line-height: 1.5;
    }

    .alert-high {
        color: #FF9CAF;
        border-color: rgba(255,102,133,0.35);
        background: rgba(255,102,133,0.085);
    }

    .alert-medium {
        color: #FFD48D;
        border-color: rgba(255,198,109,0.32);
        background: rgba(255,198,109,0.07);
    }

    .alert-low {
        color: #80F6C4;
        border-color: rgba(83,240,176,0.28);
        background: rgba(83,240,176,0.06);
    }

    .sensor-card {
        border: 1px solid var(--line);
        border-radius: 15px;
        padding: 17px;
        background: rgba(13,20,32,0.78);
        margin-bottom: 10px;
    }

    .sensor-name {
        color: var(--muted);
        font-size: 0.76rem;
        margin-bottom: 8px;
    }

    .sensor-value {
        font-family: 'DM Mono', monospace;
        font-size: 1.15rem;
        color: var(--text);
    }

    .sensor-unit {
        color: var(--cyan);
        font-size: 0.72rem;
    }

    div.stButton > button {
        width: 100%;
        min-height: 3.2rem;
        border: 1px solid rgba(98,232,255,0.5);
        border-radius: 12px;
        background: linear-gradient(105deg, #43CFEA, #6C9BFF);
        color: #06101A;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.96rem;
        font-weight: 700;
        box-shadow: 0 6px 24px rgba(63,184,238,0.14);
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        border-color: #A5F4FF;
        box-shadow: 0 0 28px rgba(98,232,255,0.23);
        transform: translateY(-1px);
        color: #06101A;
    }

    div[data-testid="stMetric"] {
        background: transparent;
    }

    [data-testid="stImage"] {
        border: 1px solid var(--line);
        border-radius: 13px;
        overflow: hidden;
        background: #0D1420;
        padding: 6px;
    }

    div[data-baseweb="slider"] > div {
        color: var(--cyan);
    }

    .disclaimer {
        border-top: 1px solid var(--line);
        margin-top: 32px;
        padding-top: 17px;
        color: #7589A0;
        font-size: 0.75rem;
        line-height: 1.7;
    }

    .mono {
        font-family: 'DM Mono', monospace;
    }

    @media (max-width: 700px) {
        .brand-name { font-size: 1.45rem; }
        .panel { padding: 17px; }
        .block-container { padding-top: 1rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# SIDEBAR — SENSOR CONTROL CENTER
# --------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div class="eyebrow">PREMAINT / CONTROL CENTER</div>
        <h2 style="margin-top:8px; font-size:1.35rem;">
            Sensor Inputs
        </h2>
        <p style="color:#8498AF;font-size:0.82rem;">
            Configure the simulated operating conditions.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-label">01 / Thermal system</div>',
                unsafe_allow_html=True)
    air = st.slider("Air temperature", 294.0, 306.0, 300.0, 0.5,
                    format="%.1f K")
    process = st.slider("Process temperature", 300.0, 320.0, 312.0, 0.5,
                        format="%.1f K")

    st.markdown('<div class="section-label">02 / Mechanical system</div>',
                unsafe_allow_html=True)
    rpm = st.slider("Rotational speed", 900, 2300, 1200, 10,
                    format="%d RPM")
    torque = st.slider("Torque", 5.0, 80.0, 65.0, 1.0,
                       format="%.1f Nm")
    wear = st.slider("Tool wear", 0, 250, 220, 5,
                     format="%d min")

    st.markdown('<div class="section-label">03 / Decision settings</div>',
                unsafe_allow_html=True)
    threshold = st.slider(
        "Classification threshold",
        min_value=0.1,
        max_value=0.9,
        value=0.5,
        step=0.05,
        format="%.2f",
        help="Changes the cutoff used to classify predicted failure risk.",
    )

    st.markdown("<br>", unsafe_allow_html=True)
    analyze = st.button("⚡  RUN DIAGNOSTIC", type="primary")

    st.markdown(
        """
        <div class="disclaimer">
            <span class="mono">SYSTEM MODE: SIMULATION</span><br>
            Inputs are simulated sensor values. This interface is an
            educational demonstration, not an industrial safety system.
        </div>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------
header_left, header_right = st.columns([3, 1])

with header_left:
    st.markdown(
        """
        <div class="brand-row">
            <div class="brand-icon">⌘</div>
            <div>
                <div class="eyebrow">INDUSTRIAL AI / CONDITION MONITORING</div>
                <div class="brand-name">PREMAINT <span>INTELLIGENCE</span></div>
            </div>
        </div>
        <div class="subtitle">
            Predictive maintenance · Machine health analytics · Risk estimation
        </div>
        """,
        unsafe_allow_html=True,
    )

with header_right:
    st.markdown(
        """
        <div style="text-align:right;padding-top:8px;">
            <div class="top-status">
                <span class="status-dot"></span>
                MODEL INTERFACE READY
            </div>
            <div style="color:#71869E;font-size:0.7rem;margin-top:9px;">
                OFFLINE INFERENCE / LOCAL MODEL
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    '<div class="section-label">01 / Diagnostic overview</div>',
    unsafe_allow_html=True,
)


# --------------------------------------------------
# SENSOR SNAPSHOT
# --------------------------------------------------
sensor_cols = st.columns(5)

sensor_data = [
    ("AIR TEMPERATURE", f"{air:.1f}", "K"),
    ("PROCESS TEMP.", f"{process:.1f}", "K"),
    ("ROTATIONAL SPEED", f"{rpm:,}", "RPM"),
    ("TORQUE", f"{torque:.1f}", "Nm"),
    ("TOOL WEAR", f"{wear}", "MIN"),
]

for col, (name, value, unit) in zip(sensor_cols, sensor_data):
    with col:
        st.markdown(
            f"""
            <div class="sensor-card">
                <div class="sensor-name">{name}</div>
                <div class="sensor-value">{value}</div>
                <div class="sensor-unit">{unit}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# --------------------------------------------------
# RUN MODEL ONLY WHEN REQUESTED
# --------------------------------------------------
if "diagnostic_result" not in st.session_state:
    st.session_state.diagnostic_result = None

if analyze:
    try:
        st.session_state.diagnostic_result = predict_one(
            air, process, rpm, torque, wear, threshold
        )
        st.session_state.diagnostic_inputs = {
            "air": air,
            "process": process,
            "rpm": rpm,
            "torque": torque,
            "wear": wear,
            "threshold": threshold,
        }
    except FileNotFoundError as exc:
        st.session_state.diagnostic_result = None
        st.error(
            f"Trained model not found: {exc}. "
            "Run `python main.py train` first."
        )


# --------------------------------------------------
# DIAGNOSTIC RESULTS
# --------------------------------------------------
result = st.session_state.diagnostic_result

if result is None:
    st.markdown(
        """
        <div class="risk-panel">
            <div class="eyebrow">SYSTEM STATUS / AWAITING ANALYSIS</div>
            <div class="risk-heading" style="margin-top:12px;">
                Ready to evaluate machine condition
            </div>
            <p class="risk-caption" style="margin-top:9px;">
                Configure the simulated sensor readings in the control center,
                then run a diagnostic to generate a model prediction.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    probability = float(result["failure_probability"])
    probability = max(0.0, min(1.0, probability))
    percent = probability * 100
    cutoff = float(threshold) * 100

    # Keep the risk classification consistent with the actual model threshold.
    is_failure = probability >= threshold

    if probability >= 0.70:
        risk_name = "HIGH RISK"
        risk_color = "#FF6685"
        alert_class = "alert-high"
    elif probability >= 0.40:
        risk_name = "MODERATE RISK"
        risk_color = "#FFC66D"
        alert_class = "alert-medium"
    else:
        risk_name = "LOWER ESTIMATED RISK"
        risk_color = "#53F0B0"
        alert_class = "alert-low"

    left, right = st.columns([1.15, 1], gap="large")

    with left:
        st.markdown(
            f"""
            <div class="risk-panel">
                <div class="eyebrow">MODEL OUTPUT / FAILURE CLASS</div>
                <div class="risk-number" style="color:{risk_color};">
                    {percent:.1f}%
                </div>
                <div class="risk-heading">Estimated failure probability</div>
                <div class="risk-track">
                    <div class="risk-fill"
                         style="width:{percent:.1f}%;background:{risk_color};">
                    </div>
                </div>
                <div class="risk-caption">
                    Model score: <span class="mono">{probability:.4f}</span>
                    &nbsp; / &nbsp;
                    Classification cutoff: <span class="mono">{cutoff:.0f}%</span>
                </div>
                <div class="alert-banner {alert_class}">
                    {risk_name} · {result["alert"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            '<div class="section-label">02 / Decision summary</div>',
            unsafe_allow_html=True,
        )

        metric_cols = st.columns(2)

        with metric_cols[0]:
            st.markdown(
                f"""
                <div class="panel">
                    <div class="metric-label">PREDICTED CLASS</div>
                    <div class="metric-value"
                         style="font-size:1.4rem;color:{risk_color};">
                        {"FAILURE" if is_failure else "NO FAILURE"}
                    </div>
                    <div class="metric-foot">Binary model output</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with metric_cols[1]:
            st.markdown(
                f"""
                <div class="panel">
                    <div class="metric-label">THRESHOLD</div>
                    <div class="metric-value">{cutoff:.0f}%</div>
                    <div class="metric-foot">Classification cutoff</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        if is_failure:
            st.warning(
                "The estimated probability meets or exceeds the selected "
                "classification threshold."
            )
        else:
            st.success(
                "The estimated probability is below the selected "
                "classification threshold."
            )

        st.caption(
            "This classification is based on the configured threshold. "
            "The visual risk band is a separate display convention."
        )

    with st.expander("Inspect prediction payload"):
        st.json(result)

    with st.expander("Review the inputs used for this prediction"):
        st.write(st.session_state.get("diagnostic_inputs", {}))


# --------------------------------------------------
# MODEL EVIDENCE
# --------------------------------------------------
st.markdown("---")
st.markdown(
    '<div class="section-label">03 / Model evidence</div>',
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='margin-top:0;'>Training & evaluation visuals</h3>",
    unsafe_allow_html=True,
)
st.caption(
    "Generated from the held-out evaluation workflow. "
    "These plots describe the current dataset and model run."
)

evidence = [
    ("failure_distribution.png", "01 — Failure label distribution"),
    ("risk_predictions.png", "02 — Predicted risk vs actual labels"),
    ("confusion_matrix.png", "03 — Confusion matrix"),
]

available_evidence = []

for filename, title in evidence:
    path = ROOT / "images" / filename
    if path.exists():
        available_evidence.append((path, title))

if available_evidence:
    evidence_cols = st.columns(len(available_evidence))

    for col, (path, title) in zip(evidence_cols, available_evidence):
        with col:
            st.markdown(
                f"<div class='metric-label'>{title.upper()}</div>",
                unsafe_allow_html=True,
            )
            st.image(str(path), use_container_width=True)
else:
    st.info("No evaluation plots found. Run `python main.py train` first.")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    """
    <div class="disclaimer">
        <span class="mono">PREMAINT AI / EDUCATIONAL BUILD</span><br>
        This application uses simulated sensor data and a machine-learning
        model for demonstration purposes. Probability estimates are not
        calibrated or validated industrial failure probabilities.
        Do not use this dashboard to make real-world safety decisions.
    </div>
    """,
    unsafe_allow_html=True,
)
