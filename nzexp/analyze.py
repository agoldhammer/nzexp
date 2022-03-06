from nzdb.dbif import xget_by_date
import spacy

nlp = spacy.load("en_core_web_sm")


def get_texts_by_date(start, end):
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


def main():
    texts = get_texts_by_date("2022-02-25", "2022-02-26")
    for text in texts:
        print(text)
        doc = nlp(text)
        for ent in doc.ents:
            print(ent.text, ent.label_)
        print("........")


if __name__ == "__main__":
    main()
