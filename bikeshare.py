import time
import pandas as pd
import numpy as np

### Formatting of code from stackoverflow.com

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print('\033[1;38;0m') #Use this to set a baseline text format

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi there! Let\'s explore some US bikeshare data!')



    # get user input for city (chicago, new york city, washington).
    cities = ('Chicago', 'New York City', 'Washington')
    while True:
        city = input('\nWould you like to see data for: ' + '\033[1mChicago, New York City, or Washington?\033[0m\n').title()
        if city in cities:
            print('\nYour choice is: \033[1;32;40m{}\033[1;38;0m\n'.format(city))  #This code '\033[1;32;40m {}.\n' formats the user's choice green
            break
        else:
            print('\033[1;33;40m','\nInvalid entry, please try again.','\033[1;38;0m\n')
            continue


    # get user input for month (all, january, february, ... , june)
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    while True:
        month = input('Which month would you like to filter by: ' + '\033[1m'+ 'January, February, March, April, May, or June?' + '\033[0m'+' Alternatively, enter' + '\033[1m ' + "all" + ' \033[0m' +'to apply no month filter.\n').lower()
        if month in months:
            print('\nYour choice is: \033[1;32;40m{}\033[1;38;0m\n'.format(month.title()))  #This code '\033[1;32;40m {}.\n' formats the user's choice green
            break
        else:
            print('\033[1;33;40m','\nInvalid entry, please try again.','\033[1;38;0m\n')
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
#        day = input('\nPlease choose a specific day to filter by: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Alternatively, enter "all" to apply no day filter.\n').lower()
        day = input('Which day would you like to filter by: ' + '\033[1m'+ 'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?' + '\033[0m'+' Alternatively, enter' + '\033[1m ' + "all" + ' \033[0m' +'to apply no month filter.\n').lower()
        if day in days:
            print('\nYour choice is: \033[1;32;40m{}\033[1;38;0m\n'.format(day.title()))  #This code '\033[1;32;40m {}.\n' formats the user's choice green
            break
        else:
            print('\033[1;33;40m','\nInvalid entry, please try again.','\033[1;38;0m\n')
            continue

    print('_'*100)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no filter
        (str) day - name of the day of week to filter by, or "all" to apply no filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    city = city.lower() #Due to format changes earlier, the city input is changed again
    df = pd.read_csv(CITY_DATA[city])

    # converts the Start Time column to datetime and creates new month and day of week columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filters by month if applicable and creates new dataframe
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filters by day of week if applicable and creates new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:\033[1;32;40m', common_month,'\033[1;38;0m')

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day:\033[1;32;40m', common_day,'\033[1;38;0m')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common starting hour:\033[1;32;40m', common_hour,'\033[1;38;0m')

    print("\nThis took %s seconds" % round((time.time() - start_time),3))
    print('_'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most common starting station:\033[1;32;40m', common_start,'\033[1;38;0m')

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most common ending station:\033[1;32;40m', common_end,'\033[1;38;0m')

    # display most frequent combination of start station and end station trip
    df['Frequent Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Frequent Trip'].mode()[0]
    print('Most common route:\033[1;32;40m', common_trip,'\033[1;38;0m')

    print("\nThis took %s seconds" % round((time.time() - start_time),3))
    print('_'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n\033[1m','Calculating Trip Duration...\n','\033[0m')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:','\033[1;32;40m',round(total_travel_time/86400,0),'\033[1;38;0m','days')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time:','\033[1;32;40m',round(mean_travel_time/60,0),'\033[1;38;0m','minutes')

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('_'*100)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n\033[1m','Calculating User Stats...\n','\033[0m')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('User Type Count:\n',user_type_count)

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nGender Count:\n', gender_count)
    except KeyError:
        print('\nGender Count: No data available.')

    # Display earliest, most recent, and most common year of birth
    try:
        birth_min = int(df['Birth Year'].min())
        print('\nEarliest year of birth:', birth_min)
    except KeyError:
        print('\nEarliest year of birth: No data available.')

    try:
        birth_max = int(df['Birth Year'].max())
        print('Most recent year of birth:', birth_max)
    except KeyError:
        print('Most recent year of birth: No data available.')

    try:
        birth_mode = int(df['Birth Year'].mode()[0])
        print('Most common year of birth:', birth_mode)
    except KeyError:
        print('Most common year of birth: No data available.')

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('_'*100)


def display_data(df):
    """Displays raw data 5 rows at a time, if requested."""

    while True:
        show_data = input('\nWould you like to see 5 rows of raw data? Type "yes" or "no":\n').lower()
        i = 0
        if show_data == 'no':
            print('\nYour choice is: \033[1;32;40m','No','\033[1;38;0m\n')
            break
        elif show_data != 'yes':
            print('\033[1;33;40m','\nInvalid entry, please try again.','\033[1;38;0m\n')
            continue
        elif show_data == 'yes': #If user answers 'yes', this code is executed, which will go into a nested loop
            print(df.iloc[i:i+5])
            i += 5
            more_data = input('\nWould you like to see 5 more rows of data? Type "yes" or "no":\n').lower()
            while True:
                if more_data == 'no':
                    print('\nYour choice is: \033[1;32;40m','No','\033[1;38;0m\n')
                    break
                elif more_data != 'yes':
                    print('\033[1;33;40m','\nInvalid entry, please try again.','\033[1;38;0m\n')
                    more_data = input('\nWould you like to see 5 more rows of data? Type "yes" or "no":\n').lower()
                    continue
                elif more_data == 'yes':
                    print(df.iloc[i:i+5])
                    i += 5
                    more_data = input('\nWould you like to see 5 more rows of data? Type "yes" or "no":\n').lower()
                    continue
            break





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter "yes" or "no".\n')
        while restart.lower() != 'no' and restart.lower() != 'yes':
            print('\033[1;33;40m','\nInvalid entry, please try again.','\033[1;38;0m\n')
            restart = input('\nWould you like to restart? Enter "yes" or "no".\n')
            continue

        if restart.lower() == 'yes':
            print('\nYour choice is: \033[1;32;40m','Yes','\033[1;38;0m\n')  #This code '\033[1;32;40m {}.\n' formats the user's choice green
            continue
        elif restart.lower() == 'no':
            print('\nYour choice is: \033[1;32;40mNo, exiting program now.\033[1;38;0m\n')  #This code '\033[1;32;40m {}.\n' formats the user's choice green
            break

            continue




if __name__ == "__main__":
	main()
