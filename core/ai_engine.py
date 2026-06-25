import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TEMPLATES = {
    "Business": "プロのビジネス秘書として、成果・課題・予定を構造化せよ。",
    "Concise": "要点のみを箇条書きで3行以内でまとめよ。",
    "Weekly": "KPT形式（Keep, Problem, Try）で今週の振り返りを作成せよ。"
}

def generate_report(memo, style="Business"):
    prompt = TEMPLATES.get(style, TEMPLATES["Business"])
    res = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": memo}]
    )
    return res.choices[0].message.content