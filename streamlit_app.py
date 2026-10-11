import streamlit as st
from groq import Groq

st.set_page_config(page_title="24/7 Free AI Agent", page_icon="🤖")

st.title("🤖 24/7 Free AI Agent")
st.write("Powered by Groq & Streamlit Community Cloud")

# Sidebar mein API key lene ke liye
api_key = st.sidebar.text_input("Enter Groq API Key", type="password")

if not api_key:
    st.warning("Please enter your Groq API Key in the sidebar to start.")
else:
    client = Groq(api_key=api_key)
    
    prompt = st.text_area("What do you want your agent to do?", placeholder="Ask anything...")
    
    if st.button("Run Agent"):
        if prompt:
            with st.spinner("Thinking..."):
                try:
                    completion = client.chat.completions.create(
                        model="llama-3.1-70b-versatile",
                        messages=[
                            {"role": "system", "content": "You are a helpful, efficient AI agent."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7,
                    )
                    st.success("Response:")
                    st.write(completion.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a prompt first.")
