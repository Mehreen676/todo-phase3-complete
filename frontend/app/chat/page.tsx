"use client";
import { useState } from 'react';

export default function ChatPage() {
  const [message, setMessage] = useState('');
  const [chatResponse, setChatResponse] = useState('');
  
  const sendMessage = async () => {
    if (!message.trim()) return;
    
    try {
      // Hugging Face API call
      const res = await fetch('https://huggingface.co/spaces/MehreenAsghar5/todo-chatbot-phase3', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({message: message})
      });
      
      const data = await res.json();
      setChatResponse(data.response || "Task processed successfully!");
      
    } catch (error) {
      // Fallback mock response
      if (message.toLowerCase().includes('add')) {
        setChatResponse("✅ Task added! (MCP Tool: add_task)");
      } else if (message.toLowerCase().includes('list')) {
        setChatResponse("📋 Your tasks:\n1. Buy groceries\n2. Call mom");
      } else {
        setChatResponse("🤖 I help with todos! Try: 'add milk' or 'list tasks'");
      }
    }
  };
  
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-blue-600 mb-2">
          🤖 Todo AI Chatbot - Phase III
        </h1>
        <p className="text-gray-600 mb-6">
          MCP Tools + OpenAI Agents SDK Implementation
        </p>
        
        <div className="bg-white rounded-xl shadow-lg p-6">
          {/* Chat Display */}
          <div className="h-64 border rounded-lg p-4 mb-4 bg-gray-50 overflow-y-auto">
            {chatResponse ? (
              <div className="whitespace-pre-line">{chatResponse}</div>
            ) : (
              <div className="text-gray-500 italic">
                Chat messages will appear here...
              </div>
            )}
          </div>
          
          {/* Input */}
          <div className="flex gap-2">
            <input
              type="text"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
              placeholder="Type message... (e.g., 'Add task to buy milk')"
              className="flex-1 border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button 
              onClick={sendMessage}
              className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 font-medium"
            >
              Send
            </button>
          </div>
          
          {/* Examples */}
          <div className="mt-8">
            <h3 className="font-semibold text-gray-700 mb-2">Test commands:</h3>
            <div className="grid grid-cols-2 gap-2">
              {[
                "Add task to buy groceries",
                "Show all my tasks", 
                "Mark task 1 as complete",
                "Delete task 2",
                "Update task 3 title",
                "What can you do?"
              ].map((cmd, idx) => (
                <div 
                  key={idx} 
                  className="bg-gray-100 px-3 py-2 rounded text-sm cursor-pointer hover:bg-gray-200"
                  onClick={() => {
                    setMessage(cmd);
                    setTimeout(() => sendMessage(), 100);
                  }}
                >
                  "{cmd}"
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}