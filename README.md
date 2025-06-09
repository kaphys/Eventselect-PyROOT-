# Eventselect

A lightweight analysis toolkit for performing event selection and transverse mass plotting on ATLAS ROOT datasets. This CLI-friendly utility is built to support comparison of physics processes like signal and background events in a simple, scriptable way.

---

## Physics Motivation

In high-energy physics experiments such as ATLAS at the Large Hadron Collider (LHC), vast amounts of data are collected from proton-proton collisions. Each collision event contains information about multiple particles (leptons, jets, MET, etc.), and a key step in physics analysis is to **select events** that match the expected signature of a signal process (e.g., a Higgs boson decaying to WW).

Event selection involves applying kinematic cuts on quantities such as:

- Number of leptons (`lep_n`)
- Missing transverse energy (MET)
- Transverse mass (`mT`)
- Angular separations (`Δφ`, `Δη`, etc.)

This project provides a minimal interface to **analyze ROOT trees**, apply **event selection cuts**, and generate **transverse mass distributions** for both signal and background Monte Carlo (MC) samples.

---

## Features

- Load ROOT files and extract `mini` trees
- Apply configurable selection cuts (or default ones)
- Compute and plot the transverse mass (`mT`)
- Compare signal and background distributions
- Save output plots for further study

---

## Installation

You need the following dependencies:

- Python 3.8+
- [ROOT](https://root.cern/)
- `cppyy` Python bindings for ROOT

### Step-by-step (Windows or Linux):

1. **Install ROOT** and ensure `root` is in your `PATH`.
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    .\venv\Scripts\activate    # Windows
    ```
3. **Install Python dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

Run Eventselect via the CLI using the `plot` or `compare` subcommands.

### Single File (Plot Transverse Mass)

```bash
python -m cli.eventselect plot \
    --file "data/mc_161055.VBFH125_WW2lep.root" \
    --label "VBF H→WW" \
    --output "plots/vbf_mt.png"
