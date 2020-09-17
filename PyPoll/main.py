import os
import csv

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_data.csv")

total_votes = 0
candidate_received = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

with open (file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        

