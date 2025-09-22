import pandas as pd
tags = pd.read_csv('tags-20210226.csv')
works = pd.read_csv('works-20210226.csv')
print(tags.head())
print(tags.shape)
print(tags.dtypes)

tags = tags[~tags['name'].str.contains('Redacted', na=True)]
print(tags.shape)
print(tags.dtypes)

tags['merger_id'] = tags['merger_id'].astype('Int64')
print(tags.dtypes)

tags.to_csv("tags_cleaned.csv", index=False)

