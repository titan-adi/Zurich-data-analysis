import pandas as pd

# Load users and repositories data
users_df = pd.read_csv("users.csv")
repos_df = pd.read_csv("repositories.csv")
"1. Who are the top 5 users in Zurich with the highest number of followers? List their login in order, comma-separated."
top_users = users_df.nlargest(5, 'followers')['login']
print(", ".join(top_users))

"2. Who are the 5 earliest registered GitHub users in Zurich? List their login in ascending order of created_at, comma-separated."

earliest_users = users_df.nsmallest(5, 'created_at')['login']
print(", ".join(earliest_users))

"3. What are the 3 most popular license among these users? Ignore missing licenses. List the license_name in order, comma-separated."

if not users_df['company'].mode().empty:
    most_common_company = users_df['company'].mode().iloc[0]
    print(most_common_company)
else:
    print("No company data available.")

    "14Who created the most repositories on weekends (UTC)? List the top 5 users' login in order, comma-separated"
repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])
repos_df['day_of_week'] = repos_df['created_at'].dt.dayofweek
weekend_repos = repos_df[repos_df['day_of_week'] >= 5]
top_weekend_users = weekend_repos['login'].value_counts().head(5).index
print(", ".join(top_weekend_users))

"15. Do people who are hireable share their email addresses more often?"
hireable_email = users_df[users_df['hireable'] == True]['email'].notnull().mean()
non_hireable_email = users_df[users_df['hireable'] == False]['email'].notnull().mean()
print(f"{hireable_email - non_hireable_email:.3f}")

"11"
projects_wiki_corr = repos_df['has_projects'].corr(repos_df['has_wiki'])
print(f"{projects_wiki_corr:.3f}")

"5.Which programming language is most popular among these users?"
popular_language = repos_df['language'].mode().iloc[0]
print(popular_language)

"7.Which language has the highest average number of stars per repository?"
avg_stars_language = repos_df.groupby('language')['stargazers_count'].mean().idxmax()
print(avg_stars_language)

"8.Let's define leader_strength as followers / (1 + following). Who are the top 5 in terms of leader_strength? List their login in order, comma-separated."
users_df['leader_strength'] = users_df['followers'] / (1 + users_df['following'])
top_leaders = users_df.nlargest(5, 'leader_strength')['login']
print(",".join(top_leaders))
