import streamlit as st
import pymupdf

# Page settings
st.set_page_config(
    page_title="AI PDF Document Agent",
    page_icon="📄"
)

# Title
st.title("📄 AI PDF Document Agent")
st.write("Upload a PDF and extract its text.")

# PDF upload
uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

# If a PDF is uploaded
if uploaded_file is not None:

    st.success("PDF uploaded successfully!")

    # Read the uploaded PDF
    pdf_bytes = uploaded_file.read()

    # Open the PDF
    document = pymupdf.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    # Show number of pages
    st.write(f"**Number of pages:** {len(document)}")

    # Extract text
    full_text = ""

    for page_number, page in enumerate(document):
        text = page.get_text()

        full_text += f"\n\n--- Page {page_number + 1} ---\n\n"
        full_text += text

    # Display extracted text
    st.subheader("📑 Extracted Text")

    st.text_area(
        "PDF Content",
        full_text,
        height=600
    )

    # Download extracted text
    st.download_button(
        label="⬇️ Download Extracted Text",
        data=full_text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )