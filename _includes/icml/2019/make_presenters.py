import pandas as pd
import numpy as np
import os

df = pd.read_csv('acceptedPapers.csv')

print(df.head())
print(list(df))
lstOfCols = ['Author.Names','Institution','First.Name','Paper.Title','Presentation.Type']

df = df[lstOfCols].replace(np.nan, '', regex=True).sort_values("Author.Names")

cnt = 1
for idx, row in df.iterrows():
  if row['Presentation.Type'] == 'an oral':
    md_file = open("../../_posts/2019_ICML_speakers/2019-04-01-"+row['First.Name']+"-"+str(cnt)+".md", "w")
    md_file.write('---\n')
    md_file.write('name: '+row['Author.Names']+'\n')
    md_file.write('title: '+row['Institution']+'\n')
    md_file.write('modal-id: 1'+'\n')
    md_file.write('img: default.jpg'+'\n')
    md_file.write('alt: Picture of '+row['First.Name']+'\n')
    md_file.write("topic: '"+row['Paper.Title']+"'\n")
    md_file.write('bio: \n')
    md_file.write('website: \n')
    md_file.write('tags: oral-icml2019\n')
    md_file.write('featuredOrder: '+str(cnt)+'\n')
    md_file.write('---')
    md_file.close()
    cnt += 1

  else:
    print("      <li><strong>"+row['Author.Names']+"</strong>, "+row['Institution']+": <em>"+row['Paper.Title']+"</em></li>")
