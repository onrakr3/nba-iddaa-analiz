import streamlit as st
import pandas as pd

st.set_page_config(page_title="NBA İddaa Üst Analiz", layout="wide")

st.title("🏀 NBA İddaa Üst ve Maç Analiz Uygulaması")
st.markdown("Takım istatistikleri, maç analizleri ve resmi takım armalarıyla güçlendirilmiş simülasyon.")

# Takım İstatistikleri ve Logo URL'leri Verisi
data_takimlar = {
    "Takım": ["Toronto", "Miami", "Boston", "Dallas", "Denver", "Utah", "La clippers", "Golden state", "Detroit", "Phoenix", "Phila", "New york", "Atlanta", "Brooklyn", "Charlotte", "Chicago", "Cleveland", "Indiana", "Milwaukee", "Orlando", "Washington", "Houston", "La lakers", "Memphis", "Minnesota", "New orleans", "Oklahama", "Portland", "Sacramento", "San antonio"],
    "Logo": [
        "https://cdn.nba.com/logos/nba/1610612761/global/L/logo.svg", # Toronto
        "https://cdn.nba.com/logos/nba/1610612748/global/L/logo.svg", # Miami
        "https://cdn.nba.com/logos/nba/1610612738/global/L/logo.svg", # Boston
        "https://cdn.nba.com/logos/nba/1610612742/global/L/logo.svg", # Dallas
        "https://cdn.nba.com/logos/nba/1610612743/global/L/logo.svg", # Denver
        "https://cdn.nba.com/logos/nba/1610612762/global/L/logo.svg", # Utah
        "https://cdn.nba.com/logos/nba/1610612746/global/L/logo.svg", # LA Clippers
        "https://cdn.nba.com/logos/nba/1610612744/global/L/logo.svg", # Golden State
        "https://cdn.nba.com/logos/nba/1610612765/global/L/logo.svg", # Detroit
        "https://cdn.nba.com/logos/nba/1610612756/global/L/logo.svg", # Phoenix
        "https://cdn.nba.com/logos/nba/1610612755/global/L/logo.svg", # Phila
        "https://cdn.nba.com/logos/nba/1610612752/global/L/logo.svg", # New York
        "https://cdn.nba.com/logos/nba/1610612737/global/L/logo.svg", # Atlanta
        "https://cdn.nba.com/logos/nba/1610612751/global/L/logo.svg", # Brooklyn
        "https://cdn.nba.com/logos/nba/1610612766/global/L/logo.svg", # Charlotte
        "https://cdn.nba.com/logos/nba/1610612741/global/L/logo.svg", # Chicago
        "https://cdn.nba.com/logos/nba/1610612739/global/L/logo.svg", # Cleveland
        "https://cdn.nba.com/logos/nba/1610612754/global/L/logo.svg", # Indiana
        "https://cdn.nba.com/logos/nba/1610612749/global/L/logo.svg", # Milwaukee
        "https://cdn.nba.com/logos/nba/1610612753/global/L/logo.svg", # Orlando
        "https://cdn.nba.com/logos/nba/1610612764/global/L/logo.svg", # Washington
        "https://cdn.nba.com/logos/nba/1610612745/global/L/logo.svg", # Houston
        "https://cdn.nba.com/logos/nba/1610612747/global/L/logo.svg", # LA Lakers
        "https://cdn.nba.com/logos/nba/1610612763/global/L/logo.svg", # Memphis
        "https://cdn.nba.com/logos/nba/1610612750/global/L/logo.svg", # Minnesota
        "https://cdn.nba.com/logos/nba/1610612740/global/L/logo.svg", # New Orleans
        "https://cdn.nba.com/logos/nba/1610612760/global/L/logo.svg", # Oklahoma
        "https://cdn.nba.com/logos/nba/1610612757/global/L/logo.svg", # Portland
        "https://cdn.nba.com/logos/nba/1610612758/global/L/logo.svg", # Sacramento
        "https://cdn.nba.com/logos/nba/1610612759/global/L/logo.svg"  # San Antonio
    ],
    "Ev_Atilan": [125.5, 120.33, 124.75, 107.75, 121.25, 114.6, 115.67, 117.75, 119.67, 116.33, 114.8, 107.4, 116.67, 108.67, 100.2, 119.25, 121.0, 118.0, 109.25, 121.5, 116.5, 119.75, 112.2, 119.0, 111.5, 113.5, 110.83, 123.5, 108.25, 115.8],
    "Ev_Yedigi": [106.25, 123.83, 100.25, 123.25, 126.5, 117.4, 102.33, 108.25, 115.0, 113.0, 110.0, 114.0, 121.0, 118.0, 111.0, 115.25, 118.75, 120.0, 118.75, 119.5, 116.75, 110.25, 110.8, 107.67, 111.0, 114.5, 107.17, 100.5, 122.0, 110.6],
    "Dep_Atilan": [112.75, 118.0, 120.67, 119.0, 108.0, 110.33, 108.0, 113.5, 117.5, 104.8, 106.67, 99.33, 124.5, 126.0, 100.33, 115.2, 111.0, 115.25, 115.6, 112.67, 111.0, 123.33, 119.0, 116.0, 120.25, 117.8, 105.0, 118.67, 102.25, 109.67],
    "Dep_Yedigi": [117.5, 118.67, 118.0, 114.25, 107.5, 112.0, 115.67, 114.67, 106.0, 121.0, 119.33, 125.0, 111.67, 120.25, 111.0, 126.2, 123.0, 109.75, 122.6, 113.0, 111.5, 113.67, 116.67, 109.6, 113.5, 119.2, 111.0, 115.33, 118.0, 109.0]
}

df = pd.DataFrame(data_takimlar)

st.sidebar.header("Menü")
secim = st.sidebar.radio("Git:", ["Takım İstatistikleri", "Maç Tahmin Simülasyonu"])

if secim == "Takım İstatistikleri":
    st.subheader("📊 Takım İç Saha ve Deplasman Ortalamaları ve Armaları")
    st.dataframe(
        df,
        column_config={
            "Logo": st.column_config.ImageColumn("Arma", width="small")
        },
        use_container_width=True
    )

elif secim == "Maç Tahmin Simülasyonu":
    st.subheader("🎯 Maç Karşılaştırma ve Üst Analizi")
    
    takimlar_liste = df["Takım"].tolist()
    ev_sahibi = st.selectbox("Ev Sahibi Takım", takimlar_liste, index=2) 
    deplasman = st.selectbox("Deplasman Takımı", takimlar_liste, index=13) 
    
    if ev_sahibi == deplasman:
        st.warning("Ev sahibi ve deplasman takımı aynı olamaz!")
    else:
        ev_row = df[df["Takım"] == ev_sahibi].iloc[0]
        dep_row = df[df["Takım"] == deplasman].iloc[0]
        
        tahmini_toplam = (ev_row["Ev_Atilan"] + ev_row["Ev_Yedigi"] + dep_row["Dep_Atilan"] + dep_row["Dep_Yedigi"]) / 2
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(ev_row["Logo"], width=80)
            st.metric(label=f"🏠 {ev_sahibi} (Ev Sahibi)", value=f"Atılan: {ev_row['Ev_Atilan']} | Yediği: {ev_row['Ev_Yedigi']}")
        with col2:
            st.image(dep_row["Logo"], width=80)
            st.metric(label=f"✈️ {deplasman} (Deplasman)", value=f"Atılan: {dep_row['Dep_Atilan']} | Yediği: {dep_row['Dep_Yedigi']}")
            
        st.info(f"📈 **Hesaplanan Maç Skor / Baremi:** {round(tahmini_toplam, 2)}")
        if tahmini_toplam > 220:
            st.success("🔥 Tahmin: **ÜST** (Yüksek skorlu geçmesi bekleniyor)")
        else:
            st.warning("⚖️ Tahmin: Normal / Alt sınırlarında")
