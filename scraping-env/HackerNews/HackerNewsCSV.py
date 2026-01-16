import csv

# Sample data
data = [
    {'id': '1', 'title': 'Post 1', 'url': 'http://example.com/1', 'rank': 1},
    {'id': '2', 'title': 'Post 2', 'url': 'http://example.com/2', 'rank': 2}
]

# Define the CSV file path
csv_file = './HackerNews/hacker_news_posts.csv'

# Write data to CSV
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'title', 'url', 'rank'])
    writer.writeheader()
    for row in data:
        writer.writerow(row)
print(f'Data written to {csv_file}')