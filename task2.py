from datasets import load_dataset
import pandas as pd

ds = load_dataset("hao-li/AIDev", "all_repository", split="train")

task2_df = pd.DataFrame({
    "REPOID": ds["id"],
    "LANG": ds["language"],
    "STARS": ds["stars"],
    "REPOURL": ds["url"],
})

task2_df.to_csv(
    "task2.csv",
    index=False,
    encoding="utf-8",
    quoting=1 
)
