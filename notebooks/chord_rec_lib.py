# This Python file uses the following encoding: utf-8

import re
import os

# Шаг по осям спектрограммы
delta_t = 0.005079
delta_f = 172.265625

# Максимальная разница в секундах между скачанной песней и её размеченной версией
MAX_DUR_DELTA = 2

# Пути к различным папкам из корневой директории проекта
dnames = {'BB_DS_DIR':'base_data/McGill-Billboard',
          'BB_PARS_DS_DIR':'base_data/billboard-2.0.1-lab/McGill-Billboard',
          'CL_DS_DIR':'base_data/chordlab',
          'CSVS_DIR':'csvs',
          'RAW_SONGS_DIR':'raw_songs',
          'WAV_SONGS_DIR':'wav_songs',
          'SPECTRS_DIR': 'spectrs',
          'SONGS_PARSED_DIR': 'songs_parsed',
          'CHORDS_DIR': '../chords'}
 
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
    for c in ['(',')','\'', '.', '\`']:
        s = s.replace(c,'')
    s = re.sub(r"\(\)\'\,\`", '', s)
    s = re.sub(r'\bthe\b','',s)
    s = re.sub(r'\ba\b','',s)
    s = re.sub(r'\ban\b','',s)
    s = re.sub('&', 'and', s)
    s = s.strip(' ')
    s = s.replace(' ', space_replacer)
    return s

def find_files(dname, frmt=None):
    """
    Поиск всех файлов определённого (опционально) формата в папке dname
    """
    files = []
    for f in os.listdir(dname):
        fname = os.path.join(dname, f) 
        if os.path.isfile(fname):
            if frmt:
                if fname.endswith(frmt):
                    files.append(fname)
            else:
                files.append(fname)
        else:
            files += find_files(fname, frmt)
    return files