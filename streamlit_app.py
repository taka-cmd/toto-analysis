import streamlit as st
from google.oauth2 import service_account
import textwrap

st.set_page_config(page_title="toto分析システム")
st.title("🏆 toto 2等・3等 照準分析システム")

try:
    if "gcp_service_account" in st.secrets:
        info = dict(st.secrets["gcp_service_account"])
        raw_key = str(info["private_key"])
        
        # 1. まず、すでにあるヘッダー、フッター、改行、空白をすべて消して「純粋な中身」だけにする
        body = raw_key.replace("-----BEGIN PRIVATE KEY-----", "").replace("-----END PRIVATE KEY-----", "")
        body = body.replace("\\n", "").replace("\n", "").replace(" ", "").strip()
        
        # 2. 【最重要】PEMのルール通り、64文字ごとに改行を入れる
        # これをやらないと InvalidData エラーが出続けます
        formatted_body = "\n".join(textwrap.wrap(body, 64))
        
        # 3. 正しいヘッダーとフッターで包み直す
        info["private_key"] = f"-----BEGIN PRIVATE KEY-----\n{formatted_body}\n-----END PRIVATE KEY-----\n"
        
        # 4. 認証実行
        credentials = service_account.Credentials.from_service_account_info(info)
        st.success("✅ ついに、PEM形式の壁を突破しました！成功です！")
        st.balloons()
        st.info("隆生さん、本当にお待たせしました。これでPCを閉じて大丈夫です！")
    else:
        st.error("Secretsが設定されていません。")
except Exception as e:
    st.error(f"❌ 認証エラー: {e}")
