import jsonlines
import numpy as np
import sys
import pandas as pd
import json
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud
from pprint import pprint
import gensim.corpora as corpora
import gensim
from gensim.utils import simple_preprocess
#import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords


metadata = []
data = []
paper_text = []
year = []
type = []
authors = []
dir = "D:\\2222222222\ML4B\Digital_Twin_Scientific_Papers.jl"

with jsonlines.open(dir) as reader:
    for obj in reader:
        if obj['relevant'] == True:
            data.append(obj['metadata']['data'])
            metadata.append(obj['metadata_extract'])
            paper_text.append(obj['paper_text'])
            year.append(obj['metadata_extract']['year'])
            type.append(obj['metadata_extract']['item_type'])
            authors.append(obj['metadata_extract']['authors'])

name = []
for names in authors:
    for n in names:
        name.append(n['fullName'])

df_metadata = pd.DataFrame(metadata)
df_data = pd.DataFrame(data)
df_pText = pd.DataFrame(paper_text)
df_year = pd.DataFrame(year)
df_type = pd.DataFrame(type)
df_name = pd.DataFrame(name)
print(df_type.value_counts())
papers = pd.concat([df_year[0:5], df_metadata.title[0:5], df_metadata.abstract[0:5], df_pText[0:5]], axis=1 )


papers['title_processed'] = \
papers.iloc[:,1].map(lambda x: re.sub('[,\\.!?]', '', x))
papers['abstract_processed'] = \
papers.iloc[:,2].map(lambda x: re.sub('[,\\.!?]', '', x))
papers['text_processed'] = \
papers.iloc[:,3].map(lambda x: re.sub('[,\\.!?]', '', x))


papers['title_processed'] = \
papers.iloc[:,1].map(lambda x: x.lower())
papers['abstract_processed'] = \
papers.iloc[:,2].map(lambda x: x.lower())
papers['text_processed'] = \
papers.iloc[:,3].map(lambda x: x.lower())

bars= pd.Series(year).unique()
y_pos= df_year.value_counts()
x_pos = np.arange(len(bars))
plt.figure(figsize=(15,7))
plt.bar(x_pos, y_pos,  width=0.5)#color=('rgbkymc')[::-1],
plt.xticks(x_pos, bars)
plt.title("Number of published articles in one year")
plt.xlabel("Year")
plt.ylabel("Quantity")
for index, value in enumerate(y_pos):
    plt.text(index, value, str(value))

labels= pd.Series(type).unique()
sizes = df_type.value_counts()
explode = (0.0, 0.1)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels,  autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Article type")



string_list = []
for i in df_name.value_counts()[0:10].index.tolist():
    string_list.append(str(i)[2:-3])


bars = pd.Series(string_list)
y_pos = np.arange(len(bars))
x_pos= df_name.value_counts()[0:10]
plt.figure(figsize=(15,7))
plt.barh(y_pos, x_pos,  )
plt.yticks(y_pos, bars)
plt.ylabel("Name")
plt.gca().invert_yaxis()
plt.xticks(x_pos)
plt.xlabel("Articles written")
plt.title("Top 10 authors with most articles")
#for index, value in enumerate(x_pos):
#    plt.text(index, value, str(value))
plt.show()

"""long_string_title = ','.join(list(papers['title_processed'].values))
long_string_abstract = ','.join(list(papers['abstract_processed'].values))
long_string_text = ','.join(list(papers['text_processed'].values))


wordcloud_title = WordCloud(width=1200, height= 600,background_color="white", contour_width=3, contour_color='steelblue', max_words=400)
wordcloud_abstract = WordCloud(width=1200, height= 600,background_color="white", contour_width=3, contour_color='steelblue', max_words=400)
wordcloud_text = WordCloud(width=1200, height= 600,background_color="white", contour_width=3, contour_color='steelblue', max_words=400)


wordcloud_title.generate(long_string_title)
wordcloud_abstract.generate(long_string_abstract)
wordcloud_text.generate(long_string_text)


plt.imshow(wordcloud_title.to_image())
plt.axis("off")
plt.show()
plt.imshow(wordcloud_abstract.to_image())
plt.axis("off")
plt.show()
plt.imshow(wordcloud_text.to_image())
plt.axis("off")
plt.show()"""

"""
stop_words = stopwords.words('english')
stop_words.extend(['threee','well','based','twin','digital','from', 'subject', 're', 'edu', 'use'])

def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))

def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc))
             if word not in stop_words] for doc in texts]


title_data = papers.title_processed.values.tolist()
title_data_words = list(sent_to_words(title_data))

abstract_data = papers.abstract_processed.values.tolist()
abstract_data_words = list(sent_to_words(abstract_data))

text_data = papers.text_processed.values.tolist()
text_data_words = list(sent_to_words(text_data))

title_data_words = remove_stopwords(title_data_words)
abstract_data_words = remove_stopwords(abstract_data_words)
text_data_words = remove_stopwords(text_data_words)

print(title_data_words[:1][0][:30])
print(abstract_data_words[:1][0][:30])
print(text_data_words[:1][0][:30])


id2word1 = corpora.Dictionary(title_data_words)
id2word2 = corpora.Dictionary(abstract_data_words)
id2word3 = corpora.Dictionary(text_data_words)

texts1 = title_data_words
texts2 = abstract_data_words
texts3 = text_data_words

corpus1 = [id2word1.doc2bow(text) for text in texts1]
corpus2 = [id2word2.doc2bow(text) for text in texts2]
corpus3= [id2word3.doc2bow(text) for text in texts3]

print(corpus1[:1][0][:30])
print(corpus2[:1][0][:30])
print(corpus3[:1][0][:30])



num_topics = 10

lda_model1 = gensim.models.LdaMulticore(corpus=corpus1, id2word=id2word1, num_topics=num_topics)
#lda_model2 = gensim.models.LdaMulticore(corpus=corpus2, id2word=id2word2, num_topics=num_topics)
#lda_model3 = gensim.models.LdaMulticore(corpus=corpus3, id2word=id2word3, num_topics=num_topics)

pprint(lda_model1.print_topics())
doc_lda = lda_model1[corpus1]

pprint(lda_model2.print_topics())
doc_lda = lda_model2[corpus2]

pprint(lda_model3.print_topics())
doc_lda = lda_model3[corpus3]

import pyLDAvis.gensim
import pickle
import pyLDAvis


pyLDAvis.enable_notebook()

LDAvis_data_filepath = os.path.join('./results/ldavis_prepared_'+str(num_topics))


if 1 == 1:
    LDAvis_prepared = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
    with open(LDAvis_data_filepath, 'wb') as f:
        pickle.dump(LDAvis_prepared, f)


with open(LDAvis_data_filepath, 'rb') as f:
    LDAvis_prepared = pickle.load(f)

pyLDAvis.save_html(LDAvis_prepared, './results/ldavis_prepared_'+ str(num_topics) +'.html')

LDAvis_prepared
"""
