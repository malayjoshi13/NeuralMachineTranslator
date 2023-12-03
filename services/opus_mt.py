# Hindi to English

# OPUS-MT models are SDMT (single direction machine translation) which can translate data in one direction only,
# thus we don't specify source and language ids while loading the tokenizer or creating the pipeline object.

from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import streamlit as st 
import time

@st.cache_resource
def load_opus_mt_pipeline():
    # Step 1 : Set the device to GPU if you want. By default pipeline uses CPU only.
    device = torch.cuda.current_device() if torch.cuda.is_available() else -1

    # # Uncomment below three lines to save the OPUS_MT model in starting, no need now.
    # model_name = 'Helsinki-NLP/opus-mt-hi-en'     
    # model = AutoModelForSeq2SeqLM.from_pretrained(model_name)    
    # model.save_pretrained("models_and_tokenizers/opus_mt")

    # Step 2.1. : Load the locally saved OPUS_MT model
    model = AutoModelForSeq2SeqLM.from_pretrained("./models/opus_mt")

    # # Uncomment below two lines to save the tokenizer in starting, no need now.
    # tokenizer = AutoTokenizer.from_pretrained(model_name)
    # tokenizer.save_pretrained("models_and_tokenizers/opus_mt")

    # Step 2.2. : Load the locally saved tokenizer
    tokenizer = AutoTokenizer.from_pretrained("./models/opus_mt")

    # Step 3 : Create pipeline object by passing the phrase “translation” along with the tokenizer and model objects.
    # Within Pipeline object three things take place:-
    # a) tokenizing the source text sequence, i.e. input = tokenizer(src_seq)
    # b) generating the target sequence ids, i.e. tgt_seq_ids = model.generate(**input)
    # c) generating the target sequence by decoding target sequence ids, i.e. tgt_seq = tokenizer.decode(tgt_seq_ids)
    translator = pipeline('translation', model=model, tokenizer=tokenizer, device=device)

    return translator


def opus_mt_translate(text):

    start = time.time()

    ########################################

    # Before using streamlit's cache and before saving model in-advance locally

    # #Step 1 : Set the device to GPU if you want. By default pipeline uses CPU only.
    # device = torch.cuda.current_device() if torch.cuda.is_available() else -1

    # # Step 2.1. : Load OPUS_MT model using AutoModelForSeqtoSeqLM class from transformers library.
    # model_name = 'Helsinki-NLP/opus-mt-hi-en' 
    # model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # # Step 2.2. : Load the tokenizer using AutoTokenizer class from transformers library.
    # tokenizer = AutoTokenizer.from_pretrained(model_name)

    # # Step 3 : Create pipeline object by passing the phrase “translation” along with the tokenizer and model objects.
    # # Within Pipeline object three things take place:-
    # # a) tokenizing the source text sequence, i.e. input = tokenizer(src_seq)
    # # b) generating the target sequence ids, i.e. tgt_seq_ids = model.generate(**input)
    # # c) generating the target sequence by decoding target sequence ids, i.e. tgt_seq = tokenizer.decode(tgt_seq_ids)
    # translator = pipeline('translation', model=model, tokenizer=tokenizer, device=device)

    ########################################

    # After using streamlit's cache and adter saving model in-advance locally

    # Step 3 : Call "load_opus_mt_pipeline" to create the pipeline object   
    translator = load_opus_mt_pipeline()

    ########################################

    # Step 4 : Get the translated sequence by passing source sequence to the pipeline object.
    # Along with source sequence, we can also pass other arguments like max_length, min_length etc. which controls the generation of target sequence.
    target_seq = translator(text, max_length=128)
    translated = target_seq[0]['translation_text']

    # Step 5 : Display time taken for process to complete
    end = time.time()
    time_taken = end - start
    print("total time taken for translation "+str(time_taken)+" seconds")

    # Step 6 : Return the translated sentence
    return translated