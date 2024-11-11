# Project Proposal

## 1. Motivation & Objective
Many smart homes are equipped with sensors that collect wireless data about the environment and how people interact with their spaces. Yet, much of this information isn't fully utilized to understand daily activities and routines. By combining this sensor data with common knowledge about how devices like door, motion, and multi sensors are typically used, we can gain deeper insights into occupants' behaviors. Our objective is to develop a system that uses advanced AI models to interpret these wireless signals and access the sensor's location. This will enhance the smart home experience, making it more responsive and intuitive to the needs of its users.

## 2. State of the Art & Its Limitations

How is it done today, and what are the limits of current practice?

Traditional sensing methods such as device fingerprinting, protocol-based identification  rely on image-based models that use bounding boxes with poor alignment that would cause high latency and low accuracy.  Moreover, these techniques usually require large datasets and assumptions that do not really reflect the real life conditions

## 3. Novelty & Rationale

What is new in your approach and why do you think it will be successful?

Stitching-the-Spectrum is a signal classification approach initiated by Uvaydov, Daniel and Zhang, etl. It creates a diverse training sample by stitching signals together. Later, the stitched signal would be fed into a U-Net-based segmentation model to handle the wideband signal, allowing each signal to be classified into a certain protocol class. We believe this approach to be useful in a smart home context because it has a better classification and localization accuracy than the traditional methods. It can handle multiple overlapping signals without prior knowledge of the real world such as the type or location of the sensor.

## 4. Potential Impact

If the project is successful, what difference will it make, both technically and broadly?

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
