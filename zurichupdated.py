import requests
import pandas as pd
import time

# Replace with your GitHub token
TOKEN = ""
HEADERS = {"Authorization": f"token {TOKEN}"}

# Define function to fetch users in Zurich with over 50 followers
def fetch_users_in_zurich():
    url = "https://api.github.com/search/users"
    params = {
        "q": "location:Zurich followers:>50",
        "per_page": 100  # Number of results per page
    }
    users = []
    page = 1

    while True:
        response = requests.get(url, headers=HEADERS, params={**params, "page": page})
        
        # Error handling
        if response.status_code != 200:
            print(f"Error fetching users: {response.status_code}, {response.json()}")
            break

        page_users = response.json().get("items", [])
        users.extend(page_users)
        print(f"Fetched {len(page_users)} users from Zurich on page {page}.")
        
        # Break if fewer than 100 users returned, indicating last page
        if len(page_users) < 100:
            break
        
        page += 1
        time.sleep(1)  # Small delay to avoid hitting rate limits

    return users

# Define function to fetch a user's repositories (up to 500 repos)
def fetch_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    params = {
        "per_page": 100  # Number of repos per page
    }
    repos = []
    page = 1

    while len(repos) < 500:
        response = requests.get(url, headers=HEADERS, params={**params, "page": page})
        
        # Error handling
        if response.status_code != 200:
            print(f"Error fetching repositories for {username}: {response.status_code}")
            break

        page_repos = response.json()
        repos.extend(page_repos)
        print(f"Fetched {len(page_repos)} repos for {username} on page {page}.")
        
        # Break if fewer than 100 repos returned, indicating last page
        if len(page_repos) < 100:
            break
        
        page += 1
        time.sleep(1)  # Small delay to avoid hitting rate limits

    return repos[:500]

# Clean up company names and format them as required
def clean_company_name(company):
    if company:
        return company.strip().lstrip('@').upper()
    return ""

# Fetch users and their repositories, then save to CSV
def main():
    users_data = []
    repos_data = []

    users = fetch_users_in_zurich()
    
    for user in users:
        # Fetch user details
        user_details = {
            "login": user["login"],
            "name": user.get("name", ""),
            "company": clean_company_name(user.get("company", "")),
            "location": user.get("location", ""),
            "email": user.get("email", ""),
            "hireable": user.get("hireable", ""),
            "bio": user.get("bio", ""),
            "public_repos": user.get("public_repos", 0),
            "followers": user.get("followers", 0),
            "following": user.get("following", 0),
            "created_at": user.get("created_at", "")
        }
        users_data.append(user_details)

        # Fetch repositories for each user
        repos = fetch_user_repositories(user["login"])
        for repo in repos:
            license_info = repo.get("license")  # Safely get license info or None
            repo_details = {
                "login": user["login"],
                "full_name": repo.get("full_name", ""),
                "created_at": repo.get("created_at", ""),
                "stargazers_count": repo.get("stargazers_count", 0),
                "watchers_count": repo.get("watchers_count", 0),
                "language": repo.get("language", ""),
                "has_projects": repo.get("has_projects", False),
                "has_wiki": repo.get("has_wiki", False),
                "license_name": license_info["key"] if license_info else ""  # Check if license_info exists
            }
            repos_data.append(repo_details)
    
    # Convert lists to DataFrames
    users_df = pd.DataFrame(users_data)
    repos_df = pd.DataFrame(repos_data)

    # Write to CSV files
    users_df.to_csv("users.csv", index=False)
    repos_df.to_csv("repositories.csv", index=False)

    print("Data collection complete. Files 'users.csv' and 'repositories.csv' have been saved.")

# Run the main function
if __name__ == "__main__":
    main()
