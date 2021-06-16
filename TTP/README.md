# NLP

## Package for NLP pre text processing 

https://pypi.org/project/racepretextproc/


### Functionalities
The functionalities which this pre-processing library will be 
#### Lower casing:
Converting a word to lower case (NLP -> nlp).
Words like Book and book mean the same but when not converted to the lower case those two are represented as two different words in the vector space model .  It is applicable to most text mining and NLP problems and can help in cases where your dataset is not very large and significantly helps with consistency of expected output. 
#### Stop words removal: 
Stop words are very commonly used words (a, an, the, etc.) in the documents. These words do not really signify any importance as they do not help in distinguishing two documents.
#### Text Normalization:
A highly overlooked preprocessing step is text normalization. Text normalization is the process of transforming a text into a canonical (standard) form. For example, the word “gooood” and “gud” can be transformed to “good”, its canonical form. Text normalization is important for noisy texts such as social media comments, text messages and comments to blog posts where abbreviations, misspellings and use of out-of-vocabulary words (oov) are prevalent . Some common approaches to text normalization include spelling-correction based approaches

#### Noise removal:
Noise removal is about removing characters digits and pieces of text that can interfere with your text analysis. Noise removal is one of the most essential text preprocessing steps. It is also highly domain dependent.
For example, in Tweets, noise could be all special characters except hashtags as it signifies concepts that can characterize a Tweet.


#### Stemming:
It is a process of transforming a word to its root form. There are different algorithms for stemming. The most common algorithm, which is also known to be empirically effective for English, is Porters Algorithm. Here is an example of stemming in action with Porter Stemmer:
#### Lemmatization:
Unlike stemming, lemmatization reduces the words to a word existing in the language. It may use a dictionary such as WordNet for mappings or some special rule-based approaches
Tokenization of data:
Splitting the sentence into words.
#### Word Cloud: 
It is a visualization technique for text data wherein each word is picturized with its importance in the context or its frequency. This is a very handy application when it comes to understanding the crux of today’s news or the content of any youtube channel
For the Race pre-processing library , user needs to provide on which column of data pre-processing steps needs to applied.
User can also opt out libraries ,which they don’t want to get applied by passing the arguments in the calling function. 
