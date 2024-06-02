import os
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv() 

API_KEY = os.getenv("YOUTUBE_API_KEY")
API_VERSION = 'v3'

youtube = build('youtube', API_VERSION, developerKey=API_KEY)

def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
        part='snippet, statistics',
        id=channel_id
    )
    response = request.execute()

    if response['items']:

        data = dict(channel_name=response['items'][0]['snippet']['title'],
                    total_subscribers=response['items'][0]['statistics']['subscriberCount'],
                    total_views=response['items'][0]['statistics']['viewCount'],
                    total_videos=response['items'][0]['statistics']['videoCount'],
        )

        return data
    else:
        return None 


# channel_id = "UC_aEa8K-EOJ3D6gOs7HcyNg" 
channel_id = "UC9LQwHZoucFT94I2h6JOcjw"
get_channel_stats(youtube, channel_id)

# Read CSV into dataframe 
df = pd.read_csv("youtube_data_united-kingdom.csv")


# Extract channel IDs and remove potential duplicates
channel_ids = df['NOMBRE'].str.split('@').str[-1].unique()


# Initialize a list to keep track of channel stats
channel_stats = []


# Loop over the channel IDs and get stats for each
for channel_id in channel_ids:
    stats = get_channel_stats(youtube, channel_id)
    if stats is not None:
        channel_stats.append(stats)


# Convert the list of stats to a df
stats_df = pd.DataFrame(channel_stats)


df.reset_index(drop=True, inplace=True)
stats_df.reset_index(drop=True, inplace=True)


# Concatenate the dataframes horizontally
combined_df = pd.concat([df, stats_df], axis=1)


# Drop the 'channel_name' column from stats_df (since 'NOMBRE' already exists)
# combined_df.drop('channel_name', axis=1, inplace=True)


# Save the merged dataframe back into a CSV file
combined_df.to_csv('updated_youtube_data_uk.csv', index=False)


combined_df.head(10)