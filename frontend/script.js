document.addEventListener('DOMContentLoaded', () => {
    // API Base URL
    const API_BASE_URL = '/api';

    // DOM Elements
    const clinicianSelect = document.getElementById('clinician-select');
    const patientSearchInput = document.getElementById('patient-search-input');
    const patientSearchButton = document.getElementById('patient-search-button');
    const patientSearchResultsDiv = document.getElementById('patient-search-results');
    const newPatientForm = document.getElementById('new-patient-form');
    const selectedClinicianIdSpan = document.getElementById('selected-clinician-id');
    const selectedPatientIdSpan = document.getElementById('selected-patient-id');
    const startEncounterButton = document.getElementById('start-encounter-button');

    // State variables
    let selectedClinicianId = null;
    let selectedPatientId = null;

    // --- Clinician Identification ---

    /**
     * Fetches clinicians from the API and populates the dropdown.
     */
    async function fetchAndPopulateClinicians() {
        try {
            const response = await fetch(`${API_BASE_URL}/clinicians`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const clinicians = await response.json();

            clinicians.forEach(clinician => {
                const option = document.createElement('option');
                option.value = clinician.clinician_id;
                option.textContent = `${clinician.first_name} ${clinician.last_name}`;
                clinicianSelect.appendChild(option);
            });
        } catch (error) {
            console.error('Error fetching clinicians:', error);
            // Optionally, display an error message to the user in the UI
        }
    }

    /**
     * Updates the selected clinician ID and UI.
     */
    function handleClinicianSelection() {
        selectedClinicianId = clinicianSelect.value || null;
        selectedClinicianIdSpan.textContent = selectedClinicianId || 'None';
        console.log('Selected Clinician ID:', selectedClinicianId);
    }

    // --- Patient Management ---

    /**
     * Fetches patients based on search term and displays results.
     */
    async function searchPatients() {
        const searchTerm = patientSearchInput.value.trim();
        patientSearchResultsDiv.innerHTML = ''; // Clear previous results

        if (!searchTerm) {
            patientSearchResultsDiv.textContent = 'Please enter a search term.';
            return;
        }

        try {
            const response = await fetch(`${API_BASE_URL}/patients?search=${encodeURIComponent(searchTerm)}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const patients = await response.json();

            if (patients.length === 0) {
                patientSearchResultsDiv.textContent = 'No patients found.';
                return;
            }

            patients.forEach(patient => {
                const patientDiv = document.createElement('div');
                patientDiv.textContent = `ID: ${patient.patient_id} - ${patient.first_name} ${patient.last_name} (DOB: ${patient.date_of_birth})`;
                patientDiv.dataset.patientId = patient.patient_id;
                patientDiv.addEventListener('click', () => handlePatientSelection(patient.patient_id));
                patientSearchResultsDiv.appendChild(patientDiv);
            });
        } catch (error) {
            console.error('Error searching patients:', error);
            patientSearchResultsDiv.textContent = 'Error searching patients. See console for details.';
        }
    }

    /**
     * Updates the selected patient ID and UI.
     * @param {string} patientId - The ID of the selected patient.
     */
    function handlePatientSelection(patientId) {
        selectedPatientId = patientId;
        selectedPatientIdSpan.textContent = selectedPatientId || 'None';
        console.log('Selected Patient ID:', selectedPatientId);
        // Highlight selected patient in search results (optional)
        Array.from(patientSearchResultsDiv.children).forEach(child => {
            child.style.backgroundColor = child.dataset.patientId === patientId ? '#e0e0e0' : '';
        });
    }

    /**
     * Handles the submission of the new patient form.
     * @param {Event} event - The form submission event.
     */
    async function handleNewPatientSubmit(event) {
        event.preventDefault();
        const formData = new FormData(newPatientForm);
        const patientData = {};
        formData.forEach((value, key) => {
            // Only include non-empty optional fields
            if (value.trim() !== '' || ['first_name', 'last_name', 'date_of_birth', 'gender'].includes(key)) {
                 patientData[key] = value.trim();
            }
        });

        // Ensure required fields are present (basic client-side check, backend should also validate)
        if (!patientData.first_name || !patientData.last_name || !patientData.date_of_birth || !patientData.gender) {
            alert('Please fill in all required fields for the new patient.');
            return;
        }

        try {
            const response = await fetch(`${API_BASE_URL}/patients`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(patientData),
            });

            if (!response.ok) {
                const errorData = await response.json().catch(() => ({ message: 'Unknown error occurred' }));
                throw new Error(`HTTP error! status: ${response.status} - ${errorData.message || 'Failed to create patient'}`);
            }

            const newPatient = await response.json();
            console.log('New patient created:', newPatient);
            alert(`Patient ${newPatient.first_name} ${newPatient.last_name} created successfully!`);

            // Display and select the new patient
            patientSearchResultsDiv.innerHTML = ''; // Clear previous search results
            const patientDiv = document.createElement('div');
            patientDiv.textContent = `ID: ${newPatient.patient_id} - ${newPatient.first_name} ${newPatient.last_name} (DOB: ${newPatient.date_of_birth})`;
            patientDiv.dataset.patientId = newPatient.patient_id;
            patientSearchResultsDiv.appendChild(patientDiv);
            handlePatientSelection(newPatient.patient_id);

            newPatientForm.reset(); // Clear the form
        } catch (error) {
            console.error('Error creating patient:', error);
            alert(`Error creating patient: ${error.message}`);
        }
    }

    // --- Start Encounter ---
    /**
     * Handles the "Start Encounter" button click.
     * (Currently a placeholder)
     */
    function handleStartEncounter() {
        if (!selectedClinicianId || !selectedPatientId) {
            alert('Please select a clinician and a patient before starting an encounter.');
            return;
        }
        // Later, this will call POST /api/encounters
        console.log('Starting encounter with Clinician ID:', selectedClinicianId, 'and Patient ID:', selectedPatientId);
        alert(`Starting encounter with Clinician ID: ${selectedClinicianId} and Patient ID: ${selectedPatientId}. (Functionality to be implemented)`);
    }

    /**
     * Tests the "Hello World" endpoint from the backend.
     */
    async function testHelloWorld() {
        try {
            // Fetch from the root path, not API_BASE_URL for this specific test
            const response = await fetch('/');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const message = await response.text();
            console.log('Hello World Test:', message);
            // Optionally, display this message somewhere in the UI for visibility
        } catch (error) {
            console.error('Error testing Hello World endpoint:', error);
        }
    }

    // --- Event Listeners ---
    clinicianSelect.addEventListener('change', handleClinicianSelection);
    patientSearchButton.addEventListener('click', searchPatients);
    newPatientForm.addEventListener('submit', handleNewPatientSubmit);
    startEncounterButton.addEventListener('click', handleStartEncounter);

    // --- Initial Load ---
    fetchAndPopulateClinicians();
    testHelloWorld(); // Call the test function
});