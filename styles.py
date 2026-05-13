import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800;900&display=swap');
    :root { --bg: #0f0f1a; --accent: #00ffe0; --accent2: #ff6ec7; --accent3: #a855f7; --card: #1a1a2e; --text: #e0e0e0; }
    
    /* ── KEYFRAME ANIMATIONS ── */
    @keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-12px)} }
    @keyframes pulse-glow { 0%,100%{box-shadow:0 0 15px #00ffe022,0 0 30px #00ffe011} 50%{box-shadow:0 0 25px #00ffe044,0 0 50px #00ffe022} }
    @keyframes gradient-shift { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }
    @keyframes fade-slide-up { from{opacity:0;transform:translateY(30px)} to{opacity:1;transform:translateY(0)} }
    @keyframes shimmer { 0%{background-position:-200% 0} 100%{background-position:200% 0} }
    @keyframes border-glow { 0%,100%{border-color:#00ffe033} 50%{border-color:#00ffe088} }
    @keyframes breathe { 0%,100%{opacity:0.6} 50%{opacity:1} }
    @keyframes neon-flicker { 0%,19%,21%,23%,25%,54%,56%,100%{text-shadow:0 0 10px #00ffe0,0 0 40px #00ffe066,0 0 80px #00ffe033} 20%,24%,55%{text-shadow:none} }
    @keyframes orb-float-1 { 0%{transform:translate(0,0) scale(1)} 33%{transform:translate(30px,-40px) scale(1.1)} 66%{transform:translate(-20px,20px) scale(0.9)} 100%{transform:translate(0,0) scale(1)} }
    @keyframes orb-float-2 { 0%{transform:translate(0,0) scale(1)} 33%{transform:translate(-40px,30px) scale(0.9)} 66%{transform:translate(25px,-25px) scale(1.1)} 100%{transform:translate(0,0) scale(1)} }
    @keyframes scanner { 0%{top:-5%} 100%{top:105%} }
    @keyframes spin-slow { 0%{transform:rotate(0deg)} 100%{transform:rotate(360deg)} }
    @keyframes count-up { from{opacity:0;transform:scale(0.5)} to{opacity:1;transform:scale(1)} }
    
    /* ── MAIN APP ── */
    .stApp { background: var(--bg); color: var(--text); font-family: 'Outfit', sans-serif; }
    
    /* ── FLOATING ORBS BACKGROUND ── */
    .orb-container { position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:0; overflow:hidden; }
    .orb { position:absolute; border-radius:50%; filter:blur(80px); opacity:0.15; }
    .orb-1 { width:400px; height:400px; background:radial-gradient(circle,#00ffe0,transparent); top:10%; left:5%; animation:orb-float-1 15s ease-in-out infinite; }
    .orb-2 { width:350px; height:350px; background:radial-gradient(circle,#ff6ec7,transparent); top:50%; right:5%; animation:orb-float-2 18s ease-in-out infinite; }
    .orb-3 { width:300px; height:300px; background:radial-gradient(circle,#a855f7,transparent); bottom:10%; left:40%; animation:orb-float-1 20s ease-in-out infinite reverse; }
    
    /* ── SIDEBAR ── */
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0a0a18 0%, #141428 50%, #1a1a2e 100%) !important;
        border-right: 2px solid transparent; border-image: linear-gradient(180deg,#00ffe0,#ff6ec7,#a855f7) 1;
        animation: border-glow 3s ease-in-out infinite; }
    [data-testid="stSidebar"]::before { content:''; position:absolute; top:0; left:0; right:0; height:2px;
        background:linear-gradient(90deg,transparent,#00ffe0,#ff6ec7,transparent); animation:shimmer 3s linear infinite; background-size:200% 100%; }
    [data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] label,[data-testid="stSidebar"] p,[data-testid="stSidebar"] span { color: #e0e0e0 !important; }
    
    /* ── HEADINGS ── */
    h1,h2,h3,h4 { color: var(--accent) !important; text-shadow: 0 0 20px #00ffe044; animation: fade-slide-up 0.6s ease-out; }
    
    /* ── METRIC CARDS ── */
    .stMetric { background: linear-gradient(135deg, #1a1a2e, #16213e, #1a1a2e) !important; background-size:200% 200% !important;
        border: 1px solid #00ffe033; border-radius: 20px !important; padding: 20px !important;
        animation: pulse-glow 3s ease-in-out infinite, fade-slide-up 0.8s ease-out, gradient-shift 6s ease infinite;
        transition: all 0.4s cubic-bezier(0.175,0.885,0.32,1.275) !important; position:relative; overflow:hidden; }
    .stMetric:hover { transform: translateY(-6px) scale(1.03) !important; border-color: #00ffe088 !important;
        box-shadow: 0 10px 40px #00ffe033, 0 0 60px #00ffe011 !important; }
    .stMetric::after { content:''; position:absolute; top:-50%; left:-50%; width:200%; height:200%;
        background:linear-gradient(45deg,transparent 40%,rgba(0,255,224,0.03) 50%,transparent 60%);
        animation:spin-slow 8s linear infinite; pointer-events:none; }
    [data-testid="stMetricValue"] { color: var(--accent) !important; font-size: 2.2rem !important; font-weight: 800 !important;
        animation: count-up 0.6s ease-out; }
    [data-testid="stMetricLabel"] { color: #aaa !important; font-size: 0.9rem !important; text-transform: uppercase; letter-spacing: 1px; }
    
    /* ── EXPANDERS ── */
    div[data-testid="stExpander"] { background: linear-gradient(135deg,#1a1a2e,#16213e) !important;
        border: 1px solid #00ffe022; border-radius: 16px !important; transition: all 0.3s ease;
        animation: fade-slide-up 0.7s ease-out; }
    div[data-testid="stExpander"]:hover { border-color: #00ffe055; box-shadow: 0 4px 20px #00ffe011; }
    
    /* ── INFO BLOCKS ── */
    .stInfo, div[data-testid="stNotification"] { background: linear-gradient(135deg,#16213e,#1a1a3a) !important;
        color: #e0e0e0 !important; border-left: 4px solid var(--accent) !important; border-radius: 12px !important;
        animation: fade-slide-up 0.5s ease-out; transition: all 0.3s ease; }
    
    /* ── SUCCESS BLOCKS ── */
    div[data-testid="stAlert"] { border-radius: 12px !important; animation: fade-slide-up 0.5s ease-out; }
    
    /* ── TITLE STYLES ── */
    .glow-title { text-align:center; font-size:3.2rem; font-weight:900; letter-spacing:-1px;
        background: linear-gradient(135deg,#00ffe0,#38bdf8,#a855f7,#ff6ec7,#00ffe0); background-size:300% 300%;
        -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
        animation: gradient-shift 4s ease infinite; margin-bottom:0; filter:drop-shadow(0 0 30px #00ffe033); }
    .sub-title { text-align:center; color:#ff6ec7; font-size:1.2rem; margin-top:4px; letter-spacing:0.5px;
        animation: fade-slide-up 0.8s ease-out, breathe 4s ease-in-out infinite; }
    
    /* ── SECTION DIVIDERS ── */
    .section-divider { height:2px; border:none; margin:2rem 0;
        background:linear-gradient(90deg,transparent,#00ffe044,#ff6ec744,#a855f744,transparent); }
    
    /* ── PLOTLY CHART CONTAINERS ── */
    [data-testid="stPlotlyChart"] { animation: fade-slide-up 0.7s ease-out; border-radius:16px; overflow:hidden;
        transition:all 0.3s ease; }
    [data-testid="stPlotlyChart"]:hover { box-shadow: 0 0 30px #00ffe011; }
    
    /* ── BUTTONS ── */
    div.stButton > button { background:linear-gradient(135deg,#00ffe0,#00b4d8,#a855f7); background-size:200% 200%;
        color:#0f0f1a; font-weight:700; border:none; border-radius:14px; padding:10px 28px;
        transition:all 0.4s cubic-bezier(0.175,0.885,0.32,1.275); animation:gradient-shift 3s ease infinite;
        text-transform:uppercase; letter-spacing:1px; }
    div.stButton > button:hover { box-shadow:0 0 30px #00ffe066,0 0 60px #00ffe022; transform:translateY(-3px) scale(1.05); }
    
    /* ── SLIDER STYLING ── */
    [data-testid="stSlider"] { animation: fade-slide-up 0.5s ease-out; }
    
    /* ── SCROLLBAR ── */
    ::-webkit-scrollbar { width:6px; }
    ::-webkit-scrollbar-track { background:#0f0f1a; }
    ::-webkit-scrollbar-thumb { background:linear-gradient(180deg,#00ffe0,#a855f7); border-radius:3px; }
    ::-webkit-scrollbar-thumb:hover { background:linear-gradient(180deg,#00ffe0,#ff6ec7); }
    
    /* ── GLASSMORPHISM HEADER BAR ── */
    .glass-header { background:rgba(15,15,26,0.6); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px);
        border:1px solid rgba(0,255,224,0.1); border-radius:24px; padding:2rem 2rem 1.5rem; margin-bottom:1.5rem;
        text-align:center; animation:fade-slide-up 0.5s ease-out; position:relative; overflow:hidden; }
    .glass-header::before { content:''; position:absolute; top:0; left:-100%; width:300%; height:2px;
        background:linear-gradient(90deg,transparent,#00ffe0,#ff6ec7,#a855f7,transparent);
        animation:shimmer 4s linear infinite; background-size:200% 100%; }
    .glass-header::after { content:''; position:absolute; bottom:0; left:-100%; width:300%; height:1px;
        background:linear-gradient(90deg,transparent,#a855f7,#ff6ec7,#00ffe0,transparent);
        animation:shimmer 4s linear infinite reverse; background-size:200% 100%; }
    
    /* ── USE CASE CARDS ── */
    .use-case-card { background:linear-gradient(135deg,#1a1a2e,#16213e); border:1px solid #00ffe022;
        border-radius:20px; padding:1.5rem; animation:fade-slide-up 0.6s ease-out;
        transition:all 0.4s cubic-bezier(0.175,0.885,0.32,1.275); position:relative; overflow:hidden; }
    .use-case-card:hover { transform:translateY(-4px); border-color:#00ffe055; box-shadow:0 8px 32px #00ffe022; }
    .use-case-card::before { content:''; position:absolute; top:0; left:0; right:0; height:3px;
        background:linear-gradient(90deg,#00ffe0,#ff6ec7,#a855f7); }
    
    /* ── ANIMATED BADGE ── */
    .model-badge { display:inline-block; background:linear-gradient(135deg,#00ffe0,#00b4d8); color:#0f0f1a;
        padding:6px 18px; border-radius:50px; font-weight:700; font-size:0.85rem; text-transform:uppercase;
        letter-spacing:1.5px; animation:pulse-glow 2s ease-in-out infinite; margin:0.5rem 0; }
    
    /* ── STAT PILL ── */
    .stat-pill { display:inline-block; background:rgba(0,255,224,0.08); border:1px solid #00ffe033;
        border-radius:50px; padding:4px 14px; margin:2px; font-size:0.8rem; color:#00ffe0;
        animation:fade-slide-up 0.5s ease-out; transition:all 0.3s; }
    .stat-pill:hover { background:rgba(0,255,224,0.15); border-color:#00ffe066; }
    </style>
    """, unsafe_allow_html=True)
    
    # ── Inject floating orbs HTML ──
    st.markdown("""
    <div class="orb-container">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="orb orb-3"></div>
    </div>
    """, unsafe_allow_html=True)

PLOT_BG = "#0f0f1a"
PAPER_BG = "#0f0f1a"
ACCENT = "#00ffe0"
ACCENT2 = "#ff6ec7"
NEON_COLORS = ["#00ffe0", "#ff6ec7", "#a855f7", "#facc15", "#38bdf8", "#fb923c"]

def style_fig(fig):
    fig.update_layout(
        paper_bgcolor=PAPER_BG, plot_bgcolor=PLOT_BG,
        font=dict(family="Outfit", color="#e0e0e0"),
        title_font=dict(color=ACCENT, size=18),
        legend=dict(bgcolor="#1a1a2e", bordercolor="rgba(0,255,224,0.2)"),
        xaxis=dict(gridcolor="rgba(255,255,255,0.07)", zerolinecolor="rgba(255,255,255,0.13)"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.07)", zerolinecolor="rgba(255,255,255,0.13)"),
        margin=dict(l=40, r=40, t=50, b=40),
    )
    return fig
