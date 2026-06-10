import os
import glob
from Bio import PDB


class ChainAFilter(PDB.Select):
    def accept_chain(self, chain):
        return chain.id == "A"

    def accept_residue(self, residue):
        return residue.id[0] == " "  # this excludes HETATM!!


def clean_pdb(pdb_path: str):
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure("protein", pdb_path)

    io = PDB.PDBIO()
    io.set_structure(structure)
    io.save(pdb_path, ChainAFilter())


if __name__ == "__main__":
    pdb_files = glob.glob("data/proteins/*.pdb")

    if not pdb_files:
        print("No .pdb files found in data/proteins/")
    else:
        for path in pdb_files:
            name = os.path.basename(path)
            try:
                clean_pdb(path)
                print(f"DONE:  {name}")
            except Exception as e:
                print(f"ERROR:  {name}  -  {e}")

        print(f"\nDone. Cleaned {len(pdb_files)} file(s).")