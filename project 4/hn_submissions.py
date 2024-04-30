import requests
import plotly.graph_objects as go

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0),  # Use .get() with default value of 0
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=lambda x: x['comments'], reverse=True)

# Extract data for plotting
titles = [sub['title'] for sub in submission_dicts]
num_comments = [sub['comments'] for sub in submission_dicts]
discussion_links = [sub['hn_link'] for sub in submission_dicts]

# Create bar chart
fig = go.Figure(data=[go.Bar(
    x=titles,
    y=num_comments,
    hovertext=discussion_links,
    marker_color='skyblue'
)])

# Customize layout
fig.update_layout(
    title='Most Active Discussions on Hacker News',
    xaxis_title='Discussion Title',
    yaxis_title='Number of Comments',
    xaxis_tickangle=-45,
    bargap=0.2,
    plot_bgcolor='rgba(0,0,0,0)'
)

# Save the plot as an HTML file
fig.write_html("hacker_news_discussions.html")

# Print a message indicating where the HTML file is saved
print("Plot saved as 'hacker_news_discussions.html'. Please open this file in your web browser to view the plot.")
