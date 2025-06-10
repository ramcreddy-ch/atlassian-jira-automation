from jira import JIRA
import os

def create_subtasks(parent_key, subtask_titles):
    jira = JIRA(server="https://your-domain.atlassian.net", basic_auth=(os.getenv("JIRA_USER"), os.getenv("JIRA_TOKEN")))
    
    for title in subtask_titles:
        issue_dict = {
            'project': {'key': parent_key.split('-')[0]},
            'summary': title,
            'description': f'Automatically created sub-task for {parent_key}',
            'issuetype': {'name': 'Sub-task'},
            'parent': {'key': parent_key},
        }
        new_issue = jira.create_issue(fields=issue_dict)
        print(f"Created sub-task: {new_issue.key}")

if __name__ == "__main__":
    create_subtasks("PROJ-123", ["Task 1", "Task 2", "Task 3"])
