import requests

url = "http://172.29.2.232:7887/process_video"
headers = {"Content-Type": "application/json"}

data = {
    "video_path": "/home/lbh/Emotion-LLaMA/examples/sample_00004671.mp4",
    "question": "The person in video says: Won't you? Impossible! Fan Xiaomei is not such a person. [reason] What are the facial expressions and vocal tone used in the video? What is the intended meaning behind his words? Which emotion does this reflect?"
}

response = requests.post(url, json=data)
print(response.json())
