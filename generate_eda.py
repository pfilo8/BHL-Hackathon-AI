import os
import sys

import pandas as pd
import sweetviz as sv


def save_analysis(report, activity_name):
    report.show_html(filepath=os.path.join('reports', f'{activity_name}-analysis.html'), open_browser=False)


if __name__ == '__main__':
    data_file_path = sys.argv[1]
    df = pd.read_csv(data_file_path)
    df = df.drop('Unnamed: 0', axis=1)

    unique_activities = df['Activity'].unique()
    report = sv.analyze(df, pairwise_analysis='off')
    save_analysis(report, 'ALL')

    for activity in unique_activities:
        df_activity = df[df['Activity'] == activity]
        report = sv.analyze(df_activity, pairwise_analysis='off')
        report.show_html(filepath=os.path.join('reports', f'{activity}-analysis.html'))
