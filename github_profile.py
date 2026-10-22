import json
import sys
from pathlib import Path
from urllib.request import Request, urlopen

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

url = "https://api.github.com/users/qyxczm"
request = Request(url, headers={"User-Agent": "stage-0-practice"})

with urlopen(request, timeout=10) as response:
    profile = json.load(response)

result = f"GitHub 用户 {profile['login']} 当前拥有 {profile['followers']} 位粉丝！"
print(result)
Path("result.txt").write_text(result + "\n", encoding="utf-8")