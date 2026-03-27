import streamlit as st
import pandas as pd
from google.oauth2 import service_account
import json

# StreamlitのSecretsから鍵を読み込む（辞書型に変換）
if "gcp_service_account" in st.secrets:
    # 修正ポイント：文字列で入っているJSONを辞書形式に戻す
    info = json.loads(st.secrets["gcp_service_account"]["json_key"])
    credentials = service_account.Credentials.from_service_account_info(info)
else:
    st.error("Secretsに鍵（JSON）が設定されていません。")
    st.stop()

st.title("🏆 toto 2等・3等 照準分析システム")
st.success("スプレッドシートとの連携に成功しました！")
st.write("隆生さんのデータを使って、当選確率を分析する準備が整いました。")
