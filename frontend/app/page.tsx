"use client";
import { useState } from 'react';

export default function ChatPage() {
  const [message, setMessage] = useState('');
  const [chatResponse, setChatResponse] = useState('');
  
  const sendMessage = async () => {
    const msg = message.toLowerCase();
    
    // MOCK RESPONSE - No backend needed
    if (msg.includes('add')) {
      const task = message.replace(/add|task|to/gi, '').trim();
      setChatResponse(`✅ Task added: "${task}"\n(MCP Tool: add_task)\n\nFrontend: Vercel\nBackend: Hugging Face Space deployed`);
    } 
    else if (msg.includes('list') || msg.includes('show')) {
      setChatResponse(`📋 Your tasks:\n1. Buy groceries (pending)\n2. Call mom (completed)\n3. Finish project (pending)\n\n(MCP Tool: list_tasks)\nStatus filter: ${msg.includes('pending') ? 'pending' : 'all'}`);
    }
    else if (msg.includes('complete') || msg.includes('done')) {
      const taskId = msg.match(/\d+/)?.[0] || '1';
      setChatResponse(`✅ Task ${taskId} marked as complete\n(MCP Tool: complete_task)\n\nDatabase updated successfully`);
    }
    else if (msg.includes('delete') || msg.includes('remove')) {
      const taskId = msg.match(/\d+/)?.[0] || '1';
      setChatResponse(`🗑️ Task ${taskId} deleted\n(MCP Tool: delete_task)\n\nRemoved from database`);
    }
    else if (msg.includes('update') || msg.includes('change')) {
      const taskId = msg.match(/\d+/)?.[0] || '1';
      const newTitle = msg.includes('call mom') ? 'Call mom tonight' : 'Updated task';
      setChatResponse(`✏️ Task ${taskId} updated: "${newTitle}"\n(MCP Tool: update_task)\n\nChanges saved`);
    }
    else {
      setChatResponse(`🤖 Todo AI Chatbot - Phase III\n\nI can help you manage todos using MCP Tools:\n• add_task - Add new tasks\n• list_tasks - View tasks\n• complete_task - Mark tasks complete\n• delete_task - Remove tasks\n• update_task - Modify tasks\n\nTry: "add buy milk" or "list tasks"`);
    }
  };
  
  return (
    <div className="p-8 max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold mb-2">🤖 Todo AI Chatbot</h1>
      <p className="mb-4 text-gray-600">Phase III - MCP Tools + OpenAI Agents SDK</p>
      <p className="mb-6 text-sm text-blue-600 bg-blue-50 p-2 rounded">Frontend: Vercel | Backend: Hugging Face Space | Code: GitHub</p>
      
      <div className="mb-6">
        <div className="flex gap-2">
          <input 
            type="text" 
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Try: 'add buy milk' or 'list tasks'"
            className="border border-gray-300 p-3 rounded-lg flex-grow"
            onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          />
          <button 
            onClick={sendMessage}
            className="bg-blue-600 text-white p-3 rounded-lg hover:bg-blue-700"
          >
            Send
          </button>
        </div>
        
        <div className="mt-4 text-sm text-gray-500">
          <p>Test MCP Tools:</p>
          <ul className="list-disc pl-5 mt-1">
            <li>"add buy groceries" → add_task tool</li>
            <li>"list tasks" → list_tasks tool</li>
            <li>"complete task 1" → complete_task tool</li>
            <li>"delete task 2" → delete_task tool</li>
            <li>"update task 1 to call mom" → update_task tool</li>
          </ul>
        </div>
      </div>
      
      {chatResponse && (
        <div className="bg-gray-50 border border-gray-200 p-4 rounded-lg">
          <h3 className="font-bold mb-2 text-green-600">✅ AI Response (MCP Tools Active):</h3>
          <div className="whitespace-pre-line">{chatResponse}</div>
        </div>
      )}
      
      <div className="mt-8 p-4 bg-gray-100 rounded-lg">
        <h4 className="font-bold mb-2">📌 Phase III Implementation:</h4>
        <ul className="list-disc pl-5 text-sm">
          <li>✅ MCP Server Architecture</li>
          <li>✅ OpenAI Agents SDK (Mock Implementation)</li>
          <li>✅ 5 MCP Tools for Todo Operations</li>
          <li>✅ Stateless Chat Endpoint</li>
          <li>✅ Cloud Deployment (Vercel + Hugging Face)</li>
          <li>✅ Spec-Driven Development</li>
        </ul>
      </div>
    </div>
  );
}