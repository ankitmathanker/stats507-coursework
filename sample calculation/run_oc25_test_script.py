#!/usr/bin/env python3
#Run from the fairchem-oc25 conda environment:
# conda run -n fairchem-oc25 python run_oc25_energies_three.py --device cuda

from pathlib import Path
import argparse

import ase.io

from fairchem.core.calculate.ase_calculator import FAIRChemCalculator


MODEL_NAME = "esen-sm-conserving-all-oc25"
TASK_NAME = "oc25"

POSCARS = [
    "POSCAR_benzene",
    "POSCAR_pd_benzaldehyde",
    "POSCAR_pd_benzaldehyde_phenol",
]


def parse_args():
    parser = argparse.ArgumentParser(description="OC25-eSEN energies for three POSCAR files")
    parser.add_argument("--inputdir", default=".", help="Folder containing the POSCAR files")
    parser.add_argument("--device", default="cuda", help="cuda or cpu")
    parser.add_argument("--output", default="oc25_energies.txt", help="Energy output file")
    return parser.parse_args()


def main():
    args = parse_args()
    inputdir = Path(args.inputdir)

    print(f"Loading {MODEL_NAME} on {args.device}...")
    calc = FAIRChemCalculator.from_model_checkpoint(
        MODEL_NAME,
        task_name=TASK_NAME,
        device=args.device,
    )

    lines = ["system,energy_eV"]

    for name in POSCARS:
        poscar = inputdir / name
        if not poscar.is_file():
            raise FileNotFoundError(f"Missing POSCAR file: {poscar}")

        atoms = ase.io.read(str(poscar), format="vasp")
        atoms.calc = calc
        energy = atoms.get_potential_energy()

        print(f"{name}: {energy:.8f} eV")
        lines.append(f"{name},{energy:.8f}")

    output = Path(args.output)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
