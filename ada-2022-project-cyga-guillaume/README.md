# ada-2022-project-cyga

## Table of Contents
1. [Abstract](#Abstract)
2. [Research questions](#Research_questions)
3. [Proposed additional datasets and files](#Proposed_additional_datasets_and_files)
4. [Methods](#Methods)
5. [Proposed timeline](#Proposed_timeline)
6. [Organisation within the team](#Organisation_within_the_team)
7. [Questions for the TAs](#Questions)


## Abstract <a name="Abstract"></a>

# The evolution of the gender gap in the film industry
Our goal with this work is to analyze the evolution in time of sexism and women discrimination in the film industry, which is known as one of the least women-friendly industries: [almost 9 in 10 films (89%) have more men in their 10 or so most senior roles, both acting and non-acting](https://www.bbc.com/culture/article/20180508-the-data-that-reveals-the-film-industrys-woman-problem). The #MeToo movement, known for its apogee in 2017 with the complaints of many known actresses about the sexism and assaults in the film industry, appeared in reality in 2007. It made less noise back then, but it was present and in many fields. The premises of free speech and liberation about the harassment, assault and rape culture women were suffering of, were launched. We want to tell the story of those women, particularly in the film industry, who suffer from daily discrimination. We want to have a look at the gender gap and how it has evolved in time, especially after the appearance of the #MeToo movement? Finally, the goal is to assess whether this movement has had a real impact on the situation.


## Research Questions <a name="Research_questions"></a>

Can we assess gender discrimination from a financial aspect: through budget, box office revenues and salaries? Is it trustworthy?

Can the summary/plot of a movie tell something about discrimination in the movie industry ? If so, how does the discrimination appear in summaries ? 

Are the types of roles attributed to women on screen a representation of the discrimination they undergo ? How did the types of roles attributed to women evolve in time ? Can this evolution attest to a decrease/increase in the gender gap ?


## Proposed additional datasets (if any) <a name="Proposed_additional_datasets_and_files"></a>

Additional dataset#1 : The IMDB 5000 Movie Dataset has been found on Kaggle. It is a CSV file of 1.49 MB. In this dataset, we are particularly interested in the IMDb score. This score between 1 and 10 is casted by IMDb users and these votes are then aggregated and summarized in a single rating (cf. https://help.imdb.com/article/imdb/track-movies-tv/ratings-faq/G67Y87TFYYP6TWAV#). The idea is to compare the rating of movies of the same genre and having equivalent stereotypical roles/tropes for feminine and masculine roles (ex: the handsome guy vs. the pretty girl). This could help to detect whether ratings are in general lower/higher in function of gender for “equivalent movies”. The added value of this feature (score of movie) lies in the fact that we can look at what people external to the film industry think so we can extract discrimination out of what people like the most to see (so which stereotypes are they reactive to) and how what people like to see has evolved. In this dataset, there is also data concerning the popularity of actors on facebook, namely the number of likes on their facebook page. Having an information about the popularity of the actors can be relevant as we could normalize by the popularity to compare discrimination in movies with different ranked actors. 

Additional dataset#2 : The Academy Awards, 1927-2015 dataset contains the official record of past Academy Award winners and nominees. It is interesting because it contains nominees and winners for different categories. This allow us to explore discrimination in other jobs of the film industry. We are interested in seeing whether the gender gap is also present not only in the cast but also in the directors for example. Unfortunately, we do not have the gender for the directors yet, but we can probably extract them using Python NLTK. This procedure needs to be confirmed.

## Methods <a name="Methods"></a>
First of all, we need to check and clean the data, and it would be very helpful to proceed to an exploratory sanity check. One must check whether all values seem reasonable, for example no negative ages, standardized date formats, NaN values. It is then important to choose well what to do with those values: finding the right ones elsewhere, discarding the row containing that value, etc.
In order to evaluate the gender gap in the film industry, we will have a look at 3 different axes. First, we'll check the financial aspect, trying to correlate the numbers to discrimination (while being careful to confounders). We'll have a look at the box office revenues and movie budgets. We also wanted to find the salaries of middle-class actors, which are expected to be reasonable to analyze but we couldn’t manage to find reliable enough free databases. 
Secondly, we will analyze the evolution of the types of roles attributed to women, to see if there is an improvement in this sense to diminish the gender gap. To do so, we will look at textual data with NLP libraries (i.e. we will treat the summaries) through topic detection, sentiment analysis, feminine pronouns occurrences, etc. to extract information on the types of roles and the types of representation of women in movies. The importance of the role will also be evaluated, as well as the general feminine presence in movies through the study of the summaries. The main idea is to correlate feminine and masculine pronouns occurrence with certain topics and stereotypes, through topic detection, and see how these correlations evolve and how they impact the gender gap. It can be a very noisy approach, but if done on sufficient data it could work. 
Finally, tropes and stereotypes will be analyzed too, from the adequate dataset, and put into relation with the summaries. We wanted at first to extract tropes from the summaries, but after discussion with our assistant, creating our own data is very hard. We will thus use the tropes that can be found in the paper related to the CMU Movies data set.
We would of course like to see a positive evolution in the gender gap, in the movie industry and elsewhere. Did the MeToo movement really impact the situation? We could compare the data before 2007, between 2007 and 2016, and after 2017 to see if the different steps of the movement made things change. As we don't have any data after 2016, we will compare the data before and after 2007. 


## Proposed timeline <a name="Proposed_timeline"></a>

See different milestones in the following point ‘Organization within the team’
- Milestone 1: doing
- Milestone 2: doing
- Milestone 3: week 12-13
- Milestone 4: week 14


## Organisation within the team <a name="Organisation_within_the_team"></a>
A list of internal milestones up until project Milestone P3.

Milestone 1:
1) Clean data: global cleaning and affine cleaning in function of what we want to do (Yasmine and Guillaume)
2) Exploratory sanity check (Alienor)
3) Think about methods and failure possibilities (Clara and Alienor)

Milestone 2:
1) Text treatment: topic detection, sentiment analysis, feminine/masculine text split on summaries (Alienor and Guillaume)
2) Extract tropes from the paper (Yasmine)
3) Financial analysis (Clara)

Milestone 3:
1) Associate stereotypes from milestone 2.1 to gender categories (in function of movies genres and other categories) (Clara and Alienor and Guillaume)
2) Correlate tropes to the extracted textual data (Yasmine)

Milestone 4:
1) Analyze worked data: What are the tropes attributed to women? How are women represented? Have stereotypes in function of gender evolved? Does the financial aspect attest of the gender gap and of its evolution? (Yasmine)
2) Correlation between the three analysis axis (Guillaume)
3) Data story and website (Clara and Alienor) 
4) Clean up the code (Guillaume)

## Questions for the TAs <a name="Questions"></a>

- What is enough data? How to know if the given data is representative/trustworthy?
For example, by merging the movie dataset with the summary dataset and by not considering the NaN or other empty fields, we are left with only 4500 ID samples. 
- Can Facebook be relevant for the popularity scores of actors since it was created in 2004 and is not so used anymore today (it could be not actually representative of the popularity of actors today)?




## Authors
- [Yasmin El Euch](https://github.com/yasmineeleuch)
- [Aliénor Bénédicte G Hamoir](https://github.com/AlienorHamoir)
- [Clara Rossignol](https://github.com/clara-rossignol)
- [Guillaume David E. Ryelandt](https://github.com/guillaumeryelandt)
