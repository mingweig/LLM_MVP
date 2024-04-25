# Special Topics: Designing Smart and Healthy Systems

**Yue Sun, Mingwei Gao**

# Generating Patient Discharge Letters using Large Language Models (LLMs) - Project Report

## Introduction and Background

In the fast-paced environment of healthcare, professionals often spend up to 50% of their time on administrative tasks, including the preparation of ward round notes and patient discharge summaries. These tasks, while critical, divert time away from direct patient care and can contribute to burnout among healthcare providers. This project aims to alleviate some of this administrative burden by leveraging the capabilities of Large Language Models (LLMs) to automate the creation of discharge summaries, thereby enhancing efficiency and allowing healthcare providers to dedicate more time to patient care.

## Project Overview and Technical Details

### System Architecture

The proposed system utilizes a streamlined technical architecture incorporating advanced language models, specifically GPT-3.5 and GPT-4. The architecture is designed to handle sensitive patient data responsibly while generating accurate and concise discharge summaries. 
<img width="468" alt="image" src="https://github.com/mingweig/LLM_MVP/assets/122922442/47f77019-688a-47ce-9cd0-6ccc25d37c57">


### Key components of the system include:

* Data Integrity: The system's data entry function is specifically designed to maintain the integrity of the patient database by ensuring that only unique patient IDs are stored, thus preventing duplication of records. This is accomplished through a meticulous check where, upon the submission of new patient data, the system verifies if the patient ID already exists within the database. In case the ID is new, the data is securely added to the database, and the action is confirmed to the user with a message indicating successful addition. If an existing ID is detected, the system advises the user to recheck the submitted information to safeguard against erroneous entries. 

* Data Privacy: The initial stage involves a filtering mechanism to remove all personally identifiable information (PII), including name, date of birth, and MRN, from patient data, ensuring HIPAA compliance and protecting patient privacy. The filtered data will include relevant medical information, such as diagnosis, treatments, and ward round notes, which are essential for generating accurate discharge letters. 

* Safety Check: A crucial safety feature is implemented via a Python function with Large Language Model embedded that evaluates whether a patient meets all criteria for safe discharge based on their medical records and current health status. This function is critical in ensuring patient safety and resilience to treatment guidelines. 

* Discharge Letter Generation: Discharge summaries are generated through an API-driven (GPT3.5/4) approach using sanitized and filtered patient data. The system employs prompt engineering techniques to tailor the LLM output, ensuring it is relevant, concise, covering key aspects of the patient’s stay without including unnecessary, inaccurate, and dramatic information or details. Reviewed templates from various healthcare sources will be provided for structuring the summary to ensure it meets professional standards.

* Logging Function: To maintain transparency and facilitate debugging, a logging model tracks all inputs and outputs of the LLM throughout the discharge letter generation process.

* User Interface: A Streamlit-based UI allows for easy input (patient ID) and retrieval of patient data and generated summaries. Additional features we incorporated include input boxes for physicians to enter their name and title for displaying and addressing purposes in the generated discharge summary. If feasible, future updates may include manual editing features for real-time adjustments.

### Functionality and Features

The system features a user interface developed with Streamlit, offering straightforward functionalities for healthcare providers to input and retrieve patient data. The interface includes safety checks and caution messages, which play a critical role in ensuring that the discharge process adheres to treatment guidelines and patient safety standards.

<img width="198" alt="image" src="https://github.com/mingweig/LLM_MVP/assets/122922442/b48a3dd3-985a-4abe-8896-981f2afdb50e">

## Data Management and Safety Protocols

### Data Handling and Privacy

Our approach to data management emphasizes privacy and the secure handling of patient information. The system filters out all personally identifiable information from the data used to generate discharge summaries. This filtering ensures compliance with privacy laws and regulations, such as HIPAA, while allowing the system to utilize essential non-PII data for letter generation.

### Safety Protocols

Safety protocols are integral to the system, incorporating a Python function to assess a patient's suitability for discharge. This function checks against established treatment guidelines to ensure that only patients who meet all safety criteria are recommended for discharge.

## Testing, Validation, and Deployment Considerations

### Testing and Validation

The system was rigorously tested using sample data from various scenarios to ensure its accuracy, reliability, and adherence to healthcare standards. Different iterations of the models (GPT-3.5 Turbo and GPT-4 Turbo) were tested to compare performance and optimize the system's efficacy.

### Deployment Considerations

The integration of this system into existing healthcare infrastructures was considered with a focus on minimizing disruption and maximizing compatibility with current technologies. Detailed deployment strategies include staged rollouts and feedback loops with end users to refine functionality and usability.

## Limitations and Future Work

### Limitations

The project addresses several limitations, including the potential for model-generated errors and the system's reliance on high-quality input data.

### Technical Limitations

One primary limitation of the current system is its reliance on the quality of the input data. Incomplete or inaccurate data can lead to erroneous discharge summaries, which can affect patient care. Additionally, the model's performance is contingent upon the nuances of language in medical records, which may vary widely between institutions or regions.

### Readability of Output

During the testing phase, it was noted that some of the LLM-generated texts were difficult to read due to the excessive use of medical jargon and a lack of adaptation to common language, which may not align well with the health literacy levels of patients. This highlights a need for improvements in the system’s formatting and the logical flow of the generated summaries. Refining the prompt engineering processes to better guide the LLM's output, enhancing the natural language generation algorithms to produce more patient-friendly language, and developing more effective template structures could significantly mitigate these issues. These improvements would make the summaries more accessible and comprehensible to patients, thereby improving communication and patient understanding of their care instructions.

### Data Extraction Complexity

The diversity and complexity of electronic health record (EHR) systems present significant challenges for the data extraction pipeline. Ensuring that diverse medical records are consistently and accurately parsed into a standardized format suitable for LLM processing is essential for the integrity and applicability of the generated discharge summaries. This standardization process is crucial, as inconsistencies or errors in data formatting could compromise the quality and reliability of the output. Without robust mechanisms to manage these variations in our project development, we could not ensure the generalizability of our product across different patient data systems, which is vital for broader adoption and effectiveness.

### Future Work

Future enhancements will focus on integrating real-time editing capabilities, improving the system's adaptability to new medical guidelines, and extending its application to other administrative tasks such as medication reconciliation and patient admission processes. Additionally, incorporating feedback loops and health literacy tools will further refine the system's utility and user-friendliness.

### Enhancement in Model Training

Future iterations could explore more sophisticated models and training datasets to improve the system's understanding of complex medical terminology and scenarios. This could help in generating more accurate and clinically relevant summaries.

### Expansion to Other Administrative Tasks

There is potential to expand the system’s capabilities to other areas, such as patient admission, medication reconciliation, and follow-up appointment scheduling. This would provide a more comprehensive suite of tools for healthcare professionals, further reducing administrative burdens.

### Ethics and AI in Healthcare

Further research into the ethical implications of AI in healthcare is crucial. Addressing issues such as bias in AI algorithms, transparency in AI decision-making processes, and obtaining patient consent for the use of their data in AI training is imperative. The development of guidelines and standards for the ethical use of AI in healthcare settings is essential to ensure these systems are implemented responsibly. Ethical deployment of AI systems must focus on preventing the perpetuation of existing biases or the introduction of new biases in clinical decision-making. It is also vital to maintain patient privacy and security, particularly when managing sensitive health information. Continuous monitoring and evaluation are necessary to ensure AI systems comply with ethical standards and regulations. Additionally, mechanisms must be established to ensure healthcare providers rigorously review AI-generated documents before integrating them into their workflows, safeguarding against potential errors and ensuring the reliability of AI-supported healthcare decisions.

## Conclusion

The project represents a significant step forward in integrating AI with healthcare administration. By automating the generation of discharge summaries, it offers the potential to significantly reduce the time healthcare professionals spend on paperwork, thus allowing them more time for patient care. However, the ethical considerations of AI deployment in healthcare—such as data privacy, algorithmic transparency, and the prevention of bias—need careful attention to ensure that the technology not only enhances efficiency but also supports fair and equitable healthcare practices.
