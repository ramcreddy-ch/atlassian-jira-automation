from jira import JIRA

jira = JIRA('https://jira.example.com', basic_auth=('user', 'api_token'))

def audit_inactive_users(days=90):
    users = jira.search_users('active=true')
    # Logic to check last login
    pass

if __name__ == "__main__":
    audit_inactive_users()
