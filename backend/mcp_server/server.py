# server.py - Naya code
import asyncio
from typing import Dict, Any

# Simple MCP-like server
class MockMCPServer:
    def __init__(self):
        self.tools = {
            "add_task": self.add_task,
            "list_tasks": self.list_tasks,
            "complete_task": self.complete_task,
            "delete_task": self.delete_task,
            "update_task": self.update_task
        }
    
    async def add_task(self, user_id: str, title: str, description: str = ""):
        return {"task_id": 1, "status": "created", "title": title}
    
    async def list_tasks(self, user_id: str, status: str = "all"):
        return {"tasks": [
            {"id": 1, "title": "Buy groceries", "completed": False},
            {"id": 2, "title": "Call mom", "completed": True}
        ]}
    
    async def complete_task(self, user_id: str, task_id: int):
        return {"task_id": task_id, "status": "completed"}
    
    async def delete_task(self, user_id: str, task_id: int):
        return {"task_id": task_id, "status": "deleted"}
    
    async def update_task(self, user_id: str, task_id: int, title: str = None, description: str = None):
        return {"task_id": task_id, "status": "updated"}
    
    async def run(self):
        print("✅ MCP Server running...")
        print("Tools available: add_task, list_tasks, complete_task, delete_task, update_task")
        await asyncio.sleep(3600)  # Keep running

if __name__ == "__main__":
    server = MockMCPServer()
    asyncio.run(server.run())