# Through the Steam: A Regular’s Code-Review of the Loyalty Stack
*Analyzing the morning rush through the lens of a Gold Tier regular.*

## Executive Summary
After analyzing the current member cohort data, it is clear that our loyalty ecosystem is driven by a few "power users" who demonstrate significantly higher engagement-to-visit ratios than the average. While the geographic spread remains concentrated in the Hartford and Waterbury hubs, there is a visible "efficiency gap" where some members spend more time in-shop with fewer loyalty rewards to show for it—suggesting a need to better align our digital app experience with our long-form "third place" visitors.

## Context & Overview
As someone who treats the corner window seat as my primary office, I’ve seen most of these faces through the steam of my morning Americano. This table represents the "core stack" of our community—10 distinct member profiles that frequent our locations across Connecticut. For me, this isn't just a list of names; it’s a snapshot of the people I share the Wi-Fi with every day. Understanding how we all interact with the loyalty program—the "Black" vs "White" cards and the "Level" progression—helps me see if the system is truly rewarding the "Gold" lifestyle I strive for.

## Key Findings

### The "Super-User" Anomaly
- **Observation**: Daniel Webb (Member ID 10) is operating on a completely different level than the rest of the cohort.
- **Implication**: While most regulars are hovering between Levels 1 and 6, Webb has reached Level 22. This suggests a "whale" behavior pattern where a specific user is likely ordering for a team or has a daily spend that far exceeds the average freelance developer's budget.
- **Supporting Data**: Member 10 shows a Level_of_membership of 22, more than triple the next highest members (Campbell and Peeler at Level 6).

### The Time-Value Inefficiency
- **Observation**: There is a negative correlation between "Time of Purchase" (total hours/visits) and "Level of Membership" for certain older demographics.
- **Implication**: Steven Hayes is spending a massive amount of time in the shop (44 units) but remains at Level 3. From my perspective as a developer, this looks like a "leaky bucket" in the UX—perhaps he isn't using the app to scan every purchase, or the loyalty rewards aren't properly incentivizing his specific stay-and-work behavior.
- **Supporting Data**: Member 5 (Hayes) has the highest Time_of_purchase (44) but a Level_of_membership of only 3.

### The Hartford Power-Hub
- **Observation**: The Hartford-based members represent the highest average loyalty levels within the group.
- **Implication**: The Hartford location likely has the best infrastructure for "regulars" like me—reliable Wi-Fi and enough outlets to keep a laptop running for a three-hour sprint.
- **Supporting Data**: Members 1, 3, and 10 are all in Hartford, boasting an average membership level of 11 (significantly boosted by the Webb anomaly, but still robust).

## Trends & Patterns

### 1. The Membership Card Divide
There is a clear tiering between the "Black" and "White" membership cards. In this cohort, 60% of members hold Black cards, while 40% hold White. Interestingly, the Black cardholders occupy the highest level (Level 22) and the lowest level (Level 1) simultaneously. This suggests that the Black card is likely an "entry-point" or a specific tier that doesn't strictly correlate with tenure, unlike my own Gold status which felt like a hard-earned grind.

### 2. The Mid-Career Sweet Spot
The data shows a "sweet spot" for engagement among members in their early 30s to early 40s.
- **Evidence**: Members like Peeler (42, Level 6), Campbell (34, Level 6), and Ashby (29, Level 5) show consistent level-to-time ratios.
- **Persona Interpretation**: This is my peer group—remote workers and freelancers who use the shop as a functional office. We are efficient; we order, we work, and we level up systematically.

### 3. Geographic Fragmentation
The customer base is split across four cities, with Waterbury (40%) and Hartford (30%) being the primary nodes. 
- **Evidence**: IDs 2, 4, 8, 9 are Waterbury-based; 1, 3, 10 are Hartford. 
- **Persona Interpretation**: If I’m looking for a quiet morning, I’m heading to the Cheshire or Bridgeport locations (IDs 5, 6, 7), as they represent the "edges" of our network and likely have less competition for the good chairs.

## Addressing Core Questions

### How does "Time of Purchase" correlate with "Level of Membership"?
Actually, the correlation is surprisingly weak. You’d think more time in the shop equals a higher level, but the data proves otherwise. Steven Hayes (ID 5) has logged 44 units of time but is only at Level 3. Meanwhile, Daniel Webb (ID 10) has only logged 27 units of time but has hit Level 22. This tells me the loyalty program rewards *transaction volume or value* rather than *dwell time*. For a regular who camps out for two hours on one latte, this is a bit of a wake-up call to start ordering that second Oat Milk Cortado if I want to keep my status.

### Is there a demographic trend regarding who holds a "Black" vs "White" card?
The "White" cards seem slightly skewed toward either the very old or the very young. Robert Breton (67) and Joshua Komisarjevsky (33) both hold White cards. However, the age range for "Black" cardholders is broad (29 to 51). From a tech perspective, the Black card seems to be the "Standard" or "Pro" tier, whereas the White card might be a legacy tier or a "Casual" tier that isn't as focused on the rewards grind.

## Actionable Insights

1. **Investigate the "Webb" Workflow**: We should see what Daniel Webb is doing right. If he’s a Hartford local at Level 22 with only 27 time-units, he’s the ultimate efficiency user. Is he pre-ordering on the app? We should use his behavior as a template for other Gold members.
2. **Re-engage the "Lingerers"**: People like Steven Hayes (ID 5) and Robert Breton (ID 2) have high "Time_of_purchase" (44 and 41 respectively) but mid-to-low levels. We should offer them "long-stay" rewards—maybe a discount on a second drink after 90 minutes—to bridge the gap between their presence and their loyalty level.
3. **Targeted Bridgeport/Cheshire Growth**: Members in these areas (Peeler, Hayes, Komisarjevsky) have decent engagement but are isolated. If I were running the program, I’d offer a "Cross-City" bonus to encourage them to visit the Hartford or Waterbury hubs.
4. **App Troubleshooting for Seniors**: Robert Breton is 67 and has spent a lot of time (41) but is only Level 4. We should ensure the mobile interface isn't a barrier for our older regulars who clearly love the shop but might not be "leveling up" due to technical friction.

## Limitations & Caveats
The data doesn't specify what "Time_of_purchase" actually measures (is it minutes, hours, or total transactions?). Without that unit of measure, my "efficiency" calculations are based on the assumption that it represents shop-presence. Additionally, as a Gold member, I don't see "Gold" on this list—only Black and White—which makes me wonder if "Black" is the internal data label for my specific tier. Finally, the "Address" is city-wide; I’d need street-level data to know if these people are my neighbors or if they're commuting in for the better Wi-Fi.

---
*Document generated from Coffee Shop Member Loyalty Data | Alex Chen, Gold Tier Regular*