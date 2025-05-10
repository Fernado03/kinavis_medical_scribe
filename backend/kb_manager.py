import json
import os
from typing import List, Dict, Any

KB_DIR = os.path.join(os.path.dirname(__file__), "kb")

def load_kb(kb_section_name: str) -> List[Dict[str, Any]]:
    """
    Loads a specified KB JSON file from the backend/kb/ directory.

    Args:
        kb_section_name: The name of the KB section (e.g., "subjective", "objective").
                         This will be used to construct the filename (e.g., "kb_subjective.json").

    Returns:
        A list of dictionaries, where each dictionary represents a KB entry.
        Returns an empty list if the file is not found or an error occurs.
    """
    file_path = os.path.join(KB_DIR, f"kb_{kb_section_name}.json")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            kb_data = json.load(f)
        return kb_data
    except FileNotFoundError:
        print(f"Error: KB file not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {file_path}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while loading {file_path}: {e}")
        return []

def query_kb(kb_data: List[Dict[str, Any]], keywords: List[str]) -> List[Dict[str, Any]]:
    """
    Queries a loaded KB based on a list of keywords.
    An entry is considered a match if any of its 'keywords' (case-insensitive)
    are present in the provided list of keywords.

    Args:
        kb_data: A list of KB entries (dictionaries) loaded from a JSON file.
        keywords: A list of keywords to search for.

    Returns:
        A list of matching KB entries.
    """
    if not kb_data or not keywords:
        return []

    matched_entries: List[Dict[str, Any]] = []
    search_keywords_lower = [kw.lower() for kw in keywords]

    for entry in kb_data:
        entry_keywords_lower = [kw.lower() for kw in entry.get("keywords", [])]
        if any(kw in entry_keywords_lower for kw in search_keywords_lower):
            matched_entries.append(entry)
    return matched_entries

def get_all_entries(kb_section_name: str) -> List[Dict[str, Any]]:
    """
    Retrieves all entries from a specified KB JSON file.
    This is a convenience function that wraps load_kb.

    Args:
        kb_section_name: The name of the KB section (e.g., "subjective").

    Returns:
        A list of all KB entries from the specified section.
        Returns an empty list if the file is not found or an error occurs.
    """
    return load_kb(kb_section_name)

if __name__ == '__main__':
    # Example Usage (for testing purposes)
    print("Testing KB Manager...")

    # Test loading
    subjective_kb = load_kb("subjective")
    if subjective_kb:
        print(f"\nSuccessfully loaded subjective KB. Found {len(subjective_kb)} entries.")
        # print("First entry:", subjective_kb[0])
    else:
        print("\nFailed to load subjective KB or it's empty.")

    objective_kb = get_all_entries("objective")
    if objective_kb:
        print(f"\nSuccessfully loaded objective KB using get_all_entries. Found {len(objective_kb)} entries.")
        # print("First entry:", objective_kb[0])
    else:
        print("\nFailed to load objective KB or it's empty.")

    assessment_kb = load_kb("assessment")
    if assessment_kb:
        print(f"\nSuccessfully loaded assessment KB. Found {len(assessment_kb)} entries.")
    else:
        print("\nFailed to load assessment KB or it's empty.")
    
    plan_kb = load_kb("plan")
    if plan_kb:
        print(f"\nSuccessfully loaded plan KB. Found {len(plan_kb)} entries.")
    else:
        print("\nFailed to load plan KB or it's empty.")

    # Test querying (assuming subjective_kb loaded successfully)
    if subjective_kb:
        print("\nQuerying subjective KB for 'headache' or 'sakit kepala':")
        results_headache = query_kb(subjective_kb, ["headache", "sakit kepala"])
        if results_headache:
            print(f"Found {len(results_headache)} entries for 'headache'/'sakit kepala'.")
            for res in results_headache:
                print(f"  ID: {res.get('id')}, Category: {res.get('category')}")
        else:
            print("No entries found for 'headache'/'sakit kepala'.")

        print("\nQuerying subjective KB for 'fever':")
        results_fever = query_kb(subjective_kb, ["fever"])
        if results_fever:
            print(f"Found {len(results_fever)} entries for 'fever'.")
            for res in results_fever:
                print(f"  ID: {res.get('id')}, Category: {res.get('category')}")
        else:
            print("No entries found for 'fever'.")
    
    # Test with a non-existent KB
    print("\nAttempting to load a non-existent KB ('non_existent_kb'):")
    non_existent_kb = load_kb("non_existent_kb")
    if not non_existent_kb:
        print("Correctly handled non-existent KB (returned empty list or printed error).")

    print("\nKB Manager testing complete.")