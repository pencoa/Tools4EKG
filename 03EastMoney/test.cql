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
MATCH (b:Company) WHERE b.share_code = line.公司代码
WITH split(line.律师事务所, ',') as splitted, b
UNWIND range(0, size(splitted)-1) as i
MERGE (
  m:Org
  {
    name: splitted[i],
    type: '律师事务所'
  }
)
MERGE (m)-[r:服务]->(b)
;

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/03EastMoney/data/CompanySurvey/jbzl.csv' AS line

WITH line
MATCH (b:Company) WHERE b.share_code = line.公司代码
WITH split(line.会计师事务所, ',') as splitted, b
UNWIND range(0, size(splitted)-1) as i
MERGE (
  m:Org
  {
    name: splitted[i],
    type: '会计师事务所'
  }
)
MERGE (m)-[r:服务]->(b)
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
'file:///home/penzm/Tools4EKG/03EastMoney/data/ShareHoldersResearch/jjcg_dup.csv' AS line

WITH line
MERGE (
  f:Fund
  {
    简称: line.基金名称,
    基金代码: line.基金代码
  }
)
WITH line, f
MATCH (c: Company {share_code: line.公司代码})
WITH f, c, line
MERGE (f)-[r:持股]->(c)
SET r.日期 = line.日期,
    r.`持股数(股)` = line.`持股数(股)`,
    r.`持仓市值(元)` = line.`持仓市值(元)`,
    r.占总股本比 = line.占总股本比,
    r.占流通比 = line.占流通比,
    r.占净值比 = line.占净值比,
    r.持仓 = line.持仓
;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/03EastMoney/data/ShareHoldersResearch/grengd_170930.csv' AS line

WITH line
MATCH (c: Company {share_code: line.code})
WITH line, c
MATCH (p: Person)-[r:任职]->(c)
WHERE p.姓名 = line.股东名称
WITH line, c, p
MERGE (p)-[r:持股]->(c)
SET r.日期 = line.日期,
    r.股份类型 = line.股份类型,
    r.`持股数(股)` = line.`持股数(股)`,
    r.占流通比 = line.占总流通股本持股比例
;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/03EastMoney/data/ShareHoldersResearch/fundgd_170930.csv' AS line

WITH line
MATCH (c: Company {share_code: line.code})
WITH line, c
MERGE (
  f:Fund
  {
    名称: line.股东名称,
    性质: line.股东性质
  }
)
WITH line, c, f
MERGE (f)-[r:持股]->(c)
SET r.日期 = line.日期,
    r.股份类型 = line.股份类型,
    r.`持股数(股)` = line.`持股数(股)`,
    r.占流通比 = line.占总流通股本持股比例
;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/03EastMoney/data/ShareHoldersResearch/cmgd_170930.csv' AS line

WITH line
MATCH (c: Company {share_code: line.code})
WITH line, c
MERGE (
  d:Company
  {
    name: line.股东名称
  }
)
WITH line, c, d
MERGE (d)-[r:持股]->(c)
SET r.日期 = line.日期,
    r.股份类型 = line.股份类型,
    r.`持股数(股)` = line.`持股数(股)`,
    r.占流通比 = line.占总流通股本持股比例
;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/01JuChao/data/brief.csv' AS line

WITH line
MATCH (c: Company {share_code: line.share_code})
WITH split(line.主承销商, ' ') as splitted, c
UNWIND range(0, size(splitted)-1) as i
MERGE (m:Company {name: splitted[i]})
MERGE (c)-[r:主承销商]->(m)
;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/01JuChao/data/brief.csv' AS line

WITH line
MATCH (c: Company {share_code: line.share_code})
WITH split(line.上市推荐人, ' ') as splitted, c
UNWIND range(0, size(splitted)-1) as i
MERGE (m:Company {name: splitted[i]})
MERGE (c)-[r:上市推荐人]->(m)
;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/01JuChao/data/brief.csv' AS line

WITH line
MATCH (c: Company {share_code: line.share_code})
WITH split(line.保荐机构, ' ') as splitted, c
UNWIND range(0, size(splitted)-1) as i
MERGE (m:Company {name: splitted[i]})
MERGE (c)-[r:保荐机构]->(m)
;


MATCH (c:Company)
WHERE ID(c) = 96086
DETACH DELETE c
;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/03EastMoney/data/CompanySurvey/jbzl.csv' AS line

WITH line
MATCH (c:Company {share_code: line.公司代码})
WITH line, c
SET c.曾用名 = line.曾用名,
    c.`A股代码` = line.`A股代码`,
    c.`A股简称` = line.`A股简称`,
    c.`B股代码` = line.`B股代码`,
    c.`B股简称` = line.`B股简称`,
    c.`H股代码` = line.`H股代码`,
    c.`H股简称` = line.`H股简称`,
    c.`证券类别` = line.`证券类别`
;

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/01JuChao/data/brief.csv' AS line

WITH line
MATCH (c:Company {share_code: line.share_code})
WITH line, c
SET c.行业种类 = line.`Principal activities`
;
