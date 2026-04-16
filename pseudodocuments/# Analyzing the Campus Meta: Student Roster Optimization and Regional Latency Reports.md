# Analyzing the Campus Meta: Student Roster Optimization and Regional Latency Reports
*A deep dive into the current student player base, squad composition, and regional distribution.*

## Executive Summary
After data-mining the current student table, it’s clear that Major 600 is the absolute "S-Tier" meta, comprising over 50% of the total player base. While the average student level (age) sits around 19, we have a few "veteran" outliers in the level 26-27 range who likely have significantly more XP in the academic grind. Regional distribution shows a heavy East Coast server presence (BAL, PIT, PHL), which is optimal for low-latency LAN connectivity, though our international players in HKG and LON are dealing with serious ping issues.

## Context & Overview
Look, if we’re going to survive this semester, we need to know who we’re loading into the lobby with. This table represents our current "guild roster"—the 34 active accounts (students) currently registered. As a CS major, I’m looking at this data to identify who’s in the same "quest lines" (Majors), who the "NPC quest givers" (Advisors) are that handle the biggest squads, and where everyone is logging in from. Understanding the distribution of our cohort helps us optimize for group projects (squads) and identify potential carry players for the harder 400-level courses.

## Key Findings

### Major 600: The S-Tier Pick
- **Observation**: A massive 53% of the students (18 out of 34) have selected Major 600.
- **Implication**: This is the dominant meta. If Major 600 represents Computer Science or Engineering, the "market" is saturated, but it also means there's a huge pool for peer-to-peer support. However, competition for "loot" (internships/grades) will be highest here.
- **Supporting Data**: StuID 1001 through 1019 are almost exclusively Major 600, with a few others scattered throughout.

### The Age Bracket "Skill Ceiling"
- **Observation**: The student levels (Age) range from a "low-level" 16 (Susan Lee, 1015) to "veteran" 27 (Bruce Wilson, 1017).
- **Implication**: We have a wide range of experience. The 16-17 year olds are likely high-IQ speedrunners who skipped grades, while the 26-27 year olds (Gompers, Wilson, Schmidt) are the "raid leaders" who probably have real-world work XP.
- **Supporting Data**: Only three students are age 26 or higher (1005, 1017, 1035), making them rare spawns in a sea of 18-20 year olds.

### Advisor Squad Loads
- **Observation**: Certain Advisors are carrying a much heavier "player load" than others.
- **Implication**: If you’re under Advisor 2192 or 2311, expect slower "tick rates" on email responses. They are managing high-density squads compared to someone like Advisor 5718 who only has two players (1034, 1035).
- **Supporting Data**: Advisor 2192 manages 4 students (1009, 1010, 1016, 1019), whereas Advisor 8423 only has one (1004).

### Regional Server Density
- **Observation**: The student base is clustered in specific "regions," notably BAL (Baltimore) and PIT (Pittsburgh).
- **Implication**: These are our primary "regional servers." Students in these areas have the highest probability of forming offline squads for study sessions or couch co-op.
- **Supporting Data**: City code BAL has 4 students (1001, 1006, 1008, 1024), and PIT also has 4 (1007, 1012, 1018, 1025).

## Trends & Patterns

### 1. The Disconnect (The Missing Player)
**Pattern**: There is a conspicuous gap in the sequence of Student IDs.
**Evidence**: The StuID moves from 1012 to 1014. StuID 1013 is completely missing from the table.
**Interpretation**: In gaming terms, 1013 "DC’d" (disconnected) or got banned. It’s a literal "404 Player Not Found." In a dataset this size, a missing sequential ID usually points to a registration drop-out or a data-entry "lag" spike.

### 2. The "Early-Game" Demographic
**Pattern**: The 18-year-old cohort is the largest single-age demographic.
**Evidence**: There are 10 students aged 18 (1001, 1006, 1007, 1014, 1019, 1024, 1025, 1027, 1033, 1034).
**Interpretation**: This is the "Freshman Class" meta. They’re high energy, probably still grinding their "Tutorial" phases, and make up the core of our social player base.

### 3. High-Latency International Players
**Pattern**: While the majority are US-based, we have a clear "Overseas Server" contingent.
**Evidence**: We see HKG (Hong Kong) appearing 3 times (1002, 1015, 1026), LON (London) once (1017), and PEK (Beijing) once (1029).
**Interpretation**: These players are likely dealing with massive time-zone "ping." If we're setting up a Discord call for a group project, these guys are going to be "lagging" in terms of availability. We need to "buff" our scheduling to accommodate them.

## Addressing Core Questions

### How does the squad composition look for potential team-based challenges?
Based on the table, if we’re looking to form a balanced team, we have a surplus of "DPS" (Major 600 students). However, the Major 520 (5 players) and Major 550 (5 players) students are the specialized builds that could bring unique utility to a group. The age distribution suggests we have enough "tanks" (older, experienced students) to lead, but the group is overwhelmingly "young" (18-20), which is great for "grinding" long hours during finals week.

### Who are the "power users" in the dataset?
If "power" is defined by diversity of experience, Bruce Wilson (1017) is the MVP candidate. He’s the oldest player (Level 27), he’s in the high-pop Major 600, and he’s connecting from the LON (London) server. That’s a high-difficulty playthrough. On the other side, Susan Lee (1015) is the youngest player (Level 16) in the same Major, meaning she’s effectively a "prodigy" build.

## Actionable Insights

1. **Recruit from Major 600 for the CS Guild**: Since this is the most popular build, we should start a Major 600-specific Discord channel. With 18 potential members, it’ll be the most active "sub-reddit" of our student base.
2. **Optimize the PIT/BAL/PHL LAN Party**: We have 11 students total in the Pittsburgh, Baltimore, and Philadelphia area. This is a "localized cluster." We should organize an IRL meet-up or LAN event since their "ping" to a central location is negligible.
3. **Monitor the "Low-Level" Prodigies**: Keep an eye on the 16-17 year olds (1010, 1015, 1016, 1022, 1029). They’ve entered the university "server" early, which usually means they have high "Int" stats but might need a "carry" when it comes to the social/living-away-from-home aspects of the game.
4. **Load-Balance Advisor 2192**: If you're a new player looking for an advisor, avoid 2192, 1148, 8722, 2311, and 8772. They are "over-capped" with 3-4 students each. Seek out Advisor 8423 or 8918 for that 1v1 "coaching" experience.

## Limitations & Caveats
This table gives us the "base stats" but lacks the "gear" (GPA, specific skills, or tech stacks). We also don't have "active/inactive" status—just because a student is on the roster doesn't mean they haven't "rage-quit" since the last update. Furthermore, the missing StuID 1013 is a "fog of war" area—we don't know if that's a deleted character or a server error. Finally, "Major" codes (e.g., 600, 520) are currently "un-translated" in the patch notes; I'm assuming 600 is the "meta" (CS/Eng) based on the population, but it could just as easily be "Intro to Underwater Basket Weaving."

---
*Document generated from Student Roster Database | Alex, CS Major & Dedicated Gamer*