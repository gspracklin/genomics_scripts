# Genomics Analysis Tools

A collection of Python utilities for genomic data analysis, focusing on Hi-C, single-cell, and sequence data processing.

## Projects

### Hi-C Analysis
- **translocation_hic.py**: Detect potential chromosomal translocations using cooler format Hi-C data
- **domain_caller.py**: Call megabase-sized domains from bedGraph files
- **juicer_2_tadbit.py**: Convert Juicer dense matrices to TADbit format
- **matrix.py**: Convert TADbit matrices to BUTLRTools format

### Single-Cell Analysis
- **singlecell_DamID.py**: Process scDamID data (Kind et al., 2015) into bedGraph format

### Sequence Processing
- **basemods_separator.py**: Parse PacBio base modifications (m6A, m4C) from GFF files
- **bismark_chr_cov.py**: Add chromosome prefix to Bismark coverage files

## Repository Structure
```
genomics-tools/
├── projects/
│   ├── hic_analysis/
│   ├── scdamid_analysis/
│   └── sequence_processing/
├── src/
│   ├── formats/
│   ├── analysis/
│   └── utils/
├── tests/
└── docs/
```

## Installation

```bash
git clone https://github.com/yourusername/genomics-tools.git
cd genomics-tools
```

## Dependencies
- numpy
- pandas
- cooler
- TADbit
- BUTLRTools

## Usage Examples

### Hi-C Translocation Detection
```bash
python src/analysis/translocation_hic.py input.cool
```

### Convert Juicer Matrix to TADbit
```bash
python src/formats/juicer_2_tadbit.py -i input.txt -o output.txt
```

### Process scDamID Data
```bash
python src/analysis/singlecell_DamID.py input_data.txt output.bedgraph
```

## Project Documentation

Detailed documentation for each project can be found in their respective directories:
- [Hi-C Analysis](projects/hic_analysis/README.md)
- [scDamID Analysis](projects/scdamid_analysis/README.md)
- [Sequence Processing](projects/sequence_processing/README.md)

## Contributing

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) before submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use these tools in your research, please cite.

## Contact

- GitHub Issues: For bug reports and feature requests
