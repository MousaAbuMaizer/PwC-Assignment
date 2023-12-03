# AI-Powered Quiz Generator

## Description
This project is an AI-powered quiz generator developed with Python and Streamlit. It enables users to generate and take quizzes on various topics, with questions dynamically created based on the users input, utilizing OpenAI's language model by using LangChain.

## Features
- **Dynamic Quiz Generation:** Create quiz questions on any given topic.
- **Customizable Quiz Length:** Choose the number of questions for each quiz.
- **Immediate Feedback:** Receive instant feedback on quiz submissions.
- **Retake Quizzes:** Option to retake or generate new quizzes with different questions.

## Installation
1. **Clone the Repository:**
   ```
   git clone https://github.com/MousaAbuMaizer/PwC-Assignment.git
   cd PwC-Assignment
   ```

2. **Set Up a Virtual Environment (Optional but Recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # Unix or MacOS
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage
1. **Start the Streamlit Application:**
   ```
   streamlit run Assignment.py
   ```

2. **Access the Web Interface:**
   - Open a web browser and navigate to `http://localhost:8501`.

3. **Generate and Take a Quiz:**
   - Enter a topic.
   - Specify the number of questions.
   - Click 'Generate Quiz' and proceed to answer the questions.
   - Submit your answers to view the results.

4. **Start a New Quiz:**
   - Use the "Start a New Quiz" option to reset and create a new quiz.

## Configuration
- Configure the OpenAI API key in the `.env` file:
  ```
  OPENAI_API_KEY= your api key here
  ```
