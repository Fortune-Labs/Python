
file_url = "Past your url here"

#creating a function to connect to the internet and download the file

def download_data(data_url):
    responce = request.urlopen(data_url) #
    data = responce.read()
    data_str =str(data)
    lines = data_str.split("\\n")
    dest_url = r'file.data'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_data(file_url)