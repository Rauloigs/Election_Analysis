""" score = int(input("What is the score? "))

if score >= 90:
    print("Grade is A")
elif score >= 80:
    print("Grade is B")
elif score >= 70:
     print("Grade is C")
elif score >= 60:
     print("Grade is D")
else:
    print("Grade is F") """

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(f"{county} has {voters} registered voters. ")

# for voters in counties_dict.values():
#     print(voters)

# for county, voters in counties_dict.items():
#     print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
   county = county_dict["county"]
   voters = county_dict["registered_voters"]
   print(f"{county} has {voters} registers voters. ")

# for county_dict in voting_data:
#     print(county_dict["county"])
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     for county, voters in counties_dict.items():
#         print(f"{county} county has {voters} registered voters.")


# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100: .2f}% of the total votes.")

# print(message_to_candidate)


