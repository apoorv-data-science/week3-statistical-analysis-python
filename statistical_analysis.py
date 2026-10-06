import pandas as pd
from scipy import stats

df = pd.read_csv("student_performance_dataset.csv")
median_hours = df["study_hours"].median()
df["study_group"] = df["study_hours"].apply(lambda x: "High study" if x >= median_hours else "Low study")
high = df.loc[df["study_group"] == "High study", "exam_score"]
low = df.loc[df["study_group"] == "Low study", "exam_score"]
result = stats.ttest_ind(high, low, equal_var=False)
print("High-study mean:", round(high.mean(), 2))
print("Low-study mean:", round(low.mean(), 2))
print("t-statistic:", round(result.statistic, 3))
print("p-value:", result.pvalue)
print("95% confidence interval:", result.confidence_interval(.95))
print("Pearson correlation:", stats.pearsonr(df["study_hours"], df["exam_score"]))
