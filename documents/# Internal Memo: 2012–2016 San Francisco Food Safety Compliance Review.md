# Internal Memo: 2012–2016 San Francisco Food Safety Compliance Review
**To:** Director of Environmental Health  
**From:** Alex Chen, Public Health Inspector  
**Date:** October 24, 2023  
**Subject:** Longitudinal Analysis of Inspection Data and Field Observations

## Executive Summary

This report summarizes key findings from our food inspection registry, focusing on the period between 2012 and 2016. During this time, our department managed a significant workload, including 3,881 routine inspections in 2016 alone. While 2,087 establishments maintained perfect scores of 100, we continue to see a concentration of high-risk violations in specific sectors. This analysis aims to refine our inspection routes and prioritize high-risk interventions for the coming fiscal year.

## Context & Registry Overview

Managing the safety of our city’s food supply requires a robust and accurate database. Our current records show that California contributes 5,902 restaurant-owner records to our dataset (filtered by `owner_state` = 'CA'). Maintaining the integrity of these entries is paramount; however, data entry remains a challenge. For instance, we currently have exactly one eatery located in Hayward, while our primary focus remains the 2,758 distinct San Francisco restaurants we inspected during the 2016 calendar year.

Our workload is not limited to routine checks. In 2014, our team conducted 30 foodborne illness investigations. Furthermore, we must track the 28 owners who currently operate five or more establishments, as their systemic practices significantly impact public health across multiple sites.

## Key Performance Indicators & Compliance Trends

### The "Perfect Score" Cohort
It is encouraging to note that 2,087 restaurants met all inspection requirements, achieving a perfect score of 100. This is a testament to the efficacy of our outreach. For context, in 2013, 184 unique eateries attained this maximum score. These businesses serve as models for safe food handling practices.

### High-Risk and Low-Risk Violations
The data from 2014 reveals a high volume of minor infractions, with 6,774 violations categorized as Low Risk. However, the 4,205 high-risk violations associated with San Francisco restaurants are our primary concern.

In 2016, San Francisco recorded the highest number of establishments flagged for the most severe health and safety hazards. Unscheduled inspections that year were particularly telling, uncovering 36,344 violations.

## Field Observations: Case Studies in Compliance

In my daily route planning, I use the `business_id` and `address` to disambiguate locations and prepare for site visits. Looking at specific cases provides insight into the challenges we face:

*   **Tiramisu Kitchen:** This establishment has undergone three routine inspections, maintaining an average score of approximately 89.33. All three of these inspections resulted in scores above 70. However, our records indicate they have incurred three High Risk violations over time. On January 14, 2014, specifically, we documented two low-risk violations during their visit. Interestingly, Tiramisu Kitchen recorded a higher count of low-risk violations than the OMNI S.F. Hotel - 2nd Floor Pantry.
*   **Specialty's Cafe & Bakery:** This business currently ranks first for the total number of high-risk violations among the establishments we evaluate. No other restaurant in the dataset exceeds their count in this critical category.
*   **Peet's Coffee & Tea:** In contrast, this chain has the highest number of inspections in our records. Despite the high frequency of visits, they maintain a strong average score of 94.95. It’s worth noting that back in 2014, they actually had the highest number of low-risk violations.
*   **Whole Foods Market:** This entity stands out for having the highest number of inspections initiated by complaints. Complaint-driven inspections are a high priority for my team as they often indicate immediate risks to the public.

## Data Anomalies and Enforcement Challenges

As an inspector, I frequently encounter outliers that require immediate enforcement action. 
*   **Critical Failures:** ABC Bakery Cafe holds the record for the lowest inspection score ever recorded in our system. On September 26, 2016, Kababayan Fast Food recorded the lowest score among all unscheduled routine inspections conducted that day.
*   **Specific Incident Documentation:** On October 4, 2016, Stacks Restaurant was documented with six distinct types of violations in a single visit. We also have records of two distinct businesses currently operating with inspection scores below 50, which warrants immediate follow-up.
*   **Geographic Hotspots:** ZIP code 94117 is of particular concern, with 74 unique businesses currently classified as High Risk. In the 94110 area, among businesses scoring below 95, nearly 56% of their violations are classified as Low Risk.

## Operational Recommendations

To improve our departmental efficiency, I recommend the following:

1.  **Address Verification:** We must clean the records for businesses like the one located at 428 11th St., which currently holds the highest count of low-risk violations. Accurate `address` and `postal_code` data are essential for planning my daily inspection routes.
2.  **Tax Code Monitoring:** We should pay closer attention to establishments under tax code H24. For example, Rue Lepic is associated with this code and has required both unscheduled inspections and reinspections. Additionally, three establishments with tax code H24 have triggered five or more complaint-based inspections.
3.  **Permit Enforcement:** We should look at the 34 distinct eateries classified as low risk that are operating with an "unpermitted food facility" description. Evergreen Garden Restaurant was notably the first to be cited for failing to post a permit or inspection report.

## Conclusion

While the majority of our 5,902 registered owners in California strive for compliance, the 4,205 high-risk violations in San Francisco suggest we cannot become complacent. By focusing our 2017 efforts on high-violation entities like Specialty's Cafe & Bakery and high-risk zones like 94117, we can better fulfill our mandate to protect public health. My next step will be to query the database for the `owner_name` and `phone_number` of all businesses scoring below 50 to initiate formal notices.