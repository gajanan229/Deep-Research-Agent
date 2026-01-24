# Question 3 - V08-2

                **Question ID:** Q3  
                **Title:** Cross-Border CBDC Regulatory Landscape  
                **Category:** professional_specialized  

                ---

                ## Original Question

                Central Bank Digital Currencies (CBDCs) are advancing rapidly with over 130 countries 
exploring or piloting implementations, yet regulatory frameworks remain fragmented 
across jurisdictions.

Analyze the emerging regulatory and operational landscape for CBDCs by examining:

1. How do the design choices of major CBDC projects (China's e-CNY, EU's digital euro 
   pilot, US research programs, India's e-rupee) differ in terms of privacy models, 
   programmability, and cross-border interoperability?

2. What are the key regulatory tensions between AML/KYC requirements and privacy 
   preservation in different CBDC implementations, and how are jurisdictions attempting 
   to balance these competing objectives?

3. How do different CBDC architectures (direct model, two-tier system, hybrid approaches) 
   affect the role of commercial banks and implications for financial stability?

4. What progress has been made on cross-border CBDC interoperability projects (mBridge, 
   Dunbar, Icebreaker) and what technical and regulatory barriers remain?

5. How are existing payment regulations (PSD2 in EU, money transmission laws in US) 
   being adapted or challenged to accommodate CBDC operations?

Synthesize these regulatory developments into a comparative framework showing how 
different jurisdictions are approaching CBDC deployment tradeoffs.


                ---

                ## Research Report

                # Research Report

**Thesis:** As central banks pursue CBDCs, national design choices reveal consistent tradeoffs—privacy, programmability, and banking-sector roles are being balanced differently across jurisdictions—producing fragmented regulatory approaches that hinder cross-border interoperability unless harmonized AML/KYC, data-protection, and technical standards are adopted.

---

## Introduction: CBDCs, Policy Context, and the Central Tradeoffs

Building on the first section’s overview of why central banks are revisiting money and payments, this introduction frames the report’s core questions and specifies the evaluative framework used to compare policy choices across jurisdictions. Central banks worldwide have accelerated public inquiry and experimentation with central bank digital currencies (CBDCs) in response to rapid private‑sector innovation in digital payments, wallets, and new digital assets. The Federal Reserve’s report Money and Payments: The U.S. Dollar in the Age of Digital Transformation describes the U.S. effort as a consultative, evidence‑gathering first step to weigh potential benefits and risks of a U.S. CBDC and to sustain public dialogue [1]. More broadly, as of Feb 6, 2025, multiple central banks were actively exploring, testing, or piloting retail and wholesale CBDC models, indicating a rapid shift from conceptual study to operational experimentation across jurisdictions [2].

This report organizes around three policy questions: how do alternative privacy models affect financial integrity and user trust; how does programmability reshape payment rails and contractual automation; and what distributional roles should commercial banks and nonbank intermediaries play in liquidity and access? To move beyond broad statements of tradeoffs, the report applies an explicit, repeatable evaluation framework. For each jurisdiction we assess six dimensions with defined indicators:

- Privacy and data protection: degree of data minimization, transaction linkability (unlinkable/partially linkable/fully linkable), on‑ledger versus off‑ledger data storage, legal limits on access, and retention periods.  
- Financial integrity (AML/CFT): coverage of AML rules, transaction monitoring capability (real‑time scoring, rule complexity), SAR/STR reporting thresholds, and estimated false positive/negative detection tradeoffs.  
- Programmability and composability: supported scripting expressiveness, determinism guarantees, external oracle reliance, and native support for conditional settlement or escrow.  
- Distributional model and banking roles: settlement architecture (central‑bank direct, two‑tier, or intermediated hybrid), deposit insurance implications, and liquidity backstops.  
- Interoperability and cross‑border settlement: message standards, atomicity of cross‑border settlement, finality latency, and reliance on intermediaries.  
- Payments safety and operational resilience: settlement finality guarantees, failover mechanisms, throughput and latency targets, and incident response arrangements.

For transparency and comparability, the report translates qualitative evidence (laws, technical specifications, pilot results, supervisory guidance) into semi‑quantitative assessments (low/medium/high and a brief rationale) across these indicators. That operational approach makes tradeoffs explicit: for example, stricter data minimization scores high on privacy but may lower scores on transaction monitoring capability, while richer programmability can expand use cases but raise complexity and operational risk. The remainder of the report applies this framework to current designs and pilots to identify feasible, accountable CBDC options for policymakers, industry, and users. Building on this explicit set of evaluative criteria, the next section establishes the technical and regulatory vocabulary the report uses to score and compare jurisdictional approaches.

## Background and Technical Foundations: CBDC Types, Architectures, and Regulatory Baselines

Building on the evaluative criteria in the previous section, this background section establishes the operational definitions and technical patterns the report uses consistently when comparing jurisdictional CBDC choices. CBDCs are usefully classified along two orthogonal axes, which this report treats as precise, operational definitions. Scope: “Retail” CBDCs are intended for general‑purpose use by households and businesses for everyday payments; “wholesale” CBDCs are limited to financial‑sector participants for large‑value or interbank settlement. Technical form: “Account‑based” systems map balances to identifiable accounts controlled via authentication and access controls; “token‑based” systems treat monetary units as bearer objects whose transfer requires transferring control of the token (often implemented cryptographically). Where designs mix identifiable accounts with bearer tokens, we label them “ledgered tokens” or “hybrid tokens.” These distinctions matter because account‑based designs prioritize identity, recoverability, and centralized controls, while token‑based designs are comparatively amenable to offline transfer and bearer‑style privacy but raise double‑spend and custody challenges.

Key terms used throughout the report are defined here to avoid ambiguity. Programmability refers to attaching conditional logic to money (for example, time/recipient constraints, automated refunds, or event‑triggered disbursements), implemented either inside the ledger (smart‑contract semantics) or at the wallet‑provider/API layer. Privacy by design denotes deliberate minimization of personal data collection, role separation, and technical controls (pseudonymization, selective disclosure, encryption, and auditability) built into the system rather than added later. Tiered verification (also called tiered identity) is a policy mechanism that associates progressively stronger identity assurance and transaction limits: low‑assurance, low‑limit tiers allow simpler onboarding; high‑assurance tiers require full KYC for higher limits or suspicious activity. “Offline” operation denotes the ability to complete a value transfer without real‑time network connectivity; this requires explicit mechanisms for double‑spend risk mitigation (hardware secure elements, expiry, periodic reconciliation) and typically constrains transaction size and risk exposure.

Three recurring architecture patterns frame governance and operational tradeoffs. Direct models have the central bank maintaining end‑user accounts (maximizing control and settlement finality but increasing central operational burdens). Two‑tier models place customer‑facing services with banks or licensed intermediaries while the central bank issues settlement balances (reducing central operational load and leveraging private‑sector intermediation). Hybrid models combine central‑bank settlement with private execution or token layers (seeking a middle ground between control, innovation, and scalability). Finally, CBDC design must sit inside an existing regulatory baseline—AML/KYC obligations, data‑protection regimes (for example, GDPR‑style principles), and payments rules (such as open‑banking standards and money‑transmitter statutes)—which constrain feasible anonymity, require traceability or tiering for higher‑value activity, and shape how programmability or cryptographic privacy tools can be used without undermining compliance. Throughout the report we adopt the definitions above; when a jurisdiction or project uses these terms differently, we explicitly map its usage to these operational meanings before scoring or comparison. Having established these technical definitions, architecture patterns, and the regulatory baseline, the next section applies this shared vocabulary to compare how major CBDC projects balance privacy, functionality, and AML/KYC obligations in practice.

## Comparative Design Choices: Privacy Models, Programmability, and AML/KYC Tradeoffs (China, EU, US, India)

Building on the shared vocabulary and architecture patterns established earlier, this section compares four leading CBDC efforts using consistent, operational definitions so readers can see how specific design choices map to regulatory aims and likely market effects. Definitions (operational). To avoid ambiguity, this comparison uses the following working definitions. "Programmability" means explicit, on‑ledger or wallet‑level support for conditional logic (e.g., time locks, merchant‑specific acceptance, automatic rebates) that can be enforced without off‑chain adjudication. "Privacy by design" denotes an explicit engineering posture that minimizes collection, retention, and linkage of personal data through techniques such as data minimization, selective disclosure, and cryptographic protections; it does not imply absolute anonymity and must be interpreted against AML/KYC and data‑protection law. "Account‑based" systems authenticate identity at the point of access and associate balances with accounts; "token‑based" systems validate ownership of bearer‑like tokens or cryptographic credentials. "Tiered verification" refers to a graduated identity regime in which low‑value wallets require minimal ID and higher‑value tiers require stronger KYC. "Offline capability" means the ability to transfer value directly between devices without an immediate online verification call to a central ledger or intermediary.

China (e‑CNY). China’s design emphasizes scale, state control, and operational traceability. The e‑CNY uses tiered verification: lower‑risk wallets retain limited pseudonymity while higher tiers are linked to strong identity and account records. A concrete policy change: the People’s Bank of China will require commercial banks to pay interest on eligible e‑CNY wallet balances starting January 1, 2026, a move expected to increase the attractiveness of holding CBDC and to create new transmission and monitoring vectors for monetary and supervisory authorities [1][2]. These design choices—programmability explored in narrow, state‑directed use cases and strong identity linkage at higher tiers—reflect regulatory rationales: supporting direct policy transmission, preserving financial stability, and enabling crime prevention and compliance, with limited privacy for small transactions but clear traceability where regulators deem necessary.

European digital euro. The ECB frames the digital euro with an explicit "privacy by design" objective and states it aims to offer “the highest privacy levels of any electronic payment option,” while also seeking inclusion and resilience in payment options [3]. That aspiration is qualified in practice by EU legal constraints: GDPR data‑protection obligations, AML rules, and payment services regulation limit any design’s ability to deliver unconditional anonymity. In operational terms, EU workstreams emphasize data minimization, wallet tiering and transaction limits to reduce KYC burdens for small payments, and technical safeguards (e.g., selective disclosure) to reconcile privacy with mandated suspicious‑activity reporting. The regulatory rationale balances civil‑liberties protection and user trust against statutory AML obligations and market‑integrity concerns.

India (e‑rupee). Public material and program statements show that India’s design priority includes financial inclusion and targeted policy delivery; pilots and statements have explored offline transfer modes and programmatic uses (for example, conditional transfers and subsidy delivery), though detailed, public technical specifications are more limited than for China or the EU. Consequently, descriptions of India’s approach should be read as an emphasis on inclusion and operational programmability for policy implementation rather than as a fully specified technical blueprint. The regulatory rationale centers on widening basic access, reducing leakage in transfers, and enabling precise fiscal execution while managing AML/KYC through tiering and transaction limits.

United States (research and policy analysis). U.S. work has been largely exploratory and analytic rather than operational deployment. Key federal outputs (for example, the Federal Reserve’s reviews and the Money and Payments discussion) stress several recurring constraints: legal authority and the need for congressional authorization to change core monetary and deposit insurance arrangements; privacy and civil‑liberties tradeoffs; potential distributional effects on bank funding and credit intermediation; and the operational burden of AML/KYC compliance. In policy framing, programmability is discussed primarily as a discretionary policy tool (e.g., targeted benefits, emergency liquidity distribution) but raises concerns about legal mandates, enforceability, and macro‑financial side effects. The U.S. posture is therefore cautious, focusing on design options that would limit undue disruption to bank intermediation and preserve existing legal protections.

How design choices map to AML/KYC and intermediation outcomes. Across jurisdictions, tiered verification is the principal operational compromise: it tries to preserve cash‑like privacy for low‑value retail use while concentrating KYC and reporting on higher‑risk activity. Strong identity linkage and traceability (as emphasized in China) make AML surveillance and enforcement straightforward but increase the potential for deposit substitution away from banks if CBDC becomes an attractive, interest‑bearing alternative; the PBOC’s requirement that banks pay interest on eligible e‑CNY balances from 2026 is a concrete step that will alter incentives for deposit holdings and monetary‑policy transmission [1][2]. Privacy‑centered designs (as pursued conceptually in the EU) seek data‑minimizing architectures and legal‑tech solutions that satisfy AML obligations without wholesale data collection, which may help preserve commercial bank deposit bases by making retail CBDC less attractive as a bank‑substitute while protecting user data [3]. Programmability affects liquidity and intermediation by enabling conditional holding or spending rules (targeted subsidies, time‑limited vouchers) that can channel demand and reduce fungibility of balances; this can lower substitution pressures but complicate banks’ liquidity management and require coordination on settlement finality and intraday credit. In short, privacy, programmability, and tiering are not only civil‑liberties or technical choices: they materially shape who intermediates money, how funds flow, and which macro‑financial risks emerge. With these operational comparisons in hand, the following section examines how those privacy, programmability, and offline access choices concretely affect bank intermediation, deposit flows, and macro‑financial stability.

## CBDC Architectures and the Role of Commercial Banks: Two-Tier, Direct, and Hybrid Models and Financial Stability Implications

Design choices about privacy, programmability, and offline access also shape who intermediates money and how payment flows are routed; next we assess how those choices map onto macro‑financial outcomes by altering banks’ traditional roles. CBDC architectures differ markedly in how they allocate deposit intermediation, payment provision, and liquidity management between the central bank and commercial banks. In a two‑tier model the central bank issues CBDC but relies on banks and payment service providers to onboard users, handle KYC/AML, and provide front‑end services; this preserves much of banks’ deposit base and their role in credit intermediation. In a direct model the central bank interfaces directly with end users, which can shrink banks’ deposit funding and compress their role as intermediaries unless compensating market structures are created. Hybrid models—whether via intermediated wallets, co‑managed accounts, or a split‑service approach—seek to retain banks’ distribution and maturity‑transformation functions while offering a central‑bank digital settlement asset.

These architecture choices matter because CBDC can exert two distinct pressures on banks. “Slow disintermediation” describes gradual deposit substitution in normal times as households and firms rebalance portfolios toward a risk‑free central bank liability, potentially raising banks’ funding costs and shrinking balance sheets. “Fast disintermediation” occurs during episodes of banking stress when the convenience and perceived safety of CBDC make rapid withdrawals more likely, expanding the scope for runs; empirical and theoretical work highlight a larger willingness of households to shift into CBDC in distressed conditions, amplifying run risk [2][1]. Both channels imply larger central‑bank balance sheets and new liquidity‑management demands for monetary authorities.

Policymakers can mitigate these risks through design levers: holding limits or tiered remuneration to preserve banks’ deposit bases; limits on retail convertibility or velocity controls to blunt run dynamics; interest‑rate design and tiered pass‑through to avoid abrupt funding cost shifts for banks; and strengthened backstop and lender‑of‑last‑resort facilities to manage transitions. Carefully calibrated hybrids and clear operational responsibilities for banks and the central bank can retain the payments efficiency gains of CBDC while protecting credit intermediation and financial stability. With these tradeoffs in mind, the next section surveys how cross‑border pilots and technical designs address settlement and messaging challenges—and how interoperability choices interact with the distribution models described here.

## Cross-Border Interoperability and Payment-Regulation Alignment: mBridge, Dunbar, Icebreaker, PSD2, and US Money Transmission Challenges

Building on the prior discussion of how CBDC architectures redistribute intermediation and liquidity roles, this section examines how recent cross‑border pilots attempt to reconcile technical interoperability with heterogeneous regulatory regimes. Three high‑profile international pilots—mBridge, Dunbar, and Icebreaker—have become focal points for testing both DLT‑based settlement mechanics and cross‑jurisdictional rule alignment. Project mBridge in particular advanced to a minimum viable product stage in mid‑2024 after multi‑year collaboration among participating central and commercial banks, demonstrating instant cross‑border settlement on a shared ledger and serving as a concrete proof of concept for multi‑CBDC settlement models [1]. Institutional governance of these pilots has been dynamic: in late‑2024 the BIS unexpectedly withdrew operational oversight of mBridge, a change that has shifted leadership and raised questions about multilateral governance arrangements for such platforms [2].

Technically, the pilots are converging on a small set of approaches: atomic settlement to eliminate payment‑vs‑payment risk, interoperable bridges that link country‑specific ledger domains, and common messaging or token standards that preserve semantic interoperability across systems. Atomic or conditional settlement reduces corridor liquidity needs by ensuring irrevocable, simultaneous exchange of assets; bridges and gateway architectures allow participating jurisdictions to retain domestic control over monetary and access rules while transacting across rails; and common messaging profiles (or ISO‑aligned wrappers) help map diverse legacy payment semantics into DLT contexts. These approaches lower some operational frictions but introduce coordination demands—consensus on message schemas, shared dispute‑resolution processes, and synchronized operating hours—without resolving legal heterogeneity.

Regulatory and compliance barriers remain the most intractable impediments to scalable interoperability. Pilots expose stark divergence in AML/KYC standards, privacy expectations, and data‑localization laws that complicate on‑chain identity and transaction screening. Existing frameworks such as PSD2 in Europe and U.S. money‑transmitter regimes are being stretched: PSD2’s open‑banking orientation aligns with interoperability aims but raises privacy‑AML tradeoffs, while U.S. state‑level money‑transmitter licensing regimes and federal supervision create fragmentation that complicates cross‑border operator models. Practical fixes under consideration include modular interoperability standards that separate settlement rails from compliance interfaces, standardized AML information‑sharing protocols, and legal memoranda to align liability and finality across jurisdictions. Together, these technical and legal workstreams suggest pilots can prove technical viability but will require sustained regulatory cooperation to scale. The following section will cluster jurisdictional strategies and evaluate policy levers that can reconcile the tradeoffs between privacy, AML, and financial‑stability objectives.

## Synthesis and Regulatory Framework: Comparative Tradeoffs, Clustering of Jurisdictional Approaches, and Policy Options

Building on recent pilot results that demonstrated technical feasibility but highlighted governance and regulatory divergence as the principal interoperability barriers, this section synthesizes those findings into a comparative regulatory framework and identifies policy levers to reconcile competing objectives. Distributed ledger pilots have surfaced three dominant jurisdictional postures toward CBDC and cross‑border payment architectures: (1) privacy‑first regimes that prioritize strong data minimization and user anonymity; (2) control‑first regimes that emphasize centralized oversight, strict KYC/AML controls, and narrow licensing; and (3) interoperability‑focused regimes that prioritize standards, mutual recognition, and platform‑agnostic connectivity. Framing these approaches as points on a tradeoff continuum clarifies how each addresses — and exacerbates — policy tensions: privacy‑first designs reduce surveillance risk but complicate compliance with AML obligations; control‑first designs simplify regulatory oversight but can impair financial inclusion and cross‑border utility; interoperability‑focused designs ease cross‑border flows but require significant coordination on legal and operational governance.

Reconciling these tensions calls for layered, modular policy architectures rather than binary choices. A tiered privacy model can reconcile privacy and AML by calibrating data visibility to transaction risk: low‑value, low‑risk retail use could retain strong pseudonymity, while higher‑value or flagged transactions trigger progressively greater identity disclosure under predefined legal thresholds. Complementing tiers with airtight audit trails and judicially supervised access gates balances individual privacy with law enforcement needs. Parallel to privacy tiers, standardized AML information‑sharing protocols — specifying minimum data elements, data retention windows, and privacy safeguards — can permit timely cross‑border investigations while limiting unnecessary data exposure.

Interoperability should be pursued through modular technical and legal standards that decouple settlement rails from compliance and governance modules. Modular standards allow jurisdictions to plug in local compliance modules (e.g., KYC registries, sanctions filters) while preserving common messaging, settlement primitives, and proof-of‑finality semantics. International cooperative mechanisms — mutual legal assistance frameworks specialized for digital asset flows, regulatory sandboxes for cross‑jurisdictional testing, and multilateral memoranda of understanding on licensing reciprocity — can reduce frictions from divergent licensing and localization regimes. Finally, governance design must embed dispute‑resolution processes and contingency protocols to preserve stability and inclusion during stress events. Together, these levers create a pragmatic policy palette enabling jurisdictions to pursue domestic priorities while achieving practical cross‑border interoperability. The following section distills these comparative findings into actionable recommendations for policymakers and industry, and outlines an agenda for further research on monetary‑policy implications, financial‑stability monitoring, and scalable privacy technologies.

## Conclusion and Future Directions: Recommendations and Research Agenda

Building on the typology of jurisdictional archetypes and the policy levers identified earlier, this concluding section synthesizes those findings into concrete recommendations and a targeted agenda for further research. The regulatory landscape for digital money requires a coordinated set of legal, operational, and technical reforms that reconcile competing policy objectives—privacy, anti‑money laundering (AML), financial stability, and inclusion. First, legal reform should clarify the status and permissible uses of tokenized money, establish licensing pathways for varied intermediaries, and codify privacy safeguards that enable tiered access to identity data for legitimate law enforcement purposes while protecting end‑user confidentiality. These reforms should be accompanied by clear supervisory mandates and enforceable compliance standards so that innovation does not outpace oversight.

Second, international AML/KYC cooperation must move from ad hoc exchanges toward standardized, secure information‑sharing protocols. Policymakers should endorse interoperable KYC schemas, common trust frameworks for identity attestation, and privacy‑preserving mechanisms for cross‑border queries that minimize data exposure. Practical steps include mutual recognition of vetted identity providers, routinized supervisory cooperation, and pilot programmes to test secure cross‑border traceability under strict legal gateways.

Third, technical standards and modular architectures are essential to enable cross‑jurisdictional interoperability without one‑size‑fits‑all rules. Standards work should prioritize plug‑and‑play interoperability layers, consensus on minimal audit trails, and the integration of scalable privacy technologies—such as selective disclosure, cryptographic proofs, and federated analytics—so that compliance and privacy are both achievable at scale. Industry, standards bodies, and central banks should jointly develop reference implementations and open testbeds.

Finally, a prioritized research agenda will strengthen policymaking. Key topics include rigorous study of monetary‑policy transmission in environments with tokenized holdings and programmable money; development of monitoring tools for cross‑border liquidity and systemic risk under new settlement geometries; and interdisciplinary work to advance scalable, privacy‑preserving cryptographic and federated analytics techniques. Empirical pilots, regulatory sandboxes, and multi‑jurisdictional stress tests should accompany theoretical work to generate actionable evidence for decisionmakers. These recommendations and research priorities set the stage for the report’s final reflections, which synthesize implications for policymakers, industry, and researchers.

---

## References

[1] Central Bank Digital Currency ( CBDC ) - Federal Reserve Board. https://www.federalreserve.gov/cbdc-faqs.htm

[2] CBDC : Your essential guide to central bank digital currencies. https://www.mastercard.com/us/en/news-and-trends/stories/2025/central-bank-digital-currency-cbdc-vs-cryptocurrency.html

[3] Ripple Unveils Ambitious XRPL 2026 Roadmap Focused on Privacy .... https://coinalertnews.com/news/2026/01/03/8594f897

[4] Cryptocurrencies vs. CBDCs: Navigating the Divergent Paths of Digital.... https://bitparse.com/cryptocurrencies-vs-cbdcs-navigating-the-divergent-paths-of-digital-money/

[5] Digital currencies Research Papers - Academia.edu. https://www.academia.edu/Documents/in/Digital_currencies

[6] An Insight Into CBDC (Central Bank Digital. https://www.ijcrt.org/papers/IJCRT2406897.pdf

[7] COMMON definition in American English | Collins English.... https://www.collinsdictionary.com/us/dictionary/english/common

[8] common - WordReference.com Dictionary of English. https://www.wordreference.com/definition/common

[9] PANews Original｜Digital Yuan 2.0 Launches, Paying Users to Hold .... https://x.com/PANewsEN/status/2013813755763925069

[10] China's e-CNY: Setting the Global Standard for CBDC Innovation. https://www.linkedin.com/pulse/chinas-e-cny-setting-global-standard-cbdc-innovation-mohammad-arif-pi7fc

[11] Digital euro and privacy - European Central Bank. https://www.ecb.europa.eu/euro/digital_euro/features/privacy/html/index.en.html

[12] 2026 Year in Preview: European Digital Regulatory Developments .... https://www.wsgr.com/en/insights/2026-year-in-preview-european-digital-regulatory-developments-for-companies-to-watch-out-for.html

[13] India's central bank proposes linking BRICS' digital currencies .... https://www.reuters.com/world/india/indias-central-bank-proposes-linking-brics-digital-currencies-sources-say-2026-01-19/

[14] India Proposes Including CBDC Interoperability Issue on Agenda for .... https://www.ainvest.com/news/india-proposes-including-cbdc-interoperability-issue-agenda-2026-brics-summit-2601/

[15] CBDC and Banks: Disintermediating Fast and Slow - SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4838345

[16] CBDC and banks: disintermediating fast and slow. https://www.bis.org/publ/work1280.htm

[17] two - WordReference.com Dictionary of English. https://www.wordreference.com/definition/two

[18] Two : Definition, Meaning, and Examples - US Dictionary. https://usdictionary.com/definitions/two/

[19] Scenarios for the Federal Reserve Board's 2026 .... https://www.sifma.org/advocacy/letters/scenarios-for-the-boards-2026-supervisory-stress-test-joint-trades

[20] Agencies issue final rule to modify certain regulatory .... https://www.federalreserve.gov/newsevents/pressreleases/bcreg20251125b.htm

[21] Project mBridge reached minimum viable product stage. https://www.bis.org/about/bisih/topics/cbdc/mcbdc_bridge.htm

[22] Top central banks forge ahead with closely watched cross-border .... https://www.933thedrive.com/2026/01/14/top-central-banks-forge-ahead-with-closely-watched-cross-border-payments-testing/

[23] PBOC to require interest on e-CNY wallets starting January 1, 2026. https://bingx.com/it-it/news/post/pboc-to-require-interest-on-e-cny-wallets-starting-january

[24] China shifts digital yuan policy to add wallet interest - CoinGeek. https://coingeek.com/china-shifts-digital-yuan-policy-to-add-wallet-interest/

[25] Cached. search://7d3ef4cfbb489e7a

[26] RBI to introduce offline eRupee transactions soon: Shaktikanta Das. https://www.thehindu.com/business/Industry/rbi-to-introduce-offline-erupee-transactions-soon-shaktikanta-das/article67824286.ece

[27] Digital rupee - Wikipedia. https://en.wikipedia.org/wiki/Digital_rupee

[28] [PDF] Money and Payments: The U.S. Dollar in the Age of Digital .... https://www.federalreserve.gov/publications/files/summary-of-public-comments-money-and-payments-20230420.pdf

[29] Public Comments - Federal Reserve Board. https://www.federalreserve.gov/cbdc-public-comments.htm

[30] Retail Central Bank Digital Currencies (CBDC), Disintermediation .... https://www.mdpi.com/2674-1032/1/4/26

[31] BIS releases full report on mBridge wholesale CBDC platform after .... https://digitalpoundfoundation.com/bis-releases-full-report-on-mbridge-wholesale-cbdc-platform-after-successful-pilot/

[32] BIS releases full report on mBridge wholesale CBDC platform after .... https://www.investing.com/news/cryptocurrency-news/bis-releases-full-report-on-mbridge-wholesale-cbdc-platform-after-successful-pilot-2922870

[33] [PDF] A legal framework for the digital euro - European Parliament. https://www.europarl.europa.eu/RegData/etudes/IDAN/2023/741518/IPOL_IDA(2023)714518_EN.pdf

[34] New Guidance, European Banking Authority (EBA), FinTech. https://www.jdsupra.com/topics/new-guidance/european-banking-authority-eba/fintech/

[35] Project Dunbar | PDF | Governance | Banks - Scribd. https://www.scribd.com/document/599278866/Project-Dunbar

[36] Governance structure of Project Dunbar [BIS, 2022a] - ResearchGate. https://www.researchgate.net/figure/Governance-structure-of-Project-Dunbar-BIS-2022a_tbl2_388212012

[37] [PDF] Central Bank Digital Currency and Privacy: A Randomized Survey .... https://www.bis.org/publ/work1147.pdf

[38] [PDF] CBDC Governance: Programmability, Privacy and Policies. https://www.cigionline.org/static/documents/DPH-paper-Freiman.pdf



                