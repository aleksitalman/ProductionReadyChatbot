import torch 
import fastapi
from fastapi.middleware.cors import CORSMiddleware
import time
import uvicorn
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline 

app = fastapi.FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #will only allow the react frontend
    allow_credentials=True,
    allow_methods=["POST"],  
    allow_headers=["*"],  
)

print("Loading PHI-3 Mini model...")

torch.random.manual_seed(0) 
model = AutoModelForCausalLM.from_pretrained( 
    "microsoft/Phi-3-mini-4k-instruct",  
    device_map="cuda",  
    torch_dtype="auto",  
    trust_remote_code=True,  
) 

tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct") 

message = {"role": "user", "content": "How are you today! Can you tell me about cats?"}, 

pipe = pipeline( 
    "text-generation", 
    model=model, 
    tokenizer=tokenizer, 
) 

generation_args = { 
    "max_new_tokens": 500, 
    "return_full_text": False, 
    "do_sample": False, 
} 

#output = pipe(message, **generation_args) 
#print("LLM Model: " + output[0]['generated_text']) 


#POST backend
@app.post('/chat')
async def chat(request: fastapi.Request):
    body = await request.json()
    user_input = body.get("input", "")

    if not user_input:
        return {"error": "No input provided."}

    start_time = time.time()

    #response from the model
    message = [{"role": "user", "content": user_input}]
    output = pipe(message, **generation_args)

    end_time = time.time()
    elapsed_time = end_time - start_time

    return {
        "response": output[0]["generated_text"],
        "time_taken": elapsed_time,
    }


#Server will start when the script is executed
if __name__ == "__main__":
    print("Starting a HTTPS server...")
    
    #Uvicorn server settings
    #Host, port, certificate and the key
    uvicorn.run(app, 
                host="127.0.0.1", 
                port=8000,
                ssl_certfile="cert.pem",  #the self signed certificate
                ssl_keyfile="key.pem",    #the secret key
    )