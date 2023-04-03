from datetime import datetime, timedelta
import requests

# URL
articles_base_url = 'https://api.spaceflightnewsapi.net/v3/articles'

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

# Requesting first data
results = requests.get(query_url)

# Converting to JSON
results = results.json()

# Printing resulting dictionary
print(results)

# Paginating through all the results
next_url = results['next']
while next_url:
    # Requesting next data
    next_results = requests.get(next_url).json()
    print(next_results)
    
    # Adding to the original results dictionary
    results['results'] += next_results['results']

    # Updating the next URL
    next_url = next_results['next']

print('Done!')
