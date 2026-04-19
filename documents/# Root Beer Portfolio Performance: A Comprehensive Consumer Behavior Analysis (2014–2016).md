# Root Beer Portfolio Performance: A Comprehensive Consumer Behavior Analysis (2014–2016)
*Strategic review of distribution, brand loyalty, and point-of-sale dynamics within the Beer Factory ecosystem.*

## Executive Summary
This report synthesizes transaction records and consumer feedback from the Beer Factory dataset to evaluate our root beer portfolio's performance between 2014 and 2016. High-level findings indicate that while established brands like Barq’s leverage deep historical roots to maintain market presence, emerging consumer preferences for cane sugar over corn syrup—evidenced by a 3,255-unit sales surplus—are reshaping our inventory requirements. Despite significant transaction volume at our Sac State outlets, profitability remains tight for certain wholesale partners, particularly A&W, which currently yields the lowest unit profit in our beverage catalog.

## Context & Overview
The Beer Factory maintains a diverse distribution network sourcing from 23 breweries across North America, complemented by a specialized international link to Australia, which houses exactly one brewery in our current dataset. Our operational focus centers on two primary high-volume locations: Sac State Union and Sac State American River Courtyard. 

Analysis of the `customers` table reveals a sophisticated demographic spread. We currently manage an email subscription list where slightly more than half of the subscribers—approximately 50.84%—are women, representing a core segment of 152 female customers who permit the company to send regular promotional updates. These foundational data points allow us to track the lifecycle of brands like Barq's, identified as the oldest root beer brand in the Beer Factory data with a brewing history dating back no later than 1930, contrasting sharply with River City, the brand with the shortest brewing history in our portfolio.

## Key Findings

### Brand Longevity and Market Maturity
The historical data suggests a strong correlation between brand maturity and consumer trust. Barq's stands out as the root beer brand with the longest history and is formally recognized as the oldest within the Beer Factory dataset. However, "newer" brands have seen varied success. 
- **Observation**: Between 1996 and 2000, we saw a cluster of brand launches. Following a chronological sequence from latest to earliest brew dates, the records highlight Sparky's Fresh Draft, followed by Bulldog, and finally Captain Eli's as the earliest entrant of that specific five-year window.
- **Implication**: Consumers often equate "heritage" with quality, yet younger brands like River City have managed to capture significant attention, even if their reception is polarizing.
- **Supporting Data**: While Barq's represents the legacy tier, River City’s market share is notable; about 28% of ratings for River City (specifically 28.0303%) are five stars, despite it also being the brand that has been worst rated the most times.

### Profitability and Wholesale Constraints
Our pricing models for wholesalers reveal a stark disparity in margin contribution across different packaging formats.
- **Observation**: The average unit profit for wholesalers of canned beers is approximately 1.1878068410462777 per unit. Rounded for reporting, wholesalers earn about $1.19 in profit for each canned beer sold.
- **Implication**: Profitability is highly sensitive to brand identity. A&W is currently identified as the root beer brand with the lowest unit profit available to wholesalers, representing the minimum margin in our distribution portfolio.
- **Supporting Data**: We also observe that for bottled root beers with a purchase price greater than $2, the average purchase price sits at exactly $3.00. This suggests a price ceiling that consumers are unwilling to exceed for standard retail bottles.

### Customer Loyalty and VIP Engagement
The "Beer Factory" top-tier customer segment is led by a distinct group of ten individuals: Tommy Kono, Scott Smith, Ken Rose, Urijah Faber, Kris Ryan, Mildred Deluca, Dick Ruthven, Edith Ryan, Frank-Paul Santangelo, and Eric Hansen.
- **Observation**: Frank-Paul Santangelo remains a case study in high-frequency purchasing. In July 2014 alone, Santangelo made 4 transactions. On a single day—July 7, 2014—he purchased four root beers, including the brands IBC and Dad’s, with exactly one of those items being in a can. 
- **Implication**: VIP customers drive specific volume trends. For example, Santangelo has a documented preference for healthier alternatives, having purchased 11 non-sweetened root beers over his customer lifecycle.
- **Supporting Data**: Other high spenders include Max Baer, who prefers Visa, and Jim Breech, a Discover user who has purchased a total of 23 bottles of beer.

## Trends & Patterns

### 1. Ingredient and Health-Consciousness Trends
A significant shift toward cane sugar is evident in our longitudinal data. We recorded 3,255 more sales of root beers containing cane sugar compared to those using corn syrup. This shift is particularly pronounced among our female demographic; for instance, 140 female customers specifically bought root beer containing artificial sweeteners. Interestingly, our "natural" additives see less traction; on average per day, root beer brands that contain honey sell about 4.38 fewer units than brands that do not contain honey.

### 2. Seasonality and Transactional Volatility
The summer of 2014 provided a high-density data set for consumer behavior. In July 2014, we recorded 10 transactions made by male customers. However, August 2014 showed specific brand stagnation; the total recorded sales of A&W root beers for that month were zero, resulting in a daily average of 0.0. During that same month, Bulldog brand root beers saw minimal movement with exactly two units purchased. By 2016, the market shifted slightly, with 14 canned A&W units purchased throughout the year.

### 3. Payment Method Dominance
Payment processing data indicates that Visa is the most commonly used credit card for purchasing non-alcoholic beer at Beer Factory, representing approximately 34.09% of all recorded transactions. In contrast, MasterCard saw 110 transactions in 2014, while American Express was used in 811 transactions specifically for bottled beer purchases. Customer Anna Himes exemplifies this consistency, having used her MasterCard ten times for payments between late December 2014 and May 2016.

## Addressing Core Questions

### How do location and geography impact sales volume?
Our data confirms that Sac State Union is our primary volume driver, having sold more bottles of beer than any other location with a total of 3,216 transactions. The Sac State American River Courtyard follows closely, accounting for approximately 49.05% of all sales and maintaining roughly 96.27% of the transaction volume seen at the Union. In Folsom, we see a localized preference for Visa, used by 56 customers. Latitude-specific data also shows that Thomas Kemper brand beer is consumed most at the coordinates 38.559615, -121.42243, where we have recorded 2,717 bottled root beer sales.

### Which brands are currently leading in quality perception?
Blue Dog Beverages is currently the brewery associated with the brand holding the highest count of 5-star ratings. Other brands maintaining high-quality tiers (reaching at least five 5-star ratings) include IBC, River City, Frostie, Sprecher, Thomas Kemper, and Virgil’s. Captain Eli’s previously led this category in 2012. Conversely, the brand identified by BrandID 10018 currently holds the highest number of 1-star ratings, though it paradoxically remains the best-selling root beer brand in the dataset with an average star rating of 3.139.

## Actionable Insights

1. **Optimize "Legacy" Marketing**: Leverage the Barq's historical data (oldest brand) to anchor "classic" root beer displays, particularly at Sac State Union where bottle sales are highest.
2. **Cane Sugar Inventory Expansion**: Increase the stock of cane-sugar-based products to address the 3,255-unit preference gap over corn syrup.
3. **VIP Outreach**: Direct marketing should target high-engagement users like Jayne Collins, who has the most reviews among all customers, and Teddy Bruschi, our top-transacting customer for August 2014. 
4. **Subscription Conversion**: Focus on the 41.46% of non-subscribed customers who give ratings above three stars; this group represents a prime audience for mailing list conversion to join our 152 existing female subscribers.
5. **Address Wholesaler Profitability**: Re-evaluate the wholesale pricing of A&W and Diet Stewarts (the latter having the minimum number of purchases) to ensure retail partners remain incentivized to carry the full Dr Pepper Snapple Group line.

## Limitations & Caveats
The current analysis is grounded in the Beer Factory dataset but faces several limitations. While we have robust data for California (showing a mean review count of 40.4 reviews per brand), our regional comparisons are limited; for example, we know Louisiana sold 561 fewer root beer bottles than Missouri, but we lack qualitative feedback from those regions. Additionally, while the average star rating from subscribers is a respectable 3.11, the "silent majority" of non-subscribers may hold different views. Finally, while we track caffeinated sales (averaging 1.2511 units daily), the lack of Twitter advertising data for 21 brands sold in August 2014 limits our ability to measure the impact of social media engagement on these specific sales figures.

***
*Document generated from customers table analysis | Senior BI Lead, Beer Factory Strategy Group*