# Heidke-Skill-Score
This repository contains my take on calculating Heidke Skill Scores (HSS) for both binary and multiclass problems.
- multi_hss takes in 2D confusion matrix and returns a skill score  
- hss takes in predicted labels and true labels and returns a skill score  

The Heidke Skill Score (HSS) is a statistical measure used to assess the accuracy of weather forecasts, particularly for categorical predictions. It helps determine the skill of a forecast when compared to a random forecast.
- HSS = 1: Perfect forecast 
- HSS = 0: No skill
- HSS < 0: Worse than random chance

The Heidke Skill Score (for binary clasification) is calculated using the following formula:  
### $\frac{2(ad-bc)}{(a+c)(c+d) + (a+b)(b+d)}$
 
$a$ = True Positives  
$b$ = False Positives  
$c$ = False Negatives  
$d$ = True Negatives  
