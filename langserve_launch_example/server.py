# importations des modules 
from fastapi import FastAPI
from langserve import add_routes
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import Runnable

# Création de l'application FastAPI et définition du titre 

app = FastAPI(title="LangServe Launch Example")

# Assurez-vous que la configuration du modèle est correcte
model = ChatGoogleGenerativeAI(model="gemini-pro")

# Création d'un Runnable à partir de votre logique de question
prompt_template = ChatPromptTemplate.from_template("Answer the following: {question}")

# Fonction pour créer un Runnable
def create_ask_question_runnable() -> Runnable:
    return prompt_template | model

# Ajoutez les routes avec le Runnable
add_routes(app, create_ask_question_runnable())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
