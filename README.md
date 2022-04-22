[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# Pneumonia Detection using Transfer Learning

## Approach

Pneumonia detection is commonly predicted using basic CNN models. However , the accuracy of these state of the art models is pretty low.
On the other hand, our approach of using Transfer learning, that is, by using VGG-19 and ResNet50, we can get a much better accuracy. 

## Project

Our project consists of 3 approaches:
* VGG-19 Model
* ResNet50 Model
* ResNet50 Model after Fine-Tuning parameters

## Dataset

Dataset consists of images of 2 classes of chest X-ray images:
1. Diseased
2. Normal

<p align="left">
<img width=50% src="images/data1.jpeg"> &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;
<img width=40% src="images/data2.jpeg"> &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; 
</p>

The dataset can be accessed from the `Data` Folder.

## Model Results

### VGG-19

<p align="left">
<img width=50% src="images/vgg_result.jpeg"> &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;
</p>

### ResNet50

<p align="left">
<img width=50% src="images/resnet50_result.jpeg"> &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;
</p>

### ResNet50 - Fine Tuned

<p align="left">
<img width=50% src="images/fine_tuned_result.jpeg"> &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;
</p>

## How to Use

* Clone the repository using :

        $ git clone https://github.com/rishusiva/Pneumonia_Detection
                
* Enter the directory using:

        $ cd Pneumonia_Detection/
      
* Install the requirements using:

        $ pip install -r requirements.txt

* Run the demo notebook 
        
## Results

* VGG-19 : 85%
* ResNet50 : 91%
* ResNet50 Tuned : 95%

<h2 align= "left"><b>Project Maintainer(s)</b></h2>

<table>
<tr align="center">
  
  <td>
  
Rishikesh S

<p align="center">
<img src = "https://avatars.githubusercontent.com/u/53835355?v=4"  height="120" alt="Your Name Here (Insert Your Image Link In Src">
</p>
<p align="center">
<a href = "https://github.com/rishusiva"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/rishikesh-sivakumar-1a166a18b/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>






  </table>

## Contribution 

Contributions are always welcome! You can contribute to this project in the following way:
- [ ] Increasing the accuracy 
- [ ] Bug fixes if any
- [ ] Creating an application

Do check out the <a href="https://github.com/rishusiva/Pose-Network/blob/main/Docs/Contribution.md">documentation</a> for Contribution Guidelines.
