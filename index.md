# Identify Topics in Scientific Digital Twin Literature

# Introduction

In our project we identify topics within scientific digital twin literature by using LDA for topic modeling.
We did approaches with multiple topic numbers for titles, abstracts and texts seperately and we ended up with a variation of topic models we want to share with you.


## Read me

The results link to the visualized Topic models. There you can explore and interpret the topic model. For the use of the interactive visualization tool please note:
- The circles on the left are topics and can be clicked to identify the frequency of the words they contain. 
- On the right side, the frequency of a word in a topic is shown with a red bar. 
- Blue bars are used to show the frequency in the entire dataset.
- Use the slide on the top right corner to adjust the ratio on red to blue.

# Related Work

[Mining Dynamics of Research Topics Based on the Combined LDA and WordNet](https://ieeexplore.ieee.org/abstract/document/8580532)

The paper describes multiple experiments combining LDA with WordNet to get dynamics of research topics. WordNet is used as an external lexical knowledge source to improve the knowledge base on which the LDA is working. As we will probably also face the issue of putting knowledge to our LDA model this is a good source of further understanding of lexical structure.

[Text mining for identifying topics in the literatures about adolescent substance use and depression](https://link.springer.com/article/10.1186/s12889-016-2932-1)

This paper used LDA to identify sub-topics among two main topics in abstracts of articles. With this approach relations regarding trends and long time relationship between the main topics can be identified. We found this approach interesting because it could be a good addition to our work, as the identified topics could be combined to get a deeper knowledge about their relationship. 

# Artifact Description

We used Latent Dirichlet allocation (LDA) as topic modeling algorithm to process our data. It learns a sets of words that seem to occur together in documents. Those sets are described as topics, which can appear multinominal in documents. The model uses the observed documents and words to infer the hidden topic structure, creating per-document topic distributions, P(topic/document), and per-topic word distributions, P(word/topic).

# Evaluation

## Data Set description

Our Data is a 31KB JSON Line document. The file contains information on 1014 scientific papers on the topic Digital Twins. Both the metadata and the JSON object data contain a lot of information that is not completly relevant for our project. We focused on the titles, the abstract and the respective texts but for the exploration of the data we also searched in publisher names, published year and publication type for correlation with the topics. The document also contains articels that are not about Digital Twins, so we have dropped those. In the end we had a total amout of 554 relevant papers. Further processing of the extracted Text and Metadata will eventually be used to feed a topic modeling model, so we stored the data in DataFrameworks to ensure that the program executes quickly. After we explored our filtered data, we removed special characters, such as punctuation marks and set all words to lowercase. Afterwards we removed stopwords to keep only meaningful words for model and created dictionaries for the words from titles, abstracts and texts.

In order to approach the solution, we played around with the data and tried to get a rough overview. First we looked at the year in which the articles were published. As you can easily see from the bar chart below, there were a lot of arcticel about Digital Twins in the years 2018 and 2019. We had no further information about the dataset, which means that it may be either that the selected data favored the respective years or that the topic was actually particularly popular in those years.

![Papers_Years](https://jappes0815.github.io/ML4B/Papers_Years.PNG)

We discovered that there are 2275 Participations in publications from 1927 Authors, that means on average four authors have worked on one article. From the list of names of authors with the most participation in publications, we can also see a tendency that points to many East Asian authors.

![Papers_Authors](https://jappes0815.github.io/ML4B/Papers_Authors.PNG)

From the 554 documents there were 311 journal articles and 243 conference Paper. We considered to include the reference to the article type when classifying the articles, but since there are only two types and they are quite similar in relevance, a differentiation is hardly useful.

![Papers_Type](https://jappes0815.github.io/ML4B/Papers_Type.PNG)

# Results

We focused on titles, abstracts and the respective texts for our topic identification, so we used the model on each of them to see how much the results will vary between them. We used models with 10 and 20 topics on each to get an idea about the allocation of topics and afterwards tried to find a good topic number. The results were safed in html files and show both, the words used in each topic and the estimated frequency of terms within a topic in comparison with the overall term frequency.

### Titles

We started by modeling [Titles with 10 Topics](https://jappes0815.github.io/ML4B/topics_title_lda10.html) to get an idea of the distribution. Some of the topics are already overlapping here, so we did an approach [with 20 Topics](https://jappes0815.github.io/ML4B/topics_title_lda20.html) to see how the distribution behaves. As expected there are more opverlaps, so we went down with the number of topics and found a good distribution for [Titles with 8 Topics](https://jappes0815.github.io/ML4B/topics_title_lda08.html).

### Abstracts

We assumed that the models using abstracts might be the best approaches, as abstracts contain more information about a paper than the title, but usually also contain only relevant information, as it summarizes the text. In our first appoach [with 10 Topics](https://jappes0815.github.io/ML4B/topics_abstract_lda10.html) even more overlaps than in our approach with titles and the same number of topics. In another approach [with 20 Topics](https://jappes0815.github.io/ML4B/topics_abstract_lda20.html) the topics were also centered more than in our model using titles. We took several approaches with topic numbers between 5 and 15, but ended up with 10 topics to be the best amount of topics here, as it had the smallest overlays between the topics. 

### Texts

As our texts dictionary contains more words than our dictionary for abstracts, we assumed that an [approach with 10 Topics](https://jappes0815.github.io/ML4B/topics_text_lda10.html) wouldn't distinguish enough, so we also tried [20 Topics](https://jappes0815.github.io/ML4B/topics_text_lda20.html) here. It appears that even with the huge amount of words within texts 20 topics is too much for this model, so we tried with numbers from 11 to 15, but despite having a bigger amount of terms, we still ended up with 10 topics being the best amount here.

### Further LDA models

#### Year analysis
- [2019 text with 10 Topics](https://jappes0815.github.io/ML4B/text_2019.html)
- [2019 text with 5 Topics](https://jappes0815.github.io/ML4B/text_2019_5.html)
- [2018 text with 10 Topics](https://jappes0815.github.io/ML4B/text_2018.html)
- [2018 text with 5 Topics](https://jappes0815.github.io/ML4B/text_2018_5.html)
- [2017 text with 10 Topics](https://jappes0815.github.io/ML4B/text_2017.html)
- [2017 text with 5 Topics](https://jappes0815.github.io/ML4B/text_2017_5.html)

#### Author analysis
- [Fai Tao text with 3 Topics](https://jappes0815.github.io/ML4B/text_Fei_Tao.html)
- [Qiang Liu with 3 Topics](https://jappes0815.github.io/ML4B/text_Qiang_Liu.html)
- [Luca Fumagalli with 3 Topics](https://jappes0815.github.io/ML4B/text_Luca_Fumagalli.html )

#### Paper type analysis
- [Conference paper text with 10 Topics](https://jappes0815.github.io/ML4B/text_conferencePaper.html)
- [Conference paper text with 5 Topics](https://jappes0815.github.io/ML4B/text_conferencePaper_5.html)
- [Journal article text with 10 Topics](https://jappes0815.github.io/ML4B/text_journalArticle.html)
- [Journal article text with 5 Topics](https://jappes0815.github.io/ML4B/text_journalArticle_5.html)

# Discussion

Comparing our results from the different approaches, we came to the conclusion that abstracts might in fact be the best data source for topic modeling of papers, as there could be more topics identified than in titles only. Texts on the other hand don't provide more valueable topics while needing a lot more resources to model.

