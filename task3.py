from datasets import load_dataset
import pandas as pd

ds = load_dataset("hao-li/AIDev", "pr_task_type", split="train")

task3_df = pd.DataFrame({
    "PRID": ds["id"],
    "PRTITLE": ds["title"],
    "PRREASON": ds["reason"],
    "PRTYPE": ds["type"],
    "CONFIDENCE": ds["confidence"],
})

task3_df.to_csv(
    "task3.csv",
    index=False,
    encoding="utf-8",
    quoting=1 
)
