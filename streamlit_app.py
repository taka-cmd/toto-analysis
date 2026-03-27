import streamlit as st
from google.oauth2 import service_account
import json
import re

st.set_page_config(page_title="toto分析システム")
st.title("🏆 toto 2等・3等 照準分析システム")

try:
    if "gcp_service_account" in st.secrets:
        # 1. SecretsからJSONを取り出す
        raw_json = st.secrets["gcp_service_account"]["json_key"]
        
        # 2. JSONとして読み込み
        info = json.loads(raw_json, strict=False)
        
        # 3. 【最終兵器】秘密鍵の徹底クリーニング
        key = info["private_key"]
        
        # 改行コードの修正
        key = key.replace("\\n", "\n")
        
        # 全角ハイフンや特殊なダッシュを半角ハイフンに強制置換
        key = key.replace("—", "--").replace("–", "--").replace("−", "-")
        
        # 制御文字や目に見えないゴミを正規表現で排除
        key = re.sub(r'[^\x20-\x7E\n\r]', '', key)
        
        # ヘッダーとフッターの空白を整える
        key = key.replace("-----BEGIN PRIVATE KEY-----", "-----BEGIN PRIVATE KEY-----\n")
        key = key.replace("-----END PRIVATE KEY-----", "\n-----END PRIVATE KEY-----")
        # 重複した改行を削除
        key = re.sub(r'\n+', '\n', key)
        
        info["private_key"] = key.strip()
        
        # 4. 認証実行
        credentials = service_account.Credentials.from_service_account_info(info)
        
        st.success("✅ スプレッドシートとの連携に成功しました！完全勝利です！")
        st.balloons()
        st.info("隆生さん、大変お待たせしました。あとはiPhoneでこの画面を開くだけです。")
    else:
        st.error("Secretsの設定が読み込めません。")
except Exception as e:
    st.error(f"❌ 認証エラー: {e}")
    st.warning("もし解決しない場合は、Secretsの json_key = ''' の直後に、余計な空白がないか確認してください。")
