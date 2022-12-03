# Twitter sentiment Analysis

## Introduction:
This document provides information about gathering data (tweets) from Twitter in real time using the Twitter API and building a model that would determine if a tweet is positive, negative, or neutral. It also discusses the pre-processing and the GaussianNB model that was used to train the data. The article concludes by discussing how to utilize the Flask framework to build a user interface for interacting with the model and making predictions based on real-time tweets.

<center><img src="https://user-images.githubusercontent.com/99461999/205411147-62cb9020-9f93-4703-926a-a2f712abafd6.png" width="800" height="300"></center>

##  Tweeter Tweet Preprocessing

#### 1. Twitter API Access :

* With the right access permissions, a set of api tokens, and secrets, we can utilize Twitter's developer accounts to access the social media platform's data through its API services.
* To get Twitter API credentials ,created the <a href="https://developer.twitter.com/en/portal/projects-and-apps" target="_blank">Twitter-Developer</a> account and generated the all screats For Reeal Time Tweets

#### 2. Label the Data:
Tweets Preprocessing and Cleaning: Preprocessing text data is a crucial step since it prepares the unprocessed text for mining, making it simpler to extract information from the text and use machine learning algorithms on it. There is a greater likelihood that you will be working with noisy and erratic data if we miss this stage. The goal of this phase is to remove any irrelevant information from the tweets, such as punctuation, special characters, numerals, and terms that don't add much meaning when read in context.

* textblob : Used the textblob used to label the data based on the polarity of the tweet into positive, negative and neutral speech.
* data cleaning:
To remove patterns which are not alphabets and some unnecessary characters, the data has been processed to make the tweets free from unwanted characters.
* Lemmatization:
Lemmatization is the process of combining a word's several inflected forms into a single unit for analysis. Similar to stemming, lemmatization adds context to the words. As a result, it ties words with related meanings together.
* Bag of words model:
We use model to representing text data when modeling text with machine learning algorithms.
* TF-IDF model :
After That used TF-IDF model for language modeling and document classification.

## Building and training the classifier

1. To build and train the classifier. Used Tensor flow based model(LSTM) and GaussianNB model to train the data. Build and train a new feed-forward classifier using those features.
2. Detail of classification and comparison of model is in <a href="https://colab.research.google.com/drive/11HHN3xMfTzE3z1xYUZUgOHIi4pLX3VV7" target="_blank">Google_Colab_Notebook</a> 
3. Download the model:  dump `naive_classifier , filename =" text_classification.joblib ` The model which has been trained in the previous step has been stored and downloaded from `colab notebbok` ,After that used flask and integrated with web application using html
### Model Training

<img width="609" alt="Screen Shot 2022-12-02 at 9 41 01 PM" src="https://user-images.githubusercontent.com/99461999/205426208-97651f50-450e-4f89-b2ac-373a0f6969ec.png">

## Model Comparison

<img width="594" alt="Screen Shot 2022-12-02 at 8 50 29 PM" src="https://user-images.githubusercontent.com/99461999/205424224-4c20503b-0c73-41ed-8fc6-1bcf82b042da.png">

[accuracy.pdf](https://github.com/shubhadapaithankar/twitter/files/10145649/accuracy.pdf)

## Tech Stack
* tweepy
* nltk
* pandas
* numpy
* matplotlib

## Tool Used in Project
1. Google Colab to train the model
2. Flask 
3. Python3
4. HTML Script


## Complete flow :

https://user-images.githubusercontent.com/99461999/205412387-60aab6c1-967c-42b0-bb9f-b22fee67ef91.mov

## Running Steps:


<img width="1440" alt="Screen Shot 2022-12-02 at 4 11 36 PM" src="https://user-images.githubusercontent.com/99461999/205412450-e705ad18-dedf-41b5-9c99-21a94eefe8d0.png">
<img width="1440" alt="Screen Shot 2022-12-02 at 4 11 56 PM" src="https://user-images.githubusercontent.com/99461999/205412458-9b2ac540-c07d-4f2e-b94c-516226d82271.png">
<img width="1440" alt="Screen Shot 2022-12-02 at 4 12 11 PM" src="https://user-images.githubusercontent.com/99461999/205412465-a2e1946c-9286-4842-8ad7-d247b47e689c.png">
<img width="1419" alt="Screen Shot 2022-12-02 at 8 47 52 PM" src="https://user-images.githubusercontent.com/99461999/205424126-70bec75a-945f-4624-a835-6b376b126a89.png">

## Full Application Working and testing Video :  <a href="https://youtu.be/RiLHzY1w3sM" target="_blank">Link</a> 

## Refrance: 
1. https://github.com/kaustav202/RealTime-TwitterDataAnalysis
2. https://github.com/sharmaroshan/Twitter-Sentiment-Analysis
