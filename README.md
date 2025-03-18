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
     GUARDIAN_API_KEY=your_guardian_api_key_here # required
     GUARDIAN_API_URL=https://content.guardianapis.com/search #required
     BROKER_TYPE=sqs  # required - can be either 'sqs' or 'kafka'
     SQS_QUEUE_URL=your_sqs_queue_url_here  # optional - leave blank as the app will make one, or you can provide one if you have a specific sqs queue you want used
     KAFKA_LOCAL_IP=your_local_machines_IP # required if using Kafka
     KAFKA_TOPIC=your_kafka_topic_name_here  # required default topic name if using kafka
     MAX_REQUESTS_PER_DAY=50  # defaults to 50
     MESSAGE_TTL_DAYS=3  # Time to live for messages in the broker (SQS or Kafka) - defaults to 3 for sqs - for kafka set the hours in docker-compose.yml which are defaulted to 76

## Setup Steps:
1. **Clone the Repository**:
   - Clone the repository to your local machine:
     ```bash
     git clone https://github.com/your-repository-url.git
     cd guardian_streaming_project
     ```

2. **Set Up Virtual Environment (Optional but Recommended)**:

   - To keep your dependencies isolated, it's recommended to use a virtual environment. Follow these steps to set it up:

   - The `venv` module is part of Python's standard library, but if it's not installed, you can install it using:
   - On macOS/Linux:
     ```bash
     sudo apt install python3-venv
     ```
   - On Windows, it should be available by default with Python.

   - Create a virtual environment:
   - Once `venv` is available, create a virtual environment in your project directory:
      ```bash
      python -m venv venv
      ```
   - activate it with:
      ```bash
      source venv/bin/activate
      ```
   - and deactivate it when your done with:
      ```bash
      deactivate
      ```
2. **Install Requirements**:
   - When inside the venv Install the required dependencies listed in the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run Security Checks**:
   - Run the `security_checks.sh` script to verify that your environment meets the necessary security requirements:
     ```bash
     bash security_checks.sh
     ```

4. **Run Tests**:
   - To verify that everything is working as expected, run the tests using `pytest`. First set your python path so pytest can correctly resolve imports:
      ```bash
     export PYTHONPATH=$(pwd)/src
     ```
   - then run:
     ```bash
     pytest tests/
     ```

5. **Run the CLI**:
   - Execute the main script to start the application and retrieve articles. Use the command below to query for articles (e.g., "books") and specify the number of results (e.g., `--page-size 5`):
     ```bash
     python src/main.py "books" --page-size 5
     ```
   - This will:
     - If **BROKER_TYPE** is set to 'sqs' in .env: Create an **SQS queue** in your aws account (if none exists).
     - Create a **DynamoDB rate counter** for API request limiting (if it does not exist already) - The same table is used for both sqs and kafka.
     - Publish the retrieved articles to the **SQS queue** or **local kafka broker**, depending on **BROKER_TYPE**.

6. **Github Actions (CI/CD)**
   - This repository includes a GitHub Actions workflow that runs Black (for code formatting) and Flake8 (for linting) on every push and pull request. This helps ensure that your code adheres to best practices.

   - If you wish to run these checks manually, you can do so by executing the following commands:
     ```bash
     black .
     flake8 .
     ```

## Deploy to AWS Lambda:
   - In this repo, I have included the required `my_lambda_function.zip`, ready to upload to your Lambda function, but below are instructions on creating it.
1. **Prepare Lambda Deployment Package**:
   - Zip the project’s source files and dependencies for deployment to AWS Lambda:
     ```bash
     zip -r deployment-package.zip src/ requirements.txt
     ```
    - Or create a directory called `package`, install the requirements into it, copy the contents of `src/` into it, and then zip it.

2. **Upload to AWS Lambda**:
   - In the AWS Console, create a new Lambda function.
   - Upload the zip package you just created as the function's deployment package.
   - Ensure that the Lambda function has the necessary permissions to interact with SQS and DynamoDB.
   - Ensure the Lambda has the correct environment variables (find this section in the Lambda configuration tab).
   - Ensure the Lambda handler has the correct entry point: module name and then file name like: `lambda_handler.lambda_handler` - it may assume the module is called `lambda_function` instead, which is incorrect.

## Kafka (For Local Development):
1. **Configure Kafka**:
   - To use Kafka as the message broker locally, set the `BROKER_TYPE` in your `.env` file to `kafka`.

2. **Run Kafka Locally with Docker**:
   - Use Docker to set up the Kafka broker:
     ```bash
     docker-compose up -d
     ```
   - This will start Kafka in the background. 
   - Now run the same commands as before in step 6.

   - Note: You may need to set the correct ownership and permissions on the data directory volume when Docker sets up Kafka. If you encounter permission issues, use the following commands:
     ```bash
     sudo chown -R $USER:$USER ./data
     sudo chmod -R 755 ./data
     ```

## Resetting DynamoDB Rate Limiter:
I’ve added a small script to reset the DynamoDB rate limiter, which applies to both the SQS and Kafka implementations. If you need to manually reset the rate limit counter, you can run the `reset_rate_limiter.py` script, which will reset the count in DynamoDB. This can be useful for testing.
