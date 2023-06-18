import numpy as np
import pandas as pd

df = pd.read_csv("outputs/results_1000.csv", index_col=[0])

for i in range(5):
    temp = df.sample(frac=1)
    temp.index = np.arange(len(temp))
    expanding_mean = np.array(temp.expanding(1).mean()).flatten()
    expanding_variance = np.array(temp.expanding(1).var()).flatten()
    results = pd.DataFrame({"mean": expanding_mean, "variance": expanding_variance}, index=temp.index)
    results.index.name = "index"
    results.to_csv(f"outputs/moments_convergence_shuffle_{i+1}.csv")
