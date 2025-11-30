from datasets import load_dataset
import pandas as pd

ds = load_dataset("hao-li/AIDev", "all_pull_request", split="train")

def clean_text(x):
    if x is None:
        return ""
    x = str(x)
    x = x.replace("\r", " ")      
    x = x.replace("\n", "\\n")    
    x = x.replace(",", "<COMMA>") 
    x = x.replace('"', "'")      
    return x.strip()

task1_df = pd.DataFrame({
    "TITLE": [clean_text(x) for x in ds["title"]],
    "ID": ds["id"],
    "AGENTNAME": [clean_text(x) for x in ds["agent"]],
    "BODYSTRING": [clean_text(x) for x in ds["body"]],
    "REPOID": ds["repo_id"],
    "REPOURL": [clean_text(x) for x in ds["repo_url"]],
})

task1_df.to_csv(
    "task1_pull_requests.csv",
    index=False,
    encoding="utf-8",
    quoting=1   
)
