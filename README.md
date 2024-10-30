# Zurich-data-analysis
# GitHub User Data from Zurich

- This project scrapes GitHub API for users located in Zurich with over 50 followers.
- The analysis revealed insights about user activities, popular programming languages, and hiring trends.
- Recommendations for developers include focusing on popular languages and optimizing profiles for visibility.

## Data Files
- `users.csv`: Contains information about users.
- `repositories.csv`: Contains information about users' public repositories.

- # GitHub User Data Analysis in Zurich

## Overview
This project involves scraping data from GitHub to analyze users located in Zurich with over 50 followers. The data collection focuses on user details and their public repositories.

## Bullet Points
- Data was scraped using the GitHub API, targeting users in Zurich with more than 50 followers and their associated repositories.
- The analysis reveals insights into user engagement, repository characteristics, and trends in programming languages among Zurich developers.
- This project provides actionable insights for developers aiming to enhance their visibility and engagement on GitHub.

## How Data Was Scraped
The data was scraped using Python and the `requests` library to interact with the GitHub API. The process involved the following steps:
1. **User Fetching**: Users in Zurich with over 50 followers were fetched using the `search/users` endpoint of the GitHub API.
2. **Repository Fetching**: For each user, their public repositories were collected using the `repos` endpoint. Up to 500 repositories were retrieved for each user, ensuring a comprehensive dataset.
3. **Data Storage**: The collected data was saved into two CSV files: `users.csv` and `repositories.csv`. These files contain essential information about users and their repositories, respectively.

## Most Interesting Fact
One of the most surprising findings from the analysis is the variety of programming languages used by developers in Zurich. While JavaScript was the most prevalent language, there was a notable interest in emerging languages like Rust and Go, indicating a diverse tech landscape and openness to new technologies.

## Actionable Recommendation for Developers
To enhance their visibility on GitHub, developers should focus on contributing to open-source projects and maintaining an active repository. Engaging with the community by providing clear documentation and regular updates can significantly boost their follower count and project visibility.

## Files Included
- **users.csv**: Contains user information including login, name, company, location, email, hireable status, bio, number of public repositories, followers, following, and account creation date.
- **repositories.csv**: Includes details about each user's public repositories, such as login, full name, creation date, star count, watcher count, language, project status, wiki status, and license type.
- **Tdsproject1.py**: Python script used to scrape the data and generate the CSV files.



