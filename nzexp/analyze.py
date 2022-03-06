from nzdb.dbif import xget_by_date
import spacy
from dataclasses import dataclass

nlp = spacy.load("en_core_web_sm")


def get_texts_by_date(start: str, end: str) -> list[str]:
    """get texts by start and end dates

    Args:
        start (string): ISO date text yyyy-mm-dd
        end (string): ISO date text yyyy-mm-dd
    """
    query = {"start": start, "end": end}
    err, cursor = xget_by_date(query)
    if err is None:
        return [s["text"] for s in cursor]
    else:
        raise err


def get_docs_by_date(start: str, end: str) -> list[spacy.tokens.Doc]:
    """get docs
    Args:
        start (string): ISO date text yyyy-mm-dd
        end (string): ISO date text yyyy-mm-dd
    """
    texts = get_texts_by_date(start, end)
    return [nlp(text) for text in texts]


@dataclass(frozen=True)
class entclass:
    text: str
    label: str


def main():
    docs = get_docs_by_date("2022-03-04", "2022-03-05")
    entcs = set()
    for doc in docs:
        for ent in doc.ents:
            entcs.add(entclass(ent.text, ent.label_))
    for entc in entcs:
        print(entc)
    print(len(docs))
    print(len(entcs))
    # spacy.displacy.serve(docs, style="ent", port=5050)
    # for text in texts:
    #     print(text)
    #     doc = nlp(text)
    #     for ent in doc.ents:
    #         print(ent.text, ent.label_)
    #     print("........")


if __name__ == "__main__":
    main()
