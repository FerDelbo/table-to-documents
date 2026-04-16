# FILM_RANK_DATABASE_REPORT_082: STATISTICAL ANALYSIS OF THE THIRTEEN HIGHEST GROSSING ENTRIES
*A comprehensive review of revenue distributions, studio market presence, and record-specific identifiers.*

## Executive Summary
This document provides a technical analysis of the 13 film records contained within the current dataset. The primary finding is a high revenue concentration in a single record, *ET the Extra-Terrestrial*, which accounts for 29.15% of the total gross recorded across the table. The dataset exhibits a non-linear decay in revenue, with a significant gap between the top-ranked entry and the remaining twelve records.

## Context & Overview
The source data consists of thirteen unique records (Film_ID 1 through 13). Each record is defined by five specific fields: `Film_ID`, `Title`, `Studio`, `Director`, and `Gross_in_dollar`. This analysis aims to categorize these records based on their fiscal performance and identify the dominant variables—specifically studio frequency and director assignments—that characterize this specific data subset. As a Database AI, my evaluation is strictly limited to the numerical and categorical values provided in these five fields.

## Key Findings

### 1. Revenue Concentration and Outlier Dominance
- **Observation**: There is a significant numerical disparity between the highest-grossing film and the rest of the dataset.
- **Implication**: The dataset is top-heavy. The first record represents a statistical outlier that skews the average gross of the entire set.
- **Supporting Data**: Record 1 (*ET the Extra-Terrestrial*) has a gross of $435,110,554. The second-ranked film (*Tootsie*) earns $177,200,000, representing a drop of approximately 59.28% from the first to the second position.

### 2. Studio Frequency and Market Representation
- **Observation**: Three studios—Paramount, Columbia, and Universal—are the most frequently occurring entities in the `Studio` field.
- **Implication**: These studios possess the highest density of records within this high-grossing subset, suggesting a higher frequency of entry into the top ranks compared to studios like MGM or Orion.
- **Supporting Data**: Paramount (including collaborations with Lorimar) appears three times (Records 3, 6, 7). Columbia (including collaborations with Rastar) appears three times (Records 2, 10, 12). Universal (including collaborations with RKO) appears twice (Records 1, 9).

### 3. Director Individualism
- **Observation**: There are thirteen unique entries in the `Director` field; no director appears more than once in this specific dataset.
- **Implication**: Revenue success at this scale is distributed across thirteen different individuals rather than being concentrated under a single director's output within these 13 records.
- **Supporting Data**: Each Film_ID (1 through 13) correlates to a unique director name, ranging from Steven Spielberg (Record 1) to Ted Kotcheff (Record 13).

### 4. Categorical Revenue Brackets
- **Observation**: The records can be segmented into three distinct gross-revenue tiers: "Primary" ($400M+), "Secondary" ($100M–$180M), and "Tertiary" (Below $100M).
- **Implication**: Only one film reaches the Primary tier, four films occupy the Secondary tier, and eight films—the majority of the dataset—reside in the Tertiary tier.
- **Supporting Data**: Record 1 is >$400M. Records 2, 3, 4, and 5 range from $109,492,484 to $177,200,000. Records 6 through 13 are all <$80,000,000.

## Trends & Patterns

### 1. The Power Law Distribution of Gross Revenue
The data follows a power law distribution rather than a linear one. As the `Film_ID` increases (which appears to correlate inversely with gross revenue), the decrease in `Gross_in_dollar` is initially precipitous and then stabilizes.
- **Evidence**: Between Film_ID 1 and 2, the gap is $257,910,554. Between Film_ID 12 and 13, the gap is only $5,554,985.
- **Interpretation**: In this dataset, the "rank" (as implied by Film_ID) does not represent a steady decline but rather an elite peak followed by a relatively flat tail of "standard" high-performers.

### 2. Studio Collaboration Patterns
The dataset contains several records where the `Studio` field lists multiple entities, indicating joint ventures or co-productions.
- **Evidence**: Record 3 (Paramount / Lorimar), Record 9 (Universal / RKO), Record 10 (Columbia / Rastar), and Record 13 (Orion / Carolco).
- **Interpretation**: 30.7% of the records (4 out of 13) involve a partnership between two studios. This suggests that shared investment is a recurring structural feature in high-grossing film production.

### 3. The $50 Million Floor
There is a notable floor in this dataset where the gross revenue begins to cluster closely.
- **Evidence**: Records 10, 11, 12, and 13 all fall within the narrow range of $47M to $57M.
- **Interpretation**: While the top end of the table is volatile and expansive, the bottom 30% of the entries demonstrate high consistency in their revenue outcomes, suggesting a stable baseline for "top-tier" performance within this data context.

## Addressing Core Questions

### Which studio achieved the highest total revenue across all entries?
Based on the aggregation of the `Gross_in_dollar` field, **Universal** is the highest-grossing studio in this dataset. 
- **Analysis**: Universal is the primary studio for Record 1 ($435,110,554) and the co-studio for Record 9 ($69,701,637). The combined gross for records associated with Universal is $504,812,191. This exceeds the total for Columbia ($286,726,892) and Paramount ($288,577,025).

### What is the average (mean) gross revenue for a film in this dataset?
The mean gross for the 13 records is **$114,827,242.38**.
- **Analysis**: The sum of all values in the `Gross_in_dollar` field is $1,492,754,151. Dividing this by 13 results in the aforementioned mean. It is important to note that only five films (Records 1, 2, 3, 4, and 5) actually perform above this average, while eight films perform below it.

### Is there a correlation between the Film_ID and the gross revenue?
Yes, there is a direct inverse correlation between the `Film_ID` and `Gross_in_dollar`.
- **Analysis**: As the `Film_ID` increments from 1 to 13, the `Gross_in_dollar` consistently decreases. Record 1 has the highest value ($435,110,554) and Record 13 has the lowest value ($47,212,904). This indicates that the dataset is sorted by revenue in descending order.

## Actionable Insights

1. **Standardize Studio Records**: The dataset uses inconsistent delimiters for co-productions (e.g., "Paramount / Lorimar" vs "Columbia / Rastar"). For future queries and automated sorting, these should be normalized into a multi-value field or separate "Primary" and "Associate" studio columns.
2. **Focus on Outlier Variable Analysis**: Given that Record 1 (*ET the Extra-Terrestrial*) outperformed the dataset average by nearly 3.8 times, identifying the missing variables (such as Genre or Release Date, which are not currently in the file) for this specific record is necessary to understand the drivers of such significant variance.
3. **Threshold Definition**: Based on this data, a "Top 5" status requires a minimum gross of $109,492,484 (Record 5). Films grossing below $100,000,000 represent the majority (61.5%) of this high-ranking list.
4. **Market Share Monitoring**: Analysts should monitor Paramount and Columbia, as they hold the highest volume of records (3 each). While Universal has the highest total gross, Paramount and Columbia show more frequent appearances in the top 13, suggesting a more consistent, volume-based performance strategy.

## Limitations & Caveats
- **Temporal Gaps**: The dataset does not contain a `Year` or `Date` field. Therefore, I cannot determine if these films were released in the same year or across a decade. This prevents inflation adjustment or chronological trend analysis.
- **Categorical Absence**: There is no `Genre` or `Country` information. I cannot assess if specific types of films (e.g., Sci-Fi vs Drama) perform better than others.
- **Critical/Audience Metrics**: The `Gross_in_dollar` field is the only performance metric. I have no data regarding production budgets, net profit, or critical ratings. A film with a high gross may still have a low profit margin if the production cost is not known.
- **Completeness**: This dataset contains only 13 records. It is a limited sample and may not be representative of the broader film industry or other high-ranking films outside of these specific entries.

---
*Document generated from 13 high-grossing film records | FilmRank Database AI*