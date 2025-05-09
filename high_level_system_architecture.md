# Project XXX: High-Level System Architecture


## Introduction / Overview 🎯

*   **What is this document about?** This document provides a high-level overview of the system architecture for Project XXX, the intelligent medical scribe assistant.
*   **What purpose does it serve?** It illustrates the main components of the system and their interactions, serving as a basis for more detailed design.
*   **Who is the intended audience?** The project team, architects, and developers.

## Section 1: Component Diagram (Mermaid) 📊

The following diagram illustrates the conceptual architecture based on the project deck:

```mermaid
graph TD
    subgraph User_Interaction_Layer
        UI[Frontend Web Application MVP]
    end

    subgraph Application_Backend_Layer [Application Backend (GCP)]
        InputMod[Input Module API]
        ASRMod[Speech Recognition (ASR) Module API]
        NLPMod[NLP/LLM Module API]
        OutputMod[Output Module API]
        DB[(Database - User Data, Notes Drafts - TBD)]
    end

    subgraph Google_Cloud_AI_Services [Google Cloud AI Services]
        GCPSpeech[Google Cloud Speech-to-Text API <br/> (medical_conversation model)]
        GeminiAPI[Google Gemini API <br/> (e.g., Gemini 1.5 Pro via Vertex AI)]
    end

    subgraph External_Systems [Future Integrations]
        EHR[EHR Systems <br/> (via FHIR)]
    end

    %% Data Flow & Interactions
    User([Clinician User]) -->|1. Uploads Audio| UI
    UI -->|2. Sends Audio to Backend| InputMod
    InputMod -->|3. Passes Audio to ASR| ASRMod
    ASRMod -->|4. Calls GCP Speech API| GCPSpeech
    GCPSpeech -->|5. Returns Transcript| ASRMod
    ASRMod -->|6. Passes Transcript to NLP| NLPMod
    NLPMod -->|7. Calls Gemini API with Prompt| GeminiAPI
    GeminiAPI -->|8. Returns Structured SOAP Note (JSON)| NLPMod
    NLPMod -->|9. Passes SOAP Note to Output| OutputMod
    OutputMod -->|10. Stores Note Draft (Optional)| DB
    OutputMod -->|11. Sends Note to Frontend| UI
    UI -->|12. Displays Transcript & SOAP Note| User
    User -->|13. Reviews & Approves (Conceptual)| UI

    %% Future
    OutputMod -.->|Future: FHIR Output| EHR
```

## Section 2: Component Descriptions 📝

*   **Frontend Web Application (UI):**
    *   **Description:** The user interface for clinicians. For the MVP, this will be a web-based application.
    *   **Responsibilities:** Allows users to upload audio files, view the ASR transcript, and view/review the AI-generated SOAP note.
    *   **Technologies (TBD):** Standard web technologies (e.g., React, Vue, Angular, or simpler HTML/CSS/JS for MVP).
*   **Input Module API:**
    *   **Description:** Backend component responsible for receiving audio input.
    *   **Responsibilities:** Handles audio file uploads from the frontend, performs initial validation (e.g., file type, size), and potentially stores the audio temporarily or passes it directly to the ASR module.
    *   **Technologies (TBD):** Backend language/framework (e.g., Python/FastAPI, Node.js/Express).
*   **Speech Recognition (ASR) Module API:**
    *   **Description:** Backend component that orchestrates the speech-to-text conversion.
    *   **Responsibilities:** Receives audio data (or a reference to it) from the Input Module, interacts with the Google Cloud Speech-to-Text API, and retrieves the transcript.
    *   **Key Dependency:** Google Cloud Speech-to-Text API (`medical_conversation` model).
*   **NLP/LLM Module API:**
    *   **Description:** Backend component responsible for generating the structured SOAP note from the transcript.
    *   **Responsibilities:** Receives the transcript from the ASR Module, applies sophisticated prompt engineering, interacts with the Google Gemini API, and retrieves the structured JSON SOAP note.
    *   **Key Dependency:** Google Gemini API (e.g., Gemini 1.5 Pro via Vertex AI).
*   **Output Module API:**
    *   **Description:** Backend component that handles the generated SOAP note.
    *   **Responsibilities:** Receives the JSON SOAP note from the NLP/LLM Module, potentially stores it in a database, and makes it available to the frontend for display. In future phases, this module will handle formatting for EHR integration (e.g., FHIR).
*   **Database (DB - TBD):**
    *   **Description:** Persistent storage for user information, uploaded audio metadata (optional), transcripts (optional), and generated SOAP note drafts.
    *   **Technologies (TBD):** A relational or NoSQL database on GCP (e.g., Cloud SQL, Firestore). The exact need and choice will be determined. For MVP, this might be minimal or even file-based storage for simplicity if full persistence isn't a hard requirement.
*   **Google Cloud Speech-to-Text API:**
    *   **Description:** External GCP service providing speech recognition capabilities, specifically using the `medical_conversation` model.
*   **Google Gemini API:**
    *   **Description:** External GCP service (via Vertex AI) providing advanced large language model capabilities for natural language understanding and generation.
*   **EHR Systems (Future):**
    *   **Description:** External Electronic Health Record systems that "XXX" aims to integrate with in the future, likely using FHIR standards.

## Section 3: Data Flow Summary ➡️

1.  The clinician uploads an audio file via the **Frontend Web Application**.
2.  The audio is sent to the **Input Module API** in the backend.
3.  The **Input Module** passes the audio to the **ASR Module API**.
4.  The **ASR Module** calls the **Google Cloud Speech-to-Text API** to get a transcript.
5.  The transcript is passed to the **NLP/LLM Module API**.
6.  The **NLP/LLM Module** uses prompt engineering to instruct the **Google Gemini API** to generate a structured JSON SOAP note from the transcript.
7.  The generated SOAP note is passed to the **Output Module API**.
8.  The **Output Module** (optionally) stores the note and sends it to the **Frontend Web Application** for the clinician to review.
9.  (Future) The **Output Module** will facilitate sending data to **EHR Systems**.

## Summary / Key Takeaways 💡

The proposed architecture is modular and leverages powerful Google Cloud AI services for its core functionalities. The MVP will focus on a web-based frontend and backend APIs to manage the workflow from audio upload to SOAP note generation. Future development will focus on enhancing features, scalability, and EHR integration.
