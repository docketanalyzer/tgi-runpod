import concurrent.futures
import time
from pathlib import Path
import requests
import runpod


# Waits up to 6mins for the server to start
for i in range(300):
    try:
        response = requests.get("http://127.0.0.1:80/health")
        print(response.status_code)
        if response.status_code == 200:
            break
    except requests.exceptions.ConnectionError:
        pass
    time.sleep(1)


def post(text, args):
    response = requests.post(
        "http://127.0.0.1:80/generate",
        json={
            "inputs": text,
            "parameters": args,
        },
    )
    return response.json()


def handler(event):
    texts = event['input']['prompt']
    if isinstance(texts, str):
        texts = [texts]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        responses = list(executor.map(post, texts, [event['input']['args']] * len(texts)))

    generated_text = [r['generated_text'] for r in responses]
    return {'generated_text': generated_text}


runpod.serverless.start({
    "handler": handler,
})

