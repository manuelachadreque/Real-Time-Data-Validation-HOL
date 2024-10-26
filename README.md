
"""

# Real-Time-Data-Validation-HOL

## Project Overview
This project aims to automate data validation and error handling for CSV files uploaded to an Amazon S3 bucket using AWS Lambda. The Lambda function is triggered each time a new CSV file is uploaded to the designated S3 bucket. Upon activation, the Lambda function performs validation checks to ensure data integrity and format compliance within the CSV file.

If any discrepancies or errors are identified, such as missing values, incorrect formats, or invalid data, the Lambda function moves the file to a designated 'error' S3 bucket for further review. This approach not only ensures cleaner data processing pipelines but also improves data reliability by isolating erroneous files promptly.

This project leverages the serverless nature of AWS Lambda, allowing for a scalable, event-driven architecture that is cost-effective and highly adaptable to varying file upload frequencies.

"""


### Project Architecture

![project architecture](resources/architecture.drawio.svg)



### Project Workflow

![project architecture](resources/worflow.drawio.svg)




### Project Setup


```
python3 -m venv myenv
myenv\Scripts\activate
source myenv/bin/activate

```

## 1.Create Buckets


## 2. Create Lambda function



