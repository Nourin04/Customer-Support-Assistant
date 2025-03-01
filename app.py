import gradio as gr
from typing import Dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# Initialize LLM
llm = ChatGroq(
    temperature=0,
    groq_api_key="your_key",  # Replace with actual API key
    model_name="llama3-8b-8192"
)

# Function to categorize query
def categorize(query: str) -> str:
    prompt = ChatPromptTemplate.from_template(
        "Categorize this customer query into one of these categories: Technical, Billing, General. Query: {query}"
    )
    chain = prompt | llm
    return chain.invoke({"query": query}).content.strip()

# Function to analyze sentiment
def analyze_sentiment(query: str) -> str:
    prompt = ChatPromptTemplate.from_template(
        "Analyze sentiment (Positive, Neutral, Negative) of this query: {query}"
    )
    chain = prompt | llm
    return chain.invoke({"query": query}).content.strip()

# Function to generate response based on category
def generate_response(query: str, category: str) -> str:
    if category == "Technical":
        prompt = ChatPromptTemplate.from_template(
            "Provide a technical support response: {query}"
        )
    elif category == "Billing":
        prompt = ChatPromptTemplate.from_template(
            "Provide a billing support response: {query}"
        )
    else:
        prompt = ChatPromptTemplate.from_template(
            "Provide a general support response: {query}"
        )

    chain = prompt | llm
    return chain.invoke({"query": query}).content.strip()

# Main function for Gradio
def gradio_interface(query: str) -> str:
    category = categorize(query)
    sentiment = analyze_sentiment(query)

    if sentiment == "Negative":
        response = "This query has been escalated to a human agent."
    else:
        response = generate_response(query, category)

    return f"**Category:** {category}\n\n**Sentiment:** {sentiment}\n\n**Response:** {response}"

# Gradio UI with light theme and modern design
gui = gr.Interface(
    fn=gradio_interface,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Enter your query here...",
        label="Customer Query",
        elem_id="query_input"
    ),
    outputs=gr.Markdown(),
    title="Customer Support Assistant",
    description="Provide a query and receive a categorized response. The system analyzes sentiment and routes to the appropriate support channel.",
    theme=gr.themes.Default(
        primary_hue="blue", 
        secondary_hue="gray", 
        font=["Poppins", "Arial", "sans-serif"],
        spacing_size="lg",  # More spacious layout
        radius_size="lg",   # Rounded corners
    ),
    live=False,  # Disable live mode to require submit button click
)

if __name__ == "__main__":
    gui.launch()
