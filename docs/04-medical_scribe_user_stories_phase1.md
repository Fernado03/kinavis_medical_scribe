# User Stories (Phase 1): AI Medical Scribe

This document outlines initial user stories for Phase 1 of the AI Medical Scribe project, focusing on core functionality related to clinician identification, patient management, and the Subjective section of the SOAP note.

## Epics

*   **Epic 1: Encounter Setup & Initiation**
*   **Epic 2: Subjective Note Generation**

## User Stories for Phase 1

---

**User Story 1.1 (Epic 1)**

*   **As a** Clinician,
*   **I want to** be able to select my identity from a pre-populated list,
*   **So that** the system knows who is creating the SOAP note for the current encounter.
*   **Acceptance Criteria:**
    *   A dropdown or similar simple selection mechanism is present on the initial screen.
    *   The list of clinicians is populated from the `Clinicians` table in the database.
    *   Selecting a clinician stores their `clinician_id` for association with the new encounter.
    *   (Hackathon Scope: No login/password required for Phase 1, simple selection is sufficient).
*   **Related Requirements:** REQ-UEM-001

---

**User Story 1.2 (Epic 1)**

*   **As a** Clinician,
*   **I want to** search for an existing patient by their name or ID,
*   **So that** I can quickly select them for the current encounter.
*   **Acceptance Criteria:**
    *   A search input field is available for patient lookup.
    *   Search queries the `Patients` table.
    *   Matching patient(s) are displayed for selection.
    *   Selecting a patient stores their `patient_id` for association with the new encounter.
*   **Related Requirements:** REQ-UEM-002

---

**User Story 1.3 (Epic 1)**

*   **As a** Clinician,
*   **I want to** be able to add a new patient if they are not found in the system,
*   **So that** I can proceed with the encounter for new patients.
*   **Acceptance Criteria:**
    *   A simple form is available to input new patient details (Full Name, DOB, Gender, NRIC/Passport, Contact, Address).
    *   Submitting the form creates a new record in the `Patients` table.
    *   The newly created patient is automatically selected for the current encounter, and their `patient_id` is stored.
    *   NRIC/Passport number is handled with consideration for security (encryption placeholder for hackathon).
*   **Related Requirements:** REQ-UEM-002, REQ-UEM-004

---

**User Story 1.4 (Epic 1)**

*   **As a** System,
*   **I want to** create a new encounter record when a clinician starts a new SOAP note,
*   **So that** all subsequent note sections (S, O, A, P) can be linked to this specific patient visit and clinician.
*   **Acceptance Criteria:**
    *   A new record is created in the `Encounters` table when a patient is selected/created and the clinician is identified.
    *   The `encounter_id` is generated and available.
    *   The `patient_id` and `clinician_id` are correctly associated with the encounter.
    *   The `encounter_date` is set to the current date.
    *   The `status` is initially set to 'in-progress'.
*   **Related Requirements:** REQ-UEM-003

---

**User Story 2.1 (Epic 2 - Subjective Note Generation)**

*   **As a** Clinician,
*   **I want to** be able to upload an audio recording of the patient's subjective complaints,
*   **So that** the system can transcribe it for me.
*   **Acceptance Criteria:**
    *   UI provides an option to upload an audio file.
    *   Uploaded audio is sent to the backend.
    *   Backend transcribes the audio using Google Cloud Speech-to-Text.
    *   The path to the raw audio and the transcribed text are saved in the `SubjectiveNotes` table, linked to the current `encounter_id`.
*   **Related Requirements:** REQ-SUB-001, REQ-SUB-003, REQ-SUB-008

---

**User Story 2.2 (Epic 2 - Subjective Note Generation)**

*   **As a** Clinician,
*   **I want to** be able to type in the patient's subjective complaints directly as text,
*   **So that** I have an alternative to audio input.
*   **Acceptance Criteria:**
    *   UI provides a text area for direct input of subjective notes.
    *   Entered text is sent to the backend.
    *   The raw text input is saved in the `SubjectiveNotes` table, linked to the current `encounter_id`.
*   **Related Requirements:** REQ-SUB-002, REQ-SUB-008

---

**User Story 2.3 (Epic 2 - Subjective Note Generation)**

*   **As a** Clinician,
*   **I want** the system to generate an AI draft of the Subjective section based on my transcribed audio or text input and relevant medical knowledge,
*   **So that** I have a structured starting point for my note.
*   **Acceptance Criteria:**
    *   Backend uses Google Gemini API and `kb_subjective.json` to process the transcribed/inputted text.
    *   An AI-generated draft of the Subjective note is produced.
    *   The AI draft is saved to the `SubjectiveNotes` table.
    *   The AI draft is displayed on the frontend for review.
*   **Related Requirements:** REQ-SUB-004, REQ-SUB-005, REQ-SUB-008, REQ-KB-001, REQ-KB-002

---

**User Story 2.4 (Epic 2 - Subjective Note Generation)**

*   **As a** Clinician,
*   **I want to** be able to easily edit the AI-generated Subjective draft,
*   **So that** I can correct inaccuracies or add further details.
*   **Acceptance Criteria:**
    *   The displayed AI draft is editable in a text area.
    *   Changes made by the clinician are captured.
*   **Related Requirements:** REQ-SUB-006

---

**User Story 2.5 (Epic 2 - Subjective Note Generation)**

*   **As a** Clinician,
*   **I want to** be able to save and confirm my final version of the Subjective note,
*   **So that** it is stored accurately and I can proceed to the Objective section.
*   **Acceptance Criteria:**
    *   A "Save/Confirm Subjective" button is available.
    *   Clicking the button updates the `clinician_final_text` field in the `SubjectiveNotes` table with the edited content.
    *   The system provides a clear indication that the Subjective section is confirmed.
*   **Related Requirements:** REQ-SUB-007, REQ-SUB-008

---