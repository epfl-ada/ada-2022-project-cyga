# ada-2022-project-cyga

## Abstract
A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?

# The evolution of the gender gap in the film industry
Our goal with this work is to analyze the evolution in time of sexism and women discrimination in the film industry, which is known as one of the least women-friendly industry (add numbers...). 
The #MeToo movement, known for his apogy in 2017 with the complaints of many known actresses about the sexism and assaults in the film industry, appeared in reality in 2007. It made less noise back then, but it was present and in many fields. The premices of free speech and liberation about the harrasment, assault and rape culture women were suffering of, were launched. 
We want to tell the story of those women, particularly in the film industry, who suffer from daily discrimination. We want to have a look at the gender gap and how it evolves with time, especially after the appearance of the #MeToo movement. Had this movement a real impact on the situation? (+150 mots)


## Research Questions
A list of research questions you would like to address during the project.


Can we assess gender discrimination from a financial aspect: through budget, box office revenues and salaries? Is it thrustworthy?

Are the types of roles attributed to women on screen a representation of the discrimination they undergo? How do the types of roles attributed to women evolve in time? Can this evolution attest of a decrease/increase in the gender gap? 


## Proposed additional datasets (if any)
List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.

## Methods
First of all, we need to check and clean the data, and it will be very helpful to proceed to an exploratory sanity check.

In order to evaluate the gender gap in the film industry, we will have a look at 3 different axis.
First, we'll check the financial aspect, trying to correlate the numbers to discrimination (while being careful to confounders). We'll have a look at the box office revenues and movies budgets. We will also try to find the salaries of middle-class actors, which are expected to be reasonable to analyze.
Secondly, we will analyze the evolution of the types of roles attributed to women, to see if there is an improvement in this sense to diminish the gender gap. To do so, we will look at textual data with NLP libraires (i.e. we will treat the summaries) through topic detection, sentiment analysis, feminine pronouns occurences, ... to extract information on the type of roles and the types of representation of women in movies. The importance of the role will also be evaluated, as well as the general feminine presence in movies through the study of the summaries. The main idea is to correlate feminine and masculine pronouns occurence with certain topics and stereotypes, through topic detection, and see how these correlation evolves and how they impact the gender gap. It ca be a very noisy approach, but if done on sufficient it could work.
Finally, tropes and stereotypes will be analyzed too, from the adequate dataset, and put into relation with the summaries. We wanted at first to extract tropes from the summaries, but after discussion with our asssistant, creating our own data is very hard. We will thus use the tropes that can be found in the paper related to the CMU Movies data set.

We would of course like to see a positive evolution in the gender gap, in the movie industry and else where. Did the MeToo movement really impact the situation? We could compare the data before 2007, between 2007 and 2016, and after 2017 to see if the different steps of the movement made things change. As we don't have any data after 2016, we will compare the data before and after 2007.

## Proposed timeline
- Milestone 1: doing
- Milestone 2: doing
- Milestone 3: week 12-13
- Milestone 4: week 14


## Organization within the team
A list of internal milestones up until project Milestone P3.

Milestone 1:
1) Clean data
2) Exploratory sanity check
3) Think about methods and failure possibilities

Milestone 2: 
1) Text treatment: topic detection, sentiment analysis, feminine/masculine text split on summaries
2) Extract tropes from the paper
3) Financial analysis

Milestone 3:
1) Associate stereotypes from milestone 2.1 to gender categories (in function of movies genres and other categories) 
2) Correlate tropes to the extracted textual data 

Milestone 4:
1) Analyze worked data: what are the tropes attributed fo women? how are women represented? have stereotypes in function of the gender evoluated? does the financial aspect attest of the gender gap and of its evolution? 
2) Correlation between the three analysis axis
3) Data story and website


## Questions for TAs (optional)
Add here any questions you have for us related to the proposed project.



## Authors
- [Yasmin El Euch](https://github.com/yasmineeleuch)
- [Aliénor Bénédicte G Hamoir](https://github.com/AlienorHamoir)
- [Clara Rossignol](https://github.com/clara-rossignol)
- [Guillaume David E. Ryelandt](https://github.com/guillaumeryelandt)
