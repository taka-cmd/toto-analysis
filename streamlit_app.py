import streamlit as st
from google.oauth2 import service_account
import re

st.title("🏆 toto 2等・3等 照準分析システム")

if "gcp_service_account" in st.secrets:
    try:
        info = dict(st.secrets["gcp_service_account"])
        key = str(info["private_key"])
        
        # 1. 徹底洗浄：PEMヘッダーや改行コード、スペースをすべて一度消し去る
        clean_key = key.replace("-----BEGIN PRIVATE KEY-----", "").replace("-----END PRIVATE KEY-----", "")
        clean_key = clean_key.replace("\\n", "").replace("\n", "").replace(" ", "").strip()
        
        # 2. 強制再構築：Googleが求める正しいPEM形式に「型」をはめ直す
        formatted_key = "-----BEGIN PRIVATE KEY-----\n" + clean_key + "\n-----END PRIVATE KEY-----\n"
        info["private_key"] = formatted_key
        
        # 3. 認証実行
        credentials = service_account.Credentials.from_service_account_info(info)
        st.success("✅ ついに成功しました！完全勝利です！")
        st.balloons()
        st.info("隆生さん、お疲れ様でした！これでiPhoneから自由に分析できます！")
        
    except Exception as e:
        st.error(f"❌ 認証エラー: {e}")
else:
    st.error("Secretsを設定してください")
