'''
Created on Dec 6, 2020

@author: ronny
'''

import pandas as pd
df = pd.read_csv('glassdoor_jobs_ex.csv')

# salary parsing


# remove negative one values from salary column

# salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0) # adds new column and identifies if column "Salary Estimate" consists "per hour"
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0) 

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])  # crates new series and splits up the salary column and also divides into half tackabuse.com/lambda-functions-in-python/
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$','')) # creates new series and basically deletes the 'K' and '$' sign from the column

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:','')) #eliminates the "per hour" and "employer provided salary" from the column

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0])) # extracts min value of salary range, [0] takes first entry before -
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1])) # extracts max value of salary range, [1] takes second entry after - 
df['avg_salary'] = (df.min_salary+df.max_salary)/2 # calculates average of both columns

# company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis=1) # extracts company name (except last three characters), but only if there exists a rating
# because we didn't specify a new series, have to let it know that we do it on rose (tat's why we needed to declare axis=1)
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1]) # Extracting State from location to new column
count_jobs = df.job_state.value_counts() # . method is the same as using the bracket, but only if there is no space in between column name

# Question: Is the job position at the head quearter?
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis =1)   # axis = 1 stands for "create new column", axis=0 --> rows, axis = 1 --> columns
# same as df['same_state2'] = df.apply(lambda x: 1 if x['Location']== x['Headquarters'] else 0, axis =1)

#age of company 
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)

#parsing of job description (python, etc.)

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
 
#r studio 
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

df.columns
# drop column "unnamed"
df_out = df.drop(['Unnamed: 0'], axis =1)

df_out.to_csv('salary_data_cleaned.csv',index = False)