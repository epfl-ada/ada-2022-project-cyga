import ast
import re
import nltk
import tqdm
import string

import matplotlib.pyplot as plt
import json as js
import pandas as pd
import seaborn as sns
import xml.etree.ElementTree as ET

from nltk.corpus import stopwords
from fuzzywuzzy import fuzz
from scipy.stats import chi2_contingency
from tqdm import tqdm


def dict_to_cols(row): 
    '''
    Allows to transform the dictionnary into a dataframe with multiple columns.
    :param row : row to transform
    :return : dataframe with multiple columns
    '''
    d = js.loads(row[1])
    return row[0], *list(d.values())


def dict_to_lst(stri):
    '''
    Allows to transform a dictionnary into a list of features.
    :param stri : 
    :return : list of features
    '''
    dict = ast.literal_eval(stri)
    lst  = list(dict.values())
    return lst


def indicator_variable(dic,x,s):
    '''
    Returns indicator variable which equals to 1 if the corresponding headline uses 
    the corresponding type of pronoun and 0 otherwise.
    :param dic: dictionary
    :param x: string
    :param s: string
    :return: indicator variable
    '''
    return int(bool(set(dic[s]) & set(x.lower().split(" "))))


def count_word(word,string):
    """
    Returns the number of times a word appears in a string.
    :param word: string
    :param string: string
    :return: integer
    """
    return string.count(word)


def group_genres(genre):
    """
    Group genres into clusters.
    :param genre: string
    :return: string
    """
    genre_groups = {
        'Romance Film': 'Romance',
        'Romantic comedy': 'Romance',
        'Romantic drama': 'Romance',
        'Comedy-drama': 'Comedy',
        'Action Comedy': 'Comedy',
        'Comedy': 'Comedy',
        'Comedy film': 'Comedy',
        'Addiction Drama': 'Drama',
        'Costume Drama': 'Drama',
        'Drama': 'Drama',
        'Historical drama': 'Drama',
        'Political drama': 'Drama',
        'Mariage drama': 'Drama',
        'Crime drama': 'Drama',
        'Biography': 'Biography',
        'Biographical film': 'Biography',
        'Documentary': 'Biography',
        'History': 'Biography',
        'Horror': 'Horror',
        'Mystery': 'Mystery',
        'Music': 'Music',
        'Musical': 'Music',
        'Action': 'Action',
        'Action/Adventure': 'Action',
        'Adventure': 'Adventure',
        'Action Thrillers': 'Action',
        'Psychological thriller': 'Thriller',
        'Crime Thriller': 'Crime',
        'Crime Fiction': 'Crime',
        'Sport': 'Sport',
        'Family Drama': 'Drama',
        'Western': 'Western',
    }
    return genre_groups.get(genre, genre)


def genre_pronoun(row):
    """
    Assigns a gender to the movie in function of the highest pronoun occurence.
    :param row: dataframe row
    :return: string
    """
    if row['fem_occurence'] > row['masc_occurence']:
        return 'F'
    elif row['fem_occurence'] < row['masc_occurence']:
        return 'M'
    else:
        return 'N'


def transform_zeros(val):
    """
    Transforms zeros into 255.
    :param val: integer
    :return: integer
    """
    if val.all() == 0: 
       return val.all()
    else:
       return 255


def clean_text(text):
    """
    Cleans text.
    :param text: string
    :return: string
    """
    # remove backslash-apostrophe 
    text = re.sub("\'", "", text) 
    # remove everything except alphabets 
    text = re.sub("[^a-zA-Z]"," ",text) 
    # remove whitespaces 
    text = ' '.join(text.split()) 
    # convert text to lowercase 
    text = text.lower() 
    
    return text


def remove_stopwords(text):
    """
    Removes stopwords.
    :param text: string
    :return: string
    """
    stop_words = set(stopwords.words('english'))
    no_stopword_text = [w for w in text.split() if not w in stop_words]
    return ' '.join(no_stopword_text)


def freq_words(x,terms=30,a=0):
    """
    Generates a wordcloud.
    :param x: dataframe
    :param terms: integer
    :return: dataframe
    """ 
    all_words = ' '.join([text for text in x])
    all_words = all_words.split()
    fdist = nltk.FreqDist(all_words)
    words_df = pd.DataFrame({'word':list(fdist.keys()), 'count':list(fdist.values())})
    
    d = words_df.nlargest(columns="count", n = terms) # selecting top 20 most frequent words
    plt.figure(figsize=(12,15))
    ax = sns.barplot(data=d, x= "count", y = "word")
    ax.set(ylabel = 'Word')
    if a == 0:
        plt.title('Most frequent words in plot summaries for male main characters')
    else:
        plt.title('Most frequent words in plot summaries for female main characters')
    plt.show()
    return d


def gender_winner_association(data):
    """
    Calculates the observed frequencies, the overall proportions, the expeected frequencies and the chi-square statistic.
    :param data: dataframe
    :return: dataframe
    """
    # Calculate the observed frequencies of male and female directors nominated for and winning awards
    male_nominated = data[(data['gender'] == 'male') & (data['winner'] == False)].count()[0]
    female_nominated = data[(data['gender'] == 'female') & (data['winner'] == False)].count()[0]
    male_winner = data[(data['gender'] == 'male') & (data['winner'] == True)].count()[0]
    female_winner = data[(data['gender'] == 'female') & (data['winner'] == True)].count()[0]

    # Calculate the overall proportions of male and female nominees in the dataset
    total_male = data[data['gender'] == 'male'].count()[0]
    total_female = data[data['gender'] == 'female'].count()[0]
    total = total_male + total_female
    male_proportion = total_male / total
    female_proportion = total_female / total
    total_nominated = data.count()[0]
    total_winner = data[data['winner'] == True].count()[0]
    
    # Calculate the expected frequencies of male and female nominees for and winning awards
    expected_nominated_male = total_nominated * male_proportion
    expected_nominated_female = total_nominated * female_proportion
    expected_winner_male = total_winner * male_proportion
    expected_winner_female = total_winner * female_proportion

    # Perform the chi-squared test
    observed = [[male_nominated, female_nominated], [male_winner, female_winner]]
    expected = [[expected_nominated_male, expected_nominated_female], [expected_winner_male, expected_winner_female]]
    stat, p, dof, expected = chi2_contingency(observed, correction=True)

    # Interpret the results
    if p < 0.05:
        print("There is a significant difference between the observed and expected frequencies (p = {})".format(p.round(3)))
    else:
        print("There is no significant difference between the observed and expected frequencies (p = {})".format(p.round(3)))


def merge_on_category(data1,data2,category,name_dict):
    """
    Merges 2 datasets on category and name.
    :param data1: dataframe
    :param data2: dataframe
    :param category: string
    :param name_dict: dictionary
    :return: dataframe
    """
    # select category in the 2 datasets
    oscars_category = data1[data1['category']==category].reset_index(drop=True)
    oscar_nominees_category = data2[data2['category']==category].reset_index(drop=True)

    #replace the names in the 2 datasets
    oscars_category['name'] = oscars_category['name'].replace(name_dict)

    #merge the 2 datasets
    oscars_category["name"] = oscars_category["name"].str.lower()
    oscar_nominees_category["name"] = oscar_nominees_category["name"].str.lower()
    merged_category = pd.merge(oscars_category, oscar_nominees_category, on=["year_ceremony", "name", "category"])

    #drop column dups_nominees
    merged_category = merged_category.drop(['dups_nominees'],axis=1)

    return merged_category


def get_names_by_category(data1, data2,category):
    """
    Returns a list of names for a given category.
    :param data1: dataframe
    :param data2: dataframe
    :param category: string
    :return: list
    """
    oscar_nominees_names = list(data1[data1['category']==category].name.unique())
    oscars_names = list(data2[data2['category']==category].name.unique())
    return oscar_nominees_names, oscars_names


def match_names(name, list_names, min_score=0):
    """
    Returns the match and similarity score of the fuzz.ratio() scorer.
    :param name: string
    :param list_names: list
    :param min_score: integer
    :return: tuple
    """
    max_score = -1
    max_name = ''
    for x in list_names:
        score = fuzz.ratio(name, x)
        if (score > min_score) & (score > max_score):
            max_name = x
            max_score = score
    return (max_name, max_score)


def func_name_mapping(df1, df2, threshold):
    """
    Creates a dictionary of names to be replaced.
    For loop to create a list of tuples with the first value being the name from the second dataframe (name to replace) 
    and the second value from the first dataframe (string replacing the name value). Then, casting the list of tuples as a dictionary.
    :param df1: dataframe
    :param df2: dataframe
    :param threshold: integer
    :return: dictionary
    """
    names = []
    for name in df1:
        match = match_names(name, df2, threshold)
        if match[1] >= threshold:
            name_tuple = (str(name), str(match[0]))
            names.append(name_tuple)
    name_mapping = dict(names)
    return name_mapping


def get_p_value_by_category(data1,data2,category,threshold):
    """
    Returns a DataFrame with the category and p value.
    :param data1: dataframe
    :param data2: dataframe
    :param category: string
    :param threshold: integer
    :return: dataframe
    """
    # Get names of nominees and winners for the given category
    oscar_nominees_names, oscars_names = get_names_by_category(data1, data2, category)
    
    # Map names between the two datasets using a threshold
    names = func_name_mapping(oscars_names, oscar_nominees_names, threshold)
    
    # Merge the datasets on the given category and get the p value
    merged = merge_on_category(data2,data1, category, names)
    p_value = gender_winner_association(merged)
    
    # Return the category and p value as a DataFrame
    return pd.DataFrame({'category': [category], 'p_value': [p_value]})


def word_frequency(movies, gender_dictionary, pos_mapping, summary_path, window=2):
    """
    This function will count the frequency of words in the summary of a movie.
    :param movies: a dataframe of movies
    :param gender_dictionary: a dictionary
    :param pos_mapping: a dictionary
    :param summary_path: a string
    :param window: an integer (default: 2)
    :return: a dictionary of word frequency
    """
    for index, movie in tqdm(movies.iterrows()):
        for name, gender in movie.Character_names.items():
            assert gender == "F" or gender == "M"
            name_list = name.split()  # split the character name into words

            # use corenlp data to get the POS of words in the summary and lemmatize the summary of the plot.
            # lemmatization is the process of grouping together the inflected forms of a word so they can be analysed as a single item.
            tree = ET.parse(summary_path + str(movie.Wikipedia_movie_ID) + ".xml") # import the data
            root = tree.getroot() # returns the root element for this tree
            pos_list = root.findall(".//*POS")      # pos of the words
            word_list = root.findall(".//*lemma")   # lemma of the words

            idx = 0
            length_pos = len(pos_list)
            count_head, count_tail = 0, 0

            # scan the plot summary and extract all characters mentioned in the characters dataframe.
            while idx < length_pos:
                if (word_list[idx].text.lower() == name_list[0] and 
                    word_list[min(idx + len(name_list) - 1, length_pos - 1)].text.lower() == name_list[-1]):
                    head_idx = idx
                    tail_idx = idx + len(name_list) - 1

                    # backward search from the first word of the name.
                    for pre_idx in range(head_idx - 1, -1, -1):
                        if pos_list[pre_idx].text in pos_mapping.keys():
                            # compute word frequency for all words/verbs/adjectives/nouns
                            try:
                                gender_dictionary[gender]["all"][word_list[pre_idx].text.lower()] += 1
                            except:
                                gender_dictionary[gender]["all"][word_list[pre_idx].text.lower()] = 1

                            try:
                                gender_dictionary[gender][pos_mapping[pos_list[pre_idx].text]][word_list[pre_idx].text.lower()] += 1
                            except:
                                gender_dictionary[gender][pos_mapping[pos_list[pre_idx].text]][word_list[pre_idx].text.lower()] = 1

                            count_head += 1
                            
                        # stop searching if the window size is reached.
                        if count_head == window:
                            break
                        # stop searching if the sentence is ended.
                        if word_list[pre_idx].text in string.punctuation:
                            break

                    # forward search from the last word of the name.
                    for nxt_idx in range(tail_idx + 1, length_pos):
                        if pos_list[nxt_idx].text in pos_mapping.keys():
                            # compute word frequency for all words/verbs/adjectives/nouns
                            try:
                                gender_dictionary[gender]["all"][word_list[nxt_idx].text.lower()] += 1
                            except:
                                gender_dictionary[gender]["all"][word_list[nxt_idx].text.lower()] = 1

                            try:
                                gender_dictionary[gender][pos_mapping[pos_list[nxt_idx].text]][word_list[nxt_idx].text.lower()] += 1
                            except:
                                gender_dictionary[gender][pos_mapping[pos_list[nxt_idx].text]][word_list[nxt_idx].text.lower()] = 1

                            count_tail += 1

                        # stop searching if the window size is reached.
                        if count_tail == window:
                            break

                        # stop searching if the sentence is ended.
                        if word_list[nxt_idx].text in string.punctuation:
                            break

                    idx = tail_idx + 1

                else:
                    idx += 1

    return gender_dictionary