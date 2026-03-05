import json
import os
from datetime import datetime
from dotenv import load_dotenv
import requests
import time
import random

# Load environment variables
load_dotenv()

# Colors for terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BG_BLUE = '\033[44m'
    BG_GREEN = '\033[42m'
    BG_GRAY = '\033[100m'

# Conversation storage
CONVERSATIONS_FILE = "conversations.json"
current_conversation = []

def load_conversations():
    """Load all saved conversations"""
    if os.path.exists(CONVERSATIONS_FILE):
        with open(CONVERSATIONS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_conversations(conversations):
    """Save conversations to file"""
    with open(CONVERSATIONS_FILE, 'w') as f:
        json.dump(conversations, f, indent=2)

def get_ollama_response(prompt):
    """Get response from Ollama AI"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:1b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 200
                }
            }
        )
        return response.json()["response"]
    except:
        return "❌ Error: Make sure Ollama is installed and running. Download from https://ollama.ai"

def typing_indicator():
    """Show typing animation"""
    indicators = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(10):
        for indicator in indicators:
            print(f"\r{Colors.YELLOW}🤖 AI is typing{indicator} {Colors.END}", end="", flush=True)
            time.sleep(0.1)
    print("\r" + " " * 30 + "\r", end="", flush=True)

def show_header():
    """Display beautiful header"""
    print(f"""
{Colors.BOLD}{Colors.BG_BLUE}
╔══════════════════════════════════════════════════════════════╗
║                    🤖 AI CHATBOT v2.0                        ║
║              Beautiful • Smart • Free • Local                ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
""")

def show_menu():
    """Display main menu"""
    print(f"{Colors.CYAN}┌─────────────────────────────────────────────────────────┐{Colors.END}")
    print(f"{Colors.CYAN}│{Colors.BOLD}                    📋 MAIN MENU                        {Colors.END}{Colors.CYAN}│{Colors.END}")
    print(f"{Colors.CYAN}├─────────────────────────────────────────────────────────┤{Colors.END}")
    print(f"{Colors.CYAN}│  1️⃣  Start New Conversation                              │{Colors.END}")
    print(f"{Colors.CYAN}│  2️⃣  View Saved Conversations                           │{Colors.END}")
    print(f"{Colors.CYAN}│  3️⃣  Search Conversations                               │{Colors.END}")
    print(f"{Colors.CYAN}│  4️⃣  Delete Conversation                                │{Colors.END}")
    print(f"{Colors.CYAN}│  5️⃣  Exit                                               │{Colors.END}")
    print(f"{Colors.CYAN}└─────────────────────────────────────────────────────────┘{Colors.END}")
    print(f"{Colors.YELLOW}Choose an option (1-5):{Colors.END} ", end="")

def format_timestamp():
    """Get current timestamp"""
    return datetime.now().strftime("%H:%M:%S")

def save_conversation():
    """Save current conversation"""
    if not current_conversation:
        print(f"{Colors.RED}❌ No conversation to save!{Colors.END}")
        return
    
    conversations = load_conversations()
    name = input(f"{Colors.YELLOW}💾 Enter conversation name: {Colors.END}")
    
    conversations[name] = {
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "messages": current_conversation
    }
    
    save_conversations(conversations)
    print(f"{Colors.GREEN}✅ Conversation saved as '{name}'!{Colors.END}")

def view_conversations():
    """View saved conversations"""
    conversations = load_conversations()
    
    if not conversations:
        print(f"{Colors.YELLOW}📭 No saved conversations yet.{Colors.END}")
        return
    
    print(f"\n{Colors.BOLD}{Colors.BLUE}📚 Saved Conversations:{Colors.END}")
    print(f"{Colors.CYAN}─" * 50 + "{Colors.END}")
    
    for i, (name, data) in enumerate(conversations.items(), 1):
        created = data["created"]
        message_count = len(data["messages"])
        print(f"{Colors.GREEN}{i}. {name}{Colors.END}")
        print(f"   📅 Created: {created}")
        print(f"   💬 Messages: {message_count}")
        print(f"{Colors.CYAN}─" * 50 + "{Colors.END}")

def chat_interface():
    """Main chat interface"""
    global current_conversation
    current_conversation = []
    
    print(f"\n{Colors.BOLD}{Colors.GREEN}🚀 Chat Started! Type 'exit' to stop, 'save' to save conversation{Colors.END}")
    print(f"{Colors.BG_GRAY}{'═' * 60}{Colors.END}")
    
    while True:
        user_input = input(f"\n{Colors.BOLD}{Colors.BLUE}👤 You [{format_timestamp()}]:{Colors.END} ")
        
        if user_input.lower() == "exit":
            save_choice = input(f"{Colors.YELLOW}💾 Save conversation before leaving? (y/n): {Colors.END}")
            if save_choice.lower() == 'y':
                save_conversation()
            break
        
        if user_input.lower() == "save":
            save_conversation()
            continue
        
        # Add user message to conversation
        user_message = {
            "type": "user",
            "message": user_input,
            "timestamp": format_timestamp()
        }
        current_conversation.append(user_message)
        
        # Show typing indicator
        typing_indicator()
        
        # Get AI response
        ai_response = get_ollama_response(user_input)
        
        # Add AI message to conversation
        ai_message = {
            "type": "ai", 
            "message": ai_response,
            "timestamp": format_timestamp()
        }
        current_conversation.append(ai_message)
        
        # Display AI response with beautiful formatting
        print(f"\n{Colors.BOLD}{Colors.GREEN}🤖 AI [{format_timestamp()}]:{Colors.END}")
        print(f"{Colors.BG_GRAY}{'─' * 60}{Colors.END}")
        print(f"{Colors.WHITE}{ai_response}{Colors.END}")
        print(f"{Colors.BG_GRAY}{'─' * 60}{Colors.END}")

def main():
    """Main application"""
    show_header()
    
    while True:
        show_menu()
        choice = input().strip()
        
        if choice == "1":
            chat_interface()
        elif choice == "2":
            view_conversations()
        elif choice == "3":
            print(f"{Colors.YELLOW}🔍 Search feature coming soon!{Colors.END}")
        elif choice == "4":
            print(f"{Colors.YELLOW}🗑️ Delete feature coming soon!{Colors.END}")
        elif choice == "5":
            print(f"{Colors.GREEN}👋 Goodbye! Thanks for chatting!{Colors.END}")
            break
        else:
            print(f"{Colors.RED}❌ Invalid choice! Please try again.{Colors.END}")

if __name__ == "__main__":
    main()
