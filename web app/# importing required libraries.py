# importing required libraries
import requests
from bs4 import BeautifulSoup
import os
import time

def get_path(url):
    return "static/URL_" + str(url.replace("/","_"))
  
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    } 

# define the function to scrape images and store it in a directory
def get_images(url):
   # get the directory path
    path = get_path(url)
    try:
        os.mkdir(path)
    except:
        pass
    # request the source code from the URL   
    response = requests.request("GET", url, headers=headers)
    # parse the data through the Beautiful Soup
    data = BeautifulSoup(response.text, 'html.parser')
    # find the image tag in the source code
    images = data.find_all('img', src=True)
    # extract the source from all the image tags
    image_src = [x['src'] for x in images]
    # select only jpeg format images
    image_src = [x for x in image_src if x.endswith('.jpeg') ]
    image_count = 1
    # store the image in the specified directory 
    for image in image_src:
        print(image)
        image_file_name = path+'/'+str(image_count)+'.jpeg' 
        print(image_file_name)
        # open the file in write binary form and add the image content to store it
        with open(image_file_name, 'wb') as f:
            res = requests.get(image)
            f.write(res.content)
        image_count = image_count+1

# define function to add the image in the html file with the class name
def get_picture_html(path, tag):
    image_html = """<p> {tag_name} </p> <picture> <img src= "../{path_name}"  height="300" width="400"> </picture>"""
    return image_html.format(tag_name=tag, path_name=path)

# define function to add the list element in the html file
def get_count_html(category, count):
    count_html = """<li> {category_name} : {count_} </li>"""
    return count_html.format(category_name = category, count_ = count)

# function to calculate the value count
def get_value_count(image_class_dict):
    count_dic = {}
    for category in image_class_dict.values():
        if category in count_dic.keys():
            count_dic[category] = count_dic[category]+1
        else:
            count_dic[category] = 1
    return count_dic

# function to generate the html file from image_class dictionary
# keys will be the path of the images and values will be the class associated to it.
def generate_html(image_class_dict):
    picture_html = ""
    count_html = ""
    
    # loop through the keys and add image to the html file
    for image in image_class_dict.keys():
        picture_html += get_picture_html(path=image, tag= image_class_dict[image])
        
    value_counts = get_value_count(image_class_dict)
    
    # loop through the value_counts and add a count of class to the html file
    for value in value_counts.keys():
        count_html += get_count_html(value, value_counts[value])

# importing the required libaries
from flask import Flask, render_template, request, redirect, url_for
from get_images import get_images, get_path, get_directory
from get_prediction import get_prediction
from generate_html import generate_html
from torchvision import models
import json

app = Flask(__name__)

# mapping
imagenet_class_mapping = json.load(open('imagenet_class_index.json'))

# use the pre-trained model
model = models.densenet121(pretrained=True)
model.eval()

# define the function to get the images from the url and predicted the class
def get_image_class(path):
    # get images from the URL and store it in a given path
    get_images(path)
    # predict the image class of the images with provided directory
    path = get_path(path)
    images_with_tags = get_prediction(model, imagenet_class_mapping, path)
    # generate html file to render once we predict the classes
    generate_html(images_with_tags)

# by deafult render the "home.html"    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        # if search button hit, call the function get_image_class 
        get_image_class(user)
        #render the image_class.html
        return redirect(url_for('success', name=get_directory(user)))


@app.route('/success/<name>')
def success(name):
    return render_template('image_class.html')


if __name__ == '__main__' :
    app.run(debug=True)

# get class of all the images present in the directory 
def get_category(model, imagenet_class_mapping, image_path):
    with open(image_path, 'rb') as file:
        image_bytes = file.read()
    transformed_image = transform_image(image_bytes=image_bytes)
    outputs = model.forward(transformed_image)
    _, category = outputs.max(1)
    
    predicted_idx = str(category.item())
    return imagenet_class_mapping[predicted_idx]

# It will create a dictionary of the image path and the predicted class
# we will use that dictionary to generate the html file. 
def get_prediction(model, imagenet_class_mapping, path_to_directory):
    files = glob.glob(path_to_directory+'/*')
    image_with_tags = {}
    for image_file in files:
        image_with_tags[image_file] = get_category(model, imagenet_class_mapping, image_path=image_file)[1]
    return image_with_tags