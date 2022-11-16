import pandas as pd

# Read the .csv to a dataframe
df = pd.read_csv('Cleaned_Laptop_data.csv')

# Make a new ID column
df['ID'] = df.index

# Create a processor df
df_proc = df[['processor_brand', 'processor_name', 'processor_gnrtn']].drop_duplicates().reset_index()
df_proc['ID'] = df_proc.index
df['proc'] = df['ID'].copy()

for i in range(len(df_proc)):
  df['proc'].iloc[i] = df_proc[(df_proc['processor_brand'] == df['processor_brand'].iloc[i]) 
  & (df_proc['processor_name'] == df['processor_name'].iloc[i]) 
  & (df_proc['processor_gnrtn'] == df['processor_gnrtn'].iloc[i])]['ID']

df.drop(columns=['processor_brand', 'processor_name', 'processor_gnrtn'])

# Visualize the mods
print(df.head())
print(df.columns)

# Save the dataframe to a new .csv
df.to_csv('new_laptop_data.csv', index=False)
df_proc.to_csv('proc.csv', index=False)