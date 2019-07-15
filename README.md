# Citizens Document Clustering

This tool uses document embeddings from Gensim by @RaRe-Technologies
to classify and make clusters from documents.

Texts are lemmatized using nouns_lemmas_extractions.py, which was built around
Reynir by @mideind. Lemmatization is available for Icelandic and Icelandic. As
of now, users need to input a path for Icelandic in nouns_lemmas_extractions.py
and provide a file as an arg (flag: -f) for English.

# License
[AGPL](https://en.wikipedia.org/wiki/Affero_General_Public_License)
