export default function ChatPage() {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-blue-600 mb-2">
          🤖 Todo AI Chatbot
        </h1>
        <p className="text-gray-600 mb-6">
          Chat with AI to manage your todos
        </p>
        
        <div className="bg-white rounded-xl shadow-lg p-6">
          <div className="h-64 border rounded-lg p-4 mb-4 bg-gray-50">
            <div className="text-gray-500 italic">
              Chat messages will appear here...
            </div>
          </div>
          
          <div className="flex gap-2">
            <input
              type="text"
              placeholder="Type message... (e.g., 'Add task to buy milk')"
              className="flex-1 border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 font-medium">
              Send
            </button>
          </div>
          
          <div className="mt-8">
            <h3 className="font-semibold text-gray-700 mb-2">Example commands:</h3>
            <div className="grid grid-cols-2 gap-2">
              {[
                "Add task to buy groceries",
                "Show all my tasks",
                "Mark task 1 as complete",
                "Delete task 2",
                "Update task 3 title",
                "What can you do?"
              ].map((cmd, idx) => (
                <div key={idx} className="bg-gray-100 px-3 py-2 rounded text-sm">
                  "{cmd}"
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}