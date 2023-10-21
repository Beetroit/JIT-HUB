
def summarize(doc):
    import json
    import requests
    import gc
    API_TOKEN='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'
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    def query(payload):
        data = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))
    data = query(
        {
            "inputs": str(doc),
            "parameters": {"do_sample": False},
        }
    )
    del doc
    gc.collect()
    return data