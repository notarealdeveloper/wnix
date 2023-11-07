#!/usr/bin/env python3

__all__ = [
    'img_to_text',
]

from functools import lru_cache

@lru_cache(maxsize=1)
def load_model():
    from transformers import pipeline
    model = pipeline(
        "image-to-text",
        model="nlpconnect/vit-gpt2-image-captioning"
    )
    return model


def img_to_text(file):

    import io
    import wnix
    import PIL.Image

    bytes = wnix.filelike_to_bytes(file)
    cache = wnix.CacheDisk()
    text = cache.load(bytes)
    if text is not None:
        return text.decode()

    file = io.BytesIO(bytes)
    img = PIL.Image.open(file)
    text = pil_img_to_text(img)
    cache.save(bytes, text.encode())
    return text


def pil_img_to_text(file):

    model = load_model()

    results = model(file)
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

to_text = img_to_text
