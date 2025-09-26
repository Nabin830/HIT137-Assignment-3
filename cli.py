# cli.py
import argparse
from PIL import Image
from app.models.sentiment_model import SentimentModel
from app.models.image_classifier import ImageClassifier


def run_sentiment(text: str):
    m = SentimentModel()
    res = m.infer(text)
    print(res)


def run_image(path: str):
    img = Image.open(path)
    m = ImageClassifier()
    res = m.infer(img)
    print(res)


def main():
    p = argparse.ArgumentParser(description="Run sentiment or image classification")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp_s = sub.add_parser("sentiment", help="Classify sentiment of a text")
    sp_s.add_argument("--text", required=True)

    sp_i = sub.add_parser("image", help="Classify an image file")
    sp_i.add_argument("--path", required=True)

    args = p.parse_args()
    if args.cmd == "sentiment":
        run_sentiment(args.text)
    elif args.cmd == "image":
        run_image(args.path)


if __name__ == "__main__":
    main()
