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

***
## Methods




***
## Results



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
For any additional questions, please contact me at:

Email: deaudrey011@gmail.com

## Repository Structure

```
├── headline_word2vec.ipynb
├── headline_modeling.ipynb                        
├── headline_EDA.ipynb  
├── README.md  
├── models                                
└── data 
```
