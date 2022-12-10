# NLP to The Myth Of Sisyphus
## Contents
* [Description](#description)
* [Requirement](#requirement)
* [Program Review](#program-review)
* [References](#references)
* [License](#license)
## Description
<img src="https://user-images.githubusercontent.com/102570051/206861980-acb86721-b425-4186-a7c6-453e72e8c941.png" width="300" height="300"><br>
[시지프 신화](https://ko.wikipedia.org/wiki/%EC%8B%9C%EC%A7%80%ED%94%84_%EC%8B%A0%ED%99%94)<br><br>
 예전 [알베르 카뮈(Albert Camus)](https://ko.wikipedia.org/wiki/%EC%95%8C%EB%B2%A0%EB%A5%B4_%EC%B9%B4%EB%AE%88) 의 소설 **`이방인`** 책을 읽고 알베르 카뮈의 사상에 대하여 관심이 생기게 되었습니다. 그러다가 이번학기 **이방인**의 사상적 단초가 되는 책이라 평가 받는 **`시지프 신화`** 라는 책을 읽게 되었는데 짧은 글임에도 불구하고 책을 읽으면서 철학에 대하여 문외한이었던 저는 책의 내용을 반쯤 이해하지 못하며 읽게 되었습니다.<br><br>
 이번 OSS Project는 크게 3가지의 주제를 통하여 책을 읽을 때 더 주의 깊게 봐야할 사상가들 혹은 소설 속 등장인물들에 대하여 살펴보고자 합니다. 또한 감성분석을 통하여 이 책의 전반적인 분위기 또한 살펴볼 것 입니다. (~~물론 이러한 툴킷을 이용한 감성분석은 철학 에세이에는 부적합하며 논리적 비약이 심함을 경고합니다.~~) 마지막으로 책의 단어 빈도수를 바탕으로 WordCloud를 통해 책의 주제와 관련된 단어들을 시각화를 하였습니다.<br>

## Requirement
 본 코드는 vscode 편집기를 활용하였습니다.
#### setup vscode
* `pip install matplotlib` for visualization
* `pip install spacy` for NLP
* `pip install nltk` for NLP
* `pip install pandas` to create csv file
* `pip install WordCloud` for wordcloud
* `pip install numpy` for array in image
* `pip install PIL` for image

## Program Review
### Person frequency Analysis
 자연어 처리 오픈소스라이브러리인 spacy를 활용하여 책 내용 속의 인물들의 빈도수를 측정하였습니다. 3번 이상 나오지 않은 인물은 제거하였으며 결과는 다음과 같습니다.<br><br>
<img src="https://user-images.githubusercontent.com/102570051/206863424-be4b320d-ff9f-471c-ba42-0fadcdc23f58.png" width="400" height="300"><br>
 가장 많이 나온 인물로는 책 속의 한 챕터를 이 인물에 할애할 정도로 많이 나온 [돈 후안](https://ko.wikipedia.org/wiki/%EB%8F%88_%ED%9B%84%EC%95%88)이라는 전설속 인물입니다. 실제로 카뮈는 돈 후안에게서 일종의 자화상 같은 일면을 발견하게 됩니다. 이 인물은 책 **`이방인`** 속 뫼르소라는 인물과 유사한 태도를 보입니다.<br><br>
 다음으로 실존주의 철학자 키르케고르, 하이데거, 현상학의 창시자 후설, 도스토예프스키와 그의 작품 속에서 나오는 등장인물들, 니체 등 여러 철학자들과 소설을 바탕으로 이 책이 쓰여져 있음을 알 수 있습니다.<br><br>
 표에는 나오지 않았지만 윌리엄 셰익스피어의 작품과 카프카 등 책 속에는 그가 영향을 받은 여러 인물들이 존재합니다. 다음에 기회가 된다면 이러한 여러 철학가들과 소설가들의 책들을 읽으면 본문을 이해하는데 훨씬 도움이 될 듯 합니다.<br><br><br>
 

### Sentiment Analysis
 감성분석을 위하여 비지도학습 기반인 VADER을 사용하여 문장별로 긍정문과 부정문을 나누었습니다. 철학적 에세이인 만큼 감성분석은 어울리지 않고 그 효과가 부정확합니다. 하지만 이 책의 주제인 부조리와 자살이라는 것을 카뮈는 하나의 감정으로 표현을 했으며, 카뮈 또한 이성과 감정의 역할에 대해 둘 다 취해야 할 것을 책에서 말합니다. 따라서 카뮈의 글에서 묻어서 나온 감정을 한 번 살펴보도록 하겠습니다. <br><br>
<img src="https://user-images.githubusercontent.com/102570051/206865842-8c404fb3-e72b-44e2-a0ea-eb625173703c.png" width="100" height="200"><br>
* 문장별 감성지수(1에 가까울수록 긍정, -1에 가까울수록 부정 (-1<=compound<=1))<br><br>

<img src="https://user-images.githubusercontent.com/102570051/206865917-59544294-2634-441d-a542-a2f728a2abab.png" width="90" height="55"><br>
* 긍정과 부정으로 나눈 문장의 갯수(0 이상 긍정, 0 미만 부정 (-1<=compound<=1))<br><br> 
<div style="text-align: left"> 예상외로 긍정적인 문장이 부정적인 문장에 비해서 3배 이상 차이가 나는 것을 볼 수 있었습니다. 철학적 에세이 특징상 여러 비판적 사고가 나온다는 점과 이 책의 주제가 부조리와 무의미라는 점에서 부정적인 문장이 더욱 많이 나올 줄 알았으나 예상을 뒤엎는 결과가 나오게 되었습니다.</div>
 <br><br><br>

### Word Frequencies and WordCloud
 자연어처리 패키지인 nltk를 사용하여서 책에 나온 주요 단어들을 간략히 추려보고 WordCloud를 사용해 이를 시각화해 보았습니다. 이때 텍스트를 전처리하는 과정에서 알파벳을 제외한 문자와 글자수가 3개 이하인 단어는 중요한 단어라고 생각지 않아 제거하였습니다. 또한 관사나 조사, 접미사 같은 불용어들을 처리하였습니다.<br><br>
<img src="https://user-images.githubusercontent.com/102570051/206863794-c8316231-14e3-4a96-ab46-7a003d68a9c1.png" width="900" height="300"><br>
* 그래프 별로 보는 단어 빈도수<br><br>
<img src="https://user-images.githubusercontent.com/102570051/206863866-846708f7-f6b4-4289-b532-11ee430027e8.png" width="450" height="300"><br>
* 워드클라우드를 이용한 시각화<br><br>

<div style="text-align: left"> 제가 읽으며 몇 문장으로 이 책 내용을 요약하자면</div><br>

> 우리 모두는 시지프스와 같은 삶을 사는 인간들이다. 삶에 부조리를 느끼더라도 자살이나 신, 혹은 소망과 같은 것으로 도약하지 말고 저항하며 삶의 가능성을 모두 맛보아라!
<br>
라고 요약할 수 있을 것 같습니다. 이는 WordCloud에서 보여주는 단어들이 제가 정리한 주제이긴 하지만 매우 그럴듯하게 책의 내용을 나타 내는 것을 알 수 있습니다. 또한 이러한 단어들에 집중하여 책을 읽으면 이해에 도움이 될 것 같습니다.

## References
* book : 파이썬 머신러닝 완벽 가이드(http://www.yes24.com/Product/Goods/108824557)<br>
   The myth of sisyphus(Albert Camus)<br><br>
* site : https://wikidocs.net/book/2155<br>
   https://github.com/amueller/word_cloud<br>
## License
This project is licensed under the terms of the MIT license.
