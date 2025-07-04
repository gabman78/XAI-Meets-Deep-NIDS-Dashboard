import streamlit as st
from sklearn.model_selection import train_test_split

from utils import (
    load_data, load_or_train_model,
    evaluate_model, plot_confusion_matrix, plot_distributions,
    plot_feature_importances, analyze_mtu_packets
)

from config import RF_MODEL_PATH_PL_DIR, RF_MODEL_PATH_ALL, DB_PATH, DB_PATH_PL_DIR, DB_PATH_ALL


def main():    
    # Titolo
    st.title("Random Forest Classifier - DAC Project")

    # Caricamento dataset
    df_unprocessed = load_data(DB_PATH)
    st.subheader("Dataset Preview")
    st.write(df_unprocessed.head())

    # Scelta feature
    dataset_selection = st.radio("Choose the columns to include:", ["Only PL & DIR", "All Features"])
    retrain = st.button("🔄 Train / Retrain the model")

    if dataset_selection == "Only PL & DIR":
        df = load_data(DB_PATH_PL_DIR)
        X, y = df, df_unprocessed['LABEL']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
        clf = load_or_train_model(X_train, y_train, RF_MODEL_PATH_PL_DIR, retrain)

    else:
        df = load_data(DB_PATH_ALL)
        X, y = df, df_unprocessed['LABEL']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
        clf = load_or_train_model(X_train, y_train, RF_MODEL_PATH_ALL, retrain)

    # Valutazione
    evaluate_model(clf, X_test, y_test)

    # Confusion Matrix
    plot_confusion_matrix(clf, X_test, y_test)

    # Distribuzione classi
    plot_distributions(df_unprocessed)

    # Feature Importance
    plot_feature_importances(clf, X.columns)

    # Analisi MTU
    analyze_mtu_packets(df_unprocessed)



if __name__ == "__main__":
    main()
