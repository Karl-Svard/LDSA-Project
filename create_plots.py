#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

# Read in file
file = open('Result_2011-08', 'r')
lines = file.readlines()

# Initialize lists
gilded_avg_list = []
score_avg_list = []

# Parse each line of the output
for line in lines:
    identifier, count = line.split('\t', 1)
    count = int(count)
    # Split the identifying string into subreddit and feature type
    sub, feature = identifier.split('_', 1)

    # Check if the count represents comments, score or gilded count
    # If comments: Save variables for later steps
    if feature == 'comments':
        current_sub = sub
        comment_count = count

    # If score: assert that the values are for the same subreddit
    # and calculate the score average. Skip if it comes from a
    # subreddit with less than 1000 comments, otherwise append
    # as tuple to list.
    if feature == 'score':
        assert sub == current_sub
        if comment_count < 1000:
            continue
        else:
            avg_score = count/comment_count
            score_avg_list.append((sub, avg_score))

    # If gilded: assert that the values are for the same subreddit
    # and calculate the gilded average. Skip if it comes from a
    # subreddit with less than 1000 comments, otherwise append
    # as tuple to list.
    if feature == 'gilded':
        assert sub == current_sub
        if comment_count < 1000:
            continue
        else:
            avg_gilded = count / comment_count
            gilded_avg_list.append((sub, avg_gilded))


# Sort from highest to lowest average.
gilded_avg_list.sort(key=lambda x: x[1], reverse=True)
score_avg_list.sort(key=lambda x: x[1], reverse=True)

# Extract values as two lists for the plotting
gilded_sub, gilded_avg = zip(*gilded_avg_list)
x_pos_gilded = np.arange(len(gilded_sub))

score_sub, score_avg = zip(*score_avg_list)
x_pos_score = np.arange(len(score_sub))

# Plot the top 10 highest score averages
plt.bar(x_pos_score[0:10], score_avg[0:10], align='center')
plt.xticks(x_pos_score[0:10], score_sub[0:10], rotation='vertical')
plt.ylabel('Average Score Per Comment')
plt.title('Top 10 score averages (2011-08)')
plt.savefig('top10_score_avg.png', bbox_inches='tight')
plt.show()

# Plot overview of all score averages
plt.bar(x_pos_score, score_avg, align='center')
plt.ylabel('Average Score Per Comment')
plt.title('Score averages across all subreddits (2011-08)')
plt.savefig('complete_score_avg.png', bbox_inches='tight')
plt.show()

# Plot the top 10 highest gilded count averages
plt.bar(x_pos_gilded, gilded_avg, align='center')
plt.xticks(x_pos_gilded, gilded_sub, rotation='vertical')
plt.ylabel('Average Gilded Amount Per Comment')
plt.title('Gilded count averages across all subreddits (2011-08)')
plt.savefig('complete_gilded_avg.png', bbox_inches='tight')
plt.show()
