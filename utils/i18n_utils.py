def get_translator(lang):
    dict = {
        "Japanese": {"Generate": "生成", "Sync Calendar": "カレンダー同期", "Download PDF": "PDFダウンロード"},
        "English": {"Generate": "Generate", "Sync Calendar": "Sync Calendar", "Download PDF": "Download PDF"}
    }
    return lambda key: dict[lang].get(key, key)