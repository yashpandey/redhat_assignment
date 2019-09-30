from __future__ import print_function
import io
import os

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaIoBaseDownload

SCOPES = [
    'https://www.googleapis.com/auth/drive.metadata.readonly',
    'https://www.googleapis.com/auth/drive.file'
]


def authorize_login_oauth():
    """
    This method is used to validate the Oauth login
    :return drive_service: returns Oauth object
    """
    store = file.Storage('storage.json')
    creds = store.get()
    flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
    creds = tools.run_flow(flow, store)
    drive_service = discovery.build('drive', 'v3', http=creds.authorize(Http()))
    return drive_service


def get_file_ids(drive_service):
    """
    This method extract the name and file id from the google drive.
    :param drive_service: auth_credentials
    :return files_to_download: returns a list of ids and name of files and directory present in your drive
    """
    results = drive_service.files().list(
        pageSize=10,
        fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    files_to_download = []
    if not items:
        print('Nothing here!')
    else:
        print('Files:')
        for item in items:
            files_to_download.append((item['name'], item['id']))
            print(u'{0} ({1})'.format(item['name'], item['id']))
    return files_to_download


def download_file(drive_service, file_id, file_name):
    """
    This file will download the files and folder present at your google drive
    :param drive_service: Oauth access credentails
    :param file_id: the id of the file which you want to download
    :param file_name: the name of the file which you want to download from the google drive
    """
    request = drive_service.files().get(fileId=file_id)
    fh = io.FileIO('downloads/' + file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))


if __name__ == '__main__':
    drive_service = authorize_login_oauth()
    target_files = get_file_ids(drive_service)
    if not os.path.exists('downloads'):
        os.mkdir('downloads')
    for file in target_files:
        download_file(drive_service, file[1], file[0])
