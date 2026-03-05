# 🤖 AI Chatbot Python

A beautiful, free, and private AI chatbot built with Python, Ollama, and a stunning terminal interface.

## ✨ Features

### 🎨 Beautiful Interface
- **Colorful terminal design** with professional styling
- **Typing indicators** for realistic conversation feel
- **Message timestamps** for every interaction
- **Professional menu system** with boxed layouts
- **Visual separators** for clean conversation flow

### 🧠 AI Capabilities
- **100% Free** - No API costs ever
- **Completely Private** - Runs locally on your computer
- **Fast Responses** - Uses optimized Llama 3.2 model
- **Smart Conversations** - Context-aware responses

### 💾 Conversation Management
- **Save conversations** with custom names
- **View saved conversations** with details
- **Message counting** and timestamps
- **JSON storage** for easy access

## 🚀 Quick Start

### Prerequisites
1. **Install Ollama**: [https://ollama.ai](https://ollama.ai)
2. **Install UV**: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Fayaza-Jiffry/ai-chatbot-python.git
   cd ai-chatbot-python
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

3. **Download AI model**:
   ```bash
   ollama pull llama3.2:1b
   ```

4. **Start Ollama**:
   ```bash
   ollama serve
   ```

5. **Run the chatbot**:
   ```bash
   uv run python chatbot_v2.py
   ```

## 🎮 How to Use

### Main Menu
```
┌─────────────────────────────────────────────────────────┐
│                    📋 MAIN MENU                        │
├─────────────────────────────────────────────────────────┤
│  1️⃣  Start New Conversation                              │
│  2️⃣  View Saved Conversations                           │
│  3️⃣  Search Conversations                               │
│  4️⃣  Delete Conversation                                │
│  5️⃣  Exit                                               │
└─────────────────────────────────────────────────────────┘
```

### Chat Commands
- **Type your message** and press Enter
- **Type "save"** to save current conversation
- **Type "exit"** to end conversation

### Sample Conversation
```
🚀 Chat Started! Type 'exit' to stop, 'save' to save conversation
════════════════════════════════════════════════════════════

👤 You [11:19:07]: hey buddy

🤖 AI [11:19:27]:
────────────────────────────────────────────────────────────
Hello! How can I assist you today?
────────────────────────────────────────────────────────────
```

## 🛠️ Technology Stack

- **Python 3.14+** - Core programming language
- **Ollama** - Local AI model runner
- **Llama 3.2** - AI model (1B parameters)
- **UV** - Fast package manager
- **Requests** - HTTP library for API calls
- **Python-dotenv** - Environment variable management

## 📁 Project Structure

```
ai-chatbot-python/
├── chatbot_v2.py          # Main chatbot application
├── chatbot.py             # Simple version
├── pyproject.toml         # Project dependencies
├── .env                   # Environment variables
├── conversations.json     # Saved conversations
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file:
```env
# Currently not used, but reserved for future features
```

### Customization
- **Colors**: Modify the `Colors` class in `chatbot_v2.py`
- **AI Model**: Change `"model": "llama3.2:1b"` to other models
- **Response Length**: Adjust `"num_predict": 200` for longer/shorter replies

## 🌟 What Makes This Special

### 🆚 Traditional AI Chatbots
| Feature | Traditional Chatbots | This Chatbot |
|---------|-------------------|--------------|
| **Cost** | 💰 Pay per message | 🆓 100% Free |
| **Privacy** | 🌐 Data sent to servers | 🔒 Completely local |
| **Internet** | 📶 Required | 📡 Offline capable |
| **Speed** | ⏳ Network dependent | ⚡ Instant local |

### 🎯 Perfect For
- **Learning** about AI and chatbots
- **Privacy-conscious** users
- **Offline usage** (no internet needed)
- **Development** and experimentation
- **Educational purposes**

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report issues
- Suggest features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Ollama** for amazing local AI infrastructure
- **Meta** for the Llama AI models
- **UV** for the lightning-fast package manager
- **Python** community for excellent libraries

## 📞 Support

If you need help:
1. Check the [Issues](https://github.com/Fayaza-Jiffry/ai-chatbot-python/issues) page
2. Create a new issue with details
3. Join the discussion

---

**Made with ❤️ by [Fayaza Jiffry](https://github.com/FayazaJiffry2024)**

*Enjoy your free, private AI chatbot!* 🎉
