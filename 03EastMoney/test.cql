USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/penzm/Tools4EKG/03EastMoney/data/CompanySurvey/jbzl.csv' AS line

CREATE (company:Company { name : line.company })
SET company.share_code  = line.share_code,
    company.简称       = line.shortname,
    company.英文名      = line.english_name,
    company.主营业务    = line.`Principal activities`
;
