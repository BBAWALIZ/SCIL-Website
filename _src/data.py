# Content for the SCIL Machinery site. All facts come from the current
# scil-machinery.com pages; copy has been tidied for grammar only.

PHONE = "+86 512 5872 4993"
PHONE_HREF = "tel:+8651258724993"
WHATSAPP = "8613221284949"
WHATSAPP_DISPLAY = "+86 132 2128 4949"
EMAIL = "info@scil-machinery.com"
EMAIL_SALES = "sales@scil-machinery.com"
EMAIL_PARTS = "sevice@scil-machinery.com"  # spelled this way on the current site; confirm with SCIL
ADDRESS = ["QingShui Industrial Park, GangKou", "FengHuang Town, Suzhou", "P.R. China"]
CATALOGUE = "https://scil-machinery.com/SCIL-Catalogue.pdf"

SOCIAL = [
    ("LinkedIn", "https://www.linkedin.com/company/scil-machinery/", "linkedin"),
    ("YouTube", "https://www.youtube.com/channel/UCVLHb5rAgUPFnxuRLX7rltw", "youtube"),
    ("Facebook", "https://www.facebook.com/infoscilmachinery/", "facebook"),
    ("Instagram", "https://www.instagram.com/scil_machinery/", "instagram"),
    ("X / Twitter", "https://twitter.com/Scil_Machinery", "x"),
]

# The line, in order. "out" is what the container looks like when it leaves.
STATIONS = [
    dict(no="01", key="injection", name="Injection", out="PET preform", token="preform",
         short="Preforms at the right weight",
         text="Make your own PET preforms in your own factory: the right weight, less material scrap, and a shorter road to your sustainability goals."),
    dict(no="02", key="blowing", name="Blowing", out="Empty PET bottle", token="bottle",
         short="200 ml to 5-gallon bottles",
         text="Inject your own preforms or buy them in: our blowing machines take both, and blow the bottle shape your brand designed, from 200 ml to 5 gallons."),
    dict(no="03", key="filling", name="Filling", out="Filled and capped", token="filled",
         short="Cold, hot, still or carbonated",
         text="Cold fill or hot fill, still or carbonated, thin or viscous: we fill them all, precisely, safely and to the exact fill level."),
    dict(no="04", key="labeling", name="Labeling", out="Labelled bottle", token="labelled",
         short="Hot-melt, self-adhesive, sleeve",
         text="Your label is the consumer's first impression. We supply reliable labelling systems for just about every container shape."),
    dict(no="05", key="packaging", name="Packaging", out="Shrink pack or case", token="pack",
         short="Shrink, tray and case packing",
         text="Shrink packs, tray packs and wrap-around cases, built to meet your requirements and those of your customers."),
    dict(no="06", key="palletizing", name="Palletizing", out="Pallet, ready to ship", token="pallet",
         short="Palletizers and smart warehouse",
         text="Manual palletizing is a headache. Automated palletizers and laser-guided vehicles raise productivity and reduce worker injury and fatigue."),
]
WATER = dict(no="00", key="water-treatment", name="Water treatment", out="Purified process water", token="water",
             short="Feeds the filler",
             text="Raw water in, drinkable water out: sand and carbon filtration, ion exchange, reverse osmosis, ozone and UV sterilising, feeding rinsing and filling.")

# id, slug (kept from the current site), station, display name, headline figure, one-line summary
MACHINES = [
    (49, "sc-hsp-ts-pet-blowing-machine", "blowing", "SC-HSP TS PET Blowing Machine", "2,000 BPH per cavity", "High-speed servo blow moulder for water, juice and carbonated drinks."),
    (48, "3rd-generation-sc-hsp8-fully-servo-blowing-machine", "blowing", "SC-HSP8 Fully Servo Blowing Machine (3rd gen.)", "up to 16,000 BPH", "Eight cavities, bottles up to 1.5 L, full PLC control of heat, water and air."),
    (34, "sc-hsp-fully-automatic-blowing-machine", "blowing", "SC-HSP Fully Automatic Blowing Machine", "up to 22,000 BPH", "Series from 4 to 12 cavities; servo-driven, low material waste."),
    (42, "sc-3000-6s-fully-automatic-blowing-machine", "blowing", "SC-3000-6S Fully Automatic Blowing Machine", "7,500 BPH", "Six cavities, containers up to 1.5 L and 340 mm tall."),
    (45, "sc-3000-4s-fully-automatic-blowing-machine", "blowing", "SC-3000-4S Fully Automatic Blowing Machine", "4,000 BPH", "Four cavities, up to 2.25 L; single-unit rotation heating saves 30% power."),
    (38, "sc-4000-4sl-fully-automatic-blowing-machine", "blowing", "SC-4000-4SL Fully Automatic Blowing Machine", "up to 6,000 BPH", "Four-cavity servo blow moulder with Siemens HMI and Festo / SMC pneumatics."),
    (37, "sc-880b-3sl-fully-automatic-blowing-machine", "blowing", "SC-880B-3SL Fully Automatic Blowing Machine", "up to 2,500 BPH", "Three-cavity servo blow moulder, easy to maintain."),
    (6, "sc-880b-semi-automatic-blowing-machine", "blowing", "SC-880B Semi-automatic Blowing Machine", "up to 2,800 BPH", "Three cavities, up to 1.5 L, PET and PP containers."),
    (43, "scb-00bc-oil-bottle-w-handle-fully-automatic-blowing-machine", "blowing", "SCB-00BC Oil Bottle Blowing Machine (with handle)", "1-hour mould change", "Fully automatic blowing of edible-oil bottles with handles."),
    (8, "scu-fully-automatic-hydraulic-extrusion-blow-machine", "blowing", "SCU Hydraulic Extrusion Blow Machine", "up to 20 L", "Extrusion blow moulding for large oil bottles and handled containers."),
    (36, "sc-90-1sl-fully-automatic-blowing-machine", "blowing", "SC-90-1SL 5-Gallon Blowing Machine", "100 BPH · 5 gal", "Infrared reheat for thick-wall gallon preforms up to 6 gallons."),
    (30, "sc-90-manual-blowing-machine", "blowing", "SC-90 Semi-automatic Blowing Machine", "5-gallon & hot-fill", "CE-standard stretch blow moulder, run by one operator."),
    (41, "sc-880-manual-blowing-machine", "blowing", "SC-880 Manual Blowing Machine", "up to 800 BPH", "Start small: low tooling cost, quick size changeover."),

    (33, "water-filling-machine", "filling", "Water Filling Machine (CGF)", "5,000–36,000 BPH", "Rinse, fill and cap PET water bottles from 200 ml to 2.5 L."),
    (21, "csd-carbonated-drinks-filling-machine", "filling", "Carbonated Drinks Filling Machine (DCGF)", "6,000–30,000 BPH", "Isobaric filling for soft drinks from 200 ml to 2.5 L."),
    (13, "juice-filling-machine", "filling", "Juice Hot-filling Machine (RCGF)", "4,000–25,000 BPH", "Hot-fill PET juice from 200 ml to 2.5 L."),
    (3, "ultra-clean-filling", "filling", "Ultra-clean Filling", "5,000–22,000 BPH", "Juice, tea and energy drinks with low dissolved oxygen and full CIP."),
    (10, "5-gallon-water-filling-line", "filling", "5-Gallon Water Filling Line (TXG)", "100–2,000 B/H", "Decap, brush-wash, rinse, fill and cap 3- and 5-gallon barrels."),
    (35, "aseptic-bricks-shaped-filling-machine", "filling", "Aseptic Brick Filling Machine", "up to 5,000 BPH", "UHT juice in sterile bricks with up to one year shelf life."),
    (31, "oil-filling-machine-series", "filling", "Oil Filling Machine Series", "Weigh filling", "Automatic fill-and-cap for PET edible oil bottles."),
    (50, "automatic-edible-oil-tin-filling-machine", "filling", "Edible Oil Tin Filling Machine", "3–18 L tins", "Weighted filling heads for metal oil tins, stainless steel build."),
    (23, "oil-filling-liner-machine", "filling", "Linear Oil Filling Machine", "Weigh filling", "PLC-controlled linear filler for edible, engine and other oils."),
    (46, "anti-corrosive-liquids-filling-machine", "filling", "Anti-corrosive Liquids Filling Machine", "up to 8,000 BPH", "PP construction for detergents, bleach and acids, bottles up to 5 L."),
    (12, "filling-liner-machine", "filling", "Linear Filling Machine (viscous liquids)", "Oils, detergents, shampoo", "Precise filling of viscous liquids and personal-care products."),
    (11, "automatic-plastic-cup-forming-filling-sealing-machine", "filling", "Cup Forming, Filling & Sealing Machine (CFD)", "12,000–40,000 cups/h", "Forms, labels, fills, seals and cuts cups for water, yoghurt and more."),
    (25, "automatic-plastic-cup-filling-sealing-machine", "filling", "Cup Filling & Sealing Machine", "up to 20,000 cups/h", "Dispatch, fill, film, date-code and double heat-seal pre-made cups."),

    (39, "rotary-hot-melt-labeling-machine", "labeling", "Rotary Hot-melt Labeling Machine", "High-volume lines", "Reel-fed wraparound labels with less glue and high accuracy."),
    (40, "rotary-self-adhesive-label-machine", "labeling", "Rotary Self-adhesive Labeling Machine", "High-volume lines", "Round, square and tapered containers; label-break warning."),
    (14, "liner-hot-melt-labeling-machine", "labeling", "Linear Hot-melt Labeling Machine", "Less glue", "Roll-fed hot-melt labels for water and soft drinks."),
    (15, "liner-self-adhesive-label-machine", "labeling", "Linear Self-adhesive Labeling Machine", "Touch-screen HMI", "For food, beverage, pharma, oil and cosmetics containers."),
    (16, "sleeve-labeling-machine", "labeling", "Sleeve Labeling Machine", "Shrink sleeves", "Sleeves the bottle body, then heat-shrinks the label into place."),

    (20, "wrap-around-case-packer", "packaging", "Wrap-around Case Packer", "Servo-synchronised", "Forms the case around grouped bottles and seals with hot-melt glue."),
    (22, "grapping-case-packer", "packaging", "Gripper Case Packer", "Bottles, jars & cans", "Picks and places containers into cartons, with or without partitions."),
    (17, "shrink-wrapper-for-traypak", "packaging", "Shrink Wrapper for Tray Packs", "5–8 s shrink", "Folds a cardboard tray around the group, wraps and shrinks."),
    (19, "automatic-heat-shrink-packing-machine", "packaging", "Automatic Heat Shrink Packer", "No tray needed", "Groups bottles and shrink-wraps them into firm packs."),
    (26, "lc-automatic-heat-shrink-packing-machine", "packaging", "LC Automatic Heat Shrink Packer", "No tray needed", "Compact shrink packer for water and soft-drink packs."),

    (18, "automatic-palletizer-machine", "palletizing", "Automatic Palletizer", "PLC-controlled", "Feeds, turns, layers and stacks cases onto pallets automatically."),
    (47, "economic-palletizer-lc-md15", "palletizing", "Economic Palletizer LC-MD15", "15 packs/min", "European parts, 1,650 mm stack height, a low-cost start."),

    (32, "water-treatment-equipment", "water-treatment", "Water Treatment System", "Filtration · RO · UV", "Purifies raw water for rinsing, mixing and filling."),
]

# Structured specs published on the current site
SPECS = {
    34: dict(caption="SC-HSP series", head=["Model", "Cavities", "Capacity up to", "Bottle size up to"], rows=[
        ["SC-HSP4", "4", "7,000 BPH", "2.25 L"],
        ["SC-HSP6", "6", "10,000 BPH", "0.90 L"],
        ["SC-HSP8", "8", "13,000 BPH", "1.5 L"],
        ["SC-HSP10", "10", "16,000 BPH", "0.80 L"],
        ["SC-HSP12", "12", "18,000 BPH", "0.60 L"],
    ]),
    48: dict(caption="Equipment parameters", rows=[
        ["Max. product volume", "1,500 ml"], ["Max. product diameter", "Ø110 mm"], ["Bottle neck size", "30 mm"],
        ["Max. product height", "< 320 mm"], ["Max. preform height", "< 125 mm"], ["Preform spacing", "38 mm"],
        ["Bottle spacing", "120 mm"], ["Mould standard thickness", "200 mm"], ["Output (500 ml water, 13 g)", "14,000–16,000 BPH"],
        ["Mould cavities", "8"], ["Heating units", "6"], ["Heating lamp layers", "10"], ["Preform holders", "208"],
        ["Voltage / frequency", "220/380 V · 50/60 Hz"], ["Power in use / installed", "45 kW / 180 kW"],
        ["High-pressure air", "25–30 bar · 10.0 m³/min"], ["Cooling water (≤12 °C)", "3 bar · 5 m³/h"],
        ["Weight (blower, heater, control box)", "7.5 t"], ["Machine (L×W×H)", "7500 × 1900 × 2300 mm"], ["Preform feeder (L×W×H)", "2100 × 1350 × 2700 mm"],
    ]),
    42: dict(caption="Specifications", rows=[
        ["Cavities", "6"], ["Theoretical output", "7,500 pcs/h"], ["Container size up to", "1.5 L"], ["Max. neck diameter", "38 mm"],
        ["Max. container height", "340 mm"], ["Heating power", "45 kW"], ["Blowing pressure", "4 MPa"], ["Machine dimensions", "2.8 × 2.6 × 2.7 m"],
    ]),
    45: dict(caption="Specifications", rows=[
        ["Cavities", "4"], ["Theoretical output", "4,000 pcs/h"], ["Container size up to", "2.25 L"], ["Max. neck diameter", "38 mm"],
        ["Max. container height", "340 mm"], ["Heating power", "50 kW"], ["Blowing pressure", "3.5 MPa"], ["Machine dimensions", "3.5 × 1.55 × 2.7 m"],
    ]),
}

TESTIMONIALS = [
    dict(name="Mohammed Alajarmeh", role="CEO", org="Nawa",
         short="We bought a 5,000 BPH water line from SCIL. The machines are uncomplicated and easy to operate, and the after-sales service is what makes SCIL unique.",
         full=["We purchased a 5,000 BPH water line from SCIL and it was the perfect choice for many reasons.", "The machines are uncomplicated and easy to operate, the credibility was at a high level, and most importantly, the after-sales service is what makes SCIL very unique."]),
    dict(name="Mohammed Awad", role="CEO", org="Halaia Springs",
         short="The machinery we bought for our bottled drinking water factory is the best. The maintenance team kept following up until every problem was solved.",
         full=["I would like to thank the SCIL team for the great work they did for us. The machinery and equipment we purchased for our bottled drinking water factory are the best.", "We got great support from Mr Al Khateeb, who was cooperative from the first contact, gave us all the information we needed and the most suitable offer, and stayed in touch until the machinery arrived and was commissioned by the team he sent.", "The maintenance team gave great support and kept following up to make sure all problems were solved well."]),
    dict(name="Samer Bouchnak", role="CEO", org="MORE",
         short="Dealing with an overseas company you don't know feels like an adventure. With SCIL it turned into an achievement. Their after-sales commitment was true in every sense.",
         full=["When I started studying a bottled water plant, I looked hard for a line supplier that met my needs and that I could trust on after-sales service. I contacted many manufacturers, but decided to work with SCIL.", "Dealing with a company overseas that you are not familiar with feels like an adventure. Over time that adventure turned into an achievement: the line was supplied, the factory ran well, and the commitment to after-sales service proved true in every sense. Experience is the best proof."]),
    dict(name="Mr Salah", role="General manager", org="Eatqan",
         short="After the Libyan civil war, SCIL was the only company that agreed to work with us. Today we are one of the best mineral water companies in Libya.",
         full=["After the Libyan civil war ended in 2012, we were involved in Libya's reconstruction.", "SCIL was the only company that agreed to work with us given the political situation in the area. Today our company is one of the best mineral water companies in Libya. Thank you for believing in us."]),
    dict(name="Abdulaziz", role="CEO", org="Najd Water",
         short="Our first contract with SCIL was a 12,000 BPH blowing machine in 2014. After its performance and service, we bought a full 24,000 BPH water line in 2018.",
         full=["Our first contract with SCIL Machinery was signed in 2014: a 12,000 BPH blowing machine.", "Because of the machine's good performance and the after-sales service, in September 2018 we bought a fully automatic 24,000 BPH water production line. Thank you, SCIL family, for always being by our side."]),
    dict(name="Abo Fahed", role="CEO", org="Valley",
         short="We bought a rotary blowing machine and a wrap-around case packer. Even after the sale, you are treated as a partner.",
         full=["I would like to take this opportunity to thank SCIL.", "We bought a rotary blowing machine and a wrap-around case packer, and the service was more than excellent. Even after the sale, you are treated as a partner."]),
    dict(name="Abass Hijazi", role="CEO", org="Safira",
         short="We signed for a 5 L line rated at 1,400 BPH. After installation, the line started giving us 1,800 BPH.",
         full=["We bought a 5 L line from SCIL Machinery rated at 1,400 BPH and signed the deal on that.", "After they finished installing the line and the engineers made sure there were no problems, the line actually started giving us 1,800 BPH. Thanks, SCIL Machinery."]),
    dict(name="Carlos Manuel", role="General manager", org="Coca-Cola Bolivia",
         short="The training SCIL provided was first class, tailored to our business. We recommend SCIL for high-quality machines and highly efficient service.",
         full=["The training provided by SCIL was first class. They tailored the sessions to our business needs, and our staff learned a great deal about the packing and container industry and its impact on our work.", "We recommend SCIL if you are looking for high-quality machines and highly efficient service."]),
]

TEAM = [
    ("t1.png", "YanFeng Liang", "梁彦峰", "CEO & Shareholder"),
    ("t2.png", "Brad Zhang", "张腾宇", "Asia Regional Manager & Shareholder"),
    ("t3.png", "Layth Alkhateeb", "", "Regional Manager & Shareholder"),
    ("t4.png", "Bo Liu", "刘勃", "Production Manager"),
    ("t5.png", "YuZhong Wang", "王玉中", "Engineering Manager"),
    ("t6.png", "XinHe Su", "苏新河", "Service Department Manager"),
    ("t7.png", "Yannic Su", "苏健阳", "Sales Manager"),
    ("t8.png", "Amer Alkhateeb", "", "Marketing Department Manager"),
    ("t9.png", "Joan Huan", "", "Logistics Department Manager"),
]

# SOLO fixed-price machines (USD unit prices as published on SCIL SOLO)
SOLO = [
    ("solo3.jpg", "Manual blowing machine, up to 800 BPH", "Reliable, heavy-duty and ideal for start-ups: PET bottles for water, juice, detergent, oil and cosmetics.", [("0.2–5 L", "$5,350"), ("0.2–7 L", "$6,350")], "blowing"),
    ("solo1.jpg", "5-gallon semi-automatic blowing machine, 150 BPH", "SC-90 stretch blow moulder, CE-standard design with microcomputer control.", [("Unit", "$13,950")], "blowing"),
    ("solo2.jpg", "0.2–1.5 L semi-automatic blowing machine, up to 2,800 BPH", "Stable two-step stretch blow moulder for bottles up to 1.5 L.", [("Unit", "$16,850")], "blowing"),
    ("solo4.jpeg", "0.2–1.5 L automatic blowing machine, 2,800 BPH", "Patented high-efficiency blowing valve, connects directly to the filler; 30% air recovery.", [("Unit", "$23,775")], "blowing"),
    ("solo5.jpg", "0.2–2 L linear washing, filling & capping line, up to 2,000 BPH", "Washer, filler and capper linked by a linear conveyor: a first line for new producers.", [("Water", "$12,850"), ("Hot fill", "$18,250"), ("CSD", "$19,850"), ("Glass", "$17,890")], "filling"),
    ("solo8.jpg", "0.2–2 L washing, filling & capping monoblock", "CGF8-8-3 monoblock: rinse, fill and cap in one frame.", [("3,000 BPH", "$17,250"), ("6,000 BPH", "$25,000")], "filling"),
    ("solo6.jpg", "3–12 L washing, filling & capping machine", "ZCGF monoblock for large bottles.", [("500 BPH", "$16,800"), ("700 BPH", "$22,450")], "filling"),
    ("solo7.jpg", "5-gallon washing, filling & capping machine, 150 BPH", "TXG-150, the key machine for 3- and 5-gallon drinking water.", [("Unit", "$8,800")], "filling"),
    ("solo9.jpg", "Plastic cup washing, filling & sealing machine", "Juice, milk, jelly, water and more.", [("4 heads · 3,000 CPH", "$14,280"), ("6 heads · 4,500 CPH", "$18,950")], "filling"),
    ("solo10.jpg", "0.2–2 L sleeve labeling machine, 6,000 BPH", "Aluminium-alloy and 304 stainless steel body.", [("Unit", "$13,400")], "labeling"),
    ("solo11.jpg", "Steam heat tunnel", "Shrinks the PVC sleeve label after the labeller.", [("Unit", "$3,850")], "labeling"),
    ("solo12.jpeg", "Semi-auto sleeve wrapper & PE film shrink machine, 2–5 packs/min", "For cans, water, beer and glass bottles without a bottom tray.", [("Unit", "$2,200")], "packaging"),
    ("solo13.jpeg", "JET thermal shrink packaging machine", "Jet-loop heating: durable, energy-saving and efficient.", [("Unit", "$3,100")], "packaging"),
    ("solo14.jpeg", "Economic palletizer, 10–15 packs per minute", "Saves time and money at the end of the line.", [("Without pallet feeder", "$29,600"), ("Complete", "$48,200")], "palletizing"),
    ("solo15.jpeg", "1 m belt conveyor", "Links separate machines into one automatic line.", [("PP belt", "$280"), ("Stainless", "$380")], "conveying"),
    ("solo16.jpeg", "1 m air conveyor", "Carries empty PET bottles from the blower to the filler.", [("Unit", "$750")], "conveying"),
    ("solo17.jpg", "Water treatment equipment", "Filtration and sterilising system for drinkable process water.", [("1.5 m", "$8,300"), ("2 m", "$9,300")], "water-treatment"),
]
