import streamlit as st
import requests
import pandas as pd

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="ALVA",
    page_icon="assets/icon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("A Legfaszább Videójáték Adatbázis")

st.markdown("Csekkold le kedvenc játékaid!")

@st.cache_data(ttl=60)
def load_games():
    response = requests.get(f"{API_BASE_URL}/games")
    response.raise_for_status()
    return response.json()


if st.button("Top games"):
    with st.spinner("Adatok frissítése..."):
        response = requests.post(f"{API_BASE_URL}/games/fetch?limit=10")
        if response.status_code == 200:
            st.success("Sikeres frissítés!")
            st.cache_data.clear()
        else:
            st.error("Hiba történt a frissítés során.")


st.subheader("Játékok listája")


games = load_games()

if not games:
    st.info("Nincs itt semmi he.")
else:
    df = pd.DataFrame(games)

    df["platform"] = df["platform"].apply(lambda x: x["name"] if x else None)
    df["publisher"] = df["publisher"].apply(lambda x: x["name"] if x else None)
    df["developer"] = df["developer"].apply(lambda x: x["name"] if x else None)

    df["category1"] = df["category1"].apply(lambda x: x["name"] if x else None)
    df["category2"] = df["category2"].apply(lambda x: x["name"] if x else None)
    df["agerating"] = df["agerating"].apply(
    lambda x: f"PEGI {x['value']}" if x else None
    )

    oszlopok = ['id', 'name', 'released', 'platform', 'category1', 'category2', 'publisher', 'developer', 'agerating']
    df_filtered = df[oszlopok]

    st.dataframe(df_filtered, use_container_width=True)