import easyocr

reader = easyocr.Reader(
    ['en'],
    verbose=False
)


def extract_text(image_path):

    result = reader.readtext(
        image_path,
        detail=1
    )

    result.sort(key=lambda x: x[0][0][1])

    lines = []
    current_line = []
    current_y = None
    threshold = 15

    for bbox, text, _ in result:

        y = bbox[0][1]

        if current_y is None or abs(y - current_y) < threshold:
            current_line.append(text)
            current_y = y

        else:
            lines.append(" ".join(current_line))
            current_line = [text]
            current_y = y

    if current_line:
        lines.append(" ".join(current_line))

    return "\n".join(lines)