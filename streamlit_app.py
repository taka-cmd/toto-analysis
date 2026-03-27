import streamlit as st
from google.oauth2 import service_account
import textwrap
import re

st.set_page_config(page_title="toto分析システム")
st.title("🏆 toto 2等・3等 照準分析システム")

if "gcp_service_account" in st.secrets:
    try:
        info = dict(st.secrets["gcp_service_account"])
        
        # 1. 隆生さんが貼り付けた生データを取り出す
        raw_key = str(info["private_key"])
        
        # 2. 中身だけを抽出（ヘッダー、フッター、改行、スペースを一旦全部消す）
        body = raw_key.replace("-----BEGIN PRIVATE KEY-----", "").replace("-----END PRIVATE KEY-----", "")
        body = body.replace("\\n", "").replace("\n", "").replace(" ", "").strip()
        
        # 3. 【RFC 1421準拠】64文字ごとに強制改行を入れる
        # 隆生さんが何文字で貼り付けても、ここで「1行64文字」に直します
        formatted_body = "\n".join(textwrap.wrap(body, 64))
        
        # 4. 正しいPEM形式（ヘッダー＋整形済み中身＋フッター）に組み立て直す
        info["private_key"] = f"-----BEGIN PRIVATE KEY-----\n{formatted_body}\n-----END PRIVATE KEY-----\n"
        
        # 5. 認証実行
        credentials = service_account.Credentials.from_service_account_info(info)
        
        st.success("✅ ついにPEM規格の壁を突破しました！成功です！")
        st.balloons()
        st.info("隆生さん、本当にお疲れ様でした。これでPCを閉じて大丈夫です！")
        
    except Exception as e:
        st.error(f"❌ 認証エラー: {e}")
        st.warning("鍵のコピペが途中で切れていないかだけ確認してください。")
else:
    st.error("❌ Secretsが設定されていません。")
