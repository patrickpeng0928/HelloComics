def getLexicon(file_name):
    '''
    read from a local file and create a list of words as a lexicon
    :param file_name: local file name
    :return: list
    '''
    word_list = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
    for line in lines:
        words = line.strip().split(',')
        for word in words:
            word_list.append(word.strip())
    return word_list