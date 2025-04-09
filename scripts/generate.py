import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.generators.file_builder import generate_code_files

if __name__ == "__main__":
    try:
        crud_id = int(input("Enter CRUD ID to generate code for: "))
        generate_code_files(crud_id)
        print(f"\n✅ CRUD files generated for CRUD ID: {crud_id}")
    except Exception as e:
        print(f"❌ Error: {e}")
