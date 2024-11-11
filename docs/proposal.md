# Project Proposal

## 1. Motivation & Objective

Many smart homes are equipped with sensors that collect wireless data about the environment and how people interact with their spaces. Yet, much of this information isn't fully utilized to understand daily activities and routines. By combining this sensor data with common knowledge about how devices like door, motion, and multi sensors are typically used, we can gain deeper insights into occupants' behaviors. Our objective is to develop a system that uses advanced AI models to interpret these wireless signals and access the sensor's location. This will enhance the smart home experience, making it more responsive and intuitive to the needs of its users.

## 2. State of the Art & Its Limitations

You Only Look Once (YOLO) is a current widely-used object detection model that divides the input (usually an image) into grids. For signal classification, YOLO divide a signal into fixed-length windows, or bounding boxes. 

Limitations of You Only Look Once (YOLO):
1. This appraoch requires the creation of an image out of in-phase/quadrature (I/Q) samples, incurring additional latency. 
2. Being a viable method for computer vision tasks, YOLO does not achieve the level of resolution required for wireless signals.
3. Modern wireless signals such as 5G and LoRa can hardly confirm into square bounding boxes which leads to a significant amount of specturm being incorrectly classified as occupied, leading to poor specturm efficiency.


## 3. Novelty & Rationale

The approach we found in a paper is called Stitiching-the-Specturm, which "stitches" different signals together to create samples where signals are overlapping and affected by real-world noises and inferences.

Novel dataset generation pipeline that generate large-scale datasets that 
1. contains signals collected On The Air(OTA) and are affected by real-world conditions
2. can be completely labeled
3. low latency 

Novel custom DL algorithm for multi-label multi-class spectrum sensing based on semantic segmentation that
1. operates at the I/Q level instead of creating images
2. classifies each and every I/Q sample incoming from the ADC without creating bounding boxes, thus increasing classification accuracy significantly
3. only uses 1024 I/Q samples as input, which leads to very low inference time.

## 4. Potential Impact

Technical impacts:
1. The network is able to achieve more accuracy (7% in the paper) than U-Net in the most challenging protocols(Wi-Fi and LTE) while maintaining similarly low latency
2. The dataset generation pipeline makes the wideband spectrum sensing algorithm more accurate even with data collected from different devices, sampling rates, antennas.
3. Intersection over Union (IoU) of 96.70%; 2.6ms of latency to process 100MHz of spectrum.

Broad impacts:
1. Less amount of data needed for understanding the signal (protocal, MAC address, etc.)
2. A more accurate classification result that takes less time
3. Significantly lower the difficulty of learning about the information of sensors (their types and locations) in a smart home without prior knowledge

## 5. Challenges

1. Data must be collected Over-the-Air (OTA) so as to capture real-world channel conditions and prepare the AI in a wireless setting with real radios
2. OTA data invovles many possible combinations of time an frequency, which significantly increases the complexity  in the case of wideband spectrum sensing
3. OTA data requries large protions of spectrum without any interference from external systems
4. Training data that assumes syncronization between sensing and transmission center frequencies results in poor accuracy

## 6. Requirements for Success

What skills and resources are necessary to perform the project?

Resources:
1. SDRs (USRP N210)
2. Smart sensors that use different protocols
3. GPUs
   
Skills:
1. The usage of USRP N210 Software Defined Radio (SDR) for collecting wireless signals
2. Signal Processing skills with GNU Radio or languages like python and matlab, etc
3. Understanding of Deep Learning and RF signals

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
