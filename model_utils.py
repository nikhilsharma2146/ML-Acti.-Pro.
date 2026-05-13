from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

def get_model(name, params):
    if name == "Logistic Regression":
        return LogisticRegression(C=params["C"], max_iter=params["max_iter"], random_state=42)
    elif name == "Decision Tree":
        return DecisionTreeClassifier(max_depth=params["max_depth"], min_samples_split=params["min_samples_split"], random_state=42)
    elif name == "Random Forest":
        return RandomForestClassifier(n_estimators=params["n_estimators"], max_depth=params["max_depth"], random_state=42)
    elif name == "KNN":
        return KNeighborsClassifier(n_neighbors=params["n_neighbors"], weights=params["weights"])

use_cases = {
    "Logistic Regression": {
        "emoji": "📧", "title": "Spam Detection = Blocking Cringe DMs 🚫",
        "desc": "Jaise Instagram pe cringe DMs filter hote hain — Logistic Regression spam ya not-spam classify karta hai. Simple, fast, aur effective! Jab koi 'Send bobs' type msg aaye, model bole — BLOCK! 😤🔒",
        "examples": ["Email spam filtering", "Fake account detection", "Ad click prediction"]
    },
    "Decision Tree": {
        "emoji": "🎮", "title": "Game Recommendation = Netflix Suggestions for Gamers 🕹️",
        "desc": "Decision Tree aise kaam karta hai jaise tum decisions lete ho — 'Kya mujhe FPS pasand hai? Haan → Call of Duty. Nahi → Minecraft.' Simple if-else tree! Like a flowchart of your vibe 🌊",
        "examples": ["Loan approval systems", "Medical diagnosis", "Customer segmentation"]
    },
    "Random Forest": {
        "emoji": "🏦", "title": "Fraud Detection = Catching Sus Transactions 🕵️",
        "desc": "Random Forest bohot saare Decision Trees ka group hai — jaise group study mein sabki opinion lo aur best answer chuno. Banking mein fraud detect karne ke liye use hota hai. Sus transaction? CAUGHT! 🚨",
        "examples": ["Credit card fraud", "Stock market prediction", "Image classification"]
    },
    "KNN": {
        "emoji": "👥", "title": "Friend Suggestions = 'People You May Know' Feature 🤝",
        "desc": "KNN dekhta hai tumhare nearest neighbors kaun hain — matlab tumse similar log. Instagram/Facebook ka 'People You May Know' basically KNN hi hai! Birds of a feather flock together 🐦",
        "examples": ["Recommendation systems", "Handwriting recognition", "Customer profiling"]
    }
}

model_descriptions = {
    "Logistic Regression": "Fast, simple, classic. Like a basic white tee — always works! 👕",
    "Decision Tree": "Logical flowchart vibes. Decisions like 'Should I reply to this text?' 📱",
    "Random Forest": "Squad goals! Group of trees making decisions together. 🌲🌲🌲",
    "KNN": "Vibe check! Finds people with similar energy/neighbors. 👥✨"
}
