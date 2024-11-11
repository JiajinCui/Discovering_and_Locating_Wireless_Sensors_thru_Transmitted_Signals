# Project Proposal

## 1. Motivation & Objective

Many smart homes are equipped with sensors that collect wireless data about the environment and how people interact with their spaces. Yet, much of this information isn't fully utilized to understand daily activities and routines. By combining this sensor data with common knowledge about how devices like door, motion, and multi sensors are typically used, we can gain deeper insights into occupants' behaviors. Our objective is to develop a system that uses advanced AI models to interpret these wireless signals and access the sensor's location. This will enhance the smart home experience, making it more responsive and intuitive to the needs of its users.

## 2. State of the Art & Its Limitations

You Only Look Once (YOLO) is a current widely-used object detection model that divides the input (usually an image) into grids. For signal classification, YOLO divide a signal into fixed-length windows, or bounding boxes. 

Limitations of You Only Look Once (YOLO):
(i) This appraoch requires the creation of an image out of in-phase/quadrature (I/Q) samples, incurring additional latency. 
(ii) Being a viable method for computer vision tasks, YOLO does not achieve the level of resolution required for wireless signals.
(ii) Modern wireless signals such as 5G and LoRa can hardly confirm into square bounding boxes which leads to a significant amount of specturm being incorrectly classified as occupied, leading to poor specturm efficiency.


## 3. Novelty & Rationale

The approach we found in a paper is called Stitiching-the-Specturm, which "stitches" different signals together to create samples where signals are overlapping and affected by real-world noises and inferences.

Novel dataset generation pipeline that generate large-scale datasets that 
(i) contains signals collected On The Air(OTA) and are affected by real-world conditions
(ii) can be completely labeled
(iii) low latency 

Novel custom DL algorithm for multi-label multi-class spectrum sensing based on semantic segmentation that
(i) operates at the I/Q level instead of creating images
(ii) classifies each and every I/Q sample incoming from the ADC without creating bounding boxes, thus increasing classification accuracy significantly.
(iii) only uses 1024 I/Q samples as input, which leads to very low inference time.

## 4. Potential Impact

Technical impacts:
(i) The network is able to achieve more accuracy (7% in the paper) than U-Net in the most challenging protocols(Wi-Fi and LTE) while maintaining similarly low latency
(ii) The dataset generation pipeline makes the wideband spectrum sensing algorithm more accurate even with data collected from different devices, sampling rates, antennas.
(iii) Intersection over Union (IoU) of 96.70%; 2.6ms of latency to process 100MHz of spectrum.

Broad impacts:
(i) Less amount of data needed for understanding the signal (protocal, MAC address, etc.)
(ii) A more accurate classification result that takes less time
(iii) Significantly lower the difficulty of learning about the information of sensors (their types and locations) in a smart home without prior knowledge

## 5. Challenges

What are the challenges and risks?

## 6. Requirements for Success

What skills and resources are necessary to perform the project?

## 7. Metrics of Success

What are metrics by which you would check for success?

## 8. Execution Plan

Describe the key tasks in executing your project, and in case of team project describe how will you partition the tasks.

## 9. Related Work

### 9.a. Papers

List the key papers that you have identified relating to your project idea, and describe how they related to your project. Provide references (with full citation in the References section below).

### 9.b. Datasets

List datasets that you have identified and plan to use. Provide references (with full citation in the References section below).

### 9.c. Software

List softwate that you have identified and plan to use. Provide references (with full citation in the References section below).

## 10. References

List references correspondign to citations in your text above. For papers please include full citation and URL. For datasets and software include name and URL.
