erDiagram
    Clinicians ||--o{ Encounters : "has"
    Patients ||--o{ Encounters : "has"
    Encounters ||--o{ SubjectiveNotes : "has"
    Encounters ||--o{ ObjectiveNotes : "has"
    Encounters ||--o{ AssessmentNotes : "has"
    Encounters ||--o{ PlanNotes : "has"

    Clinicians {
        INT clinician_id PK "Clinician ID (Auto-Increment)"
        VARCHAR(255) full_name "Full Name"
        VARCHAR(255) specialization "Specialization"
        VARCHAR(50) contact_number "Contact Number (Optional)"
        VARCHAR(255) email "Email (Unique, Optional)"
        TIMESTAMP created_at "Timestamp of creation"
        TIMESTAMP updated_at "Timestamp of last update"
    }

    Patients {
        INT patient_id PK "Patient ID (Auto-Increment)"
        VARCHAR(255) full_name "Full Name"
        DATE date_of_birth "Date of Birth"
        ENUM('Male','Female','Other','Prefer not to say') gender "Gender"
        VARCHAR(255) nric_passport_number "NRIC/Passport (Unique, Optional)"
        VARCHAR(50) contact_number "Contact Number (Optional)"
        TEXT address "Address (Optional)"
        TIMESTAMP created_at "Timestamp of creation"
        TIMESTAMP updated_at "Timestamp of last update"
    }

    Encounters {
        INT encounter_id PK "Encounter ID (Auto-Increment)"
        INT patient_id FK "Patient ID (FK)"
        INT clinician_id FK "Clinician ID (FK)"
        DATETIME encounter_date "Date and Time of Encounter"
        ENUM('in-progress','completed','cancelled') status "Status of Encounter"
        TIMESTAMP created_at "Timestamp of creation"
        TIMESTAMP updated_at "Timestamp of last update"
    }

    SubjectiveNotes {
        INT subjective_note_id PK "Subjective Note ID (Auto-Increment)"
        INT encounter_id FK "Encounter ID (FK)"
        VARCHAR(512) raw_audio_path "Path to Raw Audio File (Optional)"
        TEXT raw_text_input "Raw Text Input (Optional)"
        TEXT transcribed_text "Transcribed Text (Optional)"
        TEXT ai_draft_text "AI Drafted Subjective Note (Optional)"
        TEXT clinician_final_text "Clinician Finalized Subjective Note (Optional)"
        TIMESTAMP created_at "Timestamp of creation"
        TIMESTAMP updated_at "Timestamp of last update"
    }

    ObjectiveNotes {
        INT objective_note_id PK "Objective Note ID (Auto-Increment)"
        INT encounter_id FK "Encounter ID (FK)"
        TEXT raw_text_input "Raw Text Input (Optional)"
        TEXT ai_draft_text "AI Drafted Objective Note (Optional)"
        TEXT clinician_final_text "Clinician Finalized Objective Note (Optional)"
        TIMESTAMP created_at "Timestamp of creation"
        TIMESTAMP updated_at "Timestamp of last update"
    }

    AssessmentNotes {
        INT assessment_note_id PK "Assessment Note ID (Auto-Increment)"
        INT encounter_id FK "Encounter ID (FK)"
        TEXT ai_draft_text "AI Drafted Assessment (Optional)"
        TEXT clinician_final_text "Clinician Finalized Assessment (Optional)"
        TIMESTAMP created_at "Timestamp of creation"
        TIMESTAMP updated_at "Timestamp of last update"
    }

    PlanNotes {
        INT plan_note_id PK "Plan Note ID (Auto-Increment)"
        INT encounter_id FK "Encounter ID (FK)"
        VARCHAR(512) raw_audio_path "Path to Raw Audio File (Optional)"
        TEXT raw_text_input "Raw Text Input (Optional)"
        TEXT transcribed_text "Transcribed Text (Optional)"
        TEXT ai_draft_text "AI Drafted Plan (Optional)"
        TEXT clinician_final_text "Clinician Finalized Plan (Optional)"
        TIMESTAMP created_at "Timestamp of creation"
        TIMESTAMP updated_at "Timestamp of last update"
    }