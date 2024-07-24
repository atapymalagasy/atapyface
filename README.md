#install libraries python

pip install -r requirements.txt



#run script

uvicorn api:app --reload --port 8001    


#url

http://127.0.0.1:8001/atapyface/



#payload

Body:{

    "imgsrc": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Donald_Trump_official_portrait.jpg/640px-Donald_Trump_official_portrait.jpg"

}


