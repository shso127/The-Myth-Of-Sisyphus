import spacy
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud


nlp = spacy.load('en_core_web_lg')

with open('the myth of sisyphus.txt', encoding='utf-8') as f:
    file = f.read()

remove_LF_file = file.replace("\n"," ")
doc = nlp(remove_LF_file)

list_sents = [sent for sent in doc.sents]

# 문장별로 나눈 txt 파일을 새로 생성
with open('the myth of sisyphus1.txt', 'a', encoding='utf-8') as f:
    f.write("sentence\n")
    for index, line in enumerate(list_sents):
        f.write(str(line))
        f.write('\n')

###############################################################
#                 책에 영향을 준 인물들 찾기                    #
###############################################################

# 책에서 나온 인물을 dictionary에 저장
text_in_person = {}
i = 0

for ent in doc.ents:
    if ent.label_ == 'PERSON':
        if ent.text in text_in_person:
            continue
        else:
            text_in_person[ent.text] = i
            i += 1

# dictionary에 있는 인물이 나온 횟수를 conut
count_person = [0]*len(text_in_person)

for ent in doc.ents:
    if ent.label_ == 'PERSON':
        count_person[text_in_person[ent.text]]+=1

# 하나의 list로 합치기(3번 이상 나오지 않은 인물들은 삭제)
text_in_person_list = list(text_in_person)
frequent_person = [[count_person[i], text_in_person_list[i]] for i in range(len(text_in_person)) if count_person[i] > 2]

# 횟수별로 sorted
sort_person_frequent = {}
for item in sorted(frequent_person):
    sort_person_frequent[item[1]] = item[0]

# 인물들이 나온 횟수 시각화
plt.bar(range(len(sort_person_frequent)), list(sort_person_frequent.values()), align='center')
plt.xticks(range(len(sort_person_frequent)), list(sort_person_frequent.keys()), rotation=80)
plt.title("Count Person in the myth of sisyphus", fontsize=20)
plt.xlabel("Person", fontsize=18)
plt.ylabel("Person Frequency", fontsize=18)
plt.legend()
plt.show()


###############################################################
#          감성분석을 통한 책의 감정적 측면 살펴보기             #
###############################################################

sid = SentimentIntensityAnalyzer()

# csv 파일로 읽기
book = pd.read_csv('the myth of sisyphus1.txt', delimiter='\t')

# 필요없는 데이터 제거
book.dropna(inplace=True)

# 글자수 25개 넘지 않는 문장 제거
drop_useless = []

for i,sent in book.itertuples():
    if type(sent)==str:
        if len(sent)<25:
            drop_useless.append(i)
            
book.drop(drop_useless, inplace=True)

# 긍정,부정,중립 퍼센트 칼럼추가
book['percent'] = book['sentence'].apply(lambda sentence: sid.polarity_scores(sentence))
# compound 칼럼 추가
book['compound']  = book['percent'].apply(lambda score_dict: score_dict['compound'])
# compound가 0 이상이면 긍정 미만이면 부정으로 판단
book['result'] = book['compound'].apply(lambda c: 'pos' if c >=0 else 'neg')

print(book['compound'])
print(book['result'].value_counts())


###############################################################
#               워드 클라우드로 알아본 책의 주제                #
###############################################################
from nltk.corpus import stopwords
import nltk
import numpy as np
from PIL import Image
from wordcloud import WordCloud

#텍스트 전처리
documents = []
for sent in book['sentence']:
    documents.append(sent)

book_df = pd.DataFrame({'document':documents})

# 알파벳을 제외한 문자 제거
book_df['clean_doc'] = book_df['document'].str.replace("[^a-zA-Z]", " ")
# 3 이하 단어 제거
book_df['clean_doc'] = book_df['clean_doc'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
# 단어 소문자로 변환
book_df['clean_doc'] = book_df['clean_doc'].apply(lambda x: x.lower())

#불용어 처리
stop_words = stopwords.words('english')
tokenized_doc = book_df['clean_doc'].apply(lambda x: x.split())
tokenized_doc = tokenized_doc.apply(lambda x: [item for item in x if item not in stop_words])

# 단어들을 리스트로 만든후 워드 클라우드 생성
for index,sent in enumerate(tokenized_doc):
    if index==0:
        str = " ".join([word for word in sent])
    else:
        for word in sent:
            str += word
            str += ' '

str_to_list = str.split()

plt.figure(figsize=(17,5))
plt.xticks(fontsize=15, rotation=90)
freq_dist = nltk.FreqDist(str_to_list)
freq_dist.plot(50,cumulative=False)

custom_mask = np.array(Image.open("book.jpg"))
wc = WordCloud(max_font_size=150, width=700,height=700,contour_width=5, contour_color='red',mask=custom_mask)
wordcloud = wc.generate_from_frequencies(freq_dist)

plt.figure(figsize=(12,12))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()