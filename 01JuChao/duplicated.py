import pandas as pd

df = pd.read_csv('./data/shareholder.csv')
check = df.drop(columns=['percent','share_code','share_type','value'])
check['duplicated'] = check.duplicated('shareholder')
check_dup = check[check['duplicated']]


df = pd.read_csv('./data/brief.csv',dtype={'share_code':str, 'Circulation':str, 'PE ration':str})
check = df.drop_duplicates(subset=['company', 'shortname'])
check.to_csv('./data/brief1.csv', index=False)

df = pd.read_csv('./data/manager.csv', dtype={'share_code':str})
check = df.drop_duplicates(subset=['name', 'position', 'birth_year', 'gender', 'education_background'])
check.to_csv('./data/manager1.csv', index=False)


df = pd.read_csv('./data/shareholder.csv', dtype={'value':str, 'percent':str, 'share_code':str}, skip_blank_lines=True)
check = df.drop_duplicates(subset=['shareholder', 'value', 'percent'])
check.to_csv('./data/shareholder1.csv', index=False)


df = pd.read_csv('./data/share_person.csv')
df['duplicated'] = df.duplicated('shareholder')
df_dup = df[df['duplicated']]
