# End-to- End implementation of Loan_tap_classification

## Approach : 

Perform Exploratory data analysis 

Feature engineering 

Model building  

Insights and Recommendations

Working demo in  streamlit 

API testing in postman with flask api 

Build a docker image and share it in docker hub 

Build AWS EC2 instance 

Experiment with AWS ECR + ECS instance.

 
## Info : 

LoanTap is an online platform committed to delivering customized loan products to millennials. They innovate in an otherwise dull loan segment, to deliver instant, flexible loans on consumer friendly terms to salaried professionals and businessmen.

The team at LoanTap is building an underwriting layer to determine the creditworthiness of MSMEs as well as individuals.

This business challenge focus on the underwriting process behind Personal Loan only

## Problem Statement:

Given a set of attributes for an Individual, determine if a credit line should be extended to them. If so, what should the repayment terms be in business recommendations?



## Insights and recommendations : 

What percentage of customers have fully paid their Loan Amount?

--> Fully Paid 80.387092

Charged Off 19.612908

Around 80 % of customers have fully paid their Loan Amount. The defaulters are ~ 20%.

From Personal loan business perspective this ratio is high. These 20% will contribute in NPAs of LoanTap. To reduce the risk of NPAs, LoanTap should add slightly stringent rules to bring down this ratio to 5% to 6%. LoanTap should probably provide loans at slightly higher rate than other Banks. This will offset the risks of defaulters and maintain the profitability of the business.

Comment about the correlation between Loan Amount and Installment features.

--> Positive correlation

The majority of people have home ownership as --->> Mortage.

People with grades ‘A’ are more likely to fully pay their loan. (T/F)

--> False, people with grade B are more likely to pay the loan.

Name the top 2 afforded job titles.

--> Teachers and Managers

Suprisingly , loan status is affected by geographical location

Some of the pincodes (derived from address) has significant impact on the outcome.

Thinking from a bank's perspective, which metric should our primary focus be on.

--> Precision , Recall and more important if F1_score for banking business case

as we need to give importance to both precision and recall. We don't want to miss potential customers and at the same time we also don't want to give loan to defaulters

How does the gap in precision and recall affect the bank?

--> Recall focuses on false negative

--> precision focuses on false positive

Out of all people with grade 'A', 93% got their loan approved.

purpose_educational, purpose_small_business personal loans does positively impact the business , whereas purpose_wedding loans takes money away from the company

Trade off questions --->>

How can we make sure that our model can detect real defaulters and there are less false positives? This is important as we can lose out on an opportunity to finance more individuals and earn interest on it.

-->> Make sure recall score is good, so that we don't loose out on the customers.

Since NPA (non-performing asset) is a real problem in this industry, it’s important we play safe and shouldn’t disburse loans to anyone.

-->> Precision score need to good for this. We can avoid NPA s.

LoanTap should not disburse loans to everyone. Company’s internal policy and analysis should be in place to identify the correct persons. From data provided, 20% of people default on their loan, which inturn become NPAs for the company.

=> Low False positive means we should create the model with high Precision values. This can be achieved if we are keeping high threshold value in logistic Regression model.

=> But keeping too high values for threshold will increase False Negatives. This inturn may result in opportunity loss. In this case we will not give loans to persons which will not default but our model has predicted that they will default.

Overall, model has good prediction capability in identifying right customers (which can be easily converted).

However this model has slightly low capability on correctly identifying defaulters. Overall data has 20% defaulters, model is able to predict 10% of them correctly.
Using this model, LoanTap can easily reduce the ration of defaulters in their portfolio.

"grade" feature to classify people by LoanTap is well created. From the model it is considered to be significant.

pincode is among the significant feature.

Pincodes with Negative Coefficient: 93700, 11650, 86630, 48052, 30723, 70466, 22690
Pincodes with Positive Coefficient: 05113, 29597
LoanTap can increase their market presence in Pincodes with Positive Coefficient.
LoanTap should minimize their marketing/sales expenditure in Pincodes with Negative Coefficient.
Pincode based market segmentation should be included at strategic levels.

---By mahikshith.
