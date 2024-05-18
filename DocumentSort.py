import os
import re
import nltk
import spacy
import shutil
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from gensim import corpora, models

nltk.download('stopwords')
stop_words=set(stopwords.words('english'))
nlp=spacy.load('en_core_web_sm')

def Preprocess_Text(text):
    text=re.sub(r'\st',' ',text)
    doc=nlp(text.lower())
    tokens=[token.lemma_ for token in doc if token.is_alpha and token.text not in stop_words]
    return tokens
def Extract_Text(file_path):
    if file_path.endswith('.txt'):
        with open(file_path,'r',encoding='utf-8') as file:
            return file.read()
    elif file_path.endswith('.pdf'):
        import PyPDF2
        with open(file_path,'rb') as file:
            reader=PyPDF2.PdfFileReader(file)
            text=''
            for page_num in range(reader.numPages):
                page=reader.getPage(page_num)
                text+=page.extract_text()
            return text
    elif file_path.endswith('.docx'):
        import docx
        doc=docx.Document(file_path)
        paragraphs_text=[]

        for para in doc.paragraph:
            paragraphs_text.append(para.text)
        document_text=' '.join(paragraphs_text)
        return document_text
    return None

documents_path='Documents/'
documents=[]
document_names = os.listdir(documents_path)


for file_name in os.listdir(documents_path):
    file_path=os.path.join(documents_path,file_name)
    text=Extract_Text(file_path)
    if text:
        documents.append(Preprocess_Text(text))
        

dictionary=corpora.Dictionary(documents)
corpus=[dictionary.doc2bow(doc) for doc in documents] 

num_topics=5
lda_model=models.ldamodel(corpus,num_topics=num_topics,id2word=dictionary,passes=5)

for idx, topic in lda_model.print_topics(-1):
    print('Topics: {} \nWords: {}'.format(idx,topic))

document_topics = []
for doc_bow in corpus:
    topics = lda_model.get_document_topics(doc_bow)
    dominant_topic = max(topics, key=lambda x: x[1])[0]
    document_topics.append(dominant_topic)


for i in range(num_topics):
    topic_dir = os.path.join(documents_path, f'topic_{i}')
    if not os.path.exists(topic_dir):
        os.makedirs(topic_dir)


for file_name, topic in zip(document_names, document_topics):
    src_path = os.path.join(documents_path, file_name)
    dst_path = os.path.join(documents_path, f'topic_{topic}', file_name)
    shutil.move(src_path, dst_path)
