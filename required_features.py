import requests
import json
import random
import pytest


############################################### Recurring tasks feature #########################################################################

account_url = "test_acu_77"
server = "indev.proofhub.com/api/v5"
branch = "delivery_proofhub/public"
project_id = 1437105650
tasklist_id = 1324916412
token = "EbGBZcLlDgKqTjRDyfk84v36a9ZwzaxQonfyjTmp0e358445"
tasklist_stage_id = 1324205309
assignee_id = 1833637365
start_date = "2024-10-10 00:00:00"
due_date = "2024-10-10 00:00:00"
initial_status = "to-do"
tags = [1667392613, 1169214858, 663074479]
priority = 979791174

# create task with recurring functionality

url = f'https://{account_url}.{server}/{branch}/projects/{project_id}/tasklists/{tasklist_id}/tasks'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}
# proxies = {
#     'https': '10.10.10.10:3128'
# }
# for i in range(1500):
data = {
    "title": f"Task added from script",
    "tasklist_stage_id": tasklist_stage_id,
    "assignee_id": assignee_id,
    "start_date_time": start_date,
    "due_date_time": due_date,
    "estimated_minutes": "99:59:58",
    "description":"task for testing status of a task",
    "status":initial_status,
   # "tags": tags,
   "priority": priority
}

response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
print(response.json())
print("#####################################################################################################################")
