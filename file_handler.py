import json
import os

# folder and file name
FOLDER_NAME="scans"
FILE_NAME="scans/scan_history.json"


def save_scan_result(scan_data):
    # create folder if not exists
    if not os.path.exists(FOLDER_NAME):
        os.mkdir(FOLDER_NAME)

    # load scan history or start with empty list
    if not os.path.exists(FILE_NAME):
        data=[]
    else:
        with open(FILE_NAME, "r") as f:
            data=json.load(f)

    #it add new scan in to the list
    data.append(scan_data)
    # save scan history
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=2)


    return True


def get_scans():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


#return scans matching with given url
def get_scan_url(url):
    all_scans=get_scans()
    result=[]

    for scan in all_scans:
        # check key exists and match partially (ignore https/www)
        scan_url = scan.get("url", "")
        if url in scan_url:
            result.append(scan)

    return result


