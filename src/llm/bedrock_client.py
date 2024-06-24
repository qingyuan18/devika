import logging
import boto3
import json
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


from src.config import Config

class BedRock:
    def __init__(self):
        config = Config()
        access_key = config.get_bedrock_access_key()
        security_key = config.get_bedrock_security_key()
        self.client = Anthropic(
            api_key=api_key,
        )

    def inference(self, model_id: str, prompt: str) -> str:
        logger.info("Generating text with model %s", model_id)

        message = {
                "role": "user",
                "content": [{"text": input_text}]
            }
        messages = [prompt]
        bedrock_params = {
            "modelId": model_id,
            "messages": messages,
            "inferenceConfig": inference_config,
            "additionalModelRequestFields": additional_model_fields,
            "toolConfig": tool_config
        }

        system = [item for item in system_prompts if item.get('text')]
        if system:
            bedrock_params['system'] = system

        ## converse API
        try:
            # Send the message.
            response = bedrock_client.converse(
                modelId=model_id,
                messages=messages,
                system=system_prompts,
                inferenceConfig=inference_config,
                additionalModelRequestFields=additional_model_fields,
                #toolConfig=tool_config
            )

            return response['output']['message']['content']
        except ClientError as err:
            message = err.response['Error']['Message']
            logger.error("A client error occurred: %s", message)
            print(f"A client error occured: {message}")
            return ""







