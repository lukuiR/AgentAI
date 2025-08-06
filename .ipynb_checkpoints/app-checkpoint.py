import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime

st.set_page_config(page_title="Agent AI", layout="wide")

# ---------------------
# Sidebar
# ---------------------
st.sidebar.title("Agent AI – Menu")
section = st.sidebar.radio("Wybierz sekcję:", [
    "📅 Plan dnia",
    "📬 Skrzynka mailowa",
    "💸 Finanse",
    "🧠 Zadania i notatki",
    "🌤️ Pogoda"
])

st.title("🧠 Twój osobisty agent AI")

# ---------------------
# Sekcja: Plan dnia
# ---------------------
if section == "📅 Plan dnia":
    st.header("📅 Plan dnia")
    st.write("🕐 Tu pojawią się wydarzenia z Twojego kalendarza.")
    st.info("Integrację z Google Calendar dodamy później.")

# ---------------------
# Sekcja: Skrzynka mailowa
# ---------------------
elif section == "📬 Skrzynka mailowa":
    st.header("📬 Twoje maile")
    st.write("📧 Tu pokażemy wiadomości z Gmaila lub innego źródła.")
    st.info("Integracja z e-mailem będzie w kolejnych krokach.")

# ---------------------
# Sekcja: Finanse
# ---------------------
elif section == "💸 Finanse":
    st.header("💸 Twoje finanse")

    tab1, tab2 = st.tabs(["📊 Wydatki z CSV", "📈 Giełda i ETF-y"])

    # ------------------
    # 📊 Wydatki z pliku
    # ------------------
    with tab1:
        uploaded_file = st.file_uploader("Wgraj plik CSV z wydatkami", type="csv")
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.success("Dane załadowane!")
            st.dataframe(df)

            if 'Kwota' in df.columns:
                st.metric("Suma wydatków", f"{df['Kwota'].sum():.2f} zł")

    # ------------------
    # 📈 Giełda i ETF-y
    # ------------------
    with tab2:

        st.subheader("📈 Notowania giełdowe i ETF")

        tickers_input = st.text_input("Tickery (oddzielone przecinkami):", value="AAPL,MSFT,VOO,ARKK")
        tickers = [t.strip().upper() for t in tickers_input.split(",")]

        # Portfolio – ilość jednostek
        st.markdown("### 💼 Twoje portfolio")
        portfolio = {}
        total_value = 0.0

        for ticker in tickers:
            qty = st.number_input(f"Ilość jednostek {ticker}", min_value=0.0, value=0.0, step=1.0, key=f"qty_{ticker}")
            portfolio[ticker] = qty

        st.markdown("### 📊 Dane i wykresy")

        for ticker in tickers:
            try:
                # Dane bieżące
                stock = yf.Ticker(ticker)
                hist_day = stock.history(period="2d")
                hist_7d = stock.history(period="7d")
                hist_30d = stock.history(period="1mo")

                current_price = hist_day["Close"][-1]
                previous_close = hist_day["Close"][-2]
                change_pct = ((current_price - previous_close) / previous_close) * 100

                st.subheader(f"{ticker}")
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(label="Cena bieżąca", value=f"${current_price:.2f}")
                with col2:
                    st.metric(label="Zmiana % (1 dzień)", value=f"{change_pct:.2f}%")
                with col3:
                    if portfolio[ticker] > 0:
                        value = portfolio[ticker] * current_price
                        total_value += value
                        st.metric(label="Wartość pozycji", value=f"${value:.2f}")

                # Alert cenowy
                alert_price = st.number_input(f"🔔 Alert cenowy dla {ticker}", min_value=0.0, value=0.0, step=1.0, key=f"alert_{ticker}")
                if alert_price > 0 and current_price > alert_price:
                    st.warning(f"📣 {ticker} przekroczył próg ${alert_price}!")

                # Wykres intraday (jeśli dostępny)
                hist_intraday = stock.history(period="1d", interval="5m")
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=hist_intraday.index, y=hist_intraday["Close"], mode="lines", name="Intraday"))
                fig.update_layout(title=f"{ticker} – Intraday", xaxis_title="Czas", yaxis_title="Cena USD")
                st.plotly_chart(fig, use_container_width=True)

                # Wykres 7 dni
                fig7 = go.Figure()
                fig7.add_trace(go.Scatter(x=hist_7d.index, y=hist_7d["Close"], mode="lines", name="7 dni"))
                fig7.update_layout(title=f"{ticker} – Ostatnie 7 dni", xaxis_title="Data", yaxis_title="Cena USD")
                st.plotly_chart(fig7, use_container_width=True)

                # Wykres 30 dni
                fig30 = go.Figure()
                fig30.add_trace(go.Scatter(x=hist_30d.index, y=hist_30d["Close"], mode="lines", name="30 dni"))
                fig30.update_layout(title=f"{ticker} – Ostatnie 30 dni", xaxis_title="Data", yaxis_title="Cena USD")
                st.plotly_chart(fig30, use_container_width=True)

            except Exception as e:
                st.error(f"❌ Błąd dla {ticker}: {e}")

        if total_value > 0:
            st.success(f"💰 Wartość całkowita portfela: ${total_value:.2f}")

# ---------------------
# Sekcja: Zadania
# ---------------------
elif section == "🧠 Zadania i notatki":
    st.header("🧠 Twoje zadania i notatki")

    note = st.text_area("📝 Dodaj notatkę lub zadanie:")
    if st.button("💾 Zapisz"):
        with open("notatki.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {note}\n")
        st.success("Notatka zapisana!")

    st.subheader("📂 Historia notatek:")
    try:
        with open("notatki.txt", "r", encoding="utf-8") as f:
            notes = f.read()
        st.text_area("Zapisane notatki:", value=notes, height=200)
    except FileNotFoundError:
        st.info("Brak zapisanych notatek.")

# ---------------------
# Sekcja: Pogoda
# ---------------------
elif section == "🌤️ Pogoda":
    st.header("🌤️ Pogoda")
    st.write("☁️ Tu dodamy dane z API pogodowego (np. OpenWeather).")

