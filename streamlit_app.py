import streamlit as st
from google.oauth2 import service_account
import json
import re

st.set_page_config(page_title="toto分析システム")
st.title("🏆 toto 2等・3等 照準分析システム")

try:
    if "gcp_service_account" in st.secrets:
        # Secretsから辞書として取得
        info = dict(st.secrets["gcp_service_account"])
        
        # 秘密鍵を文字列として取り出し、徹底的に洗浄
        key = str(info["private_key"])
        
        # 【最重要】先頭と末尾の目に見えないゴミ（BOM、特殊スペース、改行）を物理的に削ぎ落とす
        key = key.strip().encode('utf-8').decode('utf-8-sig')
        
        # 鍵の中身にある「\\n」を本物の改行に変換し、余計な空白を詰める
        key = key.replace("\\n", "\n").replace(" ", "")
        
        # 鍵のヘッダーとフッターの形式をGoogleが喜ぶ形に強制整形
        key = key.replace("-----BEGINPRIVATEKEY-----", "-----BEGIN PRIVATE KEY-----\n")
        key = key.replace("-----ENDPRIVATEKEY-----", "\n-----END PRIVATE KEY-----")
        
        info["private_key"] = key
        
        # 認証実行
        credentials = service_account.Credentials.from_service_account_info(info)
        
        st.success("✅ ついに、ついに連携に成功しました！")
        st.balloons()
        st.info("隆生さん、本当にお疲れ様でした！今すぐiPhoneでURLを開いてください！")
    else:
        st.error("Secretsが設定されていません。")
except Exception as e:
    st.error(f"❌ 認証エラー: {e}")
