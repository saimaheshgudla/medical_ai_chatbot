import easyocr

reader = easyocr.Reader(
    ['en'],
    verbose=False
)

def extract_text(image_path):

    result = reader.readtext(
        image_path,
        detail=0
    )

    text = " ".join(result)

    return text