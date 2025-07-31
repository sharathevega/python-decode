# decode.py
import zlib
import base64
import json

def decompress_json(base64_str: str) -> dict:
    try:
        compressed = base64.b64decode(base64_str)
        decompressed = zlib.decompress(compressed, wbits=-15).decode("utf-8")
        return json.loads(decompressed)
    except Exception as e:
        return {"error": f"Decompression failed: {e}"}
