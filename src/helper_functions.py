# Create a custom function to extract LinkedIn profile URL's from Google
def linkedin_profiles_from_google(search_string):
    '''
    Takes a search string and returns a list of LinkedIn profiles matching that string
    '''
    # Import the beautifulsoup
    # and request libraries of python.
    import requests
    import bs4

    # Make two strings with default google search URL
    # 'https://google.com/search?q=' and
    # our customized search keyword.
    # Concatenate them
    url = 'https://www.google.com/search?q=site%3Alinkedin.com%2Fin%2F+AND+' + search_string

    # Fetch the URL data using requests.get(url),
    # store it in a variable, request_result.
    request_result=requests.get( url )

    # Creating soup from the fetched request
    soup = bs4.BeautifulSoup(request_result.text,
                             "html.parser")

    tags = soup('a')

    # Initialize a list to store profile URL's
    profile_list = []

    for tag in tags:
        url = tag.get('href', None)
        if "q=https://www.linkedin.com/in/" in url:
            start = url.find("=")
            end1 = url.find("&")
            end2 = url.find("%")
            if end2 > 0:
                end = min(end1, end2)
            else:
                end = end1
            profile_list.append(url[start+1:end])

    return profile_list

# Create a function that takes a list of candidates and backgrounds and creates a custom dataframe

def generate_candidate_experience(df):
    # Concatenate job title, company, and start/end dates
    df['dated_experience'] = df.apply(lambda x: x['job_title'] + ' at ' + x['company']
                                                      + ' from ' + str(x['start_year']) + ' to ' +
                                                      str(x['end_year']), axis=1)
    # Flatten to show experience for each candidate in list
    cpt = df.pivot_table(index=['name'], aggfunc=
                      {'dated_experience' : list
                      })
    # Clean experience
    cpt['experience'] = cpt['dated_experience'].apply(lambda x: ','.join(x))
    # Drop intermediate column
    cpt.drop(['dated_experience'], axis=1, inplace=True)
    return cpt
