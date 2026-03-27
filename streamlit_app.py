import streamlit as st
import pandas as pd
from google.oauth2 import service_account
import json

# StreamlitのSecretsから鍵を読み込む
if "gcp_service_account" in st.secrets:
    # JSON文字列を辞書形式に変換
    info = json.loads(st.secrets["gcp_service_account"]["json_key"])
    
    # 修正ポイント：秘密鍵の改行文字を正しく処理する
    info["private_key"] = info["private_key"].replace("\\n", "\n")
    
    credentials = service_account.Credentials.from_service_account_info(info)
else:
    st.error("Secretsに鍵（JSON）が設定されていません。")
    st.stop()

st.title("🏆 toto 2等・3等 照準分析システム")
st.success("スプレッドシートとの連携に成功しました！")
st.write("隆生さんのデータを使って、当選確率を分析する準備が整いました。")
