import pandas as pd
import jieba

df = pd.read_csv('./data/CompanyManagement/RptManagerList.csv')
exps = df['经历'].tolist()


with open("./data/person_resume.txt", 'a') as f:
    for exp in exps:
        f.write(exp + '\n')

with open("./data/person_resume01.txt", 'a') as f:
    for exp in exps:
        seg_list = jieba.cut(exp, cut_all=False)
        f.write("\n".join(seg_list)+"\n")
