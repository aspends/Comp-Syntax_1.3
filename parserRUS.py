import spacy
from conllu import TokenList
import re
import argparse
# Russian language model
nlp = spacy.load("ru_core_news_sm")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The program creates a conllu file.")
    parser.add_argument("featurefile", type=str, help="The file containing sentences.")
    
    args = parser.parse_args()
    
    
    with open(args.featurefile, "r") as f:
        text = f.read()

    # Split the text into sentences
    sentences = text.strip().split("\n")

    # Create an empty list to store the converted sentences
    conllu_sentences = []

    
    for sentence in sentences:
        sentence=re.sub("<|>", "", sentence)
        sentence=re.sub(":","",sentence)
        sentence=re.sub("PRON","",sentence)
        sentence=re.sub("AUX","",sentence)
        sentence=re.sub("PUNCT","",sentence)
        sentence=re.sub("ADJ","",sentence)
        sentence=re.sub("ADP","",sentence)
        sentence=re.sub("NUM","",sentence)
        sentence=re.sub("ADV","",sentence)
        sentence=re.sub("NOUN","",sentence)
        sentence=re.sub("PART","",sentence)
        sentence=re.sub("VERB","",sentence)
        sentence=re.sub("DET","",sentence)
        sentence=re.sub("PROPN","",sentence)
        sentence=re.sub("SCONJ","",sentence)
        sentence=re.sub("SSUBJ","",sentence)
        sentence=re.sub("CCONJ","",sentence)
        doc = nlp(sentence.strip())

        # Create a list of dictionaries representing the tokens
        token_dicts = []
        for token in doc:
            # Dictionary representing the token
            token_dict = {
                "id": token.i+1,
                "form": token.text,
                "lemma": token.lemma_,
                "upostag": token.pos_,
                "xpostag": "_",
                "feats": token.tag_,
                "head": token.head.i + 1 if token.head != token else 0,
                "deprel": token.dep_,
                "deps": "_",
                "misc": "_"
            }
            token_dicts.append(token_dict)

        # Create a TokenList object for the sentence and add it to the list
        tokenlist = TokenList(token_dicts)
        conllu_sentences.append(tokenlist)

    # Save the TokenList objects to a conllu file
    with open("treesRUS.conllu", "w", encoding="utf-8") as f:
        for sentence in conllu_sentences:
            f.write(sentence.serialize())
            f.write("\n")


    print("Doner!")