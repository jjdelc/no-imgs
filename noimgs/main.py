from PIL import Image
from io import BytesIO
from flask import Flask, send_file


app = Flask(__name__)


@app.route('/<int:width>x<int:height>')
def placeholder(width, height):
    img = Image.new('RGB', (width, height))
    out = BytesIO()
    img.save(out, 'PNG')
    out.seek(0)
    return send_file(out, 'image/png')


def start():
    app.run(port=7999)


if __name__ == '__main__':
    start()
