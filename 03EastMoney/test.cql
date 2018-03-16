USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/01JuChao/data/brief.csv' AS line

CREATE (company:Company { name : line.company })
SET company.share_code  = line.share_code,
    company.英文名      = line.english_name,
    company.简称    = line.shortname,
    company.邮政编码   = line.`post code`,
    company.公司电话   = line.telephone,
    company.公司传真   = line.fax,
    company.公司网址   = line.website,
    company.上市时间   = line.`listed time`,
    company.招股时间   = line.`prospectus time`
;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/01JuChao/data/manager.csv' AS line

WITH line
MERGE (
  people:Person
  {
    姓名:line.name,
    出生年份:line.birth_year,
    性别:line.gender,
    学历:line.education_background
  }
)

WITH people, line
MATCH (company:Company)
WHERE company.share_code = line.share_code
WITH people, company, line
CREATE (people)-[r:任职]->(company)
SET r.职务 = line.position
;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/03EastMoney/data/CompanySurvey/jbzl.csv' AS line

WITH line
MERGE (
  m:Org
  {
    name: line.律师事务所,
    type: '律师事务所'
  }
)

MERGE (
  n:Org
  {
    name: line.会计师事务所,
    type: '会计师事务所'
  }
)
;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/03EastMoney/data/CompanySurvey/jbzl.csv' AS line

WITH line
MATCH (a:Org) WHERE a.name = line.会计师事务所
WITH line, a
MATCH (b:Company) WHERE b.share_code = line.公司代码
WITH a, b
MERGE (a)-[r:服务]->(b)
;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/03EastMoney/data/CompanySurvey/jbzl.csv' AS line

WITH line
MERGE (
  m:Org
  {
    name: line.律师事务所,
    type: '律师事务所'
  }
)

MERGE (
  n:Org
  {
    name: line.会计师事务所,
    type: '会计师事务所'
  }
)
;

MERGE (
  m:Org
  {
    name: '深圳证券交易所',
    type: '上市交易所'
  }
)
;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/03EastMoney/data/CompanySurvey/jbzl.csv' AS line

WITH line
MATCH (company:Company {share_code: line.公司代码})
WITH line, company
MATCH (a:Org {name: line.上市交易所})
WITH company, a
MERGE (company)-[r:上市]->(a)
;


MATCH (n:Company)
WHERE NOT EXISTS (n.name)
DETACH DELETE n
;

MATCH (n) WITH n LIMIT 250 MATCH (m)-->(n) RETURN m, n;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/03EastMoney/data/ShareHoldersResearch/jjcg.csv' AS line

WITH line
MERGE (
  f:Fund
  {
    简称: line.基金名称,
    基金代码: line.基金代码
  }
)

MATCH (c: Company {share_code: line.公司代码})
WITH f, c
MERGE (f)-[r:持股]->(c)
