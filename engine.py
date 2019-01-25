import spacy

train_data = [
    ("Uber blew through one million invoices in a week", [(30, 37, 'ORG')]),
    ("I hate my invoice", [(10, 17, 'GPE')]),
    ("Spotify steps up invoice expansion", [(17, 24, "ORG")]),
    ("Google Maps launches invoice sharing", [(21, 28, "PRODUCT")]),
    ("Google rebrands its invoice apps", [(20, 27, "ORG")]),
    ("look at the invoice i found ", [(12, 19, "PRODUCT")])]

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Give me a green invoice for John Smith in France')

# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)
#     print(doc)

def parse(str):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(str)
    return doc