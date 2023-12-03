from services import m2m, mbart

def model_list(source_language, target_language):
    # If source languae is Hindi and target language is English:
    if source_language == "Hindi" and target_language == "English":
        models = [" ", "Helsinki-NLP/opus-mt-en-hi", "facebook/mbart-large-50", "facebook/m2m100_418M"]

    # If source is anything supported by mbart and m2m + target is English:
    elif source_language in mbart.mbart_languages_dict.keys() and source_language in m2m.m2m_100_languages_dict.keys() and target_language=="English":
        models = [" ", "facebook/mbart-large-50", "facebook/m2m100_418M"]

    # If source is anything only supported by mbart + target is English:
    elif source_language in mbart.mbart_languages_dict.keys() and source_language not in m2m.m2m_languages_dict.keys() and target_language=="English":
        models = [" ", "facebook/mbart-large-50"]

    # If source is anything only supported by mbart but target is not English:
    elif source_language in mbart.mbart_languages_dict.keys() and source_language not in m2m.m2m_languages_dict.keys() and target_language!="English":
        models = [" "]

    # If source is anything only supported by m2m + target is anything only supported by m2m
    elif source_language not in mbart.mbart_languages_dict.keys() and source_language in m2m.m2m_languages_dict.keys() and target_language in m2m.m2m_languages_dict.keys():
        models = [" ", "facebook/m2m100_418M"]

    # If source is supported by both, but target is not English; only supported by m2m:
    elif source_language in mbart.mbart_languages_dict.keys() and source_language in m2m.m2m_languages_dict.keys() and target_language!="English":
        models = [" ", "facebook/m2m100_418M"] 

    return models