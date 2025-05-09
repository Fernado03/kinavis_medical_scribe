# Project XXX: Vision and Scope


## Introduction / Overview 🎯

*   **What is this document about?** This document outlines the vision, scope, key objectives, and high-level requirements for Project XXX, an intelligent medical scribe assistant.
*   **What purpose does it serve?** It serves as a foundational reference for the project team and stakeholders, ensuring a shared understanding of the project's goals and boundaries. This document is derived from the initial "[`Project Deck_ XXX by KinaVis.md`](Project Deck_ XXX by KinaVis.md:1)".
*   **Who is the intended audience?** The project development team, product managers, and key stakeholders involved in the XXX project.

## Section 1: Project Vision 🌟

*   **Problem:** To alleviate clinician burnout and reduce the administrative burden of medical documentation in healthcare, particularly in Malaysia.
*   **Solution:** "XXX" is an intelligent medical scribe assistant that leverages AI (Google Cloud Speech-to-Text and Gemini API) to listen to clinician-patient encounters and automatically generate accurate, structured SOAP notes.
*   **Core Aim:** To significantly reduce administrative workload, allowing clinicians to reclaim time, focus on patient care, and mitigate burnout.

## Section 2: Project Scope 🗺️

### In Scope:

*   **AI-Powered Transcription & Note Generation:**
    *   Transcription of English medical dialogues using Google Cloud Speech-to-Text (medical\_conversation model).
    *   Generation of structured SOAP notes in JSON format using Google's Gemini API (e.g., Gemini 1.5 Pro) with sophisticated prompt engineering.
*   **Clinician-in-the-Loop Design:** AI-generated notes are drafts requiring clinician review and approval.
*   **MVP Focus:**
    *   Input: Pre-recorded English audio of clinician-patient dialogues.
    *   Output: Structured SOAP notes in JSON.
    *   Frontend: Web-based interface for audio upload, transcript viewing, and generated note display.
*   **Deployment Concept:** Cloud-based, primarily utilizing Google Cloud Platform services.

### Out of Scope (for MVP, but potential future enhancements):

*   Live audio recording and real-time transcription/note generation.
*   Direct/seamless EHR integration (MVP produces JSON for groundwork).
*   Multilingual support (Bahasa Melayu, Mandarin, Tamil) - this is on the roadmap but not for the initial MVP.
*   Advanced administrative dashboards or enterprise-level features beyond basic MVP functionality.
*   Mobile application.
*   Offline functionality.

## Section 3: Key Objectives & Success Criteria 🏆

*   **Objective 1:** Reduce documentation time for clinicians.
    *   *Success Criterion:* Demonstrable time savings in generating SOAP notes compared to manual methods during pilot testing.
*   **Objective 2:** Improve the quality and consistency of clinical notes.
    *   *Success Criterion:* Clinician feedback indicating generated notes are accurate, relevant, and well-structured.
*   **Objective 3:** Enhance clinician satisfaction by reducing administrative burden.
    *   *Success Criterion:* Positive feedback from clinicians regarding ease of use and reduction in documentation-related stress.
*   **Objective 4 (MVP):** Successfully develop and demonstrate a functional MVP with core features as defined in the project deck.
    *   *Success Criterion:* MVP successfully transcribes audio and generates coherent SOAP notes for a set of test cases.

## Section 4: High-Level Requirements (Non-Exhaustive) 📋

*   **Functional Requirements:**
    *   User registration and authentication (basic for MVP).
    *   Audio file upload (e.g., .mp3, .wav).
    *   Display of ASR transcript.
    *   Display of generated SOAP note (JSON and human-readable).
    *   Mechanism for clinicians to review and notionally "approve" or "edit" (editing itself might be out of MVP scope, but the concept of review is key).
*   **Non-Functional Requirements (Initial Thoughts - to be expanded):**
    *   **Accuracy:** High accuracy in transcription and clinical information extraction.
    *   **Usability:** Intuitive and user-friendly interface.
    *   **Security:** Basic security measures for data handling (details TBD, especially concerning PII/PHI).
    *   **Scalability (Future):** Architecture should allow for future scaling.
    *   **Reliability:** The system should reliably process audio and generate notes.
*   **Data Requirements:**
    *   Input: Audio recordings of clinician-patient dialogues.
    *   Output: Structured JSON SOAP notes.
    *   Interim: Text transcripts.

## Summary / Key Takeaways 💡

Project XXX aims to develop an AI-powered medical scribe to reduce clinician burnout by automating SOAP note generation. The MVP will focus on English audio, producing JSON SOAP notes via a web interface, with a clear clinician-in-the-loop philosophy. Future phases will explore EHR integration and multilingual support.

## Related Links / Further Reading 🔗

*   [`Project Deck_ XXX by KinaVis.md`](../../Project Deck_ XXX by KinaVis.md)
