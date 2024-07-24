from fastapi import FastAPI
from pydantic import BaseModel
import json
from deepface import DeepFace

app = FastAPI()

def analyze_img(url_img):
    demography = DeepFace.analyze(url_img, enforce_detection=False) #passing nothing as 2nd argument will find everything
    #demography = DeepFace.analyze("img4.jpg", ['age', 'gender', 'race', 'emotion']) #identical to the line above
    #demographies = DeepFace.analyze(["img1.jpg", "img2.jpg", "img3.jpg"]) #analyzing multiple faces same time
    # print(demography)
    age = demography[0].get("age", "N/A")
    emotion = demography[0].get("dominant_emotion", "N/A")
    gender = demography[0].get("dominant_gender", "N/A")
    race = demography[0].get("dominant_race", "N/A")
    print("Age: ", demography[0].get("age", "N/A"))
    print("Emotion: ", demography[0].get("dominant_emotion", "N/A"))
    print("Gender: ", demography[0].get("dominant_gender", "N/A"))
    print("Race: ", demography[0].get("dominant_race", "N/A"))

    return age,emotion,gender,race

# # Define a model for the data you want to receive in the request body
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# # Define a simple GET endpoint
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# # Define a path parameter endpoint
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}

class Ai(BaseModel):
    imgsrc: str
    # aimethod: int = None

# Define a POST endpoint
@app.post("/atapyface/")
def create_item(ai: Ai):
    age,emotion,gender,race = analyze_img(ai.imgsrc)

    return {
        "age":age, 
        "gender":gender,
        "emotion": emotion,
        "race":race

    }



# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
