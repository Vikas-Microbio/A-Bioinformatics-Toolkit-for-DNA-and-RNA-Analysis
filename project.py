import sys
import json
from datetime import datetime

def main():
    print("🧬 Advanced Genomic Sequence Processor")
    print("---------------------------------------")

    seq_data = None

    while True:
        print("\n1. Load/Input Sequence")
        print("2. Analyze Sequence (GC Content & Stats)")
        print("3. Generate Reverse Complement")
        print("4. Save Analysis Report")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            raw = input("Enter DNA/RNA sequence: ")
            try:
                seq_data = validate_sequence(raw)
                print("✅ Sequence loaded successfully.")
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            if not seq_data:
                print("❗ No sequence loaded.")
                continue
            stats = get_sequence_stats(seq_data)
            print(f"\nLength: {stats['length']} bp")
            print(f"GC Content: {stats['gc_percentage']}%")
            print(f"Nucleotide Counts: {stats['counts']}")

        elif choice == "3":
            if not seq_data:
                print("❗ No sequence loaded.")
                continue
            rc = generate_reverse_complement(seq_data)
            print(f"\nReverse Complement:\n{rc}")

        elif choice == "4":
            if not seq_data:
                print("❗ Run analysis first.")
                continue
            filename = input("Enter filename (default: report.json): ") or "report.json"
            stats = get_sequence_stats(seq_data)
            with open(filename, "w") as f:
                json.dump(stats, f, indent=4)
            print(f"💾 Saved to {filename}")

        elif choice == "5":
            sys.exit("Goodbye!")

def validate_sequence(sequence: str) -> str:
    """Validates and cleans DNA/RNA sequences."""
    cleaned = "".join(sequence.split()).upper()
    if not cleaned:
        raise ValueError("Sequence is empty")

    valid_bases = set("ACGTUN")
    if not set(cleaned).issubset(valid_bases):
        invalid = set(cleaned) - valid_bases
        raise ValueError(f"Invalid bases detected: {invalid}")
    return cleaned

def get_sequence_stats(sequence: str) -> dict:
    """Calculates GC content and base distribution."""
    seq = validate_sequence(sequence)
    length = len(seq)
    counts = {base: seq.count(base) for base in "ACGTUN"}

    # GC Calculation
    gc_count = counts["G"] + counts["C"]
    gc_pct = round((gc_count / length) * 100, 2) if length > 0 else 0

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "length": length,
        "gc_percentage": gc_pct,
        "counts": counts
    }

def generate_reverse_complement(sequence: str) -> str:
    """Creates the reverse complement for DNA or RNA."""
    seq = validate_sequence(sequence)

    # Check if RNA (contains U) or DNA
    if "U" in seq:
        mapping = str.maketrans("ACGU", "UGCA")
    else:
        mapping = str.maketrans("ACGT", "TGCA")

    return seq.translate(mapping)[::-1]

if __name__ == "__main__":
    main()
