from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging

predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/fine-grained-ner.2020-06-24.tar.gz")
print(predictor.predict(
    sentence="Did Uriah honestly think he could beat The Legend of Zelda in under three hours?."
))