import time
import pandas as pd
import numpy as np
# import json


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['all','january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['all','sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        
        city = input('Which city do you want to explore Chicago, New York or Washington? \n> ').lower()
        if city in CITIES:
           break;
        else:
            print('Please enter a valid city.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
    
        month = input("Please enter the month you want to explore. If you do not want a month filter enter 'all'. \nChoices: All, January, February, March, April, May, June\n").lower()         
        if month in MONTHS:
            break;
        else:
            print('Please enter a valid month.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
    
        day = input("Please enter the day of the week you want to explore. If you do not want to apply a month filter enter 'all'. \nChoices: All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n").lower()           
        if day in DAYS:
            break;
        else:
            print('Please enter a valid day')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)


    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)


    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    print(user_counts)


    # TO DO: Display counts of gender
    #print("Counts of gender:\n")
    #gender_counts = df['Gender'].value_counts()
    #print(gender_counts)    
    
    try:
        gender_counts = df['Gender'].value_counts()
        print(' ' * 40)
        print("Counts of gender:\n")
        print(gender_counts)
    except:
        #print('Counts of User Gender:\nSorry, no gender data available for {} City'.format(city.title()))
        print('Counts of User Gender:\nSorry, no gender data available for this city')


    # TO DO: Display earliest, most recent, and most common year of birth
    
    #birth_year = df['Birth Year']
    # the most common birth year
    #most_common_year = birth_year.value_counts().idxmax()
    #print("The most common birth year:", most_common_year)
    # the most recent birth year
    #most_recent = birth_year.max()
    #print("The most recent birth year:", most_recent)
    # the most earliest birth year
    #earliest_year = birth_year.min()
    #print("The most earliest birth year:", earliest_year)   
    
    try:
        earliest_year = df['Birth Year'].min() 
        most_recent = df['Birth Year'].max() 
        most_common_yearn = df['Birth Year'].mode()  
        print(' ' * 40)
        print('Counts of Birth Year:')
        #print('The most earliest birth year: ', int(earliest_year))
        print('The most earliest birth year: ', earliest_year)
        print('The most recent birth year: ', most_recent)
        print('The most common birth year: ', most_common_year)
    except:
        #print('Counts of Birth Year:\nSorry, no birth year data available for {} City'.format(city.title()))
        print('Counts of Birth Year:\nSorry, no birth year data available for this City')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_more_data(df):
    # Show more rows of data upon user request.   
    
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
        if view_data.lower() != 'yes':
            return;
            
        start_loc = 0
        end_loc = 5
        view_display = ''
        while view_display.lower() != 'no':
          
                print(df.iloc[start_loc:end_loc])
                start_loc += 5
                end_loc += 5
                view_display = input("Do you wish to continue?: ").lower()        
        
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_more_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
