import boto3
import json
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def list_foundation_models(self):
        """
        List the available Amazon Bedrock foundation models.

        :return: The list of available bedrock foundation models.
        """

        try:
            response = self.bedrock_client.list_foundation_models()
            models = response["modelSummaries"]
            logger.info("Got %s foundation models.", len(models))
            return models

        except ClientError:
            logger.error("Couldn't list foundation models.")
            raise



#Create the connection to Bedrock

bedrock_client = boto3.client(
    service_name='bedrock',
    region_name='us-east-1', 
    
)

bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1', 
    
)

def get_foundation_model(self, model_identifier):
        """
        Get details about an Amazon Bedrock foundation model.

        :return: The foundation model's details.
        """

        try:
            return self.bedrock_client.get_foundation_model(
                modelIdentifier=model_identifier
            )["modelDetails"]
        except ClientError:
            logger.error(
                f"Couldn't get foundation models details for {model_identifier}"
            )
            raise

# Get list of models
print("###Listing all foundation models")
response = bedrock_client.list_foundation_models()
json_response = json.dumps(response, indent=2)
print(json_response)

# List all custom models for format as json
print("###Listing all custom models")
response2 = bedrock_client.list_custom_models()
json_response2 = json.dumps(response, indent=2)
print(json_response2)
print("###Listing all custom models")

model_id = 'amazon.titan-text-lite-v1'

# get details of a specific foundation model
print("###Getting details of the specified foundation model")
response3 = bedrock_client.list_foundation_models()
for model in response3['modelSummaries']:
    if model['modelId'] == model_id:
        print(json.dumps(model, indent=2))
        break
else:
    print(f"Model {model_id} not found in foundation models.")




