import os

from django.views import View
from django.http import JsonResponse

from django_backend.custom_storages import MediaStorage

class FileUploadView(View):
    def post(self, requests, **kwargs):
        file_obj = requests.FILES.get('file', '')

        # do your validation here e.g. file size/type check

        # organize a path for the file in bucket
        file_directory_within_bucket = 'user_upload_files/{username}'.format(username=requests.user)

        # synthesize a full file path; note that we included the filename
        file_path_within_bucket = os.path.join(
            file_directory_within_bucket,
            file_obj.name
        )

        media_storage = MediaStorage()

        if not media_storage.exists(file_path_within_bucket): # avoid overwriting existing file
            media_storage.save(file_path_within_bucket, file_obj)
            file_url = media_storage.url(file_path_within_bucket)

            return JsonResponse({
                'message': 'OK',
                'fileUrl': file_url,
            })
        else:
            return JsonResponse({
                'message': 'Error: file {filename} already exists at {file_directory} in bucket {bucket_name}'.format(
                    filename=file_obj.name,
                    file_directory=file_directory_within_bucket,
                    bucket_name=media_storage.bucket_name
                ),
            }, status=400)
