import streamlit as st
from google.oauth2 import service_account
import json

st.title("🏆 toto 2等・3等 照準分析システム")

try:
    if "gcp_service_account" in st.secrets:
        # 1. Secretsから中身を取り出す
        raw_json = st.secrets["gcp_service_account"]["json_key"]
        
        # 2. 【最重要】目に見えないゴミ（BOM）を強制削除
        # 239 (0xEF) 等の不正バイトをここでシュレッダーにかけます
        raw_json = raw_json.strip().encode('utf-8').decode('utf-8-sig')
        
        # 3. 辞書に変換して、秘密鍵の改行を修正
        info = json.loads(raw_json, strict=False)
        if "private_key" in info:
            info["private_key"] = info["private_key"].replace("\\n", "\n")
        
        # 4. 認証実行
        credentials = service_account.Credentials.from_service_account_info(info)
        st.success("✅ スプレッドシートとの連携に成功しました！")
        st.balloons() # お祝いの風船を飛ばします
        st.write("隆生さんのデータを使って、当選確率を分析する準備が整いました。")
    else:
        st.error("Secretsの設定が読み込めません。")
except Exception as e:
    st.error(f"エラーが発生しました: {e}")
    st.info("一度Streamlitの『Settings > Secrets』をすべて消して貼り直すと直る場合があります。")
