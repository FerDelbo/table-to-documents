# Workforce Demographic Audit: Educational Pipelines and Age Distribution Analysis
*Internal Report: Business Intelligence Unit | Prepared by Alex Chen, Senior Data Analyst*

## Executive Summary
An analysis of the current `People_ID` dataset (n=7) reveals a predominantly mid-career workforce with a mean age of 31.6 years and a significant reliance on domestic (U.S.) higher education institutions. Despite a 28.6% international representation from the United Kingdom, there is a 100% correlation with U.S.-based collegiate graduation, suggesting a specific recruitment bias or a localized talent acquisition strategy that prioritizes U.S. educational credentials.

## Context & Overview
This report examines the demographic and educational background of a specific seven-person cohort. As we look to scale our operations and refine our recruitment KPIs, understanding the current makeup of our team is essential. This data provides a snapshot of our organizational "DNA"—where our people come from and the academic environments that shaped their professional foundations. For the Business Intelligence team, this serves as a baseline for identifying talent clusters and potential gaps in our geographic and generational diversity.

## Key Findings

### 1. Mid-Career Concentration
- **Observation**: The dataset shows a clear concentration of individuals in the 30+ age bracket.
- **Implication**: We are looking at a "mature" cohort. With 57.1% of the sample aged 30 or older, the team likely possesses significant professional experience but may lack the "digital native" entry-level pipeline that drives long-term succession planning.
- **Supporting Data**: See People_ID 3, 4, 5, 6, and 7, all of whom are 30 or older.

### 2. The U.S. Educational Monopoly
- **Observation**: Every individual in the dataset, regardless of nationality, graduated from a U.S. college.
- **Implication**: Our recruitment process, or perhaps the candidate pool we are tapping into, is heavily filtered through the U.S. higher education system. This suggests a high degree of cultural and professional alignment with U.S. business norms but indicates a lack of diverse global educational perspectives.
- **Supporting Data**: All entries in the `Graduation_College` column (Rows 1-7) represent U.S. institutions.

### 3. Institutional Hub Identification (Northeastern)
- **Observation**: Northeastern University is the only institution appearing more than once in this sample.
- **Implication**: There is a nascent "alumni cluster" from Northeastern (28.6% of the cohort). This suggests either a successful historical referral loop or a targeted recruiting effort at this specific institution.
- **Supporting Data**: People_ID 1 (Reggie Lewis) and People_ID 7 (Jerry Corcoran).

### 4. Data Integrity Alert: "United Kindom"
- **Observation**: A recurring typographical error exists in the `Nationality` field.
- **Implication**: As a Senior Analyst, I find this "dirty data" concerning. Inconsistent string entries like "United Kindom" instead of "United Kingdom" compromise our ability to run automated aggregations and filters without manual cleaning.
- **Supporting Data**: People_ID 3 (Tom Sheehey) and People_ID 5 (David Butler).

## Trends & Patterns

### The "UK-to-US" Educational Bridge
A significant pattern emerges when cross-referencing `Nationality` with `Graduation_College`. Both individuals identified as being from the "United Kindom" (Tom Sheehey and David Butler) attended prestigious U.S. state universities (Virginia and California, respectively). This indicates that our international hires are not being recruited directly from abroad, but rather are "educational transplants"—individuals who moved to the U.S. for schooling and were subsequently hired.

### Age-Nationality Correlation
There is a slight upward age trend among our international cohort. The average age of the U.S. nationals is 30.0 years, while the average age of the U.K. nationals is 35.5 years. While the sample size is small, this suggests that our international talent tends to be more senior or took longer to enter the professional pipeline following their U.S. education.

### Geographic Dispersion of Education
Aside from the Northeastern cluster in Boston, the educational background of the group is geographically diverse across the United States, spanning the Midwest (Iowa, Wisconsin), the South (Oklahoma, Virginia), and the West Coast (California). This suggests a broad geographical reach in our historical hiring, even if it remains domestically tethered.

## Addressing Core Questions

### What is the primary demographic profile of this cohort?
The primary profile is a 31-year-old U.S. national who graduated from a domestic university. The age range is relatively tight (12 years), with the youngest being 25 (Brad Lohaus) and the oldest being 37 (Tom Sheehey and Tim Naegeli). This indicates a lack of both very young (Gen Z) and more senior (50+) perspectives within this specific group.

### Are there identifiable talent "feeders" we should investigate?
Yes. Northeastern University is the clear leader. With two out of seven individuals hailing from this institution, we should investigate if there is a formal partnership or a high-performing referral program tied to this school. Additionally, the presence of graduates from large state schools like Oklahoma, Virginia, and California suggests our recruitment "net" is wide but focused on high-enrollment public institutions.

### Does the data suggest any immediate risks?
The most immediate risk is the lack of educational diversity. By only hiring from U.S. colleges—even for our international staff—we may be creating an "echo chamber" of professional methodologies. From a BI perspective, we thrive on varied approaches to problem-solving; 100% domestic education might limit our "out-of-the-box" analytical capabilities.

## Actionable Insights

1.  **Standardize Nationality Strings**: Immediately update the database to correct "United Kindom" to "United Kingdom" to ensure future SQL queries return accurate counts for international demographics.
2.  **Formalize the Northeastern Pipeline**: Since 28.6% of this cohort came from Northeastern, the Talent Acquisition team should look into career fair ROI at that campus to see if we can further optimize this successful feeder.
3.  **Diversify Educational Sourcing**: For future openings, specifically target candidates with international degrees (e.g., LSE, Oxford, or STEM-heavy universities in Asia) to break the 100% U.S. collegiate streak and bring in fresh perspectives.
4.  **Target Early-Career Talent**: With the median age at 31, we should consider an internship or junior associate program to bring in candidates in the 21-24 age range to balance the current mid-career skew.

## Limitations & Caveats
The primary limitation of this analysis is the small sample size (n=7). While the trends are stark, they may not be statistically significant when applied to the entire company. Additionally, the "Graduation_College" field does not specify the degree level (Undergraduate vs. Graduate), which would provide more context on the "UK-to-US" transition pattern. Finally, without "Department" or "Role" data, I cannot determine if these educational clusters are concentrated in one functional area or spread across the business.

---
*Document generated from workforce demographic table | Alex Chen, Senior Data Analyst*