# Internal Memorandum: Annual Food Safety Data Integrity and Inspection Summary

**To:** Department of Public Health Leadership, City Planning Committee  
**From:** Alex Riley, Food Inspection Data Manager  
**Date:** October 24, 2023  
**Subject:** Statistical Summary of the `food_inspection` Dataset and Business Registry Integrity

### **1. Executive Summary**

As the primary custodian of the city's food-service establishment records, I am providing this report to summarize the current state of our `food_inspection` dataset. This document focuses on data integrity, inspection volume, and significant outliers identified within our registry. The objective is to maintain a single source of truth for public health transparency and to ensure that our field inspectors have the most accurate `business_id` and `owner_name` information available.

Our records indicate a robust dataset with significant activity. For instance, in 2016 alone, there were 3,881 routine inspections recorded across 2,758 distinct San Francisco restaurants. While the majority of these establishments maintain high standards, with 2,087 restaurants currently holding a perfect inspection score of 100, we continue to monitor those that deviate from these benchmarks.

---

### **2. Business Registry and Owner Statistics**

The integrity of our `owner_name` and `owner_state` fields is critical for legal accountability. Currently, the count of restaurant owners in California (`owner_state = 'CA'`) stands at 5,902. This geographic concentration facilitates more efficient oversight, though we do track outliers such as the single eatery designated in the city of 'HAYWARD'.

Owner-level data shows a high degree of professionalization in the market. There are exactly 28 owners who operate five or more establishments. Interestingly, the owner with the highest establishment count maintains an impressive average inspection score of approximately 97.57. This suggests that large-scale operations in our registry often implement rigorous internal safety protocols.

However, growth in the registry varies by year. In 2012, for example, 473 eateries submitted applications for new permits. By 2014, our office was managing more acute safety data, recording 30 inspections specifically classified as Foodborne Illness Investigations.

---

### **3. Detailed Establishment Performance and Outliers**

Our database allows for granular tracking of specific businesses through their unique `business_id`. Identifying outliers is a core function of my role to ensure inspection resources are allocated effectively.

*   **High-Volume Inspections:** The business identified by `business_id 80243` has the highest inspection count in the dataset. Additionally, Peet's Coffee & Tea has the highest overall number of inspections among named establishments, maintaining an average score per inspection of 94.95.
*   **Significant Violations:** The highest violations count belongs to the entity with `business_id 75139`. This specific business was inspected 702 times, accumulating more violations than any other record.
*   **Risk Profiles:** Specialty's Cafe & Bakery ranks first for total high-risk violations. In contrast, Tiramisu Kitchen (which has an average inspection score of 89.33 across three routine inspections) recorded three high-risk violations.
*   **Score Extremes:** ABC Bakery Cafe holds the lowest inspection score on record. Conversely, in 2013, 184 unique eateries attained the maximum inspection score. On June 3, 2014, inspections in San Bruno reached a perfect score of 100.

---

### **4. Violation and Risk Category Analysis**

The `risk_category` and `violation_description` fields are essential for trend analysis. In 2014, our records show 6,774 violations categorized as Low Risk. During that same year, Peet's Coffee & Tea recorded the highest number of low-risk violations.

One specific historical marker in our data is Evergreen Garden Restaurant, which was the first business to receive a low-risk violation for the description: “Permit license or inspection report not posted.”

For more complex cases, we look at specific inspection dates:
*   **October 7, 2013:** Business certificate 304977 recorded five violations.
*   **January 14, 2014:** Tiramisu Kitchen recorded two low-risk violations.
*   **September 26, 2016:** KABABAYAN FAST FOOD recorded the lowest score among all Routine - Unscheduled inspections for that day.
*   **October 4, 2016:** Stacks Restaurant had six distinct kinds of violations documented.

It is worth noting that in 2016, the total count of violations occurring during unscheduled inspections was 36,344. That same year, San Francisco recorded the highest number of establishments categorized with the highest health and safety hazards compared to other cities in the dataset.

---

### **5. Geographic and Tax Code Insights**

We utilize `zip_code` and tax codes (such as H24 and H25) to segment our data for regional reporting.
*   **ZIP 94102:** In 2015, 128 distinct businesses in this postal code met the 90+ score threshold.
*   **ZIP 94117:** There are 74 unique `business_id` entries categorized as High Risk in this area.
*   **ZIP 94110:** Among businesses scoring below 95, approximately 56% are classified as Low Risk.
*   **Tax Code H25:** This code is assigned to 1,299 businesses.
*   **Tax Code H24:** There are 3 establishments with this tax code that have five or more complaint inspections. The business "Rue Lepic" is associated with tax code H24 for both routine and follow-up inspections.

Additionally, our precision mapping via `business_address` shows that the business with the highest count of low-risk violations is located at 428 11th St. Only a single business is recorded at the address 1825 POST St #223.

---

### **6. Data Integrity Observations**

As a Data Manager, I must highlight certain statistical anomalies that require careful query logic. For instance, Chairman Bao’s average score across all Routine - Unscheduled inspections is recorded as 0.0321. While mathematically accurate within the `food_inspection` table, such a figure warrants verification of the raw inspection entry to ensure it isn't a data entry error.

Furthermore, we track specific unique cases:
*   Whole Foods Market recorded more complaint-driven inspections than any other business.
*   34 distinct eateries were classified as low risk while having an "unpermitted food facility" description.
*   Soma Restaurant And Bar underwent three unscheduled routine inspections.
*   El Aji Peruvian Restaurant achieved its maximum score during a New Ownership inspection.

### **7. Conclusion**

The `food_inspection` dataset currently reflects 4,205 total high-risk violations associated with San Francisco restaurants. My office remains committed to the accuracy of every `business_name`, `latitude`, and `longitude` coordinate. This data is not merely a collection of rows; it is the primary tool for maintaining public safety in our city's food industry.

For any specific queries regarding these records or to request a detailed pull for a specific `zip_code`, please contact my desk directly.

**Alex Riley**  
Data Manager, City Health Department