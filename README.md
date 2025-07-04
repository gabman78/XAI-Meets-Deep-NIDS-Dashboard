# XAI-Meets-Deep-NIDS-Dashboard

**This dashboard represents the final outcome of the work presented in the paper _"XAI Meets Deep NIDS: SHAP-Guided Adversarial Analysis on SDN Traffic"_ by the Cyber Pandas team.**

---

The **XAI Dashboard for Deep Learning Network Traffic Classification** is a **web-based application** developed using **Streamlit**, designed to support the **explainability** and **evaluation** of a Deep Learning-based **Network Intrusion Detection System (NIDS)** tailored for **Software-Defined Networking (SDN)** environments.

This tool serves as the final output of the research work presented in the paper _"XAI Meets Deep NIDS: SHAP-Guided Adversarial Analysis on SDN Traffic"_ by the **Cyber Pandas** team. Its main objective is to offer **cybersecurity analysts** a **visual and interactive platform** to better understand how a deep neural model distinguishes between **benign and malicious traffic**, as well as to explore its **vulnerabilities**.

Upon accessing the dashboard, the **homepage** presents two main sections, as shown in the following image:

- **SDN Database**: Allows users to inspect the **structure and composition** of the dataset used for training, including **class distributions** and **attack categories**.
- **DL Network Analysis**: Enables exploration of the model’s decisions using **SHAP (SHapley Additive exPlanations)**, both at the **binary classification** level and across **specific attack types**.

<img width="1440" alt="Screenshot 2025-07-04 alle 16 15 25" src="https://github.com/user-attachments/assets/2ca90f1c-4623-4709-9361-960023f5d965" />


The dashboard promotes **transparency**, supports **model introspection**, and assists in identifying **weak points** by enabling **guided adversarial perturbation analysis** — all through a **user-friendly interface**.
