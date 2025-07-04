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

## 📊 SDN Database Analysis

The **SDN Database** section of the dashboard offers an interactive and visual exploration of the dataset used to train the intrusion detection model. This section is fully developed using **Streamlit** and integrates **Apache ECharts** to enable responsive and dynamic visualizations.

### 🔍 Dataset Overview

Upon accessing the SDN analysis view, users are immediately presented with a summary of the dataset:  
- **225,608** bidirectional flows  
- **13 features** per flow  
- **Binary labels** for benign/malicious classification  
- **Multi-class labels** for specific attack types  

The following visualization provides an immediate glance at the benign vs. malicious flow distribution:

![Benign vs Malicious](<img width="1422" alt="Screenshot 2025-07-04 alle 16 22 11" src="https://github.com/user-attachments/assets/79a1d26a-8009-473c-a965-8b215689eac0" />
)

### 🥧 Malicious Traffic Breakdown

To further detail the malicious flows, the dashboard includes:
- A **donut chart** showing the proportion of benign vs. malicious flows  
- A **pie chart** displaying the breakdown of malicious traffic by attack type (DDoS, Probe, DoS, BFA, Web-Attack)

All charts are **interactive**, allowing users to hover and isolate specific segments:

![Donut Chart](<img width="1424" alt="Screenshot 2025-07-04 alle 16 22 24" src="https://github.com/user-attachments/assets/edf11e57-e94b-439d-933e-2b8ffcd22b5b" />
)
![Malicious Pie Chart](<img width="706" alt="Screenshot 2025-07-04 alle 16 22 32" src="https://github.com/user-attachments/assets/28b6b94b-9a01-4421-ba46-59f327459e06" />
)

### 📦 Statistical Visualizations


Users can also explore:
- **Boxplots** showing the distribution of packet counts and payload lengths across different traffic labels.

These visualizations help identify patterns and outliers in packet-level behavior. For example, users can analyze which attacks involve longer payloads or more packets in early flow stages.

Available boxplots include:
- **Pacchetti per LABEL**: Number of packets per attack category
- **Pacchetti per LABEL-bin**: Number of packets grouped by binary class (Benign vs Malicious)
- **Primo pacchetto per LABEL (PL_first)**: Payload length of the **first packet** across categories
- **Secondo pacchetto per LABEL (PL_second)**: Payload length of the **second packet**

All charts are interactive and rendered using **Apache ECharts**, enabling responsive tooltips, zooming, and highlighting on hover.

Example:

![Boxplot](<img width="754" alt="Screenshot 2025-07-04 alle 16 22 50" src="https://github.com/user-attachments/assets/42be0b76-2f4d-45d7-bee3-8626da184dec" />
)

### 🧾 Data Table Sampling

A sample of raw SDN flows is made available in a sortable and filterable table. Users can:
- Choose the number of rows to display
- Filter columns individually to focus on specific values

![Sample Table](<img width="738" alt="Screenshot 2025-07-04 alle 16 22 40" src="https://github.com/user-attachments/assets/f5c155c4-0ccb-4d6b-81be-62fd03a54068" />
)

---

All these elements are rendered with **ECharts**, enabling high-performance, browser-based interactions. This makes the dashboard not only informative but also **highly usable** for security analysts, data scientists, or researchers exploring the dataset behavior in real time.

