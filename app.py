import streamlit as st
import openai
import os

# Title
st.set_page_config(page_title="BrandSpark - Product Name Generator", page_icon="💡")
st.title("💡 BrandSpark - AI Product Name Generator")
st.markdown("Generate catchy and creative product names using AI!")

# OpenAI API Key (input or environment variable)
openai_api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")

# Input Fields
description = st.text_area("📝 Product Description", placeholder="e.g. A smartwatch for fitness enthusiasts")
tone = st.text_input("🎨 Brand Tone (optional)", placeholder="e.g. modern, funny, luxury")

if st.button("🚀 Generate Names"):
    if not openai_api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not description:
        st.warning("Please enter a product description.")
    else:
        with st.spinner("Thinking of cool names..."):
            prompt = (
                f"Generate 5 creative, catchy, and brandable product names.\n\n"
                f"Product Description: {description}\n"
                f"Brand Tone: {tone or 'creative and market-friendly'}\n"
            )

            try:
                openai.api_key = openai_api_key
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.9
                )
                names = response['choices'][0]['message']['content']
                st.success("Here are your product name suggestions:")
                st.markdown(f"```\n{names}\n```")

            except Exception as e:
                st.error(f"Error: {str(e)}")