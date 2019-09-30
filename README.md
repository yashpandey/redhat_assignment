The purpose of the code is download all your files and folders from the Google drive. Please follow the below steps carefully to setup the project :-
  1. Create a google account if you don't have it already.
  2. Go the following link https://console.cloud.google.com/projectcreate?
  3. Create a new project 
  4. Click on library and search for `drive`
  5. Click on google drive and click on enable button
  6. Click on create credentials
  7. Choose google drive api in `Which API are you using?`
  8. In `Where will you be calling the API from?` choose Other UI option
  9. Choose `User data ` in `What data will you be accessing?` and click on create credentails
  10. Download the `credentials.json`
  
Import the `creadentails.json` your project, you can rename it if you wants to. It you want you can store the file in hashicorp vault for additional security.

Then execute the below command to installs the project related requirements:
    **pip3 install -r requirements.txt**

To download the files and folders from your google drive run the following command:
`python3 download_drive.py`

Of course you have to validate the Oauth to see the magic happen.

To execute the test:
    `pytest` 