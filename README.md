<h1>Project: Data Warehouse</h1>


<h3>Introduction</h3>
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights into what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.


<h3>Project Description</h3>
In this project, you'll apply what you've learned on data warehouses and AWS to build an ETL pipeline for a database hosted on Redshift. To complete the project, you will need to load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.

<h3>Business</h3>
- Analytics wants to understand what songs their users are listening to by analyzing a set of dimensional tables.
- Analytics wants a Data warehouse on the cloud with tables designed to optimize queries and gain insights on song plays.


<h3>Tasks</h3>
    
 - Create and launch a Redshift cluster on AWS
 - Create a Redshift cluster and IAM role to grant access to S3
 - Create a star schema and ETL pipeline to prepare the data for analytics team
 - Explore & load raw data (JSON) in S3 to Redshift staging tables
 - Define fact & dimension tables for a star schema for this particular analytic purpose
 - Write an ETL pipeline to load data from staging tables to analytics tables on Redshift
 - Connect to the Redshift cluster and run some test queries

<h43>Data Modeling Star Schema</h3>

Since the core business process/metric is an user playing a song, the fact table should store the song play records with user/song identifier together with related information about the how and where the song is played. Based on the data and tables given in the project, the star schema looks like this

![Desenho dominio de dados-Página-12](https://user-images.githubusercontent.com/92527247/187541818-b17bd232-8f21-4924-80f4-edca31202a1b.jpg)


    
 - stage_event: copy data from s3 bucket
 - stage_song: copy data from s3 bucket
 - songplays: Records in log data associated with song plays
 - users: Users in the app
 - songs: Songs in music database
 - artists: Artists in music database
 - time: Timestamps of records in songplays broken down into specific units


<h3>ETL Pipeline</h3>

 - Fill the HOST and ARN in <code>dwh.cfg</code>. You can get their values by runing
 - Run <code>create_tables.py</code>.
 - Run <code>etl.py</code> to load data from S3 into staging tables and then transfer into target tables (fact and dimension tables).

<h4>Song Dataset</h4>
    
The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are file paths to two files in this dataset.
    
<code>song_data/A/B/C/TRABCEI128F424C983.json song_data/A/A/B/TRAABJL12903CDCF1A.json</code>


<h4>Log Dataset</h4>

The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate app activity logs from an imaginary music streaming app based on configuration settings.

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are file paths to two files in this dataset.
    
    
 <code>log_data/2018/11/2018-11-12-events.json log_data/2018/11/2018-11-13-events.json</code>
     

 

