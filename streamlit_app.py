import streamlit as st
from google.oauth2 import service_account
import json

# タイトルを先に表示
st.title("🏆 toto 2等・3等 照準分析システム")

# Secretsの読み込み
try:
    if "gcp_service_account" in st.secrets:
        # 文字列として入っているJSONを辞書に変換し、改行コードを修正
        raw_json = st.secrets["gcp_service_account"]["json_key"]
        info = json.loads(raw_json, strict=False)
        info["private_key"] = info["private_key"].replace("\\n", "\n")
        
        credentials = service_account.Credentials.from_service_account_info(info)
        st.success("✅ スプレッドシートとの連携に成功しました！")
        st.write("隆生さんのデータを使って、当選確率を分析する準備が整いました。")
    else:
        st.error("Secretsに [gcp_service_account] が設定されていません。")
except Exception as e:
    st.error(f"エラーが発生しました: {e}")
