# mBART's MM --> any of the 50 languages (supported by this model) to any of the other 49 left languages (supported by this model) 
# mBART's MO --> any of the 49 languages (supported by this model) to English
# mBART's OM --> English to any of the 49 languages (supported by this model)


# Here we can observe that we specify source and language ids while loading the tokenizer and creating the pipeline object.
# This is because mBART models are MDMT (multi direction machine translation) models which can translate data in multiple directions.
# Without specifying source and language ids in case of MDMT models will result in error.

from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import streamlit as st 
import time

mbart_languages_dict = {
    'Arabic': 'ar_AR',
    'Czech': 'cs_CZ',
    'German': 'de_DE',
    'English': 'en_XX',
    'Spanish': 'es_XX',
    'Estonian': 'et_EE',
    'Finnish': 'fi_FI',
    'French': 'fr_XX',
    'Gujarati': 'gu_IN',
    'Hindi': 'hi_IN',
    'Italian': 'it_IT',
    'Japanese': 'ja_XX',
    'Kazakh': 'kk_KZ',
    'Korean': 'ko_KR',
    'Lithuanian': 'lt_LT',
    'Latvian': 'lv_LV',
    'Burmese': 'my_MM',
    'Nepali': 'ne_NP',
    'Dutch': 'nl_XX',
    'Romanian': 'ro_RO',
    'Russian': 'ru_RU',
    'Sinhala': 'si_LK',
    'Turkish': 'tr_TR',
    'Vietnamese': 'vi_VN',
    'Chinese': 'zh_CN',
    'Afrikaans': 'af_ZA',
    'Azerbaijani': 'az_AZ',
    'Bengali': 'bn_IN',
    'Persian': 'fa_IR',
    'Hebrew': 'he_IL',
    'Croatian': 'hr_HR',
    'Indonesian': 'id_ID',
    'Georgian': 'ka_GE',
    'Khmer': 'km_KH',
    'Macedonian': 'mk_MK',
    'Malayalam': 'ml_IN',
    'Mongolian': 'mn_MN',
    'Marathi': 'mr_IN',
    'Polish': 'pl_PL',
    'Pashto': 'ps_AF',
    'Portuguese': 'pt_XX',
    'Swedish': 'sv_SE',
    'Swahili': 'sw_KE',
    'Tamil': 'ta_IN',
    'Telugu': 'te_IN',
    'Thai': 'th_TH',
    'Tagalog': 'tl_XX',
    'Ukrainian': 'uk_UA',
    'Urdu': 'ur_PK',
    'Xhosa': 'xh_ZA',
    'Galician': 'gl_ES',
    'Slovene': 'sl_SI'
}

@st.cache_resource
def load_mbart_pipeline(src_lang, tgt_lang):
    src_lang = mbart_languages_dict[src_lang]
    tgt_lang = mbart_languages_dict[tgt_lang]

    print(src_lang)
    print(tgt_lang)

    # Step 1 : Set the device to GPU if you want. By default pipeline uses CPU only.
    device = torch.cuda.current_device() if torch.cuda.is_available() else -1

    # Uncomment below three lines to save the mbart model in starting, no need now.
    # model_name = 'facebook/mbart-large-50-many-to-one-mmt' # 'facebook/mbart-large-50-many-to-many-mmt'    
    # model = AutoModelForSeq2SeqLM.from_pretrained(model_name)    
    # model.save_pretrained("models_and_tokenizers/mbart")
    
    # # Step 2.1. : Load the locally saved mBART's MO model or, the mBART's MM model   
    model = AutoModelForSeq2SeqLM.from_pretrained("./models/mbart")

    # Uncomment below two lines to save the tokenizer in starting, no need now.
    # tokenizer = AutoTokenizer.from_pretrained(model_name, src_lang=src_lang, tgt_lang=tgt_lang)
    # tokenizer.save_pretrained("models_and_tokenizers/mbart")

    # # Step 2.2. : Load the locally saved tokenizer
    tokenizer = AutoTokenizer.from_pretrained("./models/mbart", src_lang=src_lang, tgt_lang=tgt_lang)

    # Step 3 : Create pipeline object by passing the phrase “translation” along with the tokenizer and model objects.
    # Within Pipeline object three things take place:-
    # a) tokenizing the source text sequence, i.e. input = tokenizer(src_seq)
    # b) generating the target sequence ids, i.e. tgt_seq_ids = model.generate(**input)
    # c) generating the target sequence by decoding target sequence ids, i.e. tgt_seq = tokenizer.decode(tgt_seq_ids)
    translator = pipeline('translation_XX_to_YY', model=model, tokenizer=tokenizer,src_lang=src_lang, tgt_lang=tgt_lang,device=device)

    return translator

def mbart_translate(text, src_lang, tgt_lang):

    start = time.time()

    ########################################

    # Before using streamlit's cache and before saving model in-advance locally

    # #Step 1 : Set the device to GPU if you want. By default pipeline uses CPU only.
    # device = torch.cuda.current_device() if torch.cuda.is_available() else -1

    # #Step 2.1. : Load the mBART's MO model or, the mBART's MM model using AutoModelForSeqtoSeqLM class from transformers library.
    # model_name = 'facebook/mbart-large-50-many-to-one-mmt' # 'facebook/mbart-large-50-many-to-many-mmt'
    # model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # # Step 2.2. : Load the tokenizer using AutoTokenizer class from transformers library.
    # src_lang = mbart_languages_dict[src_lang]
    # tgt_lang = mbart_languages_dict[tgt_lang]
    # tokenizer = AutoTokenizer.from_pretrained(model_name, src_lang=src_lang, tgt_lang=tgt_lang)

    # # Step 3 : Create pipeline object by passing the phrase “translation” along with the tokenizer and model objects.
    # # Within Pipeline object three things take place:-
    # # a) tokenizing the source text sequence, i.e. input = tokenizer(src_seq)
    # # b) generating the target sequence ids, i.e. tgt_seq_ids = model.generate(**input)
    # # c) generating the target sequence by decoding target sequence ids, i.e. tgt_seq = tokenizer.decode(tgt_seq_ids)
    # translator = pipeline('translation_XX_to_YY', model=model, tokenizer=tokenizer,src_lang=src_lang, tgt_lang=tgt_lang,device=device)

    ########################################

    # After using streamlit's cache and after saving model in-advance locally

    # Step 3 : Call "load_m2m_pipeline" to create the pipeline object   
    translator = load_mbart_pipeline(src_lang, tgt_lang)

    ########################################
    # Step 4 : Get the translated sequence by passing source sequence to the pipeline object.
    # Along with source sequence, we can also pass other arguments like max_length, min_length etc. which controls the generation of target sequence.    
    target_seq = translator(text, max_length=128)
    translated = target_seq[0]['translation_text'].strip('YY ')

    # Step 5 : Display time taken for process to complete
    end = time.time()
    time_taken = end - start
    print("total time taken for translation "+str(time_taken)+" seconds")

    # Step 6 : Return the translated sentence
    return translated