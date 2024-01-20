from transformers import AutoTokenizer, pipeline

from textSummarizer.entity import PredictionConfig
 
class ModelPrediction:

    def __init__(self, config=PredictionConfig) :
        self.config = config
        self.gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
    

    def predict(self, sample_text):

        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        pipe = pipeline("summarization", model=self.config.model_path,tokenizer=self.tokenizer)
        model_result = pipe(sample_text, **self.gen_kwargs)[0]["summary_text"]

        return model_result