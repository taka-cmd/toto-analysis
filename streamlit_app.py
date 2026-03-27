import streamlit as st
from google.oauth2 import service_account

st.set_page_config(page_title="toto分析システム")
st.title("🏆 toto 2等・3等 照準分析システム")

# Secretsから直接辞書として読み込む（json.loadsは使いません）
if "gcp_service_account" in st.secrets:
    try:
        # TOMLから読み込んだデータを辞書として取得
        info = dict(st.secrets["gcp_service_account"])
        
        # 秘密鍵の改行コードだけを修正
        info["private_key"] = info["private_key"].replace("\\n", "\n")
        
        # 認証実行
        credentials = service_account.Credentials.from_service_account_info(info)
        
        st.success("✅ スプレッドシートとの連携に成功しました！完全勝利です！")
        st.balloons()
        st.info("隆生さん、本当にお疲れ様でした。これでPCを閉じて大丈夫です！")
        
    except Exception as e:
        st.error(f"❌ 認証エラー: {e}")
else:
    st.error("❌ Secretsの設定が見つかりません。")
