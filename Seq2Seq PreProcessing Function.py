#please work
file_link = r'C:\Users\rober\Desktop\coding_projects\project_gutenberg_book.txt'     # r makes it a raw string and ignores escape characters

def word_frequency(file_link,desired_words):
    frequency_dic = {}
    for item in desired_words:
        # item = item.strip()
        # item = item.lower()
        frequency_dic[item] = 0
    

    with open (file_link, "r", encoding='utf-8') as input_file:     #opens file(with an auto close) specifies reading and encoding type
        for line in input_file:                                     
            line= line.strip()                                      #takes out unnessary spaces in the lines
            line = line.replace ('.' , '').replace (',' , '')         # replaces ,.'s with nothing                               
            line = line.lower()                                     # makes the whole thing lowercase
            refined_words = line.split(" ")                           #seperates a strings based on a delimiter, aka a character used to seperate strings
            for word in refined_words:
                if word in frequency_dic:
                    frequency_dic[word] = frequency_dic[word]+ 1      # Changes the value of keys in a dictonary 
    print(frequency_dic)

word_frequency(file_link, ['the','is','a'])
#thank you
