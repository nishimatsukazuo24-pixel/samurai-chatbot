# app.py

import streamlit as st
import google.generativeai as genai

# --- アプリの基本設定 ---
st.set_page_config(page_title="安全な侍チャットボット", page_icon="⚔️")
st.title("なりきり侍チャットボット ⚔️")

# --- 安全なAPIキー設定 ---
try:
    # StreamlitのSecrets管理機能からAPIキーを読み込む
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    st.success("APIキーの設定が完了しました。")
except Exception as e:
    st.error("エラー: APIキーを正しく設定してください。詳細はステップ2をご確認ください。")
    st.stop() # エラーがあればここで処理を停止

# --- UIとアプリのロジック ---
user_message = st.text_input("拙者になにか尋ねたいことはござるか？")

if st.button("送信いたす"):
    if user_message:
        # プロンプトの作成
        character_role = "あなたは江戸時代の侍です。古風な言葉遣いで、一人称は「拙者」、二人称は「お主」を使ってください。"
        prompt = f"{character_role} 以下の質問に答えなさい。\n\n質問: {user_message}"

        # APIを呼び出し、結果を表示
        with st.spinner("考えておりまする..."):
            response = model.generate_content(prompt)
            st.write(response.text)
    else:
        st.warning("何かメッセージを入力してくだされ。")