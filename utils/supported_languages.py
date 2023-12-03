language_list_opus_and_mbart = [
    "Arabic", "Czech", "German","Spanish","Estonian","Finnish","French","Gujarati",
    "Italian",
    "Japanese",
    "Kazakh",
    "Korean",
    "Lithuanian",
    "Latvian",
    "Burmese",
    "Nepali",
    "Dutch",
    "Romanian",
    "Russian",
    "Sinhala",
    "Turkish",
    "Vietnamese", 
    "Chinese", 
    "Afrikaans",
    "Azerbaijani",
    "Bengali",
    "Persian", 
    "Hebrew",
    "Croatian",
    "Indonesian", 
    "Georgian",
    "Khmer",
    "Macedonian",
    "Malayalam", 
    "Mongolian", 
    "Marathi",
    "Polish",
    "Pashto", 
    "Portuguese",
    "Swedish", 
    "Swahili",
    "Tamil", 
    "Telugu",
    "Thai",
    "Tagalog",
    "Ukrainian",
    "Urdu", 
    "Xhosa",
    "Galician", 
    "Slovene"    
]

language_list_m2m = [
    'Afrikaans', 'Amharic', 'Arabic', 'Asturian', 'Azerbaijani', 'Bashkir', 'Belarusian', 'Bulgarian', 'Bengali', 'Breton',
    'Bosnian', 'Catalan', 'Cebuano', 'Czech', 'Welsh', 'Danish', 'German', 'Greek', 'Spanish', 'Estonian', 'Persian',
    'Fulah', 'Finnish', 'French', 'Western Frisian', 'Irish', 'Gaelic', 'Galician', 'Gujarati', 'Hausa', 'Hebrew',
    'Croatian', 'Haitian', 'Hungarian', 'Armenian', 'Indonesian', 'Igbo', 'Iloko', 'Icelandic', 'Italian', 'Japanese',
    'Javanese', 'Georgian', 'Kazakh', 'Central Khmer', 'Kannada', 'Korean', 'Luxembourgish', 'Ganda', 'Lingala', 'Lao',
    'Lithuanian', 'Latvian', 'Malagasy', 'Macedonian', 'Malayalam', 'Mongolian', 'Marathi', 'Malay', 'Burmese', 'Nepali',
    'Dutch', 'Norwegian', 'Northern Sotho', 'Oriya', 'Punjabi', 'Polish', 'Pushto', 'Portuguese', 'Romanian', 'Russian',
    'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Albanian', 'Serbian', 'Swati', 'Sundanese', 'Swedish', 'Swahili',
    'Tamil', 'Thai', 'Tagalog', 'Tswana', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Wolof', 'Xhosa', 'Yiddish',
    'Yoruba', 'Chinese', 'Zulu']

initial = [" ", "Hindi", "English"]
language_list = list(set(language_list_opus_and_mbart + language_list_m2m))
language_list_sorted = sorted(language_list)
final_list = initial + language_list_sorted

