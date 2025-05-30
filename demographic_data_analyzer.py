import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()


    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)


    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df.loc[df['education'] == 'Bachelors', 'education'].count() / len(df.index) * 100, 1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    people_with_higher_degree = df.loc[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])), 'education'].count()
    higher_degree_and_above50k = df.loc[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K'), 'education'].count()


    # What percentage of people without advanced education make more than 50K?
    people_withthout_higher_degree = df.loc[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])), 'education'].count()
    without_higher_degree_and_above50k = df.loc[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K'), 'education'].count()


    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round(people_with_higher_degree / len(df.index) * 100, 1)
    lower_education = round(people_withthout_higher_degree / len(df.index) * 100, 1)

    # percentage with salary >50K
    higher_education_rich = round(higher_degree_and_above50k / people_with_higher_degree * 100, 1)
    lower_education_rich = round(without_higher_degree_and_above50k / people_withthout_higher_degree * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[(df['hours-per-week'] == min_work_hours), 'salary'].count()
    num_min_workers_rich = df.loc[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K'), 'salary'].count()

    rich_percentage = round(num_min_workers_rich / num_min_workers * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    high_earners = df.loc[df['salary'] == '>50K']
    country_total_earners = df['native-country'].value_counts()
    high_earners_by_country = high_earners['native-country'].value_counts()
    he_percentage_by_country = (high_earners_by_country / country_total_earners) * 100

    highest_earning_country = he_percentage_by_country.idxmax()
    highest_earning_country_percentage = round(he_percentage_by_country.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    high_earners_in_india = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India')] 

    top_IN_occupation = high_earners_in_india['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
