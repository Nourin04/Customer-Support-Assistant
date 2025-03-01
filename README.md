# Customer-Support-Assistant


A smart AI-powered customer support assistant that categorizes queries, analyzes sentiment, and generates responses based on query type. This project leverages **LangChain**, **Groq's LLaMA 3**, and **Gradio** for an interactive and user-friendly interface. It is deployed on **Hugging Face Spaces** for easy accessibility.



---

## 🚀 Features

✅ **Categorizes Queries**: Automatically classifies customer queries into three categories: **Technical, Billing, or General**.  
✅ **Sentiment Analysis**: Determines whether the query sentiment is **Positive, Neutral, or Negative**.  
✅ **Smart Response Generation**: Uses LLaMA 3 to generate appropriate responses based on the query category.  
✅ **Escalation Handling**: If a query has a **negative sentiment**, it gets escalated to a human agent.  
✅ **Modern UI**: Light-themed, spacious, and user-friendly design powered by **Gradio**.  
✅ **Deployed on Hugging Face Spaces**: Easily accessible without requiring local installation.  



---

## 📷 **Project Demo**

Check out the live demo: **[Customer Support Assistant on Hugging Face Spaces](https://huggingface.co/spaces/your-space-name)**

![UI Preview](![Screenshot (76)](https://github.com/user-attachments/assets/ec769cf4-e4e2-461b-b469-d5c84b38c0dd))  

---

## 🏗️ **Tech Stack**

- **Python** 🐍  
- **Gradio** 🎨 (for interactive UI)  
- **LangChain** 🔗 (for prompt engineering)  
- **Groq LLaMA 3** 🦙 (for AI-powered responses)  
- **Hugging Face Spaces** 🚀 (for deployment)  


---

## ⚙️ **Setup Instructions**

### 🛠️ Local Installation

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/your-username/customer-support-assistant.git
cd customer-support-assistant
```

2️⃣ **Create a virtual environment (optional but recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

4️⃣ **Set up Groq API Key**  
Replace `"your_api_key_here"` in `app.py` with your actual Groq API key.

5️⃣ **Run the application**  
```bash
python app.py
```

---

## 🌍 **Deployment on Hugging Face Spaces**

The application is deployed on **Hugging Face Spaces** using Gradio.  

### 📌 **Deployment Link**
[Click here](https://huggingface.co/spaces/noureenac/Intelligent-Customer-Support-Agent).  


---

## 🎯 **Usage Guide**

### 💡 Example Queries

Try asking the bot questions like:

🔹 **Technical Support**  
- "My internet connection keeps dropping. What should I do?"  
- "How do I reset my password?"  

🔹 **Billing Issues**  
- "I was charged twice for my subscription this month!"  
- "How do I update my credit card information?"  

🔹 **General Queries**  
- "Do you offer 24/7 customer support?"  
- "Where can I find the refund policy?"  

### 🏆 **How it Works**
1. Enter your query in the **Customer Query** box.  
2. Click **Submit** to process the query.  
3. The AI will **categorize** the query, **analyze sentiment**, and **generate a response**.  
4. If the sentiment is negative, the query will be **escalated to a human agent**.  

---

## 🚀 **Future Enhancements**
✅ **Multi-language support** for handling global customers.  
✅ **User authentication** for tracking previous interactions.  
✅ **Live chat integration** for real-time support.  
✅ **More detailed AI responses** with follow-up questions.  
✅ **Customizable UI themes** based on user preference.  

---

## 🤝 **Contributing**
Want to improve this project? Contributions are welcome!  

### 📌 Steps to Contribute
1. **Fork** this repository.  
2. Create a **new branch** (`feature-branch`).  
3. Make changes and **commit** your updates.  
4. Push to your branch and create a **Pull Request (PR)**.  

---

## 📜 **License**
This project is licensed under the **MIT License**.  

📌 **Developed by [Noureen AC](https://github.com/Nourin04) 🚀**  
```

---

