import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, roc_curve, auc)
from sklearn.preprocessing import StandardScaler
import warnings
import joblib
import io
warnings.filterwarnings("ignore")

from styles import apply_custom_styles, style_fig, ACCENT, ACCENT2
from data_utils import generate_data
from model_utils import get_model, use_cases, model_descriptions

# ──────────────────── PAGE CONFIG ────────────────────
st.set_page_config(page_title="ML Gen Z Dashboard 🧠⚡", page_icon="🧠", layout="wide")

# Apply custom styles and theme
apply_custom_styles()

# ──────────────────── SIDEBAR ────────────────────
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🎮 Control Panel</h2>", unsafe_allow_html=True)
    st.markdown("---")

    with st.expander("ℹ️ About This App", expanded=False):
        st.markdown("""
        **ML Gen Z Dashboard** 🧠⚡

        Yeh app tumhe Machine Learning sikhata hai
        bilkul chill way mein! 🔥

        - 🎛️ Dataset khud bana sakte ho
        - 🤖 4 alag models try kar sakte ho
        - 📊 Sab kuch visual hai — no boring theory
        - 🗣️ Hinglish mein explanations

        Made with 💚 for Gen Z learners
        """)

    st.markdown("### 📊 Dataset Settings")
    n_samples = st.slider("📦 Samples kitne chahiye?", 100, 2000, 500, 50)
    n_features = st.slider("🔢 Features kitne?", 2, 20, 5)
    noise = st.slider("🌀 Noise Level (flip_y)", 0.0, 0.5, 0.1, 0.05)
    test_size = st.slider("✂️ Test Split %", 10, 50, 20, 5)

    st.markdown("---")
    st.markdown("### 🤖 Model Selection")
    model_name = st.selectbox("Model chuno:", [
        "Logistic Regression", "Decision Tree", "Random Forest", "KNN"
    ])

    st.markdown("### ⚙️ Hyperparameters")
    model_params = {}
    if model_name == "Logistic Regression":
        model_params["C"] = st.slider("C (Regularization)", 0.01, 10.0, 1.0, 0.01)
        model_params["max_iter"] = st.slider("Max Iterations", 100, 1000, 200, 50)
    elif model_name == "Decision Tree":
        model_params["max_depth"] = st.slider("Max Depth 🌳", 1, 30, 5)
        model_params["min_samples_split"] = st.slider("Min Samples Split", 2, 20, 2)
    elif model_name == "Random Forest":
        model_params["n_estimators"] = st.slider("Trees 🌲", 10, 300, 100, 10)
        model_params["max_depth"] = st.slider("Max Depth 🌳", 1, 30, 10)
    elif model_name == "KNN":
        model_params["n_neighbors"] = st.slider("Neighbors (K) 👥", 1, 30, 5)
        model_params["weights"] = st.selectbox("Weights", ["uniform", "distance"])

# ──────────────────── HEADER ────────────────────
st.markdown(f'''
<div class="glass-header">
    <p class="glow-title">🧠 ML Gen Z Dashboard ⚡</p>
    <p class="sub-title">Machine Learning seekho — apni style mein 🔥💅</p>
</div>
''', unsafe_allow_html=True)

# ── Interactive Header Buttons ──
st.markdown('<div class="header-btn-container">', unsafe_allow_html=True)
c_main, c1, c2, c3, c4 = st.columns([2, 1, 1, 1, 1])

with c_main:
    st.markdown('<div class="model-badge-container">', unsafe_allow_html=True)
    if st.button(f"🤖 {model_name}"):
        st.toast(f"🤖 {model_name} is active! Check out the use cases below. 🔥")
    st.markdown('</div>', unsafe_allow_html=True)

with c1:
    if st.button(f"📦 {n_samples} samples"):
        st.toast("📦 Dataset size updated! Fresh data vibes. ✨")
with c2:
    if st.button(f"🔢 {n_features} features"):
        st.toast("🔢 More features = more complexity. Big brain time! 🧠")
with c3:
    if st.button(f"🌀 {noise} noise"):
        st.toast("🌀 Noise level set. Stay focused! 🌊")
with c4:
    if st.button(f"✂️ {test_size}% test"):
        st.toast("✂️ Train/Test split updated. Vibe check coming up! 💅")
st.markdown('</div>', unsafe_allow_html=True)

# ──────────────────── DATA GEN ────────────────────
df, X, y = generate_data(n_samples, n_features, noise)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size / 100, random_state=42)

# ──────────────────── HINGLISH CONCEPTS ────────────────────
with st.expander("📚 ML Concepts — Hinglish Mein Samjho! 🗣️🔥", expanded=False):
    c1, c2 = st.columns(2)
    with c1:
        st.info("🎯 **Classification kya hai?** \nSocho tumhare paas photos hain — kuch mein cats hain, kuch mein dogs. Model sikhta hai ki kaunsi photo kis category mein jaayegi. Bilkul swipe left/right jaisa! 💅")
        st.info("✂️ **Train/Test Split kya hai?** \nJaise exam se pehle practice karte ho (training), aur phir actual exam dete ho (testing). Model bhi aise hi seekhta hai! 📝")
        st.info("📊 **Confusion Matrix kya hai?** \nYeh batata hai model kitni baar sahi guess kiya aur kitni baar galat. Jaise score card — but ML waala! 🏏")
    with c2:
        st.info("📈 **ROC Curve kya hai?** \nYeh graph dikhata hai ki model kitna acha distinguish kar raha hai classes ke beech. Jitna zyada curve upar, utna better model! Top-left corner = *chef's kiss* 👨‍🍳")
        st.info("🌟 **Feature Importance kya hai?** \nYeh batata hai kaunsa feature sabse zyada kaam ka hai prediction mein. Jaise cricket mein — batting average sabse important stat hota hai na! 🏏")
        st.info("🎯 **Accuracy vs F1 Score?** \nAccuracy = overall kitne sahi the. F1 = precision aur recall ka balance. Jab data imbalanced ho, F1 zyada reliable hai. Like CGPA vs individual marks! 📊")

# ──────────────────── SCATTER + TRAIN/TEST ────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown("## 📊 Data Visualization")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔮 Raw Data Scatter Plot")
    fig_scatter = px.scatter(
        df, x="Feature_1", y="Feature_2", color=df["Target"].astype(str),
        color_discrete_sequence=[ACCENT, ACCENT2],
        title="Feature 1 vs Feature 2 (colored by Target)",
        labels={"color": "Class"}, opacity=0.7
    )
    style_fig(fig_scatter)
    fig_scatter.update_traces(marker=dict(size=6, line=dict(width=0.5, color="rgba(255,255,255,0.2)")))
    st.plotly_chart(fig_scatter, width='stretch')

with col2:
    st.markdown("### ✂️ Train / Test Split")
    split_df = pd.DataFrame({
        "Feature_1": np.concatenate([X_train[:, 0], X_test[:, 0]]),
        "Feature_2": np.concatenate([X_train[:, 1], X_test[:, 1]]),
        "Set": ["Train"] * len(X_train) + ["Test"] * len(X_test)
    })
    fig_split = px.scatter(
        split_df, x="Feature_1", y="Feature_2", color="Set",
        color_discrete_map={"Train": ACCENT, "Test": ACCENT2},
        title=f"Train ({len(X_train)}) vs Test ({len(X_test)})", opacity=0.7
    )
    style_fig(fig_split)
    fig_split.update_traces(marker=dict(size=6, line=dict(width=0.5, color="rgba(255,255,255,0.2)")))
    st.plotly_chart(fig_split, width='stretch')

# ──────────────────── MODEL TRAINING ────────────────────
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model = get_model(model_name, model_params)
model.fit(X_train_s, y_train)
y_pred = model.predict(X_test_s)
y_prob = model.predict_proba(X_test_s)[:, 1] if hasattr(model, "predict_proba") else np.zeros(len(y_test))

acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, zero_division=0)
rec = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

# ──────────────────── METRICS ────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown("## 🏆 Model Performance")
m1, m2, m3, m4 = st.columns(4)
m1.metric("🎯 Accuracy", f"{acc:.2%}")
m2.metric("🔬 Precision", f"{prec:.2%}")
m3.metric("📡 Recall", f"{rec:.2%}")
m4.metric("⚖️ F1 Score", f"{f1:.2%}")

if acc > 0.90:
    st.success("🎉 Broo! 90%+ accuracy — model ne full send kar diya! 🚀🔥")

# ──────────────────── EXPORT & SAVE ────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown("## 💾 Export & Save")
ex1, ex2 = st.columns(2)

with ex1:
    # Model download
    model_buffer = io.BytesIO()
    joblib.dump(model, model_buffer)
    st.download_button(
        label=f"📥 Download {model_name} Model",
        data=model_buffer.getvalue(),
        file_name=f"{model_name.lower().replace(' ', '_')}_model.joblib",
        mime="application/octet-stream",
        help="Download the trained model to use in your own projects! 🚀"
    )

with ex2:
    # Dataset download
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📊 Download Dataset (CSV)",
        data=csv,
        file_name="genz_ml_dataset.csv",
        mime="text/csv",
        help="Take your data with you! 💅"
    )

# ──────────────────── CONFUSION + ROC ────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown("## 📈 Detailed Analysis")
col3, col4 = st.columns(2)

with col3:
    st.markdown("### 🧩 Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    fig_cm = px.imshow(
        cm, text_auto=True, color_continuous_scale=[[0, "#0f0f1a"], [0.5, "#00b4d8"], [1, "#00ffe0"]],
        labels=dict(x="Predicted", y="Actual", color="Count"),
        x=["Class 0", "Class 1"], y=["Class 0", "Class 1"],
        title="Confusion Matrix Heatmap"
    )
    style_fig(fig_cm)
    fig_cm.update_layout(coloraxis_colorbar=dict(title="Count"))
    st.plotly_chart(fig_cm, width='stretch')
    st.info("🧩 **Confusion Matrix samjho:** Diagonal pe jitne zyada numbers = utna acha model. Off-diagonal = model ne galti ki. Jaise exam mein — sahi answers diagonal pe! ✅")

with col4:
    st.markdown("### 📈 ROC Curve")
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    fig_roc = go.Figure()
    fig_roc.add_trace(go.Scatter(x=fpr, y=tpr, mode="lines", name=f"ROC (AUC={roc_auc:.3f})",
                                  line=dict(color=ACCENT, width=3)))
    fig_roc.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines", name="Random",
                                  line=dict(color="rgba(255,255,255,0.2)", dash="dash", width=1)))
    fig_roc.update_layout(title=f"ROC Curve (AUC = {roc_auc:.3f})",
                          xaxis_title="False Positive Rate", yaxis_title="True Positive Rate")
    style_fig(fig_roc)
    fig_roc.update_traces(fill="tozeroy", selector=dict(name=f"ROC (AUC={roc_auc:.3f})"),
                          fillcolor="rgba(0,255,224,0.1)")
    st.plotly_chart(fig_roc, width='stretch')
    st.info("📈 **ROC Curve tip:** AUC = 1.0 matlab perfect model, 0.5 matlab random guess jaise coin flip. Apna model kahan hai? Check karo! 🪙")

# ──────────────────── FEATURE IMPORTANCE ────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown("## 🌟 Feature Importance")
feature_names = [f"Feature_{i+1}" for i in range(n_features)]

if model_name in ["Decision Tree", "Random Forest"]:
    importances = model.feature_importances_
elif model_name == "Logistic Regression":
    importances = np.abs(model.coef_[0])
else:
    from sklearn.inspection import permutation_importance
    perm = permutation_importance(model, X_test_s, y_test, n_repeats=10, random_state=42)
    importances = perm.importances_mean

imp_df = pd.DataFrame({"Feature": feature_names, "Importance": importances})
imp_df = imp_df.sort_values("Importance", ascending=True)

fig_imp = px.bar(
    imp_df, x="Importance", y="Feature", orientation="h",
    color="Importance", color_continuous_scale=[[0, "#1a1a2e"], [0.5, "#00b4d8"], [1, "#00ffe0"]],
    title=f"Feature Importance — {model_name}"
)
style_fig(fig_imp)
fig_imp.update_layout(showlegend=False, height=max(350, n_features * 35))
st.plotly_chart(fig_imp, width='stretch')

with st.expander("🤔 Feature Importance kya bata raha hai?"):
    st.info("🌟 **Top features = MVP players!** Jaise cricket team mein sabse important player hota hai, waise hi model ke liye sabse important features hote hain. Baaki features bench warmers hain! 🏏😂")

# ──────────────────── REAL LIFE USE CASES ────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown("## 🌍 Real Life Use Cases — Gen Z Edition")

uc = use_cases[model_name]
example_pills = ''.join([f'<span class="stat-pill">✅ {ex}</span>' for ex in uc['examples']])
st.markdown(f'''
<div class="use-case-card">
    <h3 style="margin-top:0;color:#00ffe0!important;">{uc["emoji"]} {uc["title"]}</h3>
    <p style="color:#ccc;font-size:1.05rem;line-height:1.7;">💡 <strong>{model_name} Real Life Mein:</strong><br>{uc["desc"]}</p>
    <div style="margin-top:12px;">{example_pills}</div>
</div>
''', unsafe_allow_html=True)

st.markdown("---")
with st.expander("🔥 Sabhi Models ke Use Cases Dekho!"):
    for name, info in use_cases.items():
        icon = "👉" if name == model_name else "  "
        st.markdown(f"**{icon} {info['emoji']} {name}:** {info['title']}")
        st.caption(info['desc'])
        st.markdown("")

# ──────────────────── MODEL SHOWDOWN ────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown("## 🏁 Model Showdown — Kaun Jeetega?")

if st.button("🚀 Sabhi Models Compare Karo!"):
    results = []
    names = ["Logistic Regression", "Decision Tree", "Random Forest", "KNN"]
    
    progress_bar = st.progress(0)
    for i, name in enumerate(names):
        # Default params for comparison
        if name == "Logistic Regression": params = {"C": 1.0, "max_iter": 100}
        elif name == "Decision Tree": params = {"max_depth": 10, "min_samples_split": 2}
        elif name == "Random Forest": params = {"n_estimators": 100, "max_depth": 10}
        elif name == "KNN": params = {"n_neighbors": 5, "weights": "uniform"}
        
        m = get_model(name, params)
        m.fit(X_train_s, y_train)
        preds = m.predict(X_test_s)
        
        results.append({
            "Model": name,
            "Vibe Check (Acc)": f"{accuracy_score(y_test, preds):.2%}",
            "Precision": f"{precision_score(y_test, preds, zero_division=0):.2%}",
            "F1 Score": f"{f1_score(y_test, preds, zero_division=0):.2%}",
            "Description": model_descriptions[name]
        })
        progress_bar.progress((i + 1) / len(names))
    
    comparison_df = pd.DataFrame(results)
    st.table(comparison_df)
    st.success("🔥 Comparison done! Choose the one with the best vibe for your data. 💅")

# ──────────────────── FOOTER ────────────────────
st.markdown('''
<hr class="section-divider">
<div style="text-align:center;padding:1.5rem 0;">
    <p style="color:#555;font-size:0.85rem;margin:0;">Built with 💚 by Gen Z for Gen Z</p>
    <p style="margin:4px 0 0;">
        <span class="stat-pill">Streamlit</span>
        <span class="stat-pill">Scikit-Learn</span>
        <span class="stat-pill">Plotly</span>
        <span class="stat-pill">2026</span>
    </p>
</div>
''', unsafe_allow_html=True)
