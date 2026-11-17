
import streamlit as st
from connect_memory_with_llm import get_response

def main():
    st.title("Ask Chatbot!")
    st.caption("Your Medical Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Get user input
    prompt = st.chat_input("Ask your medical question here...")

    if prompt:
        # Display user message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate chatbot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = get_response(prompt)
                    st.markdown(response)

                except Exception as e:
                    response = "Sorry, something went wrong. Please try again."
                    st.error(response)
                    st.exception(e)

        # Save assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })


if __name__ == "__main__":
    main()
