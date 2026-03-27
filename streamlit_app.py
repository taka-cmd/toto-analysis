import streamlit as st
from google.oauth2 import service_account

st.title("🏆 toto分析システム（最終接続テスト）")

# Secretsから直接読み込む
if "gcp_service_account" in st.secrets:
    try:
        info = dict(st.secrets["gcp_service_account"])
        # 鍵の改行だけを戻す
        info["private_key"] = info["private_key"].replace("\\n", "\n")
        
        credentials = service_account.Credentials.from_service_account_info(info)
        st.success("✅ ついに繋がりました！完全勝利です！")
        st.balloons()
    except Exception as e:
        st.error(f"認証エラー: {e}")
else:
    st.warning("Secretsを設定してください")
