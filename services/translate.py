from services import m2m, mbart, opus_mt

def do_translation(translation_model, source_text, source_language, target_language):
    if translation_model == "Helsinki-NLP/opus-mt-en-hi":
        translated_output = opus_mt.opus_mt_translate(source_text)
    elif translation_model == "facebook/mbart-large-50":
        translated_output = mbart.mbart_translate(source_text, source_language, target_language)
    elif translation_model == "facebook/m2m100_418M":
        translated_output = m2m.m2m_translate(source_text, source_language, target_language)

    return translated_output