# Guardian Streaming Project Setup

This guide walks you through the setup and execution of the Guardian Streaming Project. Please follow these steps to ensure everything is properly configured.

## Prerequisites:
1. **Python Installation**:
   - Ensure you have Python installed on your local machine (I use 3.10)

2. **AWS Account Permissions**:
   - Ensure your AWS account has the appropriate permissions to:
     - Create and manage SQS queues.
     - Create and manage DynamoDB tables.
     - Create and manage Lambda functions.

3. **AWS Environment Variables Configuration**:
   - Make sure your AWS environment variables are properly configured. You can do this by setting the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in your environment, or through the `aws configure` command.

4. **.env File Setup**:
   - Create a `.env` file in the root of the project directory and fill it with the following values:
     ```dotenv
     GUARDIAN_API_KEY=your_guardian_api_key_here
     GUARDIAN_API_URL=https://content.guardianapis.com/search
     BROKER_TYPE=sqs  # or kafka if you're using Kafka locally
     SQS_QUEUE_URL=your_sqs_queue_url_here  # Leave blank if using Kafka
     KAFKA_BROKER_URL=your_local_machines_IP_for_local_use  # Only needed if using Kafka
     KAFKA_TOPIC=your_kafka_topic_name_here  # Only needed if using Kafka
     MAX_REQUESTS_PER_DAY=50  # Rate limit for API calls
     MESSAGE_TTL_DAYS=3  # Time to live for messages in the broker (SQS or Kafka)
     ```

## Setup Steps:
1. **Clone the Repository**:
   - Clone the repository to your local machine:
     ```bash
     git clone https://github.com/your-repository-url.git
     cd guardian_streaming_project
     ```

2. **Install Requirements**:
   - Install the required dependencies listed in the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run Security Checks**:
   - Run the `security_checks.sh` script to verify that your environment meets the necessary security requirements:
     ```bash
     bash security_checks.sh
     ```

4. **Run Tests**:
   - To verify that everything is working as expected, run the tests using `pytest`:
     ```bash
     pytest tests/
     ```
     you will find the couple of kafka tests fail and this is expected as I did not get around to implementing a kafka broker beyond finding an appropriate docker-compose file. 

     another test about creating an sqs queue if it doesn't already exist fails but it works in practice.

5. **Run the CLI**:
   - Execute the main script to start the application and retrieve articles. Use the command below to query for articles (e.g., "books") and specify the number of results (e.g., `--page-size 5`):
     ```bash
     python src/main.py "books" --page-size 5
     ```
   - This will:
     - Create an **SQS queue** (if none exists).
     - Create a **DynamoDB rate counter** for API request limiting.
     - Publish the retrieved articles to the **SQS queue**.

## Deploy to AWS Lambda:
   - in this repo I have included the required my_lambda_function.zip, ready to upload to your lambda function but below are instructions on creating it.
1. **Prepare Lambda Deployment Package**:
   - Zip the project’s source files and dependencies for deployment to AWS Lambda:
     ```bash
     zip -r deployment-package.zip src/ requirements.txt
     ```
    - or create a dir - 'package' - and install the requirements into it, and also copy in the contents of src/, and then zip it.
   
2. **Upload to AWS Lambda**:
   - In the AWS Console, create a new Lambda function.
   - Upload the zip package you just created as the function's deployment package.
   - Ensure that the Lambda function has the necessary permissions to interact with SQS and DynamoDB.
   - ensure the lambda has the correct environment variables (find this section in the lambda configuration tab)
   - ensure the lambda handler has the correct entry point: module name and then file name like: lambda_handler.lambda_handler - it may assume the module is called lambda_function instead which is incorrect.

## Kafka (Optional, for Local Development):
1. **Configure Kafka**:
   - To use Kafka as the message broker locally, set the `BROKER_TYPE` in your `.env` file to `kafka`.
   
2. **Run Kafka Locally with Docker**:
   - Use Docker to set up the Kafka broker:
     ```bash
     docker-compose up -d
     ```
   - This will start Kafka and Zookeeper in the background. This feature was not completely implemented and so the .env variables KAFKA_TOPIC and KAFKA_URL are as yet unused.

