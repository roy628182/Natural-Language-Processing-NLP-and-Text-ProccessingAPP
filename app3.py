# Import necessary libraries
import streamlit as st
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, blankline_tokenize
from nltk.util import bigrams, trigrams, ngrams
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk
from nltk.corpus import wordnet
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Download NLTK data files (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Initialize the Streamlit app
st.title("Advanced NLP Text Processing App")
st.write("This app performs a variety of NLP tasks, including tokenization, n-grams, stemming, lemmatization, stopword removal, named entity chunking, and WordCloud generation.")

# Text input area
text = st.text_area("Enter your text here")

# Tokenization Options
if st.button("Word Tokenization"):
    words = word_tokenize(text)
    st.write("Word Tokens:")
    st.write(words)

if st.button("Sentence Tokenization"):
    sentences = sent_tokenize(text)
    st.write("Sentence Tokens:")
    st.write(sentences)

if st.button("Blankline Tokenization"):
    blankline_tokens = blankline_tokenize(text)
    st.write("Blankline Tokens:")
    st.write(list(blankline_tokens))

  # WordCloud Generation
#text1=st.text_area("Enter your text here which you want to display")
if st.button("Generate WordCloud"):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)
   

# Bigram and Trigram Generation
#text2= st.text_area("Enter your text here to see  bigrams and trigrams")

if st.button("Generate Bigrams"):
    words = word_tokenize(text1)
    bigram_tokens = list(bigrams(words))
    st.write("Bigrams:")
    st.write(bigram_tokens)

if st.button("Generate Trigrams"):
    words = word_tokenize(text)
    trigram_tokens = list(trigrams(words))
    st.write("Trigrams:")
    st.write(trigram_tokens)

# N-grams
n = st.number_input("Choose n for N-grams", min_value=1, max_value=10, value=2)
if st.button(f"{n}-gram Tokenization"):
    tokens = word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    st.write(f"{n}-grams:")
    st.write(n_grams)

# Stemming Options
#text3=st.text_area("Enter your word here which you want to stem")
if st.button("PorterStemmer"):
    ps = PorterStemmer()
    stemmed_words = [ps.stem(word) for word in word_tokenize(text)]
    st.write("Porter Stemmed Words:")
    st.write(stemmed_words)

if st.button("LancasterStemmer"):
    ls = LancasterStemmer()
    stemmed_words = [ls.stem(word) for word in word_tokenize(text)]
    st.write("Lancaster Stemmed Words:")
    st.write(stemmed_words)

if st.button("SnowballStemmer"):
    ss = SnowballStemmer("english")
    stemmed_words = [ss.stem(word) for word in word_tokenize(text)]
    st.write("Snowball Stemmed Words:")
    st.write(stemmed_words)

# Lemmatization
if st.button("WordNet Lemmatizer"):
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    lemmatizer = nltk.WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in word_tokenize(text)]
    st.write("Lemmatized Words:")
    st.write(lemmatized_words)

# Stopwords
st.write("StopWords of English  Language:")

if st.button("Stopwords of English"):
    stop_words = stopwords.words('english')
    st.write("English Stopwords:")
    st.write(stop_words)

# Named Entity Chunking
#text4=st.text_area("Enter a list of word")
if st.button("Named Entity Chunking"):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    named_entities = ne_chunk(tagged)
    st.write("Named Entities:")
    st.write(named_entities)

