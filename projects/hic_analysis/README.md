# Hi-C Analysis Project

## Overview
Collection of tools for Hi-C data analysis and format conversion, with a focus on:
- Chromosomal translocation detection
- Domain calling
- Matrix format conversion

## Analysis Workflows

### 1. Translocation Detection
- **Input**: `.cool` format Hi-C matrices
- **Script**: `translocation_hic.py`
- **Notebook**: `01_translocation_detection.ipynb`
- **Output**: BED format translocation calls

### 2. Domain Calling
- **Input**: bedGraph coverage files
- **Script**: `domain_caller.py`
- **Notebook**: `02_domain_analysis.ipynb`
- **Output**: BED format domain boundaries

### 3. Format Conversion
- **Juicer to TADbit**
  - Script: `juicer_2_tadbit.py`
  - Input: Juicer dense matrix
  - Output: TADbit compatible matrix
- **TADbit to BUTLRTools**
  - Script: `matrix.py`
  - Input: TADbit matrix
  - Output: BUTLRTools compatible format

## Data
- Example datasets in `data/`
- Results stored in `results/`
- Figures generated in `results/figures/`

## Dependencies
```bash
numpy>=1.19.0
pandas>=1.1.0
cooler>=0.8.11
matplotlib>=3.3.0
TADbit>=1.0.0
BUTLRTools>=1.0.0
```

## Usage Examples

```bash
# Detect translocations
python ../../src/analysis/translocation_hic.py \
    --input data/sample.cool \
    --output results/translocations.bed

# Call domains
python ../../src/analysis/domain_caller.py \
    --input data/coverage.bedgraph \
    --output results/domains.bed

# Convert formats
python ../../src/formats/juicer_2_tadbit.py \
    --input data/juicer_matrix.txt \
    --output results/tadbit_matrix.txt
```

## Notebooks
1. `01_translocation_detection.ipynb`: Workflow for identifying chromosomal translocations
2. `02_domain_analysis.ipynb`: Domain calling and visualization
3. `03_format_conversion.ipynb`: Matrix format conversion examples

## Results
Analysis results and figures are stored in the `results/` directory:
- `results/translocations/`: Translocation calls
- `results/domains/`: Domain boundaries
- `results/figures/`: Visualization plots

## References
- Juicer: Durand et al. (2016) Cell Systems
- TADbit: Serra et al. (2017) Nature Protocols
- BUTLRTools: [Citation]