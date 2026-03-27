import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from gspread_pandas import Spread

# StreamlitのSecretsから鍵を読み込む
if "gcp_service_account" in st.secrets:
    credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
else:
    st.error("Secretsに鍵（JSON）が設定されていません。")
    st.stop()

st.title("🏆 toto 2等・3等 照準分析システム")
st.write("隆生さんのスプレッドシートからデータを読み込み、当選確率を分析します。")

# ここに分析ロジックを書いていきます
st.info("スプレッドシートとの連携準備が整いました！")
