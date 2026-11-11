# Market data sources: sizing a market and building a target list

Size an education market by counting buyers in free public data, then multiplying by the share you can reach and the price they pay. The datasets below supply the counts. Most are free, and several changed status in 2025 and 2026.

**Applies to:** K-12, higher ed, and workforce. United States, with international sources at the end.

## Numbers founders need often

| Figure | Value | Data year | Source |
|---|---|---|---|
| Regular public school districts | 13,318 | 2022-23 | [Digest table 214.10](https://nces.ed.gov/programs/digest/d23/tables/dt23_214.10.asp) |
| Public schools | 99,388 | 2022-23 | Digest table 214.10 |
| Private schools | 29,727 | 2021-22 | Digest table 214.10 |
| Public school students | 49.4 million | Fall 2024 | [Digest table 203.10](https://nces.ed.gov/programs/digest/d25/tables/dt25_203.10.asp) |
| Private school students | 5.5 million | Fall 2021 | [NCES Fast Facts](https://nces.ed.gov/fastfacts/display.asp?id=372) |
| Public school teachers (full-time equivalent) | 3.2 million | Fall 2022 | NCES Fast Facts |
| Degree-granting postsecondary institutions | 3,896 (1,599 public; 1,614 private nonprofit; 683 for-profit) | 2022-23, provisional | [Digest table 317.10](https://nces.ed.gov/programs/digest/d23/tables/dt23_317.10.asp) |
| Postsecondary enrollment, degree-granting institutions | 19.0 million | Fall 2023 | [Digest table 303.10](https://nces.ed.gov/programs/digest/d24/tables/dt24_303.10.asp) |
| Public K-12 spending | $945.3 billion total; $818.2 billion current | 2022-23 | [Digest table 236.10](https://nces.ed.gov/programs/digest/d25/tables/dt25_236.10.asp) |

The [K-12 landscape](k12-landscape.md) cites NCES's newer 2023–24 counts (13,303 regular districts and 99,297 public schools), which the Digest table had not yet picked up when checked.

District size decides the sales motion. In 2021-22, the 266 districts with 25,000 or more students enrolled 34.3% of all students, and the 3,726 districts with 2,500 or more enrolled 83.2%. The other 9,475 sized districts, 71% of the total, enrolled 16.7% ([Digest table 214.20](https://nces.ed.gov/programs/digest/d22/tables/dt22_214.20.asp)).

## Federal data: what is current

The Education Department fired nearly all the staff of the National Center for Education Statistics in 2025 ([Inside Higher Ed, September 2025](https://www.insidehighered.com/news/faculty-issues/research/2025/09/25/gutted-nces-releases-first-batch-higher-ed-data)). The core counts still arrive. Summary reports, longitudinal studies, and release dates have become less dependable. The status of each dataset below was checked on November 11, 2026.

| Dataset | What it answers | Status | Limits |
|---|---|---|---|
| [Common Core of Data](https://nces.ed.gov/ccd/) (CCD) | Every public district and school, with enrollment and staffing | Current. Digest 2025 tables carry fall 2024 enrollment | No contacts, no spending by product. The legacy file pages are stale; use the file tool |
| [IPEDS](https://nces.ed.gov/ipeds/) | Every institution in federal student aid: enrollment, completions, price, finance, staff | Current. Provisional fall 2025 collection data released July 28, 2026. A new contractor runs the 2026-27 collection ([IHEP, September 2026](https://www.ihep.org/where-things-stand-with-key-postsecondary-data-collections-at-nces/)) | Institution-level only. Researchers reported errors in the September 2025 release that were later fixed, so check for revisions |
| [Digest of Education Statistics](https://nces.ed.gov/programs/digest/current_tables.asp) | Pre-built national tables | Partly stale. Tables post one at a time; many still carry 2022 or 2023 editions | Check the data year on each table, not the edition year |
| [College Scorecard](https://collegescorecard.ed.gov/data/) | Earnings, debt, and completion by institution and field of study | Current. Updated November 2, 2026 | Field-of-study files pool older award years (2014-15 through 2018-19) |
| [NAEP](https://www.nationsreportcard.gov/) | Achievement by state and for some urban districts | Current through 2024 for main reading and math. 2026 results are due in early 2027 ([NCES](https://nces.ed.gov/learn/blog/whats-horizon-2026-nations-report-card)) | No school or student results |
| [Annual Survey of School System Finances](https://www.census.gov/programs-surveys/school-finances.html) (Census) | Revenue, spending, debt, and assets by school system | Current. Fiscal 2024 tables are posted | No vendor or product detail |
| [Civil Rights Data Collection](https://civilrightsdata.ed.gov/) | School-level civil rights indicators, such as harassment and discipline reports | Delayed. 2023-24 data appeared in September 2026, eight months late and as raw files only; 2025-26 is in collection ([Education Week](https://www.edweek.org/leadership/ed-dept-releases-data-on-schools-racial-disparities-months-late/2026/09)) | Collected every other school year; some items were withheld or dropped |
| EDFacts, through [ED Data Express](https://eddataexpress.ed.gov/) | Title I status, graduation rates, chronic absenteeism, by state, district, and school | Lagging. The drafter found 2022-23 as the latest year; the site would not load for the second check | Formula-grant programs only |
| Longitudinal student studies | How students move through college | Mixed. NPSAS continues; Beginning Postsecondary Students was canceled in February 2025 (IHEP, above) | Rarely needed for sizing |

The [Urban Institute Education Data Portal](https://educationdata.urban.org/documentation/) joins CCD, IPEDS, the Civil Rights Data Collection, College Scorecard, and Census poverty estimates behind one free API with consistent identifiers. Start there when you build a target list in code.

## Money and buying signals

- **State and district report cards.** Federal law requires every state and district to publish annual report cards, including per-pupil spending for each school ([20 U.S.C. 6311(h)](https://www.law.cornell.edu/uscode/text/20/6311)). They are the fastest source for a single district and the slowest for 50 states, because each state uses its own format.
- **[USAspending](https://www.usaspending.gov/).** Federal grants and contracts by recipient. Use it to find districts and colleges that hold a specific federal award.
- **[SAM.gov](https://sam.gov/).** Open federal contract opportunities and assistance programs, run by the General Services Administration.
- **State and district procurement portals, and board-meeting records.** Board agendas and minutes list approved purchases, renewals, and vendors. They are public and free, and they are the best evidence of what a district pays a competitor. No free national index exists: search one district at a time, or pay a vendor that collects them. See the [procurement guide](../selling/procurement-guide.md).
- **[Edunomics Lab](https://edunomicslab.org/nerds/).** Georgetown's school-level spending database, NERD$. The lab was updating it when checked and gave access by request.

## Enrollment, demographics, and state finance

- **[National Student Clearinghouse Research Center](https://nscresearchcenter.org/).** The fastest read on postsecondary enrollment. Reporting institutions cover 97% of enrollment at degree-granting institutions in federal aid programs ([methodology note](https://nscresearchcenter.org/current-term-enrollment-estimates/)). Its preliminary fall 2026 report, published October 29, 2026, showed undergraduate enrollment up 0.6% from a year earlier. Reports are free. For the full picture, see the [higher-ed landscape](highered-landscape.md).
- **[WICHE, Knocking at the College Door](https://www.wiche.edu/knocking/).** Projections of high school graduates by state through 2041. The 11th edition, December 2024, projects a national peak in 2025 and a 13% decline by 2041. Use it to pick states.
- **[SHEEO, State Higher Education Finance](https://shef.sheeo.org/).** State appropriations and tuition revenue for public institutions. The fiscal 2025 report found appropriations down 1.0% and full-time-equivalent enrollment up 3.6%. Use it to judge which state systems have money.

## Workforce

The Bureau of Labor Statistics publishes employment and wages for about 830 occupations by state and metro area ([OEWS](https://www.bls.gov/oes/), May 2025 data) and ten-year [employment projections](https://www.bls.gov/emp/) (2025 to 2035, released August 27, 2026). Both are free. [Lightcast](https://lightcast.io/) sells labor market data built from job postings and profiles. Colleges often license it (practitioner observation), so ask a customer to pull a report before you buy. For employer buyers, see [corporate learning and development](corporate-ld.md).

## International

- **[UNESCO Institute for Statistics](https://databrowser.uis.unesco.org/).** Enrollment, teachers, and spending by country: more than 5,000 education indicators, last released February 2026. Country coverage is uneven.
- **OECD.** Education at a Glance is the annual cross-country indicator report, and PISA is the international assessment of 15-year-olds. NCES lists PISA 2025 results as released in September 2026 ([NCES PISA page](https://nces.ed.gov/surveys/pisa/)). OECD's own pages blocked our automated check, so find both on oecd.org.
- **[World Bank EdStats](https://datatopics.worldbank.org/education/).** Education indicators alongside the Bank's economic data, useful for comparing countries by income level.

For entering a specific country, see [international markets](international-markets.md).

## Commercial sources

All of these charge. Buy one only after the free data have defined your segment.

| Source | What you pay for |
|---|---|
| [LISTedTECH](https://listedtech.com/) | Which institution runs which LMS, SIS, or CRM. Company plans start at $3,410 a year |
| [Burbio](https://about.burbio.com/) | District board documents, budgets, strategic plans, RFPs, and vendor payments |
| [GovSpend](https://govspend.com/) | State, local, and education purchasing records and contract renewals |
| [MDR](https://mdreducation.com/) | Educator and administrator contact lists |
| [HolonIQ](https://www.holoniq.com/) | Global market sizing, trend tracking, and competitor mapping |
| Crunchbase and PitchBook | Company funding histories; see the [funding landscape](funding-landscape.md) |

## Bottom-up sizing

Market size = buyers who have the problem × the share you can reach × the annual price.

1. **Define the buyer as a row in a dataset.** "Districts with 2,500 to 24,999 students" is countable. "Schools that care about literacy" is not.
2. **Count.** Filter CCD or IPEDS. Keep the list; it becomes your target list.
3. **Cut to reachable.** Remove buyers you cannot serve: states where you lack required approvals, systems on an LMS you do not integrate with, buyers locked in multi-year contracts.
4. **Apply a price you have charged**, or one a buyer has agreed to in writing.
5. **State the win rate separately.** Market size is every reachable buyer. Your forecast is the fraction you can close.

The worked example below sizes a product sold district-wide to mid-sized districts. The counts are real; the reach, the win rate, and the price are assumptions for illustration.

| Step | Calculation | Result |
|---|---|---|
| Districts with 2,500 to 24,999 students (2021-22, Digest table 214.20) | 610 + 996 + 1,854 | 3,460 districts, 48.9% of students |
| Reachable: states where you can sell today, assumed one-quarter | 3,460 × 0.25 | 865 districts |
| Reachable market at $30,000 a year | 865 × $30,000 | $26.0 million |
| Forecast at a 10% win rate | 865 × 0.10 × $30,000 | About 87 districts, $2.6 million a year |

The same method works in higher ed: start from the 3,896 degree-granting institutions, filter in IPEDS by sector and enrollment, and remove campuses on an LMS you do not support (see [interoperability](../product/interoperability.md)).

## Why top-down numbers fail

ScaleU's view: a slide that puts the edtech market at some number of billions tells an investor nothing about your company. Those totals mix countries, segments, hardware, and tutoring, and name no buyer. Total K-12 spending fails the same way, because a district cannot redirect most of the $945.3 billion to software. An investor wants the count of buyers, the list behind the count, and the price a buyer has paid. Check the result against [unit economics](../business/unit-economics.md), and see [fundraising](../business/fundraising.md) for how investors read it.

## Related guides

- [K-12 landscape](k12-landscape.md)
- [Higher-ed landscape](highered-landscape.md)
- [Procurement guide](../selling/procurement-guide.md)
- [Buyer personas](../demand/buyer-personas.md)
- [Unit economics](../business/unit-economics.md)
- [Glossary](../glossary.md), for dataset acronyms

---
*Facts checked 2026-11-11 against the linked sources, with an independent spot-check the same day: every headline count and its data year was confirmed at the NCES table, the district-size shares and the worked example were recomputed, and the status of IPEDS, College Scorecard, NAEP, the Census finance survey, the Civil Rights Data Collection, the Clearinghouse, WICHE, SHEEO, BLS, UNESCO, and PISA was confirmed at the linked pages. No figure needed correction. Not confirmed in the second check: the latest year on ED Data Express (the site would not load) and the OECD pages (blocked). The commercial sources' descriptions, other than LISTedTECH's price, were not rechecked. Statements labeled as ScaleU's view or practitioner observation are judgment, not data.*
