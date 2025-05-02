task_delete_response = {
    "description": "Задача успешно удалена",
    "content": {
        "application/json": {
            "example": {
                "id": 1,
                "title": "title",
                "description": "description",
                "deadline": "2023-12-31T23:59:59",
            }
        }
    },
}

task_not_found_response = {
    404: {
        "description": "Задача с таким id не существует",
        "content": {
            "application/json": {"example": {"msg": "task with this ID does not exist"}}
        },
    },
}

task_mark_completed = {
    "description": "Задача отмечена как выполненная",
    "content": {
        "application/json": {"example": {"msg": "task is marked as completed"}}
    },
}
