from fastapi import FastAPI
from main import trojkat
app = FastAPI()


@app.post("/results")
def results(a,h):
    result = trojkat(a,h)
    return {"message": result}

