# Importations des modules 
import os
from fastapi import FastAPI, HTTPException
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from langserve import add_routes
from langchain.prompts import ChatPromptTemplate
import google.generativeai as genai
from dotenv import load_dotenv
from pydantic import BaseModel
# Chargements des variables d'environment
load_dotenv()
# Creation de l'application FastAPI
app = FastAPI(
    title="Langchain LLM API",
    version="1.0",
    description="API for Langchain interaction with LLM"
)


# Modèle pour la requête de l'utilisateur
class QuestionInput(BaseModel):
    question: str

# Initialisation du modèle de LLM avec Langchain
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
prompt_template = ChatPromptTemplate.from_template("Answer the following: {question}")
model = ChatGoogleGenerativeAI(model="gemini-pro")

# Ajout des routes Langserve (pour la gestion des LLM)
add_routes(app, prompt_template | model, path="/ask")

@app.post("/ask-question/")
async def ask_question(input: QuestionInput):
    """
    Endpoint pour poser une question à l'LLM.
    """
    # Validation de la question avec Pydantic
    question = input.question
    try:
        # Le traitement du modèle (Langchain + LLM)
        response = model.generate(prompt_template.format(question=question))
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
