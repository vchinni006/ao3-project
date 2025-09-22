import pandas as pd
# tags = pd.read_csv('tags-20210226.csv')
# works = pd.read_csv('works-20210226.csv')
# print(tags.head())
# print(tags.shape)
# print(tags.dtypes)

# tags = tags[~tags['name'].str.contains('Redacted', na=True)]
# print(tags.shape)
# print(tags.dtypes)

# tags['merger_id'] = tags['merger_id'].astype('Int64')
# print(tags.dtypes)

# tags.to_csv("tags_cleaned.csv", index=False)




# Read the cleaned tags file
df = pd.read_csv('tags_cleaned.csv')
print('Initial rows:', len(df))

# Ensure id and merger_id are treated as integers where possible
# merger_id may be NaN where not present

df['id'] = pd.to_numeric(df['id'], errors='coerce').astype('Int64')
if 'merger_id' not in df.columns:
    df['merger_id'] = pd.NA
else:
    df['merger_id'] = pd.to_numeric(df['merger_id'], errors='coerce').astype('Int64')

# cached_count might be numeric but could be strings; coerce to int
if df['cached_count'].dtype == 'object':
    df['cached_count'] = pd.to_numeric(df['cached_count'], errors='coerce').fillna(0).astype(int)
else:
    df['cached_count'] = df['cached_count'].fillna(0).astype(int)

# Build a mapping from id to row index
id_to_index = {int(r['id']): i for i, r in df.dropna(subset=['id']).iterrows()}

merged_rows = []
# Iterate rows that have merger_id
for i, row in df[df['merger_id'].notna()].iterrows():
    src_id = int(row['id'])
    target_id = int(row['merger_id'])
    src_count = int(row['cached_count'])
    if target_id in id_to_index:
        tgt_idx = id_to_index[target_id]
        # add src_count to target
        df.at[tgt_idx, 'cached_count'] = int(df.at[tgt_idx, 'cached_count']) + src_count
        merged_rows.append(i)
    else:
        print(f'Warning: target id {target_id} for row id {src_id} not found; skipping')

print('Merged rows count:', len(merged_rows))
# Drop merged rows
df_merged = df.drop(index=merged_rows).reset_index(drop=True)


# Write to new CSV
df_merged.to_csv('tags_cleaned_merged.csv', index=False)


# Quick verification: ensure total cached_count is same as original
orig_sum = df['cached_count'].sum()
new_sum = df_merged['cached_count'].sum()
print('Original total cached_count:', orig_sum)
print('New total cached_count:', new_sum)