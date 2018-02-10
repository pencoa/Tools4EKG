
```
pipenv run python juchao2csv.py
```

### data文件介绍
- brief.csv 公司简介信息  
- manager.csv 公司高管信息
- shareholder.csv 十大股东信息
- company_list.csv 内地上市公司列表
- hk_company_list.csv 香港上市公司列表
- share_company.csv 企业股东信息
- share_fund.csv 基金股东信息
- share_person.csv 个体股东信息

### juchao2csv.py
download and store information from cninfo, storing them as csv file.

### CSVclassification.py
divide the shareholders into three groups based on rules.

### duplicated.py
using pandas to clean up the csv file.

### load.cql
cypher scripts to load csv into Neo4j via browser.
