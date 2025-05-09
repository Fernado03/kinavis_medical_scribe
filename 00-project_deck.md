## **Project Deck: XXX by KinaVis**

**Team: KinaVis**

### **1\. Problem Statement**

Clinician burnout, driven significantly by the overwhelming burden of medical documentation, is a critical issue in healthcare globally and in Malaysia. Studies indicate that physicians can spend up to two hours on Electronic Health Record (EHR) note-taking for every one hour of direct patient care, and nurses may dedicate around 60% of their work hours to paperwork. In Malaysia, this problem is particularly acute, with reports showing approximately 26.5% of junior doctors experiencing burnout and 51% of urban hospital doctors exhibiting burnout symptoms. This excessive administrative load not only leads to clinician exhaustion and reduced job satisfaction but also detracts from the time available for patient interaction, potentially impacting the quality of care.

### **2\. Solution Overview**

"XXX" by Team KinaVis is an intelligent medical scribe assistant designed to alleviate the documentation burden on healthcare professionals. Our solution leverages advanced Artificial Intelligence to listen to clinician-patient encounters and automatically generate accurate, structured clinical notes in the widely-used SOAP (Subjective, Objective, Assessment, Plan) format. By automating this time-consuming process, "XXX" aims to significantly reduce administrative workload, allowing clinicians to reclaim valuable time, focus more on patient care, and mitigate the risks of burnout.

### **3\. Key Features of Solution**

* **AI-Powered Transcription & Note Generation:** Utilizes Google Cloud Speech-to-Text (medical\_conversation model) for high-fidelity transcription of medical dialogues and Google's Gemini API (e.g., Gemini 1.5 Pro) with sophisticated prompt engineering to generate clinically relevant and coherent SOAP notes.  
* **Structured Output for EHR Integration:** Produces notes in a standardized JSON format, laying the groundwork for seamless integration with existing Electronic Health Record (EHR) systems using interoperability standards like FHIR.  
* **Clinician-in-the-Loop Design:** Emphasizes that AI-generated notes are drafts requiring review and approval by the clinician, ensuring accuracy, accountability, and patient safety.  
* **Adaptable to Malaysian Healthcare Needs:** While the MVP focuses on English, "XXX" is designed with a roadmap for future multilingual support, including Bahasa Melayu, Mandarin, and Tamil, to cater to Malaysia's diverse linguistic landscape.  
* **Intuitive User Interface:** Features a simple, clean, and user-friendly interface (demonstrated in the MVP) for ease of adoption and minimal disruption to clinical workflows.

### **4\. Technical Architecture**

"XXX" employs a modular, cloud-based architecture:

* **Input Module:** Accepts audio input of clinician-patient dialogues (pre-recorded for the MVP, with plans for live recording).  
* **Speech Recognition (ASR) Module:** Leverages Google Cloud Speech-to-Text API with its medical\_conversation model to accurately convert spoken dialogue into text, capturing medical terminology effectively.  
* **Natural Language Processing (NLP/LLM) Module:** The transcribed text is processed by Google's Gemini API (e.g., Gemini 1.5 Pro). Custom-engineered prompts guide the LLM to analyze the transcript, extract key clinical information, and structure it into a JSON-formatted SOAP note.  
* **Output Module:** Delivers the structured SOAP note in JSON format.  
* **Frontend Interface (MVP):** A web-based application, allowing users to upload audio, view the transcript, and see the generated clinical note.  
* **Deployment (Conceptual):** Designed for cloud deployment, primarily utilizing Google Cloud Platform services for scalability and reliability.

### **5\. AI/LLM Integration**

The core intelligence of "XXX" lies in its strategic integration of specialized AI and LLM technologies:

* **ASR Integration:** We utilize Google Cloud Speech-to-Text, specifically its medical\_conversation model. This choice is driven by its optimization for medical dialogues, enhancing accuracy in recognizing clinical terms, drug names, and procedures compared to general-purpose ASR.  
* **LLM Integration:** Google's Gemini API (e.g., Gemini 1.5 Pro) serves as the NLP engine. Its advanced capabilities in understanding context, following complex instructions, and generating coherent, structured text are pivotal. The LLM is tasked with transforming the raw ASR transcript into a clinically meaningful and well-organized SOAP note.  
* **Prompt Engineering:** A critical component is our sophisticated prompt engineering strategy. Prompts are meticulously designed to instruct the Gemini API to identify and extract subjective complaints, objective findings, clinical assessments, and treatment plans from the dialogue. The prompts also enforce the generation of output in a specific JSON schema and include instructions to minimize errors and hallucinations, such as explicitly stating when information for a particular section is not present in the conversation.  
* **Data Flow:** The workflow is sequential: audio input is transcribed by the ASR module; this text transcript is then fed to the LLM module, which, guided by our prompts, generates the structured JSON SOAP note.

### **6\. Market Potential**

The market for AI-driven healthcare solutions is experiencing explosive growth. Globally, the AI healthcare market is projected to reach hundreds of billions of dollars (e.g., USD 613.8 billion by 2034), with the AI-assisted medical documentation and scribe niche itself forecasted to become a multi-billion dollar segment (e.g., USD 45.2 billion by 2026). The Asia-Pacific region, including Malaysia, is a key area of this expansion as healthcare providers increasingly adopt digital technologies. Malaysia's digital health market alone is projected to reach approximately USD 613 million by 2025\.

Currently, the Malaysian market for specialized AI medical scribes is underserved, with no single international vendor holding a dominant position. This presents a significant opportunity for "XXX" to establish itself by offering a solution tailored to local needs, including future multilingual capabilities. The target users include public and private hospitals, specialist clinics, and general practitioners across Malaysia who are seeking to improve efficiency and reduce the administrative burden.

### **7\. Growth Strategy**

Our growth strategy for "XXX" is envisioned in phased milestones:

* **Phase 1: MVP Development & Local Validation (Hackathon & Post-Hackathon):** Successfully develop and demonstrate the core MVP. Gather crucial feedback by conducting pilot tests with a small group of clinicians in local Malaysian clinics or primary care settings.  
* **Phase 2: Product Enhancement & Pilot Expansion:** Based on initial feedback, iteratively refine features, improve accuracy, and develop robust EHR integration capabilities, prioritizing FHIR compatibility. Begin development of multilingual support, starting with Bahasa Melayu. Expand pilot programs to more diverse clinical settings.  
* **Phase 3: Market Entry & Strategic Partnerships:** Officially launch "XXX" targeting small to medium-sized private clinics in Malaysia, offering a competitive and accessible solution. Concurrently, seek partnerships with local EHR vendors and healthcare IT providers to facilitate wider adoption and integration.  
* **Phase 4: Scaling & Regional Expansion:** As "XXX" gains traction and demonstrates value in the Malaysian market, explore opportunities for expansion into other Southeast Asian countries with similar healthcare challenges and linguistic diversity.

### **8\. Business Model**

"XXX" will operate on a Software-as-a-Service (SaaS) subscription model, designed to be accessible and provide clear value:

* **Subscription Tiers:** We propose a tiered pricing structure to cater to different user needs:  
  * **Individual Clinician Plan:** A basic, affordable monthly subscription for solo practitioners or small practices.  
  * **Clinic/Enterprise Plan:** Scalable plans for multi-user clinics or hospital departments, offering additional features like administrative dashboards, enhanced support, and potentially higher usage limits.  
* **Value Proposition:** The primary value delivered is significant time savings for clinicians, leading to reduced burnout, increased capacity for patient care, and improved documentation quality. This translates to enhanced operational efficiency for healthcare providers.  
* **Competitive Positioning:** Compared to some established international AI scribe solutions which can be prohibitively expensive (e.g., Nuance DAX often cited around \~$600/clinician/month), "XXX" aims to offer a more competitively priced and locally attuned solution for the Malaysian market, without compromising on core functionality and accuracy.

### **9\. Impact & Usefulness**

The adoption of "XXX" promises substantial positive impacts for clinicians, patients, and the broader Malaysian healthcare system:

* **For Clinicians:** "XXX" directly addresses the critical issue of documentation burden. By automating note generation, it can save clinicians several hours per day (as evidenced by studies like Kaiser Permanente's, which reported saving 1,794 physician workdays in one year with AI scribes). This leads to a significant reduction in stress and burnout (studies show up to 60% fewer burnout reports), enhances job satisfaction, and allows for more meaningful face-to-face interaction with patients (84% of clinicians in one study reported improved patient interactions).  
* **For Healthcare Providers & Systems:** Implementation of "XXX" can lead to improved operational efficiency, more consistent and complete medical records, and better resource allocation. This can contribute to a higher standard of care and better health outcomes.  
* **For Patients:** Patients benefit from more attentive and less rushed clinicians. Clearer, more comprehensive medical notes can also lead to better continuity of care and fewer medical errors.  
* **Specific Usefulness for Malaysia:** Beyond the universal benefits, "XXX" aims to be particularly useful in the Malaysian context by addressing local clinician burnout rates. The planned multilingual support will ensure accessibility and usability for a wider range of clinicians and patient encounters in Malaysia's diverse society, making it a more inclusive and effective tool.
