# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract

Our project uses USRP N210 Hardware Drives (UHD) and GNU Radio to collect signals being transmitted by differnt smart home sensors using different communication protocols such as WiFi, Zigbee, Z-Wave, etc. We use a spectrum sensing model called Stitching-the-Spectrum to identify and locate those sensors without prior knowledge of their exact locations or functions. We plan to develop a system that autonomously discovers and identifies wireless sensors in a smart home by analyzing RF signals, MAC addresses and communication protocols. Eventually we will localize those sensors by applying geometry with the difference between Received Signal Strength Indicator we receive from differnt locations using multiple USRP N210 as the receivers.

# 1. Introduction

* Motivation & Objective:
  Many smart homes are equipped with sensors that collect wireless data about the environment and how people interact with their spaces. Yet, much of this information isn’t fully utilized to understand daily activities and routines. By combining this sensor data with common knowledge about how devices like door, motion, and multi sensors are typically used, we can gain deeper insight into occupants’ behaviors. Our objective is to develop a system that uses advanced AI models to interpret these wireless signals and access the sensor’s location. This will enhance the smart home experience, making it more responsive and intuitive to the needs of its users.
  
* State of the Art & Its Limitations:
  You Only Look Once (YOLO) is a current widely used object detection model that divides the input (usually an image) into grids. For signal classification, YOLO divide a signal into fixed-length windows, or bounding boxes.

Limitations of You Only Look Once (YOLO):

This approach requires the creation of an image out of in-phase/quadrature (I/Q) samples, incurring additional latency.
Being a viable method for computer vision tasks, YOLO does not achieve the level of resolution required for wireless signals.
Modern wireless signals such as 5G and LoRa can hardly confirm into square bounding boxes which leads to a significant amount of spectrum being incorrectly classified as occupied, leading to poor spectrum efficiency.

* Novelty & Rationale: What is new in your approach and why do you think it will be successful?
  The approach we found in a paper is called Stitching-the-Spectrum, which “stitches” different signals together to create samples where signals are overlapping and affected by real-world noises and inferences.

Novel dataset generation pipeline that generates large-scale datasets that

contains signals collected Over-the-Air (OTA) and are affected by real-world conditions
can be completely labeled
low latency
Novel custom DL algorithm for multi-label multi-class spectrum sensing based on semantic segmentation that

operates at the I/Q level instead of creating images
classifies each I/Q sample incoming from the ADC without creating bounding boxes, thus increasing classification accuracy significantly
only uses 1024 I/Q samples as input, which leads to very low inference time.

* Potential Impact:
  Technical impacts:

The network is able to achieve more accuracy (7% in the paper) than U-Net in the most challenging protocols (Wi-Fi and LTE) while maintaining similarly low latency
The dataset generation pipeline makes the wideband spectrum sensing algorithm more accurate even with data collected from different devices, sampling rates, antennas.
Intersection over Union (IoU) of 96.70%; 2.6ms of latency to process 100MHz of spectrum.
Broad impacts:

Less amount of data needed for understanding the signal (protocol, MAC address, etc.)
A more accurate classification result that takes less time
Significantly lower the difficulty of learning about the information of sensors (their types and locations) in a smart home without prior knowledge

* Challenges:
  Data must be collected Over-the-Air (OTA) to capture real-world channel conditions and prepare the AI in a wireless setting with real radios
OTA data involves many possible combinations of time an frequency, which significantly increases the complexity in the case of wideband spectrum sensing
OTA data requires large portions of spectrum without any interference from external systems
Training data that assumes synchronization between sensing and transmission center frequencies results in poor accuracy

* Requirements for Success:
Resources:

SDRs (USRP N210)
Smart sensors that use different protocols
GPUs
Skills:

The usage of USRP N210 Software Defined Radio (SDR) for collecting wireless signals
Signal Processing skills with GNU Radio or languages like python and MATLAB, etc.
Understanding of Deep Learning and RF signals

* Metrics of Success:
 For protocol classification:

Intersection of Union (IoU): Formula: Area of Intersection / Area of Union to indicate the quality of math between the predicted and ground truth boxes. (1 means perfect overlap and 0 means no overlap at all)
For localization:

The absolute value of difference between the calculated distance and the actual distance. (The smaller the difference the higher of localization accuracy)

# 2. Related Work

# 3. Technical Approach

# 4. Evaluation and Results

# 5. Discussion and Conclusions

# 6. References
