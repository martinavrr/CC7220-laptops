import pandas as pd

# Read the .csv to a dataframe
df = pd.read_csv('Cleaned_Laptop_data.csv')
df = df.dropna()

regex='^[0-9]*$'
df= df[df.ram_gb.str.match(regex)]

# Make a new ID column
df['ID'] = df.index

# Create a processor df
df_cpu = df[['processor_brand', 'processor_name', 'processor_gnrtn']].drop_duplicates()
df_cpu.insert(0, 'ID', df_cpu.index)
df['cpu'] = df['ID'].copy()

for i in range(len(df_cpu)):
  df['cpu'].iloc[i] = df_cpu[(df_cpu['processor_brand'] == df['processor_brand'].iloc[i]) 
  & (df_cpu['processor_name'] == df['processor_name'].iloc[i]) 
  & (df_cpu['processor_gnrtn'] == df['processor_gnrtn'].iloc[i])]['ID']

# Create a ram df
df_ram = df[['ram_gb', 'ram_type']].drop_duplicates()
df_ram.insert(0, 'ID', df_ram.index)
df['ram'] = df['ID'].copy()

for i in range(len(df_ram)):
  df['ram'].iloc[i] = df_ram[(df_ram['ram_gb'] == df['ram_gb'].iloc[i]) 
  & (df_ram['ram_type'] == df['ram_type'].iloc[i])]['ID']

# Create a OS df
df_os = df[['os', 'os_bit']].drop_duplicates()
df_os.insert(0, 'ID', df_os.index)
df['os_type'] = df['ID'].copy()

for i in range(len(df_os)):
  df['os_type'].iloc[i] = df_os[(df_os['os'] == df['os'].iloc[i]) & (df_os['os_bit'] == df['os_bit'].iloc[i])]['ID']

# Create a review df
df_review = df[['star_rating', 'ratings', 'reviews']].drop_duplicates()
df_review.insert(0, 'ID', df_review.index)
df['review'] = df['ID'].copy()

for i in range(len(df_review)):
  df['review'].iloc[i] = df_review[(df_review['star_rating'] == df['star_rating'].iloc[i]) 
  & (df_review['ratings'] == df['ratings'].iloc[i])
  & (df_review['reviews'] == df['reviews'].iloc[i])]['ID']

# Create a price df
df_price = df[['latest_price']].drop_duplicates()
df_price.insert(0, 'ID', df_price.index)
df['price'] = df['ID'].copy()

for i in range(len(df_price)):
  df['price'].iloc[i] = df_price[(df_price['latest_price'] == df['latest_price'].iloc[i])]['ID']

df_price = df_price.rename(columns={'latest_price': 'INR', 'ID': 'ID'})

df_price['USD'] = 0.012 * df_price['INR']

# Drop unused columns
df = df.drop(columns=[
  'processor_brand',
  'processor_name', 
  'processor_gnrtn', 
  'ram_gb', 
  'ram_type',
  'os', 
  'os_bit',
  'star_rating', 
  'ratings', 
  'reviews',
  'latest_price',
  'discount',
  'old_price'])


# Visualize the mods
print(df.head())
print(df.columns)

# Save the dataframes to .csv
df.to_csv('laptop_data.csv', index=False)
df_cpu.to_csv('cpu.csv', index=False)
df_ram.to_csv('ram.csv', index=False)
df_os.to_csv('os.csv', index=False)
df_review.to_csv('review.csv', index=False)
df_price.to_csv('price.csv', index=False)