import boto3

s3_client = boto3.client('s3')

def fetch_image_urls_from_s3(bucket_name):
    response = s3_client.list_objects_v2(Bucket = bucket_name)
    urls = []
    for obj in response.get('Contents', []):
        url = s3_client.generate_presigned_url(
            'get_object',
            Params = {'Bucket': bucket_name, 'Key': obj['Key']},
            ExpiresIn = 3600
        )
        
        urls.append(url)

    return urls

def fetch_marking_scheme_url_from_s3(bucket_name):
    response = s3_client.list_objects_v2(Bucket = bucket_name, Prefix = 'marking_schemes/')
