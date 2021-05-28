# Identify Topics in Scientific Digital Twin Literature

# Introduction

In our project we identify topics within scientific digital twin literature by using LDA for topic modeling.
We did approaches with multiple topic numbers for titles, abstracts and texts seperately and we ended up with a variation of topic models we want to share with you:

# Related Work


# Data

## 1. Loading

Our Data is a 31KB JSON Line document. The file contains information on 1014 scientific papers on the topic Digital Twins. Further processing of the extracted Text and Metadata will eventually be used to feed a topic modeling model, so we store the data in DataFrameworks to ensure that the program executes quickly.

## 2. Cleaning

### 2.1. Relevant papers

The document also contains articels that are not about Digital Twins, so we have dropped those. In the end we had a total amout of 554 relevant papers.

### 2.2. Important Colums

Both the metadata and the JSON object data contain a lot of information that we consider irrelevant for subject identification. We focused on the titles, the abstract and the respective texts but for the exploration of the data we also searched in publisher names, published year and publication type for correlation with the topics.

## 3. Exploration 

In order to approach the solution, we played around with the data and tried to get a rough overview. First we looked at the year in which the articles were published. As you can easily see from the bar chart below, there were a lot of arcticel about Digital Twins in the years 2018 and 2019. We had no further information about the dataset, which means that it may be either that the selected data favored the respective years or that the topic was actually particularly popular in those years.

![Image](https://jappes0815.github.io/ML4B/Papers_Years.PNG)

From the 554 documents there were 311 journal articles and 243 conference Paper. We considered to include the reference to the article type when classifying the articles, but since there are only two types and they are quite similar in relevance, a differentiation is hardly useful.

![Image](https://jappes0815.github.io/ML4B/Papers_Type.PNG)
## Titles

[Titles with 10 Topics](https://jappes0815.github.io/ML4B/topics_title_lda10.html)

[Titles with 20 Topics](https://jappes0815.github.io/ML4B/topics_title_lda20.html)

## Abstracts

[Abstracts with 10 Topics](https://jappes0815.github.io/ML4B/topics_abstract_lda10.html)

[Abstracts with 20 Topics](https://jappes0815.github.io/ML4B/topics_abstract_lda20.html)


## Texts

[Texts with 10 Topics](https://jappes0815.github.io/ML4B/topics_text_lda10.html)

[Texts with 20 Topics](https://jappes0815.github.io/ML4B/topics_text_lda20.html)

[Link button](https://jappes0815.github.io/ML4B/issue_lda_2016.html){: .btn .btn-outline }
____________________________________________________________________________________________________________________

You can use the [editor on GitHub](https://github.com/Jappes0815/ML4B/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Jappes0815/ML4B/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
