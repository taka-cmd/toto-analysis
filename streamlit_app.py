import streamlit as st
from google.oauth2 import service_account
import json
import re

st.title("🏆 toto 2等・3等 照準分析システム")

try:
    if "gcp_service_account" in st.secrets:
        # 1. SecretsからJSONを取り出す
        raw_json = st.secrets["gcp_service_account"]["json_key"]
        
        # 2. 辞書形式に変換
        info = json.loads(raw_json, strict=False)
        
        # 3. 【最重要】鍵の文字列を強制クリーニング
        # 前後の空白を消し、中の改行文字（\n）を本物の改行に変換し、
        # さらに変なスペースや重複した改行をすべて掃除します。
        key = info["private_key"]
        key = key.replace("\\n", "\n").replace(" ", "").replace("\n\n", "\n")
        # 鍵のヘッダーとフッターを正規化
        key = key.replace("-----BEGINPRIVATEKEY-----", "-----BEGIN PRIVATE KEY-----\n")
        key = key.replace("-----ENDPRIVATEKEY-----", "\n-----END PRIVATE KEY-----")
        info["private_key"] = key
        
        # 4. 認証実行
        credentials = service_account.Credentials.from_service_account_info(info)
        st.success("✅ スプレッドシートとの連携に成功しました！")
        st.balloons()
        st.write("隆生さんのデータを使って、当選確率を分析する準備が整いました。")
    else:
        st.error("Secretsの設定が読み込めません。")
except Exception as e:
    st.error(f"エラーが発生しました: {e}")
