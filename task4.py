from datasets import load_dataset
import pandas as pd

def clean_patch(patch):
    if patch is None:
        return ""
    return re.sub(r"[^\x00-\x7F]+", "", patch)   # remove non-ASCII

ds = load_dataset("hao-li/AIDev", "pr_commit_details", split="train")


task4_df = pd.DataFrame({
    "PRID": ds["pr_id"],
    "PRSHA": ds["sha"],
    "PRCOMMITMESSAGE": ds["message"],
    "PRFILE": ds["filename"],
    "PRSTATUS": ds["status"],
    "PRADDS": ds["additions"],
    "PRDELSS": ds["deletions"],
    "PRCHANGECOUNT": ds["changes"],
    "PRDIFF": [clean_patch(p) for p in ds["patch"]],
})

task4_df.to_csv(
    "task4.csv",
    index=False,
    encoding="utf-8",
    quoting=1 
)
