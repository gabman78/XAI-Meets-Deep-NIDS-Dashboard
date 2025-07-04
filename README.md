# XAI-Meets-Deep-NIDS-Dashboard

**This dashboard represents the final outcome of the work presented in the paper _"XAI Meets Deep NIDS: SHAP-Guided Adversarial Analysis on SDN Traffic"_ by the Cyber Pandas team.**

---

The **XAI Dashboard for Deep Learning Network Traffic Classification** is a **web-based application** developed using **Streamlit**, designed to support the **explainability** and **evaluation** of a Deep Learning-based **Network Intrusion Detection System (NIDS)** tailored for **Software-Defined Networking (SDN)** environments.

This tool serves as the final output of the research work presented in the paper _"XAI Meets Deep NIDS: SHAP-Guided Adversarial Analysis on SDN Traffic"_ by the **Cyber Pandas** team. Its main objective is to offer **cybersecurity analysts** a **visual and interactive platform** to better understand how a deep neural model distinguishes between **benign and malicious traffic**, as well as to explore its **vulnerabilities**.

Upon accessing the dashboard, the **homepage** presents two main sections, as shown in the following image:

- **SDN Database**: Allows users to inspect the **structure and composition** of the dataset used for training, including **class distributions** and **attack categories**.
- **DL Network Analysis**: Enables exploration of the model’s decisions using **SHAP (SHapley Additive exPlanations)**, both at the **binary classification** level and across **specific attack types**.
<p align="center">
<img width="1440" alt="Screenshot 2025-07-04 alle 16 15 25" src="https://github.com/user-attachments/assets/2ca90f1c-4623-4709-9361-960023f5d965" />
</p>

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
<p align="center">
<img width="1422" alt="Screenshot 2025-07-04 alle 16 22 11" src="https://github.com/user-attachments/assets/79a1d26a-8009-473c-a965-8b215689eac0" />
</p>

### 🥧 Malicious Traffic Breakdown

To further detail the malicious flows, the dashboard includes:
- A **donut chart** showing the proportion of benign vs. malicious flows  
- A **pie chart** displaying the breakdown of malicious traffic by attack type (DDoS, Probe, DoS, BFA, Web-Attack)

All charts are **interactive**, allowing users to hover and isolate specific segments:
<p align="center">
<img width="1424" alt="Screenshot 2025-07-04 alle 16 22 24" src="https://github.com/user-attachments/assets/edf11e57-e94b-439d-933e-2b8ffcd22b5b" />
</p>
  
<p align="center">
<img width="706" alt="Screenshot 2025-07-04 alle 16 22 32" src="https://github.com/user-attachments/assets/28b6b94b-9a01-4421-ba46-59f327459e06" />
</p>

### 📦 Statistical Visualizations

Users can also explore:
- **Boxplots** showing the distribution of packet counts and payload lengths across different traffic labels.

These visualizations help identify patterns and outliers in packet-level behavior. For example, users can analyze which attacks involve longer payloads or more packets in early flow stages.

Available boxplots include:
- **Packets per LABEL**: Number of packets per attack category  
- **Packets per LABEL-bin**: Number of packets grouped by binary class (Benign vs Malicious)  
- **First Packet per LABEL (PL_first)**: Payload length of the **first packet** across categories  
- **Second Packet per LABEL (PL_second)**: Payload length of the **second packet**

All charts are interactive and rendered using **Apache ECharts**, enabling responsive tooltips, zooming, and highlighting on hover.

Example:

<p align="center">
<img width="632" alt="Screenshot 2025-07-04 alle 16 31 01" src="https://github.com/user-attachments/assets/a694f48d-d127-48ed-8b84-7e990b8297f2" />
</p>

### 🧾 Data Table Sampling

A sample of raw SDN flows is made available in a sortable and filterable table. Users can:
- Choose the number of rows to display
- Filter columns individually to focus on specific values

<p align="center">
<img width="644" alt="Screenshot 2025-07-04 alle 16 31 34" src="https://github.com/user-attachments/assets/8a5a0810-fd1c-402e-9e78-ecae701461ed" />
</p>

---

## 🧠 Model & SHAP-Based Analysis

The **DL Network Analysis** section of the dashboard allows for interactive exploration of model behavior and explainability through **SHAP (SHapley Additive exPlanations)**. It includes both global and attack-specific insights, highlighting which features and packets are most critical to classification.

## 📊 SHAP-Based Model Analysis

### 🔍 SHAP – 100 Samples

This interactive chart presents the **median importance** of six features — **PL**, **IAT**, **DIR**, **WIN**, **TTL**, **FLG** — across the first 10 packets of each flow, computed on a sample of 100 malicious flows.  

🎛️ Users can **toggle individual features** or **select specific packets** to focus the analysis on areas of interest.

<p align="center">
 <img width="687" alt="Screenshot 2025-07-04 alle 16 38 08" src="https://github.com/user-attachments/assets/5ff4519c-6a86-4af9-b6c4-449c9d0289d6" />
</p>

🧠 **Insight**: Features from the first 4 packets — especially the **TTL of packet 4** — stand out as the most influential.

---

### 🎯 SHAP‑Guided Attack Success Rate

An adversarial experiment on 100 correctly classified malicious flows used SHAP to modify only the **TTL of packet 4**.

<p align="center">
<img width="672" alt="Screenshot 2025-07-04 alle 16 38 19" src="https://github.com/user-attachments/assets/99e3a1f9-3162-472c-b652-72f411e51be4" />
</p>

✅ **Result**: **94% success rate** — showing a **potential vulnerability** in this core decision feature.

---

### 📈 Performance per Class

Explore the model's metrics interactively by hovering over bars to see customized details.

<p align="center">
<img width="676" alt="Screenshot 2025-07-04 alle 16 38 28" src="https://github.com/user-attachments/assets/257ace5f-978f-4d07-948a-05b3eaf9bf0e" />
</p>

---

### 📂 SHAP by Attack Category

This section offers **dynamic SHAP views by attack category** (for BFA, DDoS, Dos and Probe), with filtering via dropdown selectors.

<p align="center">
 <img width="684" alt="Screenshot 2025-07-04 alle 16 38 47" src="https://github.com/user-attachments/assets/49cb48a2-0ab7-4c7b-bca5-e4913ad8fb91" />
</p>

#### In the example: **Brute Force Attack (BFA)**  
- Visualize per-feature importance for **pkt 1–10**, filtered to highlight **TTL and DIR** on **packet 4**

---

### 🎣 Results Modifying Random Features on 100 Samples

Dynamic table with sorting and filtering by **packet number**, **feature**, and **success rate**.

<p align="center">
  <img width="681" alt="Screenshot 2025-07-04 alle 16 39 02" src="https://github.com/user-attachments/assets/567c14a3-9061-4943-83ce-ae3f742ba857" />
</p>

📝 Only modifications to **TTL** and **WIN** succeeded in altering classifications.

---

### 🎯 Average Success per Feature

This bar chart allows toggling features and inspecting **average success rates** per feature interactively.

<p align="center">
 <img width="510" alt="Screenshot 2025-07-04 alle 16 40 24" src="https://github.com/user-attachments/assets/c05b2914-903f-4497-a5c4-cdeaabe565bf" />
</p>

✅ **TTL remains the most effective feature**, even in non-guided attacks.

---

### 🧪 TTL Distribution – Packet 4

An interactive histogram comparing **TTL values of packet 4** for benign vs malicious flows. Users can **filter by class** and hover to read exact counts.

<p align="center">
<img width="673" alt="Screenshot 2025-07-04 alle 16 41 03" src="https://github.com/user-attachments/assets/0c41437b-4084-4513-ae7c-36b420ecd84d" />
</p>

- **Benign flows**: Diverse TTL distribution (`128`, `64`, `-1`)  
- **Malicious flows**: Concentration at `-1` (padding)

📌 The **`-1` TTL value** proved critical in distinguishing classes — information revealed interactively by the histogram.

---

🔧 All charts are built with **Apache ECharts** and embedded via **Streamlit**, allowing real-time filtering, toggling of features/packets, tooltip inspection and zoom/pan interactions — empowering analysts to conduct a **deep-dive, customized exploration** of model behavior.
