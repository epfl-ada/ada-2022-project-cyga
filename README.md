# ada-2022-project-cyga

## Table of Contents
1. [Abstract](#Abstract)
2. [Datastory](#Datastory)
3. [Research questions](#Research_questions)
4. [Proposed additional datasets and files](#Proposed_additional_datasets_and_files)
5. [Methods](#Methods)
6. [Proposed timeline](#Proposed_timeline)
7. [Organisation within the team](#Organisation_within_the_team)


## Datastory <a name="Datastory"></a>
The Datastory of our project can be found [here](https://yasmineeleuch.github.io/gender-gap/#what).

It was created via Jekyll.
 
 
## Abstract <a name="Abstract"></a>
# The evolution of the gender gap in the film industry
Our goal with this work is to analyze the evolution in time of the gender gap and women discrimination in the film industry, which is known as one of the least women-friendly industries: [almost 9 in 10 films (89%) have more men in their 10 or so most senior roles, both acting and non-acting](https://www.bbc.com/culture/article/20180508-the-data-that-reveals-the-film-industrys-woman-problem). In a recent interview with The CEO Magazine, actress and producer Reese Witherspoon spoke out about the ongoing gender imbalances in Hollywood. She discussed the difficulties that women face in the industry, particularly when it comes to the types of roles available to them. “These women are accomplished and they deserve to be the center of their own stories,” said Witherspoon. “But very often, everything the woman in the script says appears to be in service of the male characters.” This quote highlights one of the major issues faced by women in the movie industry – the lack of complex, fully-developed female characters and the frequent sidelining of women's stories in favor of male-driven narratives. The film industry has long been criticized for its gender imbalances, including the underrepresentation of women in acting and directing roles and the frequent awarding of prizes to men. Witherspoon's comments speak to the need for greater representation and equal opportunities for women in Hollywood. This need from the film community gave birth to, among other things, the #MeToo movement, known for its apogee in 2017 with the complaints of many known actresses about the sexism and assaults in the film industry. This gender rights movement appeared in reality in 2007, which translates this desire of improvement already present for a long time. 

In an effort to understand the gender gap in the fast-growing and money-generating industry that is the film industry, we will use the [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) dataset to examine the representation of women in movie plots, principal roles, lexical fields, movie ratings, awards nominees, and winners.


## Research Questions <a name="Research_questions"></a>
In order to have a real insight on gender (in)equality on screen and on set, we worked around different axes around the topic of women representation. The different questions around women representation are the following:
Are women present (quantitatively) in movies ?
What are they associated with ? How do we talk about these women ?
What kind of roles are the most appreciated ? How do people like to see women ?
How do women interact, with other women and with men? Are there existing methods present to assess the gender gap in movies?


## Proposed additional datasets (if any) <a name="Proposed_additional_datasets_and_files"></a>

Additional dataset#1 : The IMDb title basics and title ratings datasets have been found on [IMDb](https://datasets.imdbws.com/) (title.ratings.tsv and title.basics.tsv). The title_bascis.tsv is useful to associate movie titles to the IMDb movies IDs. We are mainly interested in the IMDb score and number of votes per movie. This score, between 1 and 10, casted by IMDb users, and these votes are then aggregated and summarized in a single [rating](https://help.imdb.com/article/imdb/track-movies-tv/ratings-faq/G67Y87TFYYP6TWAV#). The idea is to compare the ratings of movies with the same features and determine whether casting a female or a male main protagonist impacts the rating of a movie. The added value of this feature (score of movie) lies in the fact that we can look at what people external to the film industry think, so we can extract discrimination out of what people like the most to see (so which stereotypes are they reactive to) and how what people like to see has evolved. 

Additional dataset#2 : The Academy Awards nominees (oscar_nominees.csv), 1929-2019 dataset contains the official record of past Academy Award nominees. This dataset contains the nominees for each year in different categories as well as their genre. 

Additional dataset#3 : The Academy Awards nominees and winners (oscar_nom_win.csv), 1929-2020 dataset contains the official record of past Academy Award nominees and whether the nominees won an award for a specific category. This time, the genre is not included. The final goal is to merge this dataset with the previous one in order to perform some analyses on both datasets.

Additional dataset#3 : The Bechdel dataset (Bechdel.csv) contains the Bechdel score for a variety of movies. The Bechdel test, also known as the Bechdel-Wallace test, is a measure of the representation of women in fiction. It consists of three criteria:
The work must have at least two women in it who talk to each other.
The conversation must be about something other than a man.
The women must have names.
The Bechdel test is often used to evaluate the representation of women in films, but it can also be applied to other forms of fiction, such as books and plays.
It has since become a widely used measure of gender representation in media. However, it is not a perfect measure, and some critics argue that it is too simplistic, and does not take into account other factors such as the agency and complexity of female characters.


## Methods <a name="Methods"></a>
Our notebook is subdivided into different axes. We are trying to answer the question asked before. 

1. Is there a pay gap and financial indices which could attest to potential gender discrimination in the movie industry?

We did some exploration in order to assess the gender gap through financial indicators, but did not find enough data. The only feature we were able to look at is the movie box office revenue. This could have been an interesting aspect for the gender gap as gender discrimination is often primarily expressed through the pay gap.

2. Are women present (quantitatively)?

We first performed some little insights on datasets, by looking at the number of actresses vs actors. In a second step, we analyzed the feminine/masculine pronouns occurrence in the movie plots. We then included a timeline in our analysis : in other words, we looked at if there was a difference over time periods. Finally, we detected the main character of a movie by analyzing the summaries. We then looked at the evolution of main role attribution in function of the gender through time and realized linear regressions to attest to a significant trend or not. 

3. What are they associated with? How do we talk about these women?
Globally, we want to see if the movie plot summaries contain gender stereotypes and analyze how characters are described and talked about in function of their gender. 

Associate certain movie genres to male and female actors and see what stereotypes get out of it - visualization with word clouds.
By using a word frequency function, determine the words associated with masculine and feminine characters separately and look at stereotypes.
Predict the gender of the main character based on the movie plot. This is done with a ML model. We divide the data into a training and a test set, as we already know the gender of the main character.
Using the plot summaries from the CMU Movie Summary Corpus, run through the Stanford CoreNLP pipeline (tagging, parsing, NER, and coref), we took into account the 2 words before and after the main character name and identified gender-specific words that are pertinent to these names and calculate their frequency.
By means of word embedding (BERT and Word2Vec), we tried to determine whether words from summaries were more associated with men or women. Nevertheless, the model was too big and we encountered some problems in its training. We thus didn’t manage to make it work properly.

4. What kind of roles are the most appreciated? How do people like to see women? 
From IMDB ratings, we checked the number of women between high and low score movies. We quickly looked at the number of votes depending on different features, as the number of votes can also indicate what people are attracted the most to. For the same genre and the same release year, we compared the ratings of movies where the main actor was female or male, in order to determine if the gender of the main character could have an impact on the final rating of the movie.
Using the Oscars nominees and winners dataset, we looked at the jobs related to the movie industry (i.e. not only actresses or actors). Is the work of women in general (other fields than acting) less/at the same level/more appreciated than the work of men? To this end, we compared all the Oscars nominees for all categories and looked at their evolution through time (linear regression). Then we performed some statistical tests ($Chi^2$ test) among different categories in order to see if women are less likely to win awards than men. 

5. How do women interact, with other women and with men? 

Finally, we compared our overall results with existing methods to assess the gender inequality in the movies, namely the Bechdel Test. As explained before, it is not a perfect measure. However, the Bechdel test remains a widely used and influential tool for evaluating the representation of women in media. This allowed us to conclude on the gender gap and its evolution in the film industry.


6. Conclusion
After conducting an analysis on the gender gap in the film industry, it is clear that there is a significant imbalance in the representation and opportunities afforded to male and female movie industry workers. This gap can be observed in various areas of the industry, including the number of female directors and writers, the prevalence of male-dominated storylines and characters, and recognition received by male and female talent.  This gender gap is a complex issue with many contributing factors, including longstanding cultural biases, systemic discrimination, and a lack of diversity and inclusivity in the industry. Closing the gender gap in the film industry will require a concerted effort from all stakeholders, including studios, production companies, and industry organizations, to promote equal representation and opportunities for women. It will also require a commitment to diversity and inclusivity at all levels of the industry, from hiring and casting to financing and distribution. We can already observe a certain improvement, for example in the ratio of lead roles attributed to women as well as in the representation of women on screen with the evolution of the Bechdel score. But it is important to continue to critically examine and address imbalances and inequalities in the representation of all categories within the film industry. Overall, it is clear that the gender gap in the film industry is a pressing issue that needs to be addressed in order to create a more diverse and equitable industry for all. By acknowledging and addressing this gap, we can work towards creating a film industry that better reflects and serves the diverse experiences and perspectives of our society. 


## Proposed timeline <a name="Proposed_timeline"></a>

See different milestones in the following point ‘Organization within the team’

* Milestone 1: Project definition, and first insights in the dataset. 

* Milestone 2: Data cleaning and preprocessing; Looking for new datasets.

* Milestone 3: Answering questions 1-5 - coding, analysis of results, comparison with literature.

* Milestone 4: Code proofreading, datastory preparation,  and plot customizing.


## Organization within the team <a name="Organisation_within_the_team"></a>
A list of internal milestones up until project Milestone P3.

* * Yasmine : datasets preprocessing, main character detection, stereotypes with movie genres (word clouds), datastory (website) coding
* Aliénor : pronoun occurrences, main character detection evolution, rating analysis, datastory customizing 
* Clara : data preprocessing, financial analysis, Stanford CoreNLP-processed summaries extraction of words associated with character names, code proofreading, plots customizing
* Guillaume : work on the additional datasets (oscars nominees, oscar winners, and Bechdel), datastory writing


## Authors
- [Yasmin El Euch](https://github.com/yasmineeleuch)
- [Aliénor Bénédicte G Hamoir](https://github.com/AlienorHamoir)
- [Clara Rossignol](https://github.com/clara-rossignol)
- [Guillaume David E. Ryelandt](https://github.com/guillaumeryelandt)

