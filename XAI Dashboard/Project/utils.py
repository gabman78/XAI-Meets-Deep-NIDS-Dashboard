import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os


def load_data(path):
    if path.endswith(".parquet"):
        return pd.read_parquet(path)
    elif path.endswith(".csv"):
        return pd.read_csv(path)
    else:
        raise ValueError("Formato file non supportato: usa CSV o Parquet.")

def train_and_save_model(X_train, y_train, path):
    clf = RandomForestClassifier(n_estimators=100, max_depth=None, random_state=42, n_jobs=-1)
    clf.fit(X_train, y_train)
    joblib.dump(clf, path)
    return clf

def load_or_train_model(X_train, y_train, model_path, retrain):
    if os.path.exists(model_path) and not retrain:
        st.info(f"✅ Modello caricato da {model_path}.")
        return joblib.load(model_path)
    else:
        clf = train_and_save_model(X_train, y_train, model_path)
        st.success(f"🚀 Modello addestrato e salvato in {model_path}.")
        return clf

def evaluate_model(clf, X_test, y_test):
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f"### Accuracy: {accuracy:.4f}")
    st.text("Classification Report:")
    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    per_class = report_df.drop(index=["accuracy", "macro avg", "weighted avg"])
    st.dataframe(per_class.style.background_gradient(subset=["precision", "recall", "f1-score"], cmap="Greens"))

def plot_confusion_matrix(clf, X_test, y_test):
    y_pred = clf.predict(X_test)
    cm = confusion_matrix(y_test, y_pred, normalize='true') * 100
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(cm, annot=True, fmt='.1f', cmap='Blues', ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("True")
    st.subheader("Matrice di Confusione")
    st.pyplot(fig)

def plot_distributions(df):
    st.subheader("Distribuzione delle Classi (LABEL e LABEL-bin)")
    fig1, ax1 = plt.subplots()
    sns.countplot(x='LABEL', data=df, ax=ax1)
    ax1.set_title('Distribuzione Classi - LABEL')
    ax1.set_yscale('log')
    st.pyplot(fig1)

    if 'LABEL-bin' in df.columns:
        fig2, ax2 = plt.subplots()
        sns.countplot(x='LABEL-bin', data=df, ax=ax2)
        ax2.set_title('Distribuzione Classi - LABEL-bin')
        ax2.set_yscale('log')
        st.pyplot(fig2)

def plot_feature_importances(clf, feature_names):
    st.markdown("### ⭐ Feature Importances")
    feat_imp = pd.DataFrame({
        "Feature": feature_names,
        "Importance": clf.feature_importances_
    }).sort_values(by="Importance", ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=feat_imp, x="Importance", y="Feature", ax=ax)
    ax.set_title("Top 10 Feature Importances")
    st.pyplot(fig)

def analyze_mtu_packets(df):
    st.subheader("📊 Analisi: Biflussi con almeno un pacchetto MTU (1500 bytes)")
    if 'PL' in df.columns:
        mtu_count = df['PL'].apply(lambda pkt_list: 1500 in pkt_list).sum()
        st.write(f"Numero di biflussi con almeno un pacchetto da 1500 bytes: **{mtu_count}** su {len(df)} totali")
    else:
        st.warning("La colonna 'PL' non è disponibile nel dataset.")

