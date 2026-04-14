from transformers import pipeline

### Load the NER model and tokenizer from Hugging Face
def load_ner():
    return pipeline(
        "ner",
        model="cahya/bert-base-indonesian-NER",
        tokenizer="cahya/bert-base-indonesian-NER",
        aggregation_strategy="simple"
    )


### Redaction function that replaces detected entities with [REDACTED]
def redact_names(text, entities, labels):
    offset = 0

    for ent in sorted(entities, key=lambda x: x["start"]):
        if ent["entity_group"] in labels:
            start = ent["start"] + offset
            end = ent["end"] + offset

            text = text[:start] + "[REDACTED]" + text[end:]
            offset += len("[REDACTED]") - (end - start)

    return text


### Highlighting function that wraps detected entities in <mark> tags
def highlight_text(text, entities, labels):
    result = ""
    last = 0

    for ent in sorted(entities, key=lambda x: x["start"]):
        if ent["entity_group"] in labels:
            s, e = ent["start"], ent["end"]

            result += text[last:s]
            result += f"<mark>{text[s:e]}</mark>"
            last = e

    result += text[last:]
    return result