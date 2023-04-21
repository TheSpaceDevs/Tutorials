from datetime import datetime, timedelta
import requests

# URL
launch_base_url = 'https://lldev.thespacedevs.com/2.2.0/launch/'

# Time frame: now - 31 days ago
now = datetime.now()
month_ago = now - timedelta(days=31)

# Adding the time frame to the filters
net_filters = f'net__gte={month_ago.isoformat()}&net__lte={now.isoformat()}'
# Only SpaceX as the launch service provider
lsp_filter = 'lsp__id=121'
# No suborbital launches
orbital_filter = 'include_suborbital=false'

# Combine filters
filters = '&'.join(
    (net_filters, lsp_filter, orbital_filter)
)

# Set mode to detailed to include all related objects
mode = 'mode=detailed'

# Limit returned results to just 2 per query
limit = 'limit=2'

# Ordering the results by ascending T-0 (NET)
ordering = 'ordering=net'

# Assemble the query URL
query_url = launch_base_url + '?' + '&'.join(
    (filters, mode, limit, ordering)
)
print(f'query URL: {query_url}')

# Function to handle requesting data
def get_results(query_url: str) -> dict or None:
    """
    Requests data using
    the request GET method.

    Parameters
    ----------
    quer_url : str
        URL to query.

    Returns
    -------
    results : dict or None
        Results from the query.

    Notes
    -----
    Prints exceptions instead of
    raising them as this is script
    is only meant as a tutorial.
    """
    try:
        # Requesting data
        results = requests.get(query_url)
    except Exception as e:
        # Print exception when it occurs
        print(f'Exception: {e}')
    else:
        # Checking status of the query
        status = results.status_code
        print(f'Status code: {status}')

        # Return when the query status isn't 200 OK
        # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
        if status != 200:
            return

        # Converting to JSON and returning
        return results.json()

# Perform first query
results = get_results(query_url)

# Checking if it was succesful
if not results:
    # Quitting the program as an example
    # use your own error handling here
    quit()

# Printing resulting dictionary
print(results)

# Paginating through all the results
next_url = results['next']
while next_url:
    # Requesting next data
    next_results = get_results(next_url)

    # Checking if it was succesful
    if not results:
        # Quitting the program as an example
        # use your own error handling here
        quit()

    # Printing next results
    print(next_results)
    
    # Adding to the original results dictionary
    results['results'] += next_results['results']

    # Updating the next URL
    next_url = next_results['next']

print('Done!')
