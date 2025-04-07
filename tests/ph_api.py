# tests/test_tasks_api.py
import json

import pytest
from utils.helpers import create_recurring_task, update_recurring_task, get_recurred_task
# delete_task
from config.config import Config
from datetime import date, timedelta

class TestProofHubAPI:

    def setup_method(self, value):
        # Define an instance variable
        self.interval = 5

    def test_create_recurring_task(self):
        """Test creating a new task in ProofHub."""
        title = "Automated Task"
        description = "Task created via API automation test."
        current_date = f"{date.today()}"
        print(date.today())
        rrule = {
            "rrule": f"RRULE:FREQ=DAILY;INTERVAL={self.interval};COUNT=3;WKST=MO",
            "copy_items": {
                "fields": "n",
                "comments": "y",
                "attachments": "n",
                "subtasks": "y"
            }
        }
        response = create_recurring_task(Config.PROJECT_ID, Config.TASKLIST_ID, title, description,
                                         Config.TASKLIST_STAGE_ID, current_date, rrule)
        assert response.status_code == 200

        # Extract task ID for further use
        task_id = response.json().get("data").get("id")
        assert task_id, "Task ID was not returned in response."

        # Add task ID to pytest cache for other tests
        pytest.task_id = task_id
    #
    # def test_delete_task(self):
    #     """Test deleting the task in ProofHub."""
    #     task_id = pytest.task_id  # Get task ID from previous test
    #
    #     response = delete_task(task_id)
    #     assert response.status_code == 204, "Task deletion failed!"
    #
    #     # Verify task deletion by trying to retrieve the deleted task
    #     response = get_task(task_id)
    #     assert response.status_code == 404, "Task was not deleted successfully."

    def test_update_recurring_task(self):
        """Test updating the recurring task in ProofHub."""
        status = "done"
        response = update_recurring_task(Config.PROJECT_ID, Config.TASKLIST_ID, status, pytest.task_id)
        assert response.status_code == 200, "Task created!"

        # Extract task ID for further use
        recurred_task_id = response.json().get("data")[0]
        assert recurred_task_id, "Task ID was not returned in response."

        # Add task ID to pytest cache for other tests
        pytest.recurred_task_id = recurred_task_id

    def test_get_recurred_task(self):
        """Test retrieving the task created in ProofHub."""

        response = get_recurred_task(Config.PROJECT_ID, Config.TASKLIST_ID, pytest.recurred_task_id)
        recurred_task_start_date = response.json().get("data").get("start_date_time").split(" ")[0]
        expected_date = date.today() + timedelta(days=self.interval)
        recurred_task_occurrence_count = json.loads(response.json().get("data")["recurrence_rule"]).get("current_instance")
        assert response.status_code == 200, "Task retrieval failed!"
        assert recurred_task_start_date == f"{expected_date}"
        assert recurred_task_occurrence_count == 2
