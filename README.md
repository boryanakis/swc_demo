# SWC Demo for Bash and Python

This scenario is based on real life experiences of _REAL_ graduate students all over the world. 

## You  
A graduate student interested in the effect of climate change on your favorite topic, and you start by doing an exploratory analysis on temperature. 

## Data  
For each state, you have a file containing the average temperature in April for the years 1950 - 2018 . Your advisor tells you that you should look at the last 25 years. 

#### Your Plan  
Do this in Excel. Open a file, find the last 25 data points, calculate the means, record it in a spreadsheet. [x 50]. 2 mins per file = 100 mins (1 hr 40 minutes that are gone forever..) 

Please don't do this!  
(1) it is a colossal waste of your time  
(2) it's mindless work; you are a grad student, your job is to be generatign new knowledge through research  
(3) the chances that you will make a mistake of some kind (typo, miscalculation, etc) are pretty high  
(4) MAINLY: what happens when your advisor changes her mind, and says "Actually, I think it would be better to examine the last 50 years"...? :cold_sweat: :scream: :weary:

## Better plan

With some help, you write a `Python` program that calculates the mean temperature for the last N years for a given state. 
The program is used as follows:

```
python calculate_mean.py FILE_WITH_TEMPS STATE_ABBR N
```
where `FILE_WITH_TEMPS` is a CSV file with two columns [year,temperature] and no column names, `STATE_ABBR` is the state abbreviation, and `N` is the number of most recent years which you are interested in. 

Okay! Now, all you have to do is type the 50 commands and voila! But who are you kidding? You will copy-paste the command 50 times, and then edit so that each command is being executed on a different state. 

#### Advantages 

Less time-consuming than the Excel plan, and less error-prone. Overall, not bad! 

#### Disadvantages 

Copy-pasting is never error-_free_ on the first try.  

## Even Better Plan  

Write a shell script that runs the `Python` program on every one of your files. With this, the calculations take less than 30 seconds, and you can use the remaining 1 hr 39 mins 30 sec to read one of the many papers you have been told to read. 

#### Advantages

When your advisor changes her mind about the number of years you should be looking at, you don't break a sweat! \#NBD



