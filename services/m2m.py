# m2m_100 --> any of the 100 languages (supported by this model) to any of the other 99 left languages (supported by this model) 

# Here we can observe that we specify source and language ids while loading the tokenizer and creating the pipeline object.
# This is because m2m_100 model are MDMT (multi direction machine translation) models which can translate data in multiple directions.
# Without specifying source and language ids in case of MDMT models will result in error.

from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import streamlit as st 
import time

m2m_languages_dict = {
    'Afrikaans': 'af',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Asturian': 'ast',
    'Azerbaijani': 'az',
    'Bashkir': 'ba',
    'Belarusian': 'be',
    'Bulgarian': 'bg',
    'Bengali': 'bn',
    'Breton': 'br',
    'Bosnian': 'bs',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Czech': 'cs',
    'Welsh': 'cy',
    'Danish': 'da',
    'German': 'de',
    'Greek': 'el',
    'English': 'en',
    'Spanish': 'es',
    'Estonian': 'et',
    'Persian': 'fa',
    'Fulah': 'ff',
    'Finnish': 'fi',
    'French': 'fr',
    'Western Frisian': 'fy',
    'Irish': 'ga',
    'Gaelic': 'gd',
    'Galician': 'gl',
    'Gujarati': 'gu',
    'Hausa': 'ha',
    'Hebrew': 'he',
    'Hindi': 'hi',
    'Croatian': 'hr',
    'Haitian': 'ht',
    'Hungarian': 'hu',
    'Armenian': 'hy',
    'Indonesian': 'id',
    'Igbo': 'ig',
    'Iloko': 'ilo',
    'Icelandic': 'is',
    'Italian': 'it',
    'Japanese': 'ja',
    'Javanese': 'jv',
    'Georgian': 'ka',
    'Kazakh': 'kk',
    'Central Khmer': 'km',
    'Kannada': 'kn',
    'Korean': 'ko',
    'Luxembourgish': 'lb',
    'Ganda': 'lg',
    'Lingala': 'ln',
    'Lao': 'lo',
    'Lithuanian': 'lt',
    'Latvian': 'lv',
    'Malagasy': 'mg',
    'Macedonian': 'mk',
    'Malayalam': 'ml',
    'Mongolian': 'mn',
    'Marathi': 'mr',
    'Malay': 'ms',
    'Burmese': 'my',
    'Nepali': 'ne',
    'Dutch': 'nl',
    'Norwegian': 'no',
    'Northern Sotho': 'ns',
    'Oriya': 'or',
    'Punjabi': 'pa',
    'Polish': 'pl',
    'Pushto': 'ps',
    'Portuguese': 'pt',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Sindhi': 'sd',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Somali': 'so',
    'Albanian': 'sq',
    'Serbian': 'sr',
    'Swati': 'ss',
    'Sundanese': 'su',
    'Swedish': 'sv',
    'Swahili': 'sw',
    'Tamil': 'ta',
    'Thai': 'th',
    'Tagalog': 'tl',
    'Tswana': 'tn',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Uzbek': 'uz',
    'Vietnamese': 'vi',
    'Wolof': 'wo',
    'Xhosa': 'xh',
    'Yiddish': 'yi',
    'Yoruba': 'yo',
    'Chinese': 'zh',
    'Zulu': 'zu'
}

@st.cache_resource
def load_m2m_pipeline(src_lang, tgt_lang):
    src_lang = m2m_languages_dict[src_lang]
    tgt_lang = m2m_languages_dict[tgt_lang]

    # Step 1 : Set the device to GPU if you want. By default pipeline uses CPU only.
    device = torch.cuda.current_device() if torch.cuda.is_available() else -1

    # #Uncomment below three lines to save the m2m_100 model in starting, no need now.
    # model_name = 'facebook/m2m100_418M' # 'facebook/m2m100_1.2B'
    # model = AutoModelForSeq2SeqLM.from_pretrained(model_name)    
    # model.save_pretrained("models_and_tokenizers/m2m")

    # Step 2.1. : Load the locally saved M2M100's 418 Million or 1.2 Billion parameter model
    model = AutoModelForSeq2SeqLM.from_pretrained("./models/m2m")

    # #Uncomment below two lines to save the tokenizer in starting, no need now.
    # tokenizer = AutoTokenizer.from_pretrained(model_name, src_lang=src_lang, tgt_lang=tgt_lang)
    # tokenizer.save_pretrained("models_and_tokenizers/m2m")

    # Step 2.2. : Load the locally saved tokenizer
    tokenizer = AutoTokenizer.from_pretrained("./models/m2m", src_lang=src_lang, tgt_lang=tgt_lang)

    # Step 3 : Create pipeline object by passing the phrase “translation” along with the tokenizer and model objects.
    # Within Pipeline object three things take place:-
    # a) tokenizing the source text sequence, i.e. input = tokenizer(src_seq)
    # b) generating the target sequence ids, i.e. tgt_seq_ids = model.generate(**input)
    # c) generating the target sequence by decoding target sequence ids, i.e. tgt_seq = tokenizer.decode(tgt_seq_ids)
    translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=src_lang, tgt_lang=tgt_lang, device=device)

    return translator

def m2m_translate(text, src_lang, tgt_lang):

    start = time.time()

    ########################################

    # Before using streamlit's cache and before saving model in-advance locally

    # #Step 1 : Set the device to GPU if you want. By default pipeline uses CPU only.
    # device = torch.cuda.current_device() if torch.cuda.is_available() else -1

    # # Step 2.1. : Load M2M100's 418 Million or 1.2 Billion parameter model using AutoModelForSeqtoSeqLM class from transformers library.
    # model_name = 'facebook/m2m100_418M' # 'facebook/m2m100_1.2B'
    # model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # # Step 2.2. : Load the tokenizer using AutoTokenizer class from transformers library.
    # src_lang = m2m_100_languages_dict[src_lang]
    # tgt_lang = m2m_100_languages_dict[tgt_lang]
    # tokenizer = AutoTokenizer.from_pretrained(model_name, src_lang=src_lang, tgt_lang=tgt_lang)

    # # Step 3 : Create pipeline object by passing the phrase “translation” along with the tokenizer and model objects.
    # # Within Pipeline object three things take place:-
    # # a) tokenizing the source text sequence, i.e. input = tokenizer(src_seq)
    # # b) generating the target sequence ids, i.e. tgt_seq_ids = model.generate(**input)
    # # c) generating the target sequence by decoding target sequence ids, i.e. tgt_seq = tokenizer.decode(tgt_seq_ids)
    # translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=src_lang, tgt_lang=tgt_lang, device=device)

    ########################################

    # After using streamlit's cache and adter saving model in-advance locally

    # Step 3 : Call "load_m2m_pipeline" to create the pipeline object   
    translator = load_m2m_pipeline(src_lang, tgt_lang)

    ########################################

    # Step 4 : Get the translated sequence by passing source sequence to the pipeline object.
    # Along with source sequence, we can also pass other arguments like max_length, min_length etc. which controls the generation of target sequence.    
    target_seq = translator(text, max_length=128)
    translated = target_seq [0]['translation_text']

    # Step 5 : Display time taken for process to complete
    end = time.time()
    time_taken = end - start
    print("total time taken for translation "+str(time_taken)+" seconds")

    # Step 6 : Return the translated sentence
    return translated