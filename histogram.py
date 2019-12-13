def file_or_string(source_text):
    content = ''
    if '.txt' in source_text:
        file = open(source_text, 'r')
        content = file.read()
        file.close()
    else:
        content = source_text
    return content

def list_of_lists_histogram(source_text):
    words = []
    content = file_or_string(source_text)
    words = content.split()
    histogram = []
    for word in words:
        is_in_histogram = False
        for i in range(len(histogram)):
            if word == histogram[i][0]:
                histogram[i][1] += 1
                is_in_histogram = True

        if is_in_histogram == False:
            histogram.append([word, 1])
    
    return histogram

def list_of_tuples_histogram(source_text):
    words = []
    content = file_or_string(source_text)
    words = content.split()
    histogram = []
    for word in words:
        is_in_histogram = False
        for i in range(len(histogram)):
            if word == histogram[i][0]:
                histogram[i] = (word, (histogram[i][1])+1)
                is_in_histogram = True

        if is_in_histogram == False:
            histogram.append((word, 1))
    
    return histogram

def dictionary_histogram(source_text):
    words = []
    histogram = {}
    content = file_or_string(source_text)
    words = content.split()
    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def unique_words(histogram):
    return len(histogram)

def word_frequency(histogram, word):
    for i in range(len(histogram)):
        if word == histogram[i][0]:
            return histogram[i][1]
        
hist = list_of_tuples_histogram('poetry_snippet.txt')