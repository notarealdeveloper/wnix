#!/usr/bin/env python3

__all__ = [
    'image_to_text',
    'image_and_text_to_text',
]

import io
import assure
from functools import lru_cache


def image_to_text(image):

    import wnix

    bytes = assure.bytes(image)

    cache = wnix.CacheDefault('image_to_text')
    if cache.have(bytes):
        return cache.load(bytes).decode()

    text = image_to_text_nocache(bytes)
    cache.save(bytes, text.encode())
    return text


def image_to_text_nocache(bytes):

    import PIL.Image
    file = io.BytesIO(bytes)
    image = PIL.Image.open(file)

    model = load_model_image_to_text()

    results = model(image)
    outputs = []
    for result in results:
        output = result['generated_text'].strip()
        outputs.append(output)

    if isinstance(file, (list, tuple)):
        return outputs
    elif len(outputs) == 1:
        return outputs[0]
    else:
        raise TypeError(file)


@lru_cache(maxsize=1)
def load_model_image_to_text():
    from transformers import pipeline
    model = pipeline(
        "image-to-text",
        model="nlpconnect/vit-gpt2-image-captioning"
    )
    return model


def image_and_text_to_text(image, text):

    import wnix

    image_bytes = assure.bytes(image)
    text_bytes = text.encode()
    bytes = image_bytes + text_bytes

    cache = wnix.CacheDefault('image_and_text_to_text')
    if cache.have(bytes):
        return cache.load(bytes).decode()

    text = image_and_text_to_text_nocache(image_bytes, text)
    cache.save(bytes, text)
    return text

def image_and_text_to_text_nocache(image_bytes, text):

    import PIL.Image
    file = io.BytesIO(image_bytes)
    image = PIL.Image.open(file)

    processor, model = load_model_image_and_text_to_text()
    encoding = processor(image, text, return_tensors="pt")

    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    return model.config.id2label[idx]

@lru_cache(maxsize=1)
def load_model_image_and_text_to_text():
    from transformers import ViltProcessor, ViltForQuestionAnswering
    name = "dandelin/vilt-b32-finetuned-vqa"
    processor = ViltProcessor.from_pretrained(name)
    model = ViltForQuestionAnswering.from_pretrained(name)
    return (processor, model)


to_text = image_to_text
and_text_to_text = image_and_text_to_text

