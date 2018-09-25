import re

# Пути к различным папкам из корневой директории проекта
dnames = {'BB_DS_DIR':'base_data\\McGill-Billboard',
          'BB_PARS_DS_DIR':'base_data/billboard-2.0.1-lab\\McGill-Billboard',
          'CL_DS_DIR':'base_data\\chordlab',
          'CSVS_DIR':'csvs'}
 
def format_name(s, space_replacer='_'):
    """
    Приведение к общему виду названий артистов и песен
    Входные данные:
    * s - исходная строка для форматирования
    * space_replacer - на какой символ заменять пробел в строке s
    Выходные данные:
    * Отформатированная строка s
    """
    s = s.lower()
#    for c in ['(',')','\'']:
#        s = s.replace(c,'')
    s = re.sub(r"\(\)\'\,\`", '', s)
    s = re.sub('&', 'and', s)
    s = s.strip(' ')
    s = s.replace(' ', space_replacer)
    return s