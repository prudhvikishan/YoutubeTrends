# YoutubeTrends
Graphical representation of Youtube videos Trend analytics using Cassandra

Goal of the project is to display the top YouTube videos of different channels in each category like genre, region, language etc based on no.of views,likes,subscribers,comments and dislikes. The data for the project is obtained from Google's YouTube API which contains the real data that is consumed by YouTube.

The data is retrieved from API in the form of JSON's containing millions of records daily. 
Database storgae is implemented by using Cassandra for this use case. Cassandra provides faster retrieval of data when required.

Steps in the project:
1) Creation of database and tables in the Cassandra based on our requirements.
2) Python language is used to parse the multi nested JSON data and download into the Cassandra by providing the connection details in the code.
3) A developer defined engagement score is calculated to have a statistical analysis for the videos that have been inserted into the DB.
4) The results are then sorted based on engagement score for different categories.
5) To display the results to an UI we have used PHP.


Source code files are present in the repository. Each file has been named according to their functionality. 
# Once data loading is done into the DB, we need to execute the youtubeTrend.py program for the whole project to run and display the results.
