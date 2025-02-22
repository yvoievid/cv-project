# UI screenshot classifier


The world of UI designs are diverce, especially the desktop UIs. Each has it's own usage, and it's good to have a well designed dataset of images of UI. 
To create such dataset we can take a screenshot of each UI manually but this is detious and disonorable work. 
Hopefully there is a way to do it automatically by downloading images from Appstore data manifests of each app. 
But there is a ptoblem: *not all of this screenshots represent a valuable information*. Moreover, there are a lot of Mobile screenshots, which we are not interested in.

This repository will conduct experiments to classify the dataset of **Desktop UI Images** to three classes: clean-ui, ui-to-crop, unnecesary.

Here are the descriptions for each class:

* clean-ui - images that perfectly represent the UI 
* ui-to-crop - images that have redundant information like advertising text and need to be cropped
* unnecesary - images of mobile UI, or the ones that just contain text or some not UI pictures.


To classify images I have manually created dataset of 4000 labeled images and will make inference on 20k UI image dataset.

Experiments will be conducted using ResNet50, ViT, CLIP Encoder + XGBoost, BLIP2 Encoder + XGboost