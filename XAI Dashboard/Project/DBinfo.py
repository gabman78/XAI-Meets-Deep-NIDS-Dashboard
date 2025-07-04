import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_echarts import st_echarts
from config import DB_PATH
import numpy as np

def visualizza_dashboard(default_path=DB_PATH):
    st.title("📶 SDN Database")

    try:
        df = pd.read_parquet(default_path)
        num_flussi = len(df)
        num_attributi = len(df.columns)

        st.markdown(f"""
        <div style='padding: 10px; background-color: #f9f9f9; border-radius: 8px; margin-bottom: 20px; font-size: 16px;'>
            ✅ Il dataset contiene <b>{num_flussi:,}</b> biflussi e <b>{num_attributi-1}</b> colonne.
        </div>
        """, unsafe_allow_html=True)


        if "LABEL-bin" in df.columns:
            conteggi = df["LABEL-bin"].value_counts().to_dict()
            benigni = conteggi.get(0, 0)
            maligni = conteggi.get(1, 0)
            totale = benigni + maligni

            st.subheader("📊 Traffico Benigno/Maligno")

            # Testo con stile
            st.markdown(f"""
            <div style='font-size: 18px; line-height: 1.8;'>
                🟢 <b>Benigno (0):</b> <span style='color:green'>{benigni}</span><br>
                🔴 <b>Maligno (1):</b> <span style='color:red'>{maligni}</span><br>
                📦 <b>Totale:</b> <span style='color:#444'>{totale}</span>
            </div>
            """, unsafe_allow_html=True)

            # ECharts: Bar Chart con due colori
            bar_options = {
                "xAxis": {"type": "category", "data": ["Benigno", "Maligno"]},
                "yAxis": {"type": "value"},
                "series": [{
                    "data": [
                        {"value": benigni, "itemStyle": {"color": "#4caf50"}},  
                        {"value": maligni, "itemStyle": {"color": "#e53935"}}   
                    ],
                    "type": "bar"
                }]
            }

            st_echarts(options=bar_options, height="400px")


            # --- ECharts: Pie Chart
            st.markdown("#### 🥧 Grafico a torta (percentuale)")
            pie_options = {
                "tooltip": {"trigger": "item"},
                "legend": {"top": "bottom"},
                "series": [{
                    "name": "Traffico",
                    "type": "pie",
                    "radius": ["30%", "60%"],
                    "avoidLabelOverlap": False,
                    "label": {"show": True, "formatter": "{b}: {d}%"},
                    "emphasis": {"label": {"show": True, "fontSize": 16, "fontWeight": "bold"}},
                    "data": [
                        {"value": benigni, "name": f"Benigno ({benigni})", "itemStyle": {"color": "#4caf50"}},
                        {"value": maligni, "name": f"Maligno ({maligni})", "itemStyle": {"color": "#e53935"}}
                    ]
                }]
            }
            st_echarts(options=pie_options, height="400px")

            # --- ECharts: Maligni per LABEL
            if "LABEL" in df.columns:
                st.subheader("🎯 TRAFFICO MALEVOLO - Distribuzione delle LABEL")

                conteggi_label = df[df["LABEL-bin"] == 1]["LABEL"].value_counts()
                percentuali_label = (conteggi_label / conteggi_label.sum() * 100).round(2)
                tabella_label = pd.DataFrame({
                    "Occorrenze": conteggi_label,
                    "Percentuale (%)": percentuali_label
                })

                st.dataframe(tabella_label)
                dati_echarts = [
                {
                    "value": int(v),
                    "name": f"{k} ({v / conteggi_label.sum() * 100:.2f}%)"
                }
                for k, v in conteggi_label.items()
            ]


        label_options = {
            "tooltip": {"trigger": "item"},
            "legend": {
                "orient": "vertical",
                "left": "left"
            },
            "series": [{
                "name": "LABEL",
                "type": "pie",
                "radius": "65%",
                "center": ["60%", "50%"],
                "label": {
                    "show": True,
                    "formatter": "{b}",
                    "position": "outside"
                },
                "labelLine": {"show": True},
                "emphasis": {
                    "label": {
                        "show": True,
                        "fontSize": 16,
                        "fontWeight": "bold"
                    }
                },
                "data": dati_echarts
            }]
        }

        st.markdown("#### 🧬 Grafico a torta delle LABEL dei flussi maligni")
        st_echarts(options=label_options, height="500px")



        st.subheader("👁️‍🗨️ Visualizzazione campionata")
        n = st.slider("Numero righe da visualizzare", 5, 10000, 10)
        st.dataframe(df.sample(n=n))

        # Bottone per attivare il filtro
        if "filtro_attivo" not in st.session_state:
            st.session_state.filtro_attivo = False

        # Bottone per attivare il filtro
        if st.button("🔍 Filtra per colonna"):
            st.session_state.filtro_attivo = True

        # Se il filtro è attivo, mostra i controlli
        if st.session_state.filtro_attivo:
            st.markdown("### 🎯 Filtro attivo")

            # Pre-seleziona 'LABEL' se presente
            colonna_default = "LABEL" if "LABEL" in df.columns else df.columns[0]
            colonna = st.selectbox("Seleziona colonna", df.columns, index=df.columns.get_loc(colonna_default), key="colonna_filtro")

            valore = st.selectbox("Seleziona valore", df[colonna].astype(str).unique(), key="valore_filtro")
            filtrato = df[df[colonna].astype(str) == valore]

            st.success(f"{len(filtrato)} righe trovate per `{colonna} = {valore}`")
            st.dataframe(filtrato.head(100))

            # Download CSV
            csv = filtrato.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="💾 Download CSV",
                data=csv,
                file_name=f"filtrato_{colonna}_{valore}.csv",
                mime="text/csv"
            )
    
            

    except Exception as e:
        st.error(f"Errore: {e}")


def analisi_boxplot():
    st.title("📦 Analisi Boxplot")

    try:
        df = pd.read_parquet(DB_PATH)
       
        # Pre-elaborazione per i grafici
        df["PL_count"] = df["PL"].apply(len)
        df["PL_first"] = df["PL"].apply(lambda x: x[0] if len(x) > 0 else None)
        df["PL_second"] = df["PL"].apply(lambda x: x[1] if len(x) > 1 else None)

        opzioni = {
            "Pacchetti per LABEL ": ("LABEL", "PL_count"),
            "Pacchetti per LABEL-bin ": ("LABEL-bin", "PL_count"),
            "Primo pacchetto per LABEL (PL_first)": ("LABEL", "PL_first"),
            "Secondo pacchetto per LABEL (PL_second)": ("LABEL", "PL_second"),
        }

        scelta = st.selectbox("Scegli il grafico", list(opzioni.keys()))

        if scelta:
            x, y = opzioni[scelta]
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.boxplot(data=df, x=x, y=y, palette='Set2', showmeans=True, ax=ax)
            ax.set_title(scelta)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Errore: {e}")

