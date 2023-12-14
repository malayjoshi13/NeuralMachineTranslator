# NeuralMachineTranslator

This repository is a dedicated effort to facilitate a hands-on experience for me (and hopefully you) to develop a Streamlit-based Neural Machine Translation application (using Transformer-based Pretrained Language Models from HuggingFace), containerize it using Docker and deploy it on Cloud Platform. The three models used here are: 
- Helsinki-NLP/opus-mt-hi-en (read more at https://huggingface.co/Helsinki-NLP/opus-mt-hi-en)
- facebook/mbart-large-50-many-to-one-mmt (read more at https://huggingface.co/facebook/mbart-large-50-many-to-one-mmt)
- facebook/m2m100_418M (read more at https://huggingface.co/facebook/m2m100_418M)

Here is a user-flow video of the developed Streamlit-based NMT application running on local (will soon deploy it over cloud as well):<br>

https://github.com/malayjoshi13/NeuralMachineTranslator/assets/71775151/2941b3ad-92f6-4099-bbf4-aba90e6c8152

<br>

**Note**: this repository is not aimed at doing a comparative analysis between the three used Transformer-based Pretrained Language Models, will leave it for future work. Currently, this repository aims to only for developing a Streamlit-based application around a practical use case using existing models and learn process to deploy the same to be used in real-time by users across the globe. Also, due to constrain of computational resources, dockerization and deployment is still in progress. Will soon update about the hosted web application!! 

## Repository Structure

- models --> folder containing sub-folders having weight and tokenizer files for each of the three Transformer-based Pretrained Language Models pre-downloaded from HuggingFace. This is done to avoid the real-time loading of models from HuggingFace which has a dependency on the user's internet bandwidth.
- services --> folder containing files for initializing each of the three Transformer-based Pretrained Language Models, `show_models.py` file to show user available model options and `translate.py` file to use the three models to translate the user's input source sentence into the target language.
- app.py --> Streamlit-based file that defines the layout of NMT's UI and controls user flow and translation process.
- requirements.txt --> file having needed libraries for this NMT application to run.

## Getting started

```
git clone https://github.com/malayjoshi13/NeuralMachineTranslator.git
cd NeuralMachineTranslator
conda create -n "NMT" python=3.7
conda activate NMT
pip install -r requirements.txt
streamlit run app.py
```

Enjoy using Streamlit-based Neural Machine Translation application (using Transformer-based Pretrained Language Models from HuggingFace)!!

## Observations 

**Downloading model from HuggingFace and loading it + no streamlit caching**
- time taken for first translation of sentence “यह मेरी बिल्ली है” (which includes downloading model from HuggingFace) → 419.98 sec
- time taken for second translation of sentence “यह मेरा घोड़ा है”→ 71.64 sec
- time taken for third translation of sentence “यह मेरी बिल्ली है” → 139.14 sec
- time taken for fourth translation of sentence “यह मेरा घर है” → 154.40 sec
- time taken for fifth translation of sentence “ये मेरे पिता है” → 63.38 sec

**Downloading model from HuggingFace and then loading it + with streamlit caching**
- time taken for first translation of sentence “यह मेरी बिल्ली है” (which includes downloading model from hugging face) → 386.80 sec
- time taken for second translation of sentence “यह मेरा घोड़ा है” → 4.56 sec
- time taken for third translation of sentence “यह मेरी बिल्ली है” → 5.63 sec
- time taken for fourth translation of sentence “यह मेरा घर है” → 4.86 sec
- time taken for fifth translation of sentence “ये मेरे पिता है” → 3.30 sec

**Observation 1:** Streamlit caching significantly reduces the time taken from the second translation onwards as the translation model does not re-load during every translation. 

```Note: translation model downloaded from HuggingFace gets stored at “C:\Users\<username>\.cache\huggingface\hub” and then for every translation, the script picks up from there only. But to download from HuggingFace while the user is using this NMT application takes a lot of time and needs a good quality internet connection. Thus, we must download the required model files in-advance only so that the user doesn’t have to do it.```

..................................................................................................

**Loading model which is already downloaded in local + with streamlit caching**
- time taken for first translation of sentence “यह मेरी बिल्ली है” (which includes downloading model from hugging face) → 136.17 sec
- time taken for second translation of sentence “यह मेरा घोड़ा है” → 9.63 sec
- time taken for third translation of sentence “यह मेरी बिल्ली है” → 5.91 sec
- time taken for fourth translation of sentence “यह मेरा घर है” → 4.72 sec
- time taken for fifth translation of sentence “ये मेरे पिता है” → 3.52 sec

**Observation 2:** Streamlit caching + loading model from local, further significantly reduces the time taken from first translation onwards as the model is not downloaded from the internet (due to using model from local) + model is not re-loaded for every translation (due to streamlit caching).

..................................................................................................

**Observation 3:** ```facebook/mbart-large-50-many-to-one-mmt``` fails to translate short sentences like “ये मेरे पिता है” to English, but very well translates longer sentences like “राधा को टीम में उनके उत्कृष्ट समर्पण और अभिनव योगदान के लिए कर्मचारी ऑफ द मंथ का सम्मान मिला।” to English. Will do its analysis later on.

## End-note
Thank you for patiently reading till here. I am pretty sure just like me, you would have also learnt something new about developing a Streamlit-based application using models hosted on HuggingFace, then dockerizing the application and deploying it to cloud platform. Using these learnt concepts, I will push myself to explore more practical deployment techniques, tools and concepts to scale this repo further. I encourage you also to do the same!!

## Contributing
You are welcome to contribute to the repository with your PRs. In case of query or feedback, please write to me at 13.malayjoshi@gmail.com or https://www.linkedin.com/in/malayjoshi13/.
