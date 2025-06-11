# Setting Up ROOT and PyROOT on Windows


## 1. Prerequisites

Before starting, make sure you have:

- Python (via Miniconda or Anaconda)
- Visual Studio with C++ Desktop Development tools
- CMake (optional if using precompiled ROOT)
- Downloaded the pre-compiled ROOT binaries (from [https://root.cern/install](https://root.cern/install))


## 2. One-Time Setup

In this step, we:

- Add Conda to the Windows PATH (optional)
- Initialize Conda in CMD
- Check which Python version ROOT expects
- Create a compatible Conda environment



```python
# Only run this ONCE to add Conda to PATH — not needed if already added by installer
#!setx PATH "%USERPROFILE%\miniconda3;%USERPROFILE%\miniconda3\Scripts;%USERPROFILE%\miniconda3\Library\bin;%PATH%"

```


```python
# One-time Conda initialization for CMD
#!conda init cmd.exe  #uncomment


Check version compatibility:


```python
%%cmd
root-config --python-version
python --version
```

    Microsoft Windows [Version 10.0.19045.5854]
    (c) Microsoft Corporation. Alle rechten voorbehouden.
    
    C:\%USERPROFILE%>root-config --python-version
     3.11.2
    
    C:\%USERPROFILE%>python --version
    Python 3.12.9
    
    C:\%USERPROFILE%>

Create environment (if versions mismatch):


```python
# Create the Conda environment with compatible Python version (adjust version as needed)
#!conda create -n root_env python=3.11.2 -y

```

> **Important:** You cannot activate Conda environments directly from Jupyter cells.  
> Instead, run this step in a **Command Prompt** manually:

```cmd
conda activate root_env


---
## 3. Daily Setup (Every time you want to use ROOT)

In this step, we:
- Activate the environment
- Initialize ROOT
- Test PyROOT


> Run these in a **Command Prompt** every day:

```cmd
conda activate root_env
call "<path_to_your_root_installation>\bin\thisroot.bat"
python -c "import ROOT; print('ROOT', ROOT.__version__)"


## 4. Using ROOT in Jupyter or Python

After setup, you can use PyROOT directly in notebooks or scripts:

It seems that conda does not activate inside jupyter notebook.


```python
import ROOT

# Print ROOT version
print("ROOT version:", ROOT.__version__)

# Draw a histogram (basic example)
h = ROOT.TH1F("h", "My Histogram", 100, -4, 4)
for i in range(1000):
    h.Fill(ROOT.gRandom.Gaus())
h.Draw()

```

    ROOT version: 6.32.10
    

## 5. Optional: Create a `.bat` File for Daily Setup

Create a file named `start_root_env.bat` with the following contents:

```bat
@echo off
call conda activate root_env
call "<path_to_your_root_installation>\bin\thisroot.bat"
cmd


some notes for next time:
1. dont forget: root-config python--vesion (done)
2. check this conda activation (before it used to work) 
3. make generic code for any folder. (done)
4. Upload to GitHub.


```python
!python --version
```

    Python 3.12.9
    

## Troubleshooting (Windows-Specific)

| Error | Solution |
|-------|----------|
| `'conda' not recognized` | Re-run `conda init cmd.exe` as admin |
| `DLL load failed` | Run `thisroot.bat` before Python |
| Version mismatch | `conda create -n root_env python=3.11.2` |


```python

```
