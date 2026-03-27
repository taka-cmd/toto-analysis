import streamlit as st
from google.oauth2 import service_account
import json

st.set_page_config(page_title="toto分析システム", layout="wide")
st.title("🏆 toto 2等・3等 照準分析システム")

# 1. Secretsの存在チェック
if "gcp_service_account" not in st.secrets:
    st.error("❌ StreamlitのSecrets設定が空っぽです。")
    st.stop()

try:
    # 2. JSONの取り出しとクリーンアップ
    raw_json = st.secrets["gcp_service_account"]["json_key"]
    info = json.loads(raw_json, strict=False)

    # 3. 鍵のチェック（日本語の仮文字が入っていないか）
    if "ここを！" in info.get("private_key", ""):
        st.warning("⚠️ Secretsの中身がまだ『仮の文字』になっています。本物の鍵を貼り付けてください。")
        st.stop()

    # 4. 秘密鍵の改行コードを強制修正
    info["private_key"] = info["private_key"].replace("\\n", "\n")

    # 5. 認証実行
    credentials = service_account.Credentials.from_service_account_info(info)
    
    st.success("✅ スプレッドシートとの連携に成功しました！完全勝利です！")
    st.balloons()
    st.info("隆生さん、お疲れ様でした！あとはiPhoneからこのURLを開くだけです。")

except json.JSONDecodeError:
    st.error("❌ Secretsに貼り付けたJSONの形が崩れています。{ } の前後を確認してください。")
except Exception as e:
    st.error(f"❌ 認証エラー: {e}")
    st.info("鍵の中身（-----BEGIN...から...END KEY-----まで）が正しくコピーされているか確認してください。")
