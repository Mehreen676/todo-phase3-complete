# Feature: AI Chatbot for Todo Management

## User Stories
- As a user, I can chat with AI to manage my todos
- As a user, I can say "Add task to buy groceries" and it gets added
- As a user, I can ask "Show my pending tasks" and see them
- As a user, my chat history is saved between sessions

## Acceptance Criteria
- Chat interface loads with OpenAI ChatKit
- User can type natural language commands
- AI understands and executes todo operations
- Conversations are saved to database
- MCP tools are properly exposed for AI agent
## MCP Tools Specification

### Tool 1: add_task
**Purpose**: Create a new task
**Parameters**: user_id (string), title (string), description (string, optional)
**Returns**: task_id, status, title

### Tool 2: list_tasks
**Purpose**: Get user's tasks
**Parameters**: user_id (string), status (optional: "all", "pending", "completed")
**Returns**: List of tasks

### Tool 3: complete_task
**Purpose**: Mark task as complete
**Parameters**: user_id (string), task_id (integer)
**Returns**: task_id, status, title

### Tool 4: delete_task
**Purpose**: Delete a task
**Parameters**: user_id (string), task_id (integer)
**Returns**: task_id, status, title

### Tool 5: update_task
**Purpose**: Update task details
**Parameters**: user_id (string), task_id (integer), title (optional), description (optional)
**Returns**: task_id, status, title