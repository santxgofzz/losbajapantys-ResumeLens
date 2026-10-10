# Diseño del Lenguaje y Gramática Libre de Contexto (CFG)

## 1. Definición Formal de la Gramática (4-tupla)

$G = (V, \Sigma, P, S)$ donde:

**1. V (Variables / No Terminales):**
$V = \{ ResumeProfile, ListaSkills, Skill, Status \}$

**2. Σ (Alfabeto / Terminales):**
$\Sigma = \{ \text{'CANDIDATE:'}, \text{'ROLE:'}, \text{'LOCATION:'}, \text{'CONTACT:'}, \text{'Email:'}, \text{'SUMMARY:'}, \text{'EXPERIENCE:'}, \text{'Duration:'}, \text{'NORMALIZED\_SKILLS:'}, \text{'-'}, \text{'EVALUATION:'}, \text{'Profile evaluated:'}, \text{'Qualification pattern:'}, \text{'ACCEPTED'}, \text{'REJECTED'}, STRING, ID \}$

**3. S (Símbolo Inicial):**
$S = ResumeProfile$

**4. P (Reglas de Producción):**
$$ResumeProfile \rightarrow \text{ 'CANDIDATE:' } STRING \text{ 'ROLE:' } STRING \text{ 'LOCATION:' } STRING \text{ 'CONTACT:' } \text{ 'Email:' } STRING \text{ 'SUMMARY:' } STRING \text{ 'EXPERIENCE:' } STRING \text{ 'Duration:' } STRING \text{ 'NORMALIZED\_SKILLS:' } ListaSkills \text{ 'EVALUATION:' } \text{ 'Profile evaluated:' } STRING \text{ 'Qualification pattern:' } Status$$
$$ListaSkills \rightarrow Skill \ ListaSkills \ \mid \ \epsilon$$
$$Skill \rightarrow \text{'-' } ID$$
$$Status \rightarrow \text{'ACCEPTED'} \ \mid \ \text{'REJECTED'}$$
