"use client";
import { useState } from 'react';

export default function ChatPage() {
  const [message, setMessage] = useState('');
  const [chatResponse, setChatResponse] = useState('');
  
  const sendMessage = async () => {
    try {
      const res = await fetch('https://todo-backend-phase3-working.onrender.com/chat', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          user_id: 'test_user_001',  // Fixed user_id
          message: message
        })
      });
      
      const data = await res.json();
      console.log('Backend response:', data);  // Debug
      
      // Response format check
      if (data.response) {
        setChatResponse(data.response);
      } else if (data.message) {
        setChatResponse(data.message);
      } else {
        setChatResponse(JSON.stringify(data));
      }
      
    } catch (error) {
      setChatResponse(`Error: ${error}`);
    }
  };
  
  return (
    <div className="p-8 max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">🤖 Todo AI Chatbot</h1>
      <p className="mb-4 text-gray-600">Phase III - MCP Tools Integration</p>
      
      <div className="mb-6">
        <div className="flex gap-2">
          <input 
            type="text" 
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Try: 'add buy milk' or 'list my tasks'"
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
          <p>Test commands:</p>
          <ul className="list-disc pl-5 mt-1">
            <li>"add buy groceries"</li>
            <li>"list tasks" or "show my tasks"</li>
            <li>"complete task 1"</li>
            <li>"delete task 1"</li>
            <li>"update task 1 to call mom"</li>
          </ul>
        </div>
      </div>
      
      {chatResponse && (
        <div className="bg-gray-50 border border-gray-200 p-4 rounded-lg">
          <h3 className="font-bold mb-2">🤖 AI Response:</h3>
          <div className="whitespace-pre-line">{chatResponse}</div>
        </div>
      )}
    </div>
  );
}