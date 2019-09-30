import pytest
import download_drive
import os


@pytest.fixture
def service():
    return download_drive.authorize_login_oauth()


@pytest.fixture
def file_list(service):
    file_list = download_drive.get_file_ids(service)
    return file_list


def test_download_file_id_exists(file_list, service):
    for file in file_list:
        assert service.files().get(fileId=file[1])


def test_download_file_name_exist(file_list):
    for file in file_list:
        assert os.path.exists('downloads/{}'.format(file[0]))


def test_download_file_name_return_false_for_wrong_name():
    assert not os.path.exists('downloads/{}'.format('abc'))


def test_download_file_has_extension(service, file_list):
    for file in file_list:
        assert service.files().get(fileId=file[1], fields='fileExtension')


def test_no_download_file_has_none_size(service, file_list):
    for file in file_list:
        assert service.files().get(fileId=file[1], fields='size') is not 0


def test_download_file_has_created_time(service, file_list):
    for file in file_list:
        assert service.files().get(fileId=file[1], fields='createdTime') is not None


