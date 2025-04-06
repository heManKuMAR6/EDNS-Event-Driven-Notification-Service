# Event-Driven Notification Service (EDNS)

This project implements an Event-Driven Notification Service using AWS Serverless Application Model (SAM). The service provides an API endpoint to receive event data, processes it using a Lambda function, stores the event details in an S3 bucket and a DynamoDB table, and sends notifications via SNS.

## Project Structure


## Getting Started

1. **Install AWS SAM CLI:**  
   Follow the [AWS SAM installation guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html).

2. **Build the Application:**  
   In the project root, run:



3. **Test Locally:**  
Start the local API gateway:

You can test the API endpoint using the sample event in `events/sample_event.json`:


4. **Deploy to AWS:**  
Deploy the application using:
Follow the prompts to configure your stack name, region, and other parameters.

## Project Components

- **API Gateway:** Exposes an endpoint `/event` to receive event data.
- **Lambda Function:** Processes incoming events, stores data in S3 and DynamoDB, and sends notifications via SNS.
- **S3 Bucket:** Stores a JSON copy of each event.
- **DynamoDB Table:** Logs event data for querying and further analysis.
- **SNS Topic:** Sends notifications when a new event is processed.

## Naming Conventions

- **Project Name:** EDNS (Event-Driven Notification Service)
- **Lambda Function:** EDNSEventProcessorFunction
- **S3 Bucket:** edns-event-data-bucket
- **DynamoDB Table:** EDNSEventTable
- **SNS Topic:** EDNSNotificationTopic

## License

This project is licensed under the MIT License.
