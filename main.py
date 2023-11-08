from fastapi import FastAPI
from pydantic import BaseModel
from speech import identify_transfer_info, bank_name_list

app = FastAPI()

class Body(BaseModel):
    text: str

@app.post("/speech-to-text")
async def speech_to_text(body: Body):
    try:
        result = identify_transfer_info(body.text, bank_name_list)
        # print("i want tranfer 5000 naira")
        return result
    except Exception as e:
        return str(e)

