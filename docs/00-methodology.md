**Project:** AI Medical Scribe (SOAP Note Generator)
**Team:** KinaVis
**Duration:** 1 Week
**Tech Stack:** HTML, CSS, JavaScript, Python (with Flask or Django), MySQL, Google Cloud Speech-to-Text, Google Gemini API.
**Location Context:** Malaysia
**Current Date:** Friday, May 9, 2025

---

**Phase 1: Foundation, User Management & Core Subjective Functionality**

* **Detailed Requirements, UX/UI Design, and Technical Architecture:**
    * Finalize the end-to-end clinician workflow for the single-page S-O-A-P interface, including how a clinician is identified and how a patient is selected/created for an encounter.
    * Create detailed wireframes or mockups for all UI states (login (optional), patient selection/creation, Subjective input, Objective input, AI suggestion display, editing mode, Assessment display, Plan input, final report view).
    * Define user interaction patterns (e.g., how sections are confirmed, how navigation occurs).
    * Outline error handling strategies and user feedback mechanisms.
    * Confirm choices for specific Python libraries.
* **Database Schema Design & Implementation (MySQL):**
    * Define and create tables:
        * **`Clinicians` Table:**
            * `clinician_id` (PK)
            * `full_name`, `license_number` (e.g., MMC number), `specialty`, `email` (for login, unique), `password_hash` (if implementing login)
            * `created_at`, `updated_at`
        * **`Patients` Table:**
            * `patient_id` (PK)
            * `full_name`, `date_of_birth`, `gender`, `nric_passport_number` (ensure security/encryption as per Malaysian PDPA), `contact_number`, `address`
            * `created_at`, `updated_at`
        * **`Encounters` Table:**
            * `encounter_id` (PK)
            * `patient_id` (FK referencing `Patients.patient_id`)
            * `clinician_id` (FK referencing `Clinicians.clinician_id`)
            * `encounter_date`, `status` (e.g., ENUM('in-progress', 'completed'))
            * `created_at`, `updated_at`
        * `SubjectiveNotes` (subjective\_id PK, encounter\_id FK, raw\_audio\_path, raw\_text\_input, transcribed\_text, ai\_generated\_draft, clinician\_final\_text, created\_at, updated\_at).
        * `ObjectiveNotes` (objective\_id PK, encounter\_id FK, raw\_text\_input, ai\_generated\_draft, clinician\_final\_text, created\_at, updated\_at).
        * `AssessmentNotes` (assessment\_id PK, encounter\_id FK, ai\_generated\_draft, clinician\_final\_text, created\_at, updated\_at).
        * `PlanNotes` (plan\_id PK, encounter\_id FK, raw\_audio\_path, raw\_text\_input, transcribed\_text, ai\_generated\_draft, clinician\_final\_text, created\_at, updated\_at).
    * Establish all foreign key relationships.
* **Basic Clinician & Patient Management Implementation:**
    * **Frontend:**
        * Implement a basic mechanism to identify the clinician (e.g., simple dropdown to select from pre-populated `Clinicians` for the hackathon, or a very basic login if time permits).
        * Implement a basic mechanism for patient selection/creation at the start of an encounter (e.g., search existing patients by ID/name, or a simple form to add a new patient to the `Patients` table).
    * **Backend (Python):**
        * Logic to handle clinician identification and patient selection/creation, ensuring the `clinician_id` and `patient_id` are available when a new encounter is created.
* **Knowledge Base (KB) Framework & Initial Content (v0.1):**
    * Establish the format for KBs (e.g., JSON files: `kb_subjective.json`, etc.).
    * Develop a Python module/functions to load and query these KBs.
    * Populate each KB with initial entries (5-10 per section) including keywords, example phrases, instructions for Gemini, and examples with Malaysian context.
* **Environment Setup & "Hello World" Connectivity:**
    * Initialize Git repository.
    * Set up Python virtual environment, install backend framework and libraries.
    * Create basic HTML/CSS/JavaScript structure.
    * Implement basic API endpoint and test frontend-to-backend communication.
    * Test Python-to-MySQL connection.
    * Configure Google Cloud project, enable APIs, manage API keys securely, and test basic API calls.
* **Subjective Section - Core Implementation:**
    * **Frontend:** Develop UI for audio upload/text input. JavaScript to capture input and send to backend.
    * **Backend (Python):**
        * Create API endpoint for Subjective data processing.
        * Implement audio transcription (Google Cloud Speech-to-Text, `medical_conversation` model).
        * Develop initial prompt engineering for Gemini (Subjective), integrating `kb_subjective.json`.
        * Call Gemini API.
        * Save raw input, transcribed text, AI draft to `SubjectiveNotes`, linked to a new `Encounters` record (which includes the `patient_id` and `clinician_id`).
        * Return AI draft to frontend.
    * **Frontend:** Display AI draft, allow editing, implement "Save/Confirm Subjective" (updating `clinician_final_text`).

**Phase 2: Objective & Assessment Section Development**

* **Objective Section - Full Implementation:**
    * **Frontend:** Develop UI for text input. JavaScript to send data.
    * **Backend (Python):** API endpoint for Objective data. Prompt engineering for Gemini (Objective) using `kb_objective.json`. Call Gemini. Save to `ObjectiveNotes`. Return AI draft.
    * **Frontend:** Display AI draft, allow editing, implement "Save/Confirm Objective."
* **Assessment Section - Core AI Logic, Display, and Editing:**
    * **Backend (Python):** API endpoint triggered after S & O confirmation. Retrieve confirmed S & O from MySQL. Develop advanced prompt engineering for Gemini (Assessment) using S+O data and `kb_assessment.json`. Call Gemini. Save AI draft to `AssessmentNotes`. Return AI draft.
    * **Frontend:** Trigger Assessment generation. Display AI draft, allow editing, implement "Save/Confirm Assessment."

**Phase 3: Plan Section, Report Generation & Workflow Integration**

* **Plan Section - Full Implementation:**
    * **Frontend:** UI for audio upload/text input.
    * **Backend (Python):** API endpoint for Plan data. Transcribe audio if applicable. Retrieve confirmed Assessment for context. Develop prompt engineering for Gemini (Plan) using Assessment context and `kb_plan.json`. Call Gemini. Save to `PlanNotes`. Return AI draft.
    * **Frontend:** Display AI draft, allow editing, implement "Save/Confirm Plan."
* **Full SOAP Report Generation and Display (with User Info):**
    * **Backend (Python):**
        * Create API endpoint to retrieve the complete SOAP note for an encounter.
        * Fetch all confirmed `clinician_final_text` fields (S, O, A, P).
        * From the `Encounters` table, get the `clinician_id` and `patient_id`.
        * Query `Clinicians` table for the clinician's details (e.g., full name, license number).
        * Query `Patients` table for the patient's details (e.g., full name, DOB, patient ID).
        * Structure all this data for display.
    * **Frontend:**
        * Implement "View Full Report" functionality.
        * Display the complete, formatted SOAP note, clearly including the fetched patient and clinician details at the top or bottom of the report, along with the S, O, A, P content.
* **End-to-End Workflow & Navigation:**
    * Ensure smooth transitions between sections and the final report view.
    * Implement clear visual cues.
    * Consider allowing users to (optionally) go back and revise previous confirmed sections.

**Phase 4: Enhancements, Malaysian Context Integration & Testing**

* **UX Enhancements Implementation:**
    * **Basic Smart Templates:** Implement 2-3 pre-defined templates.
    * **Enhanced Review Interface:** Clearly distinguish AI-generated text from clinician edits.
* **Knowledge Base Refinement & Malaysian Context Deep Dive:**
    * Iterate on and expand all KBs with more comprehensive examples (Malaysian medical terms, local conditions).
    * Refine Gemini prompts for better handling of Malaysian contextual nuances, negations, and uncertainties.
* **Simple Feedback Capture for AI Improvement:**
    * Implement backend logic to log original AI drafts alongside `clinician_final_text` upon edits.
* **Comprehensive Testing:**
    * Unit tests, integration tests, end-to-end scenario testing (including scenarios with clinician/patient data), and informal usability testing.

**Phase 5: Final Polishing, PDF Export (with User Info) & Presentation Readiness**

* **UI/UX Polishing:**
    * Refine CSS for a professional and clean look and feel.
    * Ensure the application is reasonably responsive on different screen sizes (if web-based).
    * Improve clarity of all buttons, labels, and instructions.
* **PDF Export Functionality for SOAP Report (with User Info):**
    * Integrate a Python PDF generation library.
    * **Crucially:** Ensure the PDF generation logic queries and includes the clinician's full name (and optionally license number) and the patient's full name (and optionally patient ID, DOB) from the `Clinicians` and `Patients` tables, along with the encounter date and SOAP content. The PDF should look like an official clinical note.
    * Add a "Download PDF Report" button.
* **Final Bug Fixing & Performance Tweaks:**
    * Address all critical bugs identified during testing.
    * Optimize any slow backend processes or database queries if noticeable.
* **Demo Script & Presentation Preparation:**
    * Prepare a compelling demonstration script showcasing various scenarios, including:
        * Audio input and transcription.
        * AI assistance at each S, O, A, P stage.
        * Clinician editing and confirmation.
        * Use of a smart template.
        * Examples highlighting Malaysian context.
        * Final report generation and PDF export with clinician and patient details.
    * Develop presentation slides covering the problem (clinician burnout in Malaysia), your solution (XXX by KinaVis), key features, technical architecture, AI/LLM integration details, the live demo, and future improvements.
    * Write a `README.md` with setup instructions to run the project locally for the demo.

This version focuses purely on developing a robust, demonstrable prototype within the hackathon week.