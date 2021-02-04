#!/usr/bin/env python3
from fastapi import FastAPI
from enum import Enum

class Model(str, Enum):
  first_string = "string1"
  second_string = "string2"
  third_string = "string3"

app = FastAPI()

@app.get("/")
async def root():
  return {"message" : "Hello world!"}

@app.get("/{model}")
async def get_model(model: Model):
    if model == Model.first_string:
      return {"model" : model, "message": "hey this is only here coz of enums LMAO"}

    if model == Model.second_string:
      return {"model" : model, "message": "wow second string much"}

    return {"model" : model, "message": "not cool, this guy doesnt get his own check. feelsbadman"}