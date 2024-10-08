import boto3
import json

#Create the connection to Bedrock
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1', 
    
)

# Define prompt and model parameters
prompt_data = """Write me a poem about pittsburgh"""

text_gen_config = {
    "maxTokenCount": 512,
    "stopSequences": [], 
    "temperature": 0,
    "topP": 0.9
}

body = json.dumps({
    "inputText": prompt_data,
    "textGenerationConfig": text_gen_config  
})

# model_id = 'amazon.titan-tg1-large'
model_id = 'amazon.titan-text-lite-v1'
accept = 'application/json' 
content_type = 'application/json'

# Invoke model 
response = bedrock_runtime.invoke_model(
    body=body, 
    modelId=model_id, 
    accept=accept, 
    contentType=content_type
)

# Print response
response_body = json.loads(response['body'].read())
print(response_body['results'][0]['outputText'])