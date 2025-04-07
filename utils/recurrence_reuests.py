# utils/helpers.py
import json
import requests
from config.config import Config


def create_recurring_task(project_id, tasklist_id, title, description, tasklist_stage_id, date, rrule_data):
    url = f"{Config.BASE_URL}/{Config.BRANCH}/projects/{project_id}/tasklists/{tasklist_id}/tasks"
    payload = {
        "title": title,
        "description": description,
        "tasklist_stage_id": tasklist_stage_id,
        "start_date_time": date,
        "recurrence_rule": rrule_data
    }
    response = requests.post(url, data=json.dumps(payload), headers=Config.HEADERS, verify=False)
    return response


def update_recurring_task(project_id, tasklist_id, status, task_id):
    url = f"{Config.BASE_URL}/{Config.BRANCH}/projects/{project_id}/tasklists/{tasklist_id}/tasks/{task_id}"
    payload = {
        "status": status
    }
    response = requests.put(url, data=json.dumps(payload), headers=Config.HEADERS, verify=False)
    return response


def get_recurred_task(project_id, tasklist_id, rec_task_id):
    url = f"{Config.BASE_URL}/{Config.BRANCH}/projects/{project_id}/tasklists/{tasklist_id}/tasks/{rec_task_id}"
    response = requests.get(url, headers=Config.HEADERS, verify=False)
    return response

# def delete_task(task_id):
#     url = f"{Config.BASE_URL}/tasks/{task_id}"
#     response = requests.delete(url, headers=Config.HEADERS)
#     return response
