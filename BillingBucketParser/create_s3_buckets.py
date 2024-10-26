import boto3

# instantiate a boto3 resource fors3 and name your bucket
s3 = boto3.resource('s3')
region ='eu-west-2'


#check if bucket exists if not creates a bucket
def create_bucket(bucket_name):

    all_my_buckets = [bucket.name for bucket in s3.buckets.all()]
    print(all_my_buckets)

    if bucket_name not in all_my_buckets:
        print(f"'{bucket_name}' bucket name does not exists creating now...")
        s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-2',
        },
    )

        print(f"'{bucket_name} has been created.")
    else:
        print(f"{bucket_name} bucket already exists. no need to createa new one. ")


buckets_names=['manuela-billing-x','manuela-billing-errors-x']

for bucket_name in buckets_names:
    create_bucket(bucket_name)