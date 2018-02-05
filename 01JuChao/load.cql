
// Uniqueness constraints.
CREATE CONSTRAINT ON (c:Company) ASSERT c.name IS UNIQUE;
CREATE CONSTRAINT ON (c:Company) ASSERT c.share_code IS UNIQUE;


// 加入公司信息
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///Users/randypen/Code/Tools4EKG/01JuChao/data/brief.csv' AS line

CREATE (company:Company { name : line.company })
SET company.share_code  = line.share_code,
    company.简称       = line.shortname,
    company.英文名      = line.english_name,
    company.主营业务    = line.`Principal activities`
;


// 加入公司高管信息，根据个人信息同名去重
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///Users/randypen/Code/Tools4EKG/01JuChao/data/manager.csv' AS line

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
CREATE (people)-[r:WORKON]->(company)
SET r.type = line.position
;


// 增加法人关系
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///Users/randypen/Code/Tools4EKG/01JuChao/data/brief.csv' AS line
WITH line
MATCH (company:Company{share_code:line.share_code})
WITH line, company
MERGE (people:Person { 姓名:line.legal_person } )-[r:WORKON]->(company)
WITH people, company
CREATE (people)-[r:法人]->(company)
;


// MATCH p=()-->()
// RETURN p;
//
// // 删除所有
// MATCH (n)
// DETACH DELETE n;
//
// MERGE (people:Person)-[r:WORKON]->(company:Company{share_code:"000001"})
// RETURN people
