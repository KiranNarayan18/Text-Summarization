from textSummarizer.components.prediction import ModelPrediction
from textSummarizer.config.configuration import ConfigurationManager

config = ConfigurationManager()
model_prediction_config = config.get_model_predictions_config()

prediction_obj = ModelPrediction(config=model_prediction_config)

sample_str =  """Hannah: Hey, do you have Betty's number?
Amanda: Lemme check
Hannah: <file_gif>
Amanda: Sorry, can't find it.
Amanda: Ask Larry
Amanda: He called her last time we were at the park together
Hannah: I don't know him well
Hannah: <file_gif>
Amanda: Don't be shy, he's very nice
Hannah: If you say so..
Hannah: I'd rather you texted him
Amanda: Just text him 🙂
Hannah: Urgh.. Alright
Hannah: Bye
Amanda: Bye bye"""

print(prediction_obj.predict(sample_str))

