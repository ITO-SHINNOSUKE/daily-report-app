import os
from openai import OpenAI

# 明示的に環境変数を指定してクライアントを作成します
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def generate_report(memo):
    try:
        # 念のためキーが取得できているか確認するログ（デバッグ用）
        print(f"DEBUG: Key loaded: {os.environ.get('OPENAI_API_KEY')[:5]}...") 
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "あなたは優秀な秘書です。"},
                {"role": "user", "content": memo}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"