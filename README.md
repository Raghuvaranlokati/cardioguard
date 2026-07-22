# CardioGuard: Multimodal Clinical ECG & Heart Rhythm Analyzer

CardioGuard is an open-source, production-grade deep learning framework and web application designed for clinical electrocardiogram (ECG) analysis. 

The system leverages multimodal deep neural networks to process:
1. **Raw ECG Signals (1D)**: Utilizing 1D CNNs + LSTMs for time-series heart rate and rhythm analysis.
2. **Visual ECG Plots (2D)**: Utilizing 2D CNNs (ResNet) to analyze plotted waveform images.
3. **Patient Metadata (Tabular)**: Integrating age, sex, weight, and history using dense networks to produce final diagnostic classifications.

---

## 📊 Datasets Utilized

CardioGuard combines three gold-standard open databases to achieve generalizability and diagnostic breadth:

1. **PTB-XL ECG Database** (21,837 records, 18,885 patients)
   * **Purpose**: Primary dataset for multimodal fusion training. Provides 12-lead raw signals paired with demographic patient metadata.
2. **MIT-BIH Arrhythmia Database** (48 half-hour recordings)
   * **Purpose**: Beat-by-beat segmentation training. Used to detect individual heartbeat anomalies such as Premature Ventricular Contractions (PVCs).
3. **PhysioNet/Computing in Cardiology Challenges (2020/2021)** (40,000+ records)
   * **Purpose**: Cross-source model validation. Used to train robust, noise-resistant networks that generalize across different hospital recording systems.

---

## 🛠️ Project Architecture

```
cardioguard/
├── .github/                 # GitHub templates & workflows
│   ├── ISSUE_TEMPLATE/      # Issue templates (Bugs, Features)
│   └── pull_request_template.md
├── backend/                 # FastAPI Gateway & inference pipelines
├── frontend/                # Interactive clinical dashboard (HTML/CSS/JS)
├── models/                  # PyTorch model definitions & training scripts
│   ├── ecg_models.py        # CNN, LSTM, and Fusion architectures
│   └── train.py             # Data loader & training loops
├── CONTRIBUTING.md          # Guidelines for developers
├── LICENSE                  # Open-source MIT License
├── CODE_OF_CONDUCT.md       # Community standards
└── requirements.txt         # Core dependencies
```

---

## 🚀 Getting Started

*Detailed setup, data preparation, and training instructions will be added as implementation progresses.*

---

## 🤝 Contributing

We welcome contributions from the data science and medical AI communities! Please review [CONTRIBUTING.md](CONTRIBUTING.md) to understand our workflow, branch styling, and PR expectations.
