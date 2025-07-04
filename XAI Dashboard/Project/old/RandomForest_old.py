import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.utils.multiclass import unique_labels
import os
import joblib

from config import MODEL_PATH, DB_PATH_PL_DIR, DB_PATH_ALL
from utils import load_data

# ---------- Configurazione Streamlit ----------
st.set_page_config(page_title="PL_DIR Random Forest", layout="wide")
st.title("🌲 Random Forest Classifier su PL_ e DIR_")


# ---------- Funzioni ----------

def split_features_and_target(df, target_col='LABEL'):
    if target_col not in df.columns:
        st.error(f"❌ Colonna '{target_col}' non trovata.")
        st.stop()
    return df.drop(columns=[target_col]), df[target_col]

def train_model(X_train, y_train):
    clf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    clf.fit(X_train, y_train)
    joblib.dump(clf, MODEL_PATH)
    return clf

def load_or_train_model(X_train, y_train, retrain=False):
    if os.path.exists(MODEL_PATH) and not retrain:
        st.info("✅ Modello caricato da file.")
        return joblib.load(MODEL_PATH)
    st.info("🔁 Addestramento modello in corso...")
    return train_model(X_train, y_train)

def show_classification_report(y_test, y_pred):
    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose().round(2)

    st.markdown("### 📋 Classification Report per Classe")
    per_class = report_df.drop(index=["accuracy", "macro avg", "weighted avg"])
    st.dataframe(per_class.style.background_gradient(subset=["precision", "recall", "f1-score"], cmap="Greens"))

    st.markdown("### 📊 Macro e Weighted Averages")
    aggregates = report_df.loc[["accuracy", "macro avg", "weighted avg"]]
    st.dataframe(aggregates.style.background_gradient(cmap="Oranges", axis=None))

def show_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    labels = unique_labels(y_test, y_pred)
    cm_df = pd.DataFrame(cm, index=[f"True {l}" for l in labels], columns=[f"Pred {l}" for l in labels])
    st.markdown("### 📊 Confusion Matrix")
    st.dataframe(cm_df.style.format("{:.0f}").background_gradient(cmap="Blues", axis=None))

def show_feature_importance(clf, X):
    importances = clf.feature_importances_
    top_features = pd.DataFrame({
        "Feature": X.columns,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False).head(10)

    st.markdown("### ⭐ Feature Importances")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=top_features, x="Importance", y="Feature", ax=ax)
    ax.set_title("Top 10 Feature Importances")
    st.pyplot(fig)

# ---------- Main Logic ----------

# Caricamento dataset
try:
    df = st.session_state.get("df") or load_data(DB_PATH_PL_DIR)
    st.session_state.df = df
    st.success(f"✅ CSV caricato con {df.shape[0]} righe e {df.shape[1]} colonne.")
except Exception as e:
    st.error(f"Errore nel caricamento del CSV: {e}")
    st.stop()


# Split features e target
X, y = split_features_and_target(df)

# Split train/test
st.markdown("### ⚙️ Split train/test e addestramento modello")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)


# Pulsante retrain
retrain = st.button("🔄 Addestra / Ri-addestra il modello")

# Carica/addestra modello
clf = load_or_train_model(X_train, y_train, retrain=retrain)
y_pred = clf.predict(X_test)

# Valutazione
st.metric(label="🎯 Accuratezza", value=f"{accuracy_score(y_test, y_pred):.4f}")
show_classification_report(y_test, y_pred)
show_confusion_matrix(y_test, y_pred)
show_feature_importance(clf, X)

st.success("✅ Modello completato e visualizzato!")
