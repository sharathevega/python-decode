# encode.py
import zlib
import base64
import json

def compress_json(data: dict) -> str:
    try:
        json_str = json.dumps(data, separators=(",", ":"))
        compressed = zlib.compress(json_str.encode("utf-8"))[2:-4]
        encoded = base64.b64encode(compressed).decode("utf-8")
        return encoded
    except Exception as e:
        return f"Compression failed: {e}"
