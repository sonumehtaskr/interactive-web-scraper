import streamlit as st
from scraper import scrape_titles

st.title("🕸️ Interactive Web Scraper")
st.markdown("Enter a website URL and HTML tag to scrape content.")

url = st.text_input("Website URL", "https://news.ycombinator.com/")
tag = st.text_input("HTML Tag to Scrape", "a")
class_name = st.text_input("Class name (optional)", "")

if st.button("Scrape"):
    with st.spinner("Scraping..."):
        results = scrape_titles(url, tag, class_name)
    st.subheader("Scraped Data")
    for idx, item in enumerate(results, 1):
        st.markdown(f"{idx}. {item}")
