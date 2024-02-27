import base64
import hashlib
import hmac
import json
import time
import re
import os
import logging
from mitmproxy import http, ctx

def JWT_Token():
    payload = {
      "deviceId": "19kic05ge2j2aeai",
      "appVersion": "1.19",
      "platform": "android",
      "applicationBuildCode": "35",
      "originalDeviceId": None,
      "iat": int(time.time()),
      "exp": int(time.time()) + 30
    }
    enc_payload = base64.urlsafe_b64encode(json.dumps(payload).encode("utf-8")).decode("utf-8")
    header = {"alg": "HS256", "typ": "JWT"}
    enc_header = base64.urlsafe_b64encode(json.dumps(header).encode("utf-8")).decode("utf-8")
    msg = f"{enc_header}.{enc_payload}"
    sign = hmac.new(b"site-secret#Nerd!01", msg.encode("utf-8"), hashlib.sha256).digest()
    enc_sign = base64.urlsafe_b64encode(sign).decode("utf-8").rstrip("=")
    token = f"{enc_header}.{enc_payload}.{enc_sign}"
    return token

class AI_mate:
    api = "https://prod.aimate.online/v1/api/"
    def request(self, flow: http.HTTPFlow) -> None:
        if not self.api in flow.request.pretty_url:
            ...
        else:
            match flow.request.pretty_url.split("/")[-1]:
                case "create-user":
                  try:
                    data = json.loads(flow.request.text)
                    data["deviceId"] = "19kic05ge2j2aeai"
                    flow.request.text = json.dumps(data)
                    flow.request.headers["authorization"] = f"Bearer {JWT_Token()}"
                  except json.JSONDecodeError:
                    ctx.log.error("Zzz")
                case "conversations":
                    flow.request.headers["authorization"] = f"Bearer {JWT_Token()}"
                case "resume":
                    flow.request.headers["authorization"] = f"Bearer {JWT_Token()}"
                    
addons = [AI_mate()]

def websocket_message(flow: http.HTTPFlow):
    message = flow.websocket.messages[-1]
    dec = message.content.decode('utf-8')
    if "token" in dec:
        mod_bytes = re.sub(r'"token":\s*"([^"]*)"', '"token": "%s"' % JWT_Token(), dec, flags=re.DOTALL).encode("utf-8")
        message.content = mod_bytes
