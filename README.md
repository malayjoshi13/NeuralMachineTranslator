# NeuralMachineTranslator

This repository is a dedicated effort to facilitate a hands-on experience for me (and hopefully you) to develop a Streamlit-based Neural Machine Translation application (using Transformer-based Pretrained Language Models from HuggingFace), containerize it using Docker and deploy it on Cloud Platform.

Here is a user-flow video of the developed Streamlit-based NMT application hosted on Cloud Platform:

## Repository Structure

- models --> folder containing sub-folders having weight and tokenizer files for each of the three Transformer-based Pretrained Language Models pre-downloaded from HuggingFace. This is done to avoid the real-time loading of models from HuggingFace which has a dependency on the user's internet bandwidth.
- services --> folder containing files for initializing each of the three Transformer-based Pretrained Language Models, `show_models.py` file to show user available model options and `translate.py` file to use the three models to translate the user's input source sentence into the target language.
- app.py --> Streamlit-based file that defines the layout of NMT's UI and controls user flow and translation process.
- requirements.txt --> file having needed libraries for this NMT application to run.
