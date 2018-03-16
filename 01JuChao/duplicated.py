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

df = pd.read_csv('./jjcg.csv',dtype={'基金代码':str, '公司代码':str})
df['持股数(股)'].replace(',','',inplace=True, regex=True)
df['持股数(股)'] = pd.to_numeric(df['持股数(股)'], errors='raise', downcast='integer')
df['持仓市值(元)'].replace(',','',inplace=True, regex=True)
df.to_csv('./jjcg_dup.csv', index=False)


df = pd.read_csv('./sdltgd.csv',dtype={'code':str})
df['持股数(股)'].replace(',','',inplace=True, regex=True)
check = df.drop(columns=['名次'])
people = check[check['股东性质']=='个人']
other = check[check['股东性质'] != '个人']
people.to_csv('./grengd.csv', index=False)
other.to_csv('./qitagd.csv', index=False)


```
分类

基金资产管理计划
信托计划
证券投资基金
保险产品
全国社保基金
'计划'

------------------

证券公司
投资公司


```

other = check[check['股东性质'] != '个人']
other.to_csv('./tuantigd.csv', index=False)
trust1 = other[other['股东性质'].isin(['基金资产管理计划', '信托计划', '证券投资基金', '保险产品', '全国社保基金', '集合理财计划'])]
trust1.to_csv('./trust1.csv', index=False)
untrust1 = other[~(other['股东性质'].isin(['基金资产管理计划', '信托计划', '证券投资基金', '保险产品', '全国社保基金', '集合理财计划']))]
untrust1.to_csv('./untrust1.csv', index=False)
trust2 = untrust1[untrust1['股东名称'].str.contains('计划')]
trust2.to_csv('./trust2.csv', index=False)
untrust2 = untrust1[~(untrust1['股东名称'].str.contains('计划'))]
untrust2.to_csv('./untrust2.csv', index=False)
foreigner = untrust2[untrust2['股东名称'].str.contains('[a-zA-Z]')]
untrust3 = untrust2[~(untrust2['股东名称'].str.contains('[a-zA-Z]'))]
foreigner.to_csv('./foreigner.csv', index=False)
untrust3.to_csv('./untrust3.csv', index=False)
inmain = foreigner[foreigner['股东名称'].str.contains('[\u4E00-\u9FA5]')]
foreign = foreigner[~foreigner['股东名称'].str.contains('[\u4E00-\u9FA5]')]
foreign.to_csv('./foreign.csv', index=False)
trust3 = inmain[inmain['股东名称'].str.contains('基金|财产专户')]
untrust4 = inmain[~inmain['股东名称'].str.contains('基金|财产专户')]
trust3.to_csv('./trust3.csv', index=False)
untrust4.to_csv('./untrust4.csv', index=False)
trust4 = foreign[foreign['股东名称'].str.contains('FOUNDATION TRUST|FUND')]
trust4.to_csv('./trust4.csv', index=False)
trust = [trust1, trust2, trust3, trust4]
trust = pd.concat(trust)
trust.to_csv('./trust.csv', index=False)
untrust5 = foreign[~foreign['股东名称'].str.contains('FOUNDATION TRUST|FUND')]
untrust = [untrust3, untrust4, untrust5]
untrust = pd.concat(untrust)
untrust.to_csv('./untrust.csv', index=False)


####

df = pd.read_csv('./grengd.csv', dtype={'code':str})
check = df[df['日期']=='2017-09-30']
check.to_csv('./grengd_170930.csv', index=False)

df = pd.read_csv('./trust.csv', dtype={'code':str})
check = df[df['日期']=='2017-09-30']
check.to_csv('./fundgd_170930.csv', index=False)

df = pd.read_csv('./untrust.csv', dtype={'code':str})
check = df[df['日期']=='2017-09-30']
check.to_csv('./cmgd_170930.csv', index=False)


selfhold = check[check['股东名称'].str.contains('自有资金')]
selfhold.to_csv('./cmgdselfhold_170930.csv', index=False)
leaf = check[~check['股东名称'].str.contains('自有资金')]
leaf.to_csv('./cmgd_170930.csv', index=False)
