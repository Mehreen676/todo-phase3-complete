from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import os
import json

app = FastAPI(title="Todo AI Chatbot", version="1.0")

# CORS Setup - FIXED
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rest of your code remains same...
# Models
class ChatRequest(BaseModel):
    user_id: str
    message: str
    conversation_id: Optional[str] = None

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

# ========== MOCK OPENAI AGENTS SDK ==========
# (Actual SDK requires OpenAI API key, yeh mock version hai)

class OpenAIAgent:
    """Mock OpenAI Agent that simulates Agents SDK behavior"""
    
    def __init__(self):
        self.system_prompt = """You are a helpful Todo assistant. 
        You have access to these tools:
        1. add_task - Add new task: needs title
        2. list_tasks - List all tasks
        3. complete_task - Mark task as complete: needs task_id
        4. delete_task - Delete task: needs task_id
        5. update_task - Update task: needs task_id and new title/description
        
        Always respond naturally and confirm actions."""
    
    async def run(self, user_message: str, tools: List[Dict]) -> Dict[str, Any]:
        """Simulate AI agent processing"""
        user_message = user_message.lower()
        
        # AI Logic - Determines which tool to use
        if "add" in user_message or "create" in user_message or "new" in user_message:
            # Extract task title
            words = user_message.split()
            if "add" in words:
                task_title = " ".join(words[words.index("add")+1:])
            elif "create" in words:
                task_title = " ".join(words[words.index("create")+1:])
            elif "new" in words:
                task_title = " ".join(words[words.index("new")+1:])
            else:
                task_title = user_message.replace("add", "").replace("create", "").replace("new", "").strip()
            
            return {
                "response": f"Sure, I'll add '{task_title}' to your todo list!",
                "tool_calls": [{
                    "name": "add_task",
                    "arguments": {
                        "title": task_title,
                        "description": ""
                    }
                }]
            }
        
        elif "list" in user_message or "show" in user_message or "view" in user_message:
            filter_type = "all"
            if "pending" in user_message:
                filter_type = "pending"
            elif "completed" in user_message:
                filter_type = "completed"
            
            return {
                "response": f"Let me get your {filter_type} tasks for you...",
                "tool_calls": [{
                    "name": "list_tasks",
                    "arguments": {
                        "status": filter_type
                    }
                }]
            }
        
        elif "complete" in user_message or "done" in user_message or "finish" in user_message:
            # Extract task ID (simple logic)
            task_id = 1  # Default
            
            return {
                "response": f"Marking task {task_id} as complete!",
                "tool_calls": [{
                    "name": "complete_task",
                    "arguments": {
                        "task_id": task_id
                    }
                }]
            }
        
        elif "delete" in user_message or "remove" in user_message:
            task_id = 1  # Default
            
            return {
                "response": f"Deleting task {task_id}...",
                "tool_calls": [{
                    "name": "delete_task",
                    "arguments": {
                        "task_id": task_id
                    }
                }]
            }
        
        elif "update" in user_message or "change" in user_message or "edit" in user_message:
            task_id = 1  # Default
            
            return {
                "response": f"Updating task {task_id}...",
                "tool_calls": [{
                    "name": "update_task",
                    "arguments": {
                        "task_id": task_id,
                        "title": "Updated Task"
                    }
                }]
            }
        
        else:
            return {
                "response": "I'm your Todo assistant! I can help you: add tasks, list tasks, complete tasks, delete tasks, or update tasks. What would you like to do?",
                "tool_calls": []
            }

# ========== MCP TOOLS IMPLEMENTATION ==========
# (Same as before, but now used by AI agent)

async def add_task(user_id: str, title: str, description: str = "") -> Dict[str, Any]:
    """MCP Tool 1: Add new task"""
    print(f"[MCP Tool] add_task: {title}")
    
    # Here you would save to database
    task_id = 1  # Mock ID
    
    return {
        "tool_name": "add_task",
        "result": {
            "task_id": task_id,
            "status": "created",
            "title": title,
            "description": description,
            "message": f"Task '{title}' added successfully"
        }
    }

async def list_tasks(user_id: str, status: str = "all") -> Dict[str, Any]:
    """MCP Tool 2: List tasks"""
    print(f"[MCP Tool] list_tasks: status={status}")
    
    # Mock tasks
    tasks = [
        {"id": 1, "title": "Buy groceries", "completed": False, "user_id": user_id},
        {"id": 2, "title": "Call mom", "completed": True, "user_id": user_id},
        {"id": 3, "title": "Finish project", "completed": False, "user_id": user_id}
    ]
    
    # Filter by status
    if status == "pending":
        tasks = [t for t in tasks if not t["completed"]]
    elif status == "completed":
        tasks = [t for t in tasks if t["completed"]]
    
    return {
        "tool_name": "list_tasks",
        "result": {
            "tasks": tasks,
            "count": len(tasks),
            "status": status
        }
    }

async def complete_task(user_id: str, task_id: int) -> Dict[str, Any]:
    """MCP Tool 3: Mark task as complete"""
    print(f"[MCP Tool] complete_task: task_id={task_id}")
    
    return {
        "tool_name": "complete_task",
        "result": {
            "task_id": task_id,
            "status": "completed",
            "message": f"Task {task_id} marked as complete"
        }
    }

async def delete_task(user_id: str, task_id: int) -> Dict[str, Any]:
    """MCP Tool 4: Delete task"""
    print(f"[MCP Tool] delete_task: task_id={task_id}")
    
    return {
        "tool_name": "delete_task",
        "result": {
            "task_id": task_id,
            "status": "deleted",
            "message": f"Task {task_id} deleted"
        }
    }

async def update_task(user_id: str, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    """MCP Tool 5: Update task"""
    print(f"[MCP Tool] update_task: task_id={task_id}")
    
    return {
        "tool_name": "update_task",
        "result": {
            "task_id": task_id,
            "status": "updated",
            "title": title or f"Task {task_id}",
            "message": f"Task {task_id} updated successfully"
        }
    }

# ========== AGENT SETUP ==========
agent = OpenAIAgent()
mcp_tools = {
    "add_task": add_task,
    "list_tasks": list_tasks,
    "complete_task": complete_task,
    "delete_task": delete_task,
    "update_task": update_task
}

# ========== API ENDPOINTS ==========
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """Main chat endpoint with AI Agent"""
    try:
        # Step 1: AI Agent decides what to do
        ai_response = await agent.run(request.message, list(mcp_tools.keys()))
        
        # Step 2: Execute MCP tools if agent called them
        tool_results = []
        if "tool_calls" in ai_response and ai_response["tool_calls"]:
            for tool_call in ai_response["tool_calls"]:
                tool_name = tool_call["name"]
                arguments = tool_call["arguments"]
                
                if tool_name in mcp_tools:
                    # Add user_id to arguments
                    arguments["user_id"] = request.user_id
                    
                    # Execute the tool
                    result = await mcp_tools[tool_name](**arguments)
                    tool_results.append(result)
        
        # Step 3: Prepare final response
        return {
            "response": ai_response["response"],
            "agent_used": True,
            "agent_type": "OpenAIAgent",
            "tool_calls": ai_response.get("tool_calls", []),
            "tool_results": tool_results,
            "conversation_id": request.conversation_id or "conv_" + request.user_id[:8]
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {
        "service": "Todo AI Chatbot API",
        "version": "1.0",
        "phase": "III",
        "features": [
            "OpenAI Agents SDK (Mock)",
            "MCP Tools Integration",
            "5 Todo Operations",
            "Stateless Architecture"
        ],
        "endpoints": {
            "POST /chat": "Chat with AI agent",
            "GET /tools": "List available tools",
            "GET /health": "Health check"
        }
    }

@app.get("/tools")
async def list_tools_endpoint():
    """List all available MCP tools"""
    return {
        "tools": [
            {
                "name": "add_task",
                "description": "Add new todo task",
                "parameters": ["user_id", "title", "description(optional)"]
            },
            {
                "name": "list_tasks",
                "description": "List user's tasks",
                "parameters": ["user_id", "status(optional)"]
            },
            {
                "name": "complete_task",
                "description": "Mark task as complete",
                "parameters": ["user_id", "task_id"]
            },
            {
                "name": "delete_task",
                "description": "Delete a task",
                "parameters": ["user_id", "task_id"]
            },
            {
                "name": "update_task",
                "description": "Update task details",
                "parameters": ["user_id", "task_id", "title(optional)", "description(optional)"]
            }
        ],
        "agent": "OpenAIAgent (Mock)",
        "mcp_tools_count": 5
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "agent": "running"}

# ========== RUN SERVER ==========
if __name__ == "__main__":
    import uvicorn
    print("=" * 50)
    print("🚀 Todo AI Chatbot API - Phase III")
    print("📌 Features:")
    print("   • OpenAI Agents SDK Integration")
    print("   • 5 MCP Tools for Todo Operations")
    print("   • Mock AI Agent with Natural Language")
    print("   • FastAPI Backend")
    print(f"   • Listening on: http://localhost:8000")
    print("=" * 50)
    uvicorn.run(app, host="0.0.0.0", port=8000)