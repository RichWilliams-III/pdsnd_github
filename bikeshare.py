import time
import pandas as pd
import numpy as np

# This is name of cities that are in the program Chicago, New York, Washington 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    user_input_test = 'N'
    while user_input_test == 'N':
        print("Which City would you like to explore ? ")
        print("Enter in 'C' for Chicago") 
        print("Enter in 'N' for New York") 
        print("Enter in 'W' for Washington") 
        
        user_input = input()
        if user_input.lower() == "c":
            city = "chicago"
            user_input_test = 'Y'
        if user_input.lower() == "n":
            city = "new york city"
            user_input_test = 'Y'
        if user_input.lower() == "w":
            city = "washington"
            user_input_test = 'Y'
            
        if user_input_test == 'N':
            print ("you must enter in a valid city")
        
    # TO DO: get user input for month (all, january, february, ... , june)

    user_month_test  = 'N'
    while user_month_test == 'N':
        print("Which Month would you like to look at ? ")
        print("Jan, Feb, Mar, Apr, May, Jun or 'all' for all months:") 
        user_input = input()
        if user_input.lower() == "jan":
            month = "january"
            user_month_test = 'Y'
        if user_input.lower() == "feb":
            month = "february"
            user_month_test = 'Y'
        if user_input.lower() == "mar":
            month = "march"
            user_month_test = 'Y'  
        if user_input.lower() == "apr":
            month = "april"
            user_month_test = 'Y'
        if user_input.lower() == "may":
            month = "may"
            user_month_test = 'Y'
        if user_input.lower() == "jun":
            month = "june"
            user_month_test = 'Y'
        if user_input.lower() == "all":
            month = "all"
            user_month_test = 'Y'
        if user_month_test == 'N':
            print ("you must enter in a valid month")
        
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    user_day_test  = 'N'
    while user_day_test == 'N':
        print("Which day would you like to look at ? ")
        print("Mon, Tue, Wed, Thu, Fri, Sat, Sun  or 'all' for all days of the week:") 
        user_input = input()
        if user_input.lower() == "mon":
            day = "monday"
            user_day_test = 'Y'
        if user_input.lower() == "tue":
            day = "tuesday"
            user_day_test = 'Y'
        if user_input.lower() == "wed":
            day = "wednesday"
            user_day_test = 'Y'  
        if user_input.lower() == "thu":
            day = "thursday"
            user_day_test = 'Y'
        if user_input.lower() == "fri":
            day = "friday"
            user_day_test = 'Y'
        if user_input.lower() == "sat":
            day = "saturday"
            user_day_test = 'Y'
        if user_input.lower() == "sun":
            day = "sunday"
            user_day_test = 'Y'
        if user_input.lower() == "all":
            day = "all"
            user_day_test = 'Y'
        if user_day_test == 'N':
            print ("you must enter in a valid day")
    

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    print('Most common month :', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    print('Most common day :', common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    common_start_hour = df['hour'].mode()[0]
    
    print('Most common start hour :', common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Popular Start station:', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Popular End station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    
    #popular_comination_station = df.groupby(['Start Station', 'End Station']).size().idmax()

    popular_comination_station = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    popular_comination_station_txt = popular_comination_station.head(1).to_string(header=False)
    popular_comination_station_anz = popular_comination_station.head(1).to_string(header=False, index = False)
    popular_comination_station_txt = popular_comination_station_txt.replace(popular_comination_station_anz, '')
    print("Most frequent combination of start station and end station :", popular_comination_station_txt, " With ",  popular_comination_station_anz, " Occurrences ")
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    #total_time = df['End Time']-df['Start Time']
    total_time = ((pd.to_datetime(df['End Time']) - 
                            pd.to_datetime(df['Start Time']))
                                .dt.total_seconds() / 60)
    
    print ("Total travel time in min :", total_time.sum())
    total_hours = total_time.sum()/ 60 
    print ("Total travel time in hours :", total_hours)

    # TO DO: display mean travel time

    print ("Total mean travel time in min :", total_time.mean())
    total_hours_mean = total_time.mean()/ 60 
    print ("Total mean travel time in hours :", total_hours_mean)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("Counts of user types:\n", user_types)

    # TO DO: Display counts of gender
    
    if "Gender" in df.columns: 

        gender_male = len( df[df.Gender == "Male"])
        gender_female = len( df[df.Gender == "Female"])

        print ("\nNumbers by Gender :")
        print ("Male : ", gender_male)
        print ("Female : ", gender_female)
    else:
        print ("\nNo Gender data provided")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns: 
        most_common_year = df['Birth Year'].mode()[0]

        print ("\nMost common birth year :", most_common_year.astype(int))

        most_recent_year = df['Birth Year'].sort_values(ascending=False)

        print ("\nMost recent year :", most_recent_year.head(1).to_string(header=False, index = False)[:-2])

    else:
        print ("\nNo Birth Year data provided")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

