from app.models.sentiment_model import SentimentModel
from app.models.image_model import ImageClassifier

def test_sentiment():
    # Created the sentiment model and print description
    m = SentimentModel()
    print("INFO:", m.info())
    # Two test sentences
    examples = [
        "I  love to Study on Darwin!",
        "This is the worst experience I have had."
    ]
    # Loop through test sentences and running the  model
    for s in examples:
        print("TEXT:", s)
        print(" ->", m.infer(s))  # this is the prediction
        print()

def test_image():
    # Created the image classifier and print description
    m = ImageClassifier()
    print("INFO:", m.info())
    # Path to a sample image 
    path = "assets/sample.jpg"
    print("IMAGE:", path)
    print(" ->", m.infer(path))  # this is the prediction

if __name__ == "__main__":
    test_sentiment()             # Run sentiment test
    print("-" * 60)
    try:
        test_image()             # Run image test
    except FileNotFoundError:    # if the image is not found then this messge will appeaers
        print(" Please put a test image at assets/sample.jpg to run the image test.")