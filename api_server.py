import traceback
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from app_EmotionLlamaClient import process_video_question

app = FastAPI()

class VideoQuestionRequest(BaseModel):
    video_path: str
    question: str

@app.post("/process_video")
def process_video(req: VideoQuestionRequest):
    try:
        response = process_video_question(req.video_path, req.question)
        return {"response": response}
    except Exception as e:
        traceback.print_exc()  
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7887)
