KZ AI Constitution


The KZ AI Constitution project is aimed at building an AI-powered system that can handle tasks related to the analysis, generation, and decision-making based on constitutional documents and legal texts. This project integrates advanced machine learning models, document processing, and natural language understanding techniques to help users navigate and query legal documents effectively.
Technologies Used
•	Python: The main programming language.
•	Streamlit: For the interactive web interface.
•	Ollama: For handling document embeddings and generation.
•	Chroma: For similarity search and document storage.
•	PyPDF2: For reading and processing PDF documents.
•	langchain: For chaining multiple models and operations.
•	Flask/FastAPI: (if applicable) Backend APIs for interacting with the AI system.
•	Docker: (optional) For containerizing the app and its dependencies.
Features
•	Document Upload: Upload constitutional and legal documents in PDF format for processing.
•	Query Legal Texts: Ask questions based on the uploaded documents and retrieve relevant passages.
•	AI-Driven Analysis: Use AI to analyze and summarize complex legal documents and provide insights.
•	Similarity Search: Find similar documents and content to the queried legal texts.
Setup Instructions
Screenshot:
![image](https://github.com/user-attachments/assets/a72faaac-4fbd-446c-a913-038fc1880d70)
Requirements
Before starting the project, ensure that the following dependencies are installed:
•	Python 3.8+
•	Streamlit
•	Ollama (for embeddings and document queries)
•	Chroma (for document embedding storage)
•	PyPDF2 (for PDF parsing)
•	Flask/FastAPI (for the backend API)
Installation Steps
1.	Clone the repository:
bash
КопироватьРедактировать
git clone <repository_url>
cd KZ-AI-Constitution
2.	Create and activate a virtual environment (optional but recommended):
bash
КопироватьРедактировать
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3.	Install the dependencies:
bash
КопироватьРедактировать
pip install -r requirements.txt
4.	Install Ollama:
o	For Ubuntu:
bash
КопироватьРедактировать
curl -sSL https://ollama.com/install | bash
o	For Windows:
Download and install Ollama from here.
5.	Run the application:
Start the Streamlit application by running:
bash
КопироватьРедактировать
streamlit run main.py
requirements.txt
text
КопироватьРедактировать
streamlit
ollama
chromadb
PyPDF2
flask
langchain
How It Works
Document Upload and Embedding
1.	Users upload legal documents (PDF format).
2.	The documents are parsed using PyPDF2 and the text is fed into Ollama for embedding generation.
3.	These embeddings are then stored in Chroma, allowing efficient similarity search.
Querying the Constitution
1.	The user submits a query related to the legal document via the Streamlit UI.
2.	The query is embedded using Ollama.
3.	A similarity search is performed on the stored document embeddings to retrieve the most relevant sections.
4.	The results are displayed on the UI.
Folder Structure
bash
КопироватьРедактировать
/KZ-AI-Constitution
    /utils
        rag_pipeline.py   # Contains logic for document querying and embeddings
    main.py               # The main Streamlit application
    requirements.txt      # Python dependencies
    README.md             # This file
Contributions
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for more details.



