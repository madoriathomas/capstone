# What's New? Headline Classification Analysis

**Author:** _Madoria Thomas_

<img src="https://mediacloud.theweek.co.uk/image/private/s--X-WVjvBW--/f_auto,t_content-image-full-desktop@1/v1604800220/theweek/2019/02/wd-newspapers_uk_-_dan_kitwoodgetty_images_0.jpg" width=60%>

## Overview

There is much speculation as to when exactly newspapers became a source of news, but there is evidence that proves they were circulated as early as 202 BC in ancient China. It would take until about 1440 when Johannes Gutenberg invented the moving printing press that the first newspapers as we know them would appear in Europe where they could more quickly be mass produced. From there, the first true newspaper in America would eventually pop up in 1690 in Boston. Of course now in the digital age, the need for paper newspapers has waned in favor of online news sources. In addition, certain niches and industries might prefer being online rather than in print.[source](https://www.psprint.com/resources/newspaper-history/)

There are more news sources online than ever before which is where I step in.

***
## Business Problem

With the constant barrage of information available on the internet, I have been tasked by the New York Times (NYT) to find a provide a quick and easily accessible news solution for users who may already be overwhelmed. My goal is to build a news classifier to accurately guess what the topic is from the headline, and vice versa. The model could then be utilized by the user to only show them the news stories they are interested in at that particular time. 

***
## Data

**Acknowledgements** This data set can be found [here](https://github.com/kotartemiy/topic-labeled-news-dataset) and has been provided by the [News API](https://newscatcherapi.com/news-api) team.

At a glance:</br>
- Total Columns: 6</br>
- Column Names: 'topic', 'link', 'domain', 'published_date', 'title', 'lang'</br>
- Total Rows: 108774</br>
- Target: 'topic'</br>
- Predictor: 'title'</br>

The target is the ‘topic’ column in which there are 8 categories: TECHNOLOGY, HEALTH, WORLD, ENTERTAINMENT, SPORTS, BUSINESS, NATION, and SCIENCE. Each topic has 15000 rows except for ‘SCIENCE’ with only 3774. 

Not used: I have a demo "data_scrape" notebook I created using the NewsCatcherAPI. The "scrape_news_articles.csv" containing the results is also available with an extra 31994 rows of data, but I kept it on standby for simplicity. 

***
## Methods

First, I cleaned the data before diving into the modeling process. As with the common NLP procedure, I lowercased, tokenized, lemmatized, removed stop words, and vectorized.</br>
Second, I tried multiple iterations of random forest classifers, and multinominalNB before my final model. 

***
## Results

The final model which is a MultinominalNB with an alpha tuned to 0.25 ended up as the best model. Accuracy was at 80% while recall and precision were both at 81%.

***
## Recommendations

- Use model to predict news topics by their headline
- Use model to only show topics/headlines user is interested in at that time

***
## Next Steps

- Expand the range of topics already offered
- Continue crafting a more user-friendly interface
- Look into possible membership page or email newsletter 

***
## For More Information
Feel free to check out how I came to my analysis in my ML [notebook](https://github.com/madoriathomas/headline_classification/blob/main/notebooks/headline_modeling.ipynb) and my [presentation](https://github.com/madoriathomas/headline_classification/blob/main/news_classification.pdf). 

For any additional questions, please contact me at:

Email: deaudrey011@gmail.com

## Repository Structure

```
├── setup.sh
├── requirements.txt
├── README.md
├── Procfile
├── news_preds.py 
├── news_classification.pdf
├── environment.yml  
├── notebooks 
├── models                                
└── data 
```
