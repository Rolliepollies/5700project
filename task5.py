from datasets import load_dataset
import pandas as pd

keywords = [
    "race","racy","buffer","overflow","stack","integer","signedness","underflow",
    "improper","unauthenticated","gain access","permission","cross site","css",
    "xss","denial service","dos","crash","deadlock","injection","request forgery",
    "csrf","xsrf","forged","security","vulnerability","vulnerable","exploit",
    "attack","bypass","backdoor","threat","expose","breach","violate","fatal",
    "blacklist","overrun","insecure"
]

task1 = pd.read_csv("task1.csv")
task3 = pd.read_csv("task3.csv")

merged = task1.merge(task3, left_on="ID", right_on="PRID", how="left")

def detect_security(text):
    if not isinstance(text, str):
        return 0
    t = text.lower()
    return int(any(k in t for k in keywords))


merged["SECURITY"] = [
    max(detect_security(title), detect_security(body))
    for title, body in zip(merged["TITLE"], merged["BODYSTRING"])
]

task5_df = merged[[
    "ID",
    "AGENTNAME",
    "PRTYPE",
    "CONFIDENCE",
    "SECURITY"
]]

task5_df.rename(columns={
    "AGENTNAME": "AGENT",
    "PRTYPE": "TYPE"
}, inplace=True)

task5_df.to_csv(
    "task5.csv",
    index=False,
    encoding="utf-8",
    quoting=1 
)
