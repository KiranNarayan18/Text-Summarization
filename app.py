# app.py
from textSummarizer.components.prediction import ModelPrediction
from textSummarizer.config.configuration import ConfigurationManager

config = ConfigurationManager()
model_prediction_config = config.get_model_predictions_config()

prediction_obj = ModelPrediction(config=model_prediction_config)


import streamlit as st


def main():
    st.title("Text Summarization Dashboard")


    col1, col2, col3 = st.columns([5, 2, 5])

    # Input text area (first column)
    with col1:
        input_text = st.text_area("","Enter text to summarize", height=200)

        

    # Button container (between columns)
    with col2:
        button_container = st.container()
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center; height: 100px;">
                
            </div>
            """,
            unsafe_allow_html=True
        )

        
        st.button("Summarize", key="summarize_button")

    # Output text area (second column)
    with col3:
        output_text_area = st.empty()

    # Button to trigger the summarization
    with button_container:

        summarized_text = "Summarized Text"
        if st.session_state.summarize_button:
            summarized_text = prediction_obj.predict(input_text)
            # st.write(summarized_text)

            # Update the content of the second text area
        
        output_text_area.text_area("", summarized_text, height=200)



if __name__ == "__main__":
    main()
