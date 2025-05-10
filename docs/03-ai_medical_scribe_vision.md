# Product Vision: AI Medical Scribe (SOAP Note Generator)

*This document outlines the high-level vision, goals, and strategy for the AI Medical Scribe. It serves as a guiding star for development and decision-making.*

## 1. Introduction

The AI Medical Scribe is a project by Team KinaVis aimed at developing a tool to assist clinicians in generating SOAP (Subjective, Objective, Assessment, Plan) notes. The primary problem it aims to solve is the time-consuming nature of clinical documentation, which contributes to clinician burnout. This tool will leverage AI, specifically Google Cloud Speech-to-Text and Google Gemini API, to streamline the note-taking process. The initial context for this project is Malaysia, with a focus on a 1-week hackathon development sprint.

## 2. Vision Statement

To empower clinicians by significantly reducing the administrative burden of documentation, allowing them to focus more on patient care, through an intelligent and intuitive AI-powered SOAP note generation tool.

## 3. Goals

*   **Goal 1:** Reduce the time clinicians spend on writing SOAP notes by at least 50% for common encounters within the hackathon scope.
    *   *Metric:* Time taken to complete a SOAP note using the tool versus traditional methods (simulated or based on estimates).
*   **Goal 2:** Achieve a high level of accuracy in AI-generated draft notes for Subjective, Objective, Assessment, and Plan sections, requiring minimal clinician editing for common scenarios.
    *   *Metric:* Clinician satisfaction score (e.g., on a 1-5 scale) on the quality of AI drafts; percentage of AI-generated text retained by clinicians in the final note.
*   **Goal 3:** Develop a functional prototype demonstrating the end-to-end SOAP note generation workflow, including audio transcription, AI drafting, clinician editing, and final report generation (including PDF export) within the 1-week hackathon timeframe.
    *   *Metric:* Successful completion and demonstration of all core features outlined in `methodology.md` for the hackathon.
*   **Goal 4:** Ensure the system can incorporate Malaysian contextual nuances in medical terminology and common conditions, as outlined in the knowledge base.
    *   *Metric:* Qualitative feedback from demo audience on the relevance and accuracy of Malaysian context handling.

## 4. Target Audience

*   **Primary Audience:** Clinicians (doctors, specialists) in Malaysia who are responsible for creating SOAP notes as part of patient encounters. They are likely tech-savvy to a degree but require a simple, efficient, and intuitive interface.
*   **Secondary Audience:** Healthcare administrators or institutions in Malaysia looking for solutions to improve clinical efficiency and reduce documentation overhead. (For the hackathon, the focus is primarily on the clinician user).

## 5. Key Features / Strategic Themes

*   **Theme/Feature 1: AI-Powered Transcription & Drafting:**
    *   Utilize Google Cloud Speech-to-Text for accurate medical audio transcription (Subjective & Plan sections).
    *   Employ Google Gemini API for intelligent drafting of S, O, A, and P sections based on transcribed audio, text inputs, and a structured knowledge base.
*   **Theme/Feature 2: Clinician-Centric Workflow & Editing:**
    *   Provide an intuitive single-page interface for capturing/inputting data for each SOAP section.
    *   Allow seamless review and editing of AI-generated drafts by clinicians.
    *   Enable easy confirmation and saving of each section.
*   **Theme/Feature 3: Comprehensive Report Generation:**
    *   Generate a complete, formatted SOAP note including patient and clinician details.
    *   Offer PDF export functionality for the final report, suitable for clinical records.
*   **Theme/Feature 4: Malaysian Contextualization & Knowledge Base Integration:**
    *   Develop and integrate a knowledge base (`kb_subjective.json`, `kb_objective.json`, etc.) with Malaysian medical terms, local conditions, and specific instructions for the Gemini API to improve contextual relevance.
*   **Theme/Feature 5: User & Encounter Management (Basic):**
    *   Implement basic mechanisms for clinician identification and patient selection/creation to associate notes with the correct individuals and encounters.

---