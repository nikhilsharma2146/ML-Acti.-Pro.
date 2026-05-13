import streamlit as st
import pandas as pd
from sklearn.datasets import make_classification

@st.cache_data
def generate_data(n_samples, n_features, noise, seed=42):
    X, y = make_classification(
        n_samples=n_samples, n_features=n_features, n_informative=max(2, n_features // 2),
        n_redundant=max(1, n_features // 4), n_classes=2, flip_y=noise, random_state=seed
    )
    cols = [f"Feature_{i+1}" for i in range(n_features)]
    df = pd.DataFrame(X, columns=cols)
    df["Target"] = y
    return df, X, y
