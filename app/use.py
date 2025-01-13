from vercel_blob import put
from django.conf import settings


def upload_file_to_blob(file, filename):
    """
    Upload a file to Vercel Blob Storage.

    Args:
        file: The InMemoryUploadedFile object to upload.
        filename: The name of the file to store in blob storage.

    Returns:
        str: The URL of the uploaded blob.
    """
    # Read the content of the file as bytes
    content = file.read()

    # Upload the file to blob storage
    blob = put(
        filename,
        content,
        {
            'access': 'public',
            'token': settings.VERCEL_BLOB_READ_WRITE_TOKEN,
        }
    )
    return blob['url']
