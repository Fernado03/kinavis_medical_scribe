# High-Level Requirements Outline: AI Medical Scribe

## 1. Introduction

This document outlines the initial high-level requirements for the AI Medical Scribe project. It is derived from the project scope defined in `methodology.md` and the Product Vision document. This outline will serve as a basis for more detailed user stories and technical specifications.

## 2. Core Functional Areas

### 2.1. User & Encounter Management
*   **REQ-UEM-001:** System must allow for clinician identification (e.g., dropdown selection or basic login).
*   **REQ-UEM-002:** System must allow for patient selection from existing records or creation of new patient records.
*   **REQ-UEM-003:** System must create and manage unique encounters, linking them to the correct clinician and patient.
*   **REQ-UEM-004:** Patient data (especially NRIC/Passport) must be handled securely, considering Malaysian PDPA.

### 2.2. SOAP Note Creation - Subjective Section
*   **REQ-SUB-001:** Allow audio input for the Subjective section.
*   **REQ-SUB-002:** Allow direct text input for the Subjective section.
*   **REQ-SUB-003:** Transcribe uploaded audio using Google Cloud Speech-to-Text (`medical_conversation` model).
*   **REQ-SUB-004:** Generate an AI draft of the Subjective note using Google Gemini API, informed by transcribed/inputted text and `kb_subjective.json`.
*   **REQ-SUB-005:** Display the AI-generated draft to the clinician.
*   **REQ-SUB-006:** Allow clinician to edit the AI-generated draft.
*   **REQ-SUB-007:** Allow clinician to save/confirm the final Subjective note.
*   **REQ-SUB-008:** Store raw audio (path), raw text input, transcribed text, AI draft, and clinician final text in `SubjectiveNotes` table.

### 2.3. SOAP Note Creation - Objective Section
*   **REQ-OBJ-001:** Allow direct text input for the Objective section.
*   **REQ-OBJ-002:** Generate an AI draft of the Objective note using Google Gemini API, informed by inputted text and `kb_objective.json`.
*   **REQ-OBJ-003:** Display the AI-generated draft to the clinician.
*   **REQ-OBJ-004:** Allow clinician to edit the AI-generated draft.
*   **REQ-OBJ-005:** Allow clinician to save/confirm the final Objective note.
*   **REQ-OBJ-006:** Store raw text input, AI draft, and clinician final text in `ObjectiveNotes` table.

### 2.4. SOAP Note Creation - Assessment Section
*   **REQ-ASS-001:** Trigger Assessment generation after Subjective and Objective sections are confirmed.
*   **REQ-ASS-002:** Retrieve confirmed Subjective and Objective notes from the database.
*   **REQ-ASS-003:** Generate an AI draft of the Assessment using Google Gemini API, informed by S+O data and `kb_assessment.json`.
*   **REQ-ASS-004:** Display the AI-generated draft to the clinician.
*   **REQ-ASS-005:** Allow clinician to edit the AI-generated draft.
*   **REQ-ASS-006:** Allow clinician to save/confirm the final Assessment.
*   **REQ-ASS-007:** Store AI draft and clinician final text in `AssessmentNotes` table.

### 2.5. SOAP Note Creation - Plan Section
*   **REQ-PLN-001:** Allow audio input for the Plan section.
*   **REQ-PLN-002:** Allow direct text input for the Plan section.
*   **REQ-PLN-003:** Transcribe uploaded audio using Google Cloud Speech-to-Text if applicable.
*   **REQ-PLN-004:** Retrieve confirmed Assessment note from the database for context.
*   **REQ-PLN-005:** Generate an AI draft of the Plan note using Google Gemini API, informed by Assessment context, transcribed/inputted text, and `kb_plan.json`.
*   **REQ-PLN-006:** Display the AI-generated draft to the clinician.
*   **REQ-PLN-007:** Allow clinician to edit the AI-generated draft.
*   **REQ-PLN-008:** Allow clinician to save/confirm the final Plan note.
*   **REQ-PLN-009:** Store raw audio (path), raw text input, transcribed text, AI draft, and clinician final text in `PlanNotes` table.

### 2.6. Report Generation & Display
*   **REQ-REP-001:** System must be able to retrieve and assemble the complete SOAP note (all confirmed S, O, A, P sections) for a given encounter.
*   **REQ-REP-002:** System must retrieve and display relevant clinician details (full name, license number) with the report.
*   **REQ-REP-003:** System must retrieve and display relevant patient details (full name, DOB, patient ID) with the report.
*   **REQ-REP-004:** Display the complete, formatted SOAP note in the UI.
*   **REQ-REP-005:** Allow PDF export of the final SOAP report, including clinician and patient details.

### 2.7. Knowledge Base (KB) System
*   **REQ-KB-001:** Implement a system to load and query KBs (e.g., `kb_subjective.json`, `kb_objective.json`, etc.).
*   **REQ-KB-002:** KBs must store keywords, example phrases, instructions for Gemini, and examples with Malaysian context.

### 2.8. User Experience (UX) & Workflow
*   **REQ-UX-001:** Provide a single-page application interface for the S-O-A-P workflow.
*   **REQ-UX-002:** Ensure smooth navigation and clear visual cues between sections.
*   **REQ-UX-003 (Phase 4):** Implement basic smart templates (2-3 pre-defined).
*   **REQ-UX-004 (Phase 4):** Enhance review interface to clearly distinguish AI-generated text from clinician edits.
*   **REQ-UX-005 (Optional):** Allow users to go back and revise previously confirmed sections.

## 3. Non-Functional Requirements (Initial Thoughts)

*   **NFR-PERF-001:** Transcription and AI draft generation should be reasonably fast to not disrupt clinician workflow (specific timings TBD).
*   **NFR-SEC-001:** Secure handling of API keys and patient data (as per REQ-UEM-004).
*   **NFR-USAB-001:** Interface should be intuitive and require minimal training for clinicians.
*   **NFR-REL-001:** The system should reliably save data at each step.

## 4. Technical Stack (as per methodology.md)
*   HTML, CSS, JavaScript (Frontend)
*   Python (with Flask or Django for Backend)
*   MySQL (Database)
*   Google Cloud Speech-to-Text API
*   Google Gemini API

## 5. Assumptions
*   Access to Google Cloud services and necessary APIs will be available.
*   Initial KBs will be populated with sufficient examples for core functionality.
*   For the hackathon, "basic" implementations of user/patient management are acceptable.

---