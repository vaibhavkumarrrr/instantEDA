import pandas as pd
from ydata_profiling import ProfileReport
df = pd.read_csv('nissan-dataset1.csv')
profile = ProfileReport(df, title="Profiling Report")
x=profile.to_file(output_file='nissan.html')
