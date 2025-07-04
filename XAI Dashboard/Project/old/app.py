
import streamlit as st
from streamlit_echarts import st_echarts
import pickle, numpy as np, pandas as pd, os, torch


st.title("SHAP Visualization with ECharts – Bar Grouped")

file_path = "pickle/shap_values_100Samples_seed1_5r_DeepExplainer.pickle"

if os.path.exists(file_path):
    st.success(f"✅ File trovato: {file_path}")
    with open(file_path, "rb") as f:
        shap_values = pickle.load(f)
    sv_malicious = shap_values[1] if isinstance(shap_values, list) and len(shap_values)>1 else shap_values[0]

    normalized = []
    for sv in sv_malicious:
        arr = sv.detach().cpu().numpy() if isinstance(sv, torch.Tensor) else np.array(sv)
        s = arr.sum()
        normalized.append(arr[0]/s if s!=0 else 0)
    median_sv = np.median(np.array(normalized), axis=0)*100
    df = pd.DataFrame(median_sv.reshape(10,6), columns=['PL','IAT','DIR','WIN','TTL','FLG'])
    df['Packet'] = [f'Pkt {i+1}' for i in range(10)]

    features = df.columns[:-1].tolist()
    packets = df['Packet'].tolist()
    selected_features = st.multiselect("Feature da mostrare:", features, default=features)
    selected_packets = st.multiselect("Pacchetti da mostrare:", packets, default=packets)
    df = df[df['Packet'].isin(selected_packets)].reset_index(drop=True)
    packets = df['Packet'].tolist()

    color_map = {'PL':'#1f77b4','IAT':'#ff7f0e','DIR':'#2ca02c','WIN':'#d62728','TTL':'#9467bd','FLG':'#8c564b'}
    series = []
    for feat in selected_features:
        series.append({
            "name": feat,
            "type": "bar",
            "barCategoryGap": "20%",
            "data": df[feat].round(2).tolist(),
            "itemStyle": {"color": color_map[feat]}
        })

    # Stelle rosse
    star_label = "PKT"
    stars = {
        "name": star_label,
        "type": "scatter",
        "symbol": "roundRect",
        "symbolRotate": 45,  
        "symbolSize": 15,
        "itemStyle": {"color": "#ffd700"},
        "data": []
    }

    for i, row in df.iterrows():
        pkt_sum = row[selected_features].sum()
        stars["data"].append([i, round(pkt_sum, 2)])

    series.append(stars)

    option = {
        "title":{"text":"Feature Importance per Packet","left":"center"},
        "tooltip":{"trigger":"axis", "axisPointer":{"type":"shadow"}},
        "legend":{"top":"10%", "data": selected_features + ["PKT"]},
        "xAxis": {
        "type": "category",
        "data": packets,
        "name": "Packet Index",             
        "nameLocation": "middle",
        "nameGap": 30,
        "axisLabel": {
            "fontSize": 12,
            "rotate": 0                   
        },
        "nameTextStyle": {
            "fontSize": 14,
            "fontWeight": "bold"
        }
        },
        "yAxis": {
            "type": "value",
            "name": "Median Importance [%]",          
            "nameLocation": "middle",
            "nameGap": 45,
            "axisLabel": {
                "fontSize": 12
            },
            "nameTextStyle": {
                "fontSize": 14,
                "fontWeight": "bold"
            }
        },

        "grid": {
            "left": "12%",  
            "right": "12%",
            "bottom": "15%",
            "top": "15%"
        },
        "series": series
    }

    st_echarts(option, height="600px", width="100%", renderer="svg")
else:
    st.error(f"❌ File non trovato: {file_path}")
