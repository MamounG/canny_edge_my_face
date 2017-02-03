# canny_edge_my_face
use a canny edge filter

# Problem
I run into a little complication here as I don't have a camera nor acces to a computer equiped with a camera. 

In order to fulfill the assignement I used a small node found on internet that publish in a topic (/image) a png picture. A picture of my face is provided in order to stick with the node's name.

# Usage
To use it first start the node imagePublisher:
rosrun canny_edge_my_face imagePublisher.py ~/canny_edge_my_face/myFace.png

and then start the filter:
rosrun canny_edge_my_face canny_edge.py

you can then see the resulting image in the topic /edge_image
