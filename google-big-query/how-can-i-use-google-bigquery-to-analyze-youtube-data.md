# How can I use Google BigQuery to analyze YouTube data?
// plain

Google BigQuery is a powerful tool for analyzing YouTube data. It allows you to query and analyze large amounts of data quickly and efficiently. Here is an example of how to use BigQuery to analyze YouTube data:

```
# Standard SQL
SELECT video_id, title, view_count
FROM `bigquery-public-data.youtube_views.all_videos`
ORDER BY view_count DESC
LIMIT 10
```

## Output example

```
video_id	title	view_count
X_7U_pXG9QI	Despacito - Luis Fonsi ft. Daddy Yankee	806878791
VYOjWnS4cMY	Shape of You - Ed Sheeran	539111319
kJQP7kiw5Fk	See You Again - Wiz Khalifa ft. Charlie Puth	441119051
e-ORhEE9VVg	Uptown Funk - Mark Ronson ft. Bruno Mars	387622701
MUSVFetJ0Qc	Gangnam Style - PSY	363869090
fRh_vgS2dFE	Sorry - Justin Bieber	306950305
QFaFIcGh5H8	Sugar - Maroon 5	246797185
HBYirj2c_jw	All of Me - John Legend	243067435
YQHsXMglC9A	Roar - Katy Perry	235855683
XbGs_rK2PQA	Blank Space - Taylor Swift	215481717
```

The example code above shows how to query the `bigquery-public-data.youtube_views.all_videos` table to get the top 10 videos by view count. It returns a list of video_id, title, and view_count for each video.

## Code explanation

1. `SELECT`: specifies the columns that you want to query from the table.
2. `FROM`: specifies the table that you want to query from.
3. `ORDER BY`: sorts the results by the specified column.
4. `LIMIT`: limits the number of results returned.

## Helpful links
- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [YouTube Analytics with BigQuery](https://cloud.google.com/blog/products/data-analytics/youtube-analytics-with-bigquery)

onelinerhub: [How can I use Google BigQuery to analyze YouTube data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-to-analyze-youtube-data)