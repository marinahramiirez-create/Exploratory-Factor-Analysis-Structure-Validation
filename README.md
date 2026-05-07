# Exploratory-Factor-Analysis-Structure-Validation

![Analysis](https://img.shields.io/badge/Analysis-EFA-blue)
![Software](https://img.shields.io/badge/Software-Jamovi-lightgrey)
![Psychometrics](https://img.shields.io/badge/Psychometrics-Construct%20Validity-orange)

## Project Overview
This project examines the internal structure of a 17 item psychometric instrument. Using **Exploratory Factor Analysis (EFA)**, the study identifies the underlying dimensions of the construct, ensuring that the items group logically and statistically according to their theoretical basis.

## Methodology
The analysis was performed using **Jamovi** following these steps:
1. **Sampling Adequacy:** Assessment of the correlation matrix via **Kaiser-Meyer-Olkin (KMO)** and **Bartlett's Test of Sphericity**.
2. **Factor Extraction:** Principal Axis Factoring.
3. **Rotation:** **Oblimin** (oblique) rotation to allow for correlation between factors.
4. **Factor Retention:** Parallel Analysis and Scree Plot inspection.

## Repository Structure
| File | Description |
| :--- | :--- |
| `BASE DE DATOS 5.csv` | Dataset with raw scores for 17 items. |
| `PRACTICA TEMA 5.docx` | Full report with KMO, Bartlett, and Factor Loading matrices. |

---

## Key Results

### 1. Adequacy and Sphericity
* **KMO Index:** **.868**, which is considered "meritorious" for factor analysis.
* **Bartlett's Test:** $\chi^2(136) = 2094.2, p < .001$, confirming the matrix is not identity.

### 2. Factor Structure
A **2-factor solution** was determined through Parallel Analysis:
* **Factor 1:** Higher loadings on items 11, 1, 5, and 9 (reverse).
* **Factor 2:** Higher loadings on items 6, 4 (reverse), 10 (reverse), and 8.
* **Note on Inversion:** Items such as **9, 7, 3** in Factor 1 and **4, 10, 12** in Factor 2 show negative loadings, indicating they are reverse coded items that measure the opposite pole of the factor.

## Final Conclusions
1. **Construct Validity:** The 17 items effectively reduce into two primary dimensions that explain the variance of the measured phenomenon.
2. **Item Performance:** Most items show factor loadings above **.40**, suggesting good individual representation within their respective factors.
3. **Internal Logic:** The presence of negative loadings confirms the importance of reverse item management in the scoring phase.

---

## Tools Used
* **Jamovi:** Statistical spreadsheet for factor analysis.
* **Principal Axis Factoring:** For latent variable identification.
