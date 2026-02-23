# Workforce Demographics: Preliminary Analysis of Employee Sample (N=10)
*Interpreting regional distribution and age demographics for strategic resource allocation.*

## Executive Summary
This analysis examines a subset of 10 employees to identify demographic trends and geographic distribution. The dataset reveals a workforce heavily concentrated in the West Country (60% in Bristol and Bath) with a mean age of 31.9, though a significant data integrity issue regarding location nomenclature (specifically the "Wasps" entries) requires immediate remediation before scaling this analysis.

## Context & Overview
As we look to refine our Business Intelligence reporting, this small-scale dataset provides a snapshot of our current employee distribution. For a mid-level analyst, this table is more than just a list; it is a baseline for understanding our human capital's lifecycle stage and regional footprint. My objective here is to parse the raw identifiers into a narrative that helps HR and Operations understand where our talent is located and how the age distribution might affect long-term succession planning and office utility.

## Key Findings

### 1. Geographic Concentration & Regional Hubs
- **Observation**: There is a clear "West Country" cluster within the data.
- **Implication**: Bristol and Bath account for 60% of the total sample. This suggests that the organization's physical footprint or recruitment efforts are highly localized in this region, which may offer opportunities for centralized regional events but poses a risk in terms of geographic diversity.
- **Supporting Data**: Employees 1, 3, and 4 are based in Bristol; Employees 2, 7, and 9 are based in Bath.

### 2. Age Demographic Stratification
- **Observation**: The workforce demonstrates a wide age range (23 to 43), but with a noticeable "mid-career" bulge.
- **Implication**: With a median age of 29.5 and a mean of 31.9, the team is relatively young but possesses several "veteran" anchors (those aged 40+). This creates a mentor-mentee dynamic that is vital for institutional knowledge transfer.
- **Supporting Data**: The range spans 20 years, from George Chuter (23) to Mark Regan (43).

### 3. Data Integrity & Categorical Anomalies
- **Observation**: The `City` column contains non-geographic entries.
- **Implication**: Two entries (Employee ID 5 and 8) list "Wasps" as their city. From a data hygiene perspective, this is a "dirty data" red flag. "Wasps" is traditionally a professional sports entity, not a municipality. This suggests a potential system entry error or a legacy field from a different database schema.
- **Supporting Data**: See `City` column for Tim Payne (ID 5) and Phil Vickery (ID 8).

### 4. The "29-Year-Old" Cohort
- **Observation**: There is a statistically significant mode in the age data.
- **Implication**: 30% of the sample is exactly 29 years old. This suggests a specific "hiring vintage" or a targeted recruitment drive approximately 5-7 years ago for entry-level roles that have now matured into mid-level positions.
- **Supporting Data**: Lee Mears (ID 2), Tim Payne (ID 5), and Matt Stevens (ID 7) are all 29.

## Trends & Patterns

### The Veteran-Junior Gap
I’ve identified a distinct gap in the "33 to 35" age bracket. We have a cluster of employees in their 20s and early 30s, and then a jump to 36, 40, and 43. 
- **Evidence**: 70% of the workforce is 32 or younger. Only 30% are 36 or older.
- **Interpretation**: This suggests a potential "missing middle" in our management pipeline. We have high-level veterans (Regan, Vickery) and a large group of rising talent, but few employees in the immediate 34-35 age range who would typically be transitioning into senior leadership.

### Regional Density vs. Isolation
There is a pattern of "Hub and Spoke" locations. 
- **Evidence**: Bristol (3) and Bath (3) form a hub. Sale (1) and Leicester (1) represent isolated "spoke" locations. 
- **Interpretation**: Employees in Sale and Leicester may lack the face-to-face peer support available to the Bristol/Bath cohorts. From a Business Intelligence perspective, I would recommend checking if these individuals have higher turnover rates or lower engagement scores due to geographic isolation.

## Addressing Core Questions

### What is the primary age demographic of the current workforce?
Based on the analysis of these 10 rows, the primary demographic is the "Late-20s Professional." The median age of 29.5 is the most telling metric here, as it minimizes the impact of the outliers like George Chuter (23) and Mark Regan (43). Specifically, 50% of the workforce falls between the ages of 28 and 30, indicating a very tight peer group that likely shares similar career goals and life stages.

### How reliable is the current location data for regional planning?
Currently, the location data is only 80% reliable for geographic mapping. While the Bristol and Bath entries are standard, the "Wasps" entries for Tim Payne and Phil Vickery (IDs 5 and 8) are non-standard. If we were to run a geospatial visualization (like a heat map) in Tableau or Power BI, these rows would likely return null values or errors. Before any office expansion or regional budget allocation, we must verify the actual physical work locations for these individuals.

### Are there any notable outliers that might skew our understanding of the team?
Yes, Mark Regan (ID 3, Age 43) and Phil Vickery (ID 8, Age 40) are significant outliers on the upper end of the age scale. Conversely, George Chuter (ID 1, Age 23) is an outlier on the lower end. Regan is exactly 20 years older than Chuter. When calculating "average" team age, these individuals shift the mean upward (31.9) significantly compared to the median (29.5). For any benefit or culture-related planning, we should look at the median to ensure we are serving the majority of the team.

## Actionable Insights

1.  **Standardize Location Fields**: Immediately audit the `City` column. The presence of "Wasps" suggests that data might have been pulled from a source where "Team" and "City" were conflated. I recommend implementing a dropdown/validation list for the `City` field in the source HRIS to prevent future inconsistencies.
2.  **Succession Planning for the "Missing Middle"**: With 70% of the sample aged 32 or younger, there is a looming gap between our senior-most employees (40+) and the rest of the staff. We should investigate professional development programs to fast-track the 29-32-year-old cohort into leadership roles to bridge this 10-year seniority gap.
3.  **Regional Engagement Strategy**: Given that 60% of the team is within the Bristol-Bath corridor, the company should consider these cities as the primary sites for "In-Real-Life" (IRL) collaboration days or regional town halls to maximize attendance with minimal travel costs.
4.  **Targeted Retention for the '29s'**: Since 30% of the team is at the same age/life stage (29), HR should tailor benefits or engagement activities that appeal to this specific demographic (e.g., mid-career growth opportunities, family-forming benefits) to prevent a "bulk exit" of this critical cohort.
5.  **Remote Support for Sale/Leicester**: Evaluate the support structures for Andrew Sheridan (Sale) and Louis Deacon (Leicester). Being the sole representatives in their respective locations, they may require more intentional digital engagement to remain aligned with the West Country-centric majority.

## Limitations & Caveats
- **Sample Size**: This analysis is based on a limited N=10 sample. While it provides directional insights, it is not statistically significant for the entire organization and may be subject to sampling bias.
- **Categorical Clarity**: The "City" column appears to have been used for "Club" or "Organization" names in some instances (e.g., Wasps), which compromises the geographic accuracy of the analysis.
- **Temporal Staticity**: This table is a point-in-time snapshot. It does not show tenure or hire date, which would be necessary to determine if the age clusters are a result of specific hiring cycles.
- **Missing Context**: Without "Department" or "Job Title" data, I cannot determine if the age/location clusters are functional (e.g., all 29-year-olds are in Sales) or coincidental.

---
*Document generated from Employee Demographic Subset | Alex Chen, Mid-Level Data Analyst*