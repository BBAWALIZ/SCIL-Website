<?php

/*
|--------------------------------------------------------------------------
| SCIL Machinery: site facts that are the same in every language
|--------------------------------------------------------------------------
| Contact details, the machine list, SOLO prices and the team. Words that
| change by language live in lang/en, lang/ar and lang/zh.
*/

return [

    'contact' => [
        'phone' => '+86 512 5872 4993',
        'phone_href' => 'tel:+8651258724993',
        'whatsapp' => '8613221284949',
        'whatsapp_display' => '+86 132 2128 4949',
        'email' => 'info@scil-machinery.com',
        'email_sales' => 'sales@scil-machinery.com',
        // Spelled "sevice@" on the old site. Confirm the real mailbox before launch.
        'email_parts' => 'sevice@scil-machinery.com',
        'address' => ['QingShui Industrial Park, GangKou', 'FengHuang Town, Suzhou', 'P.R. China'],
        'catalogue' => 'https://scil-machinery.com/SCIL-Catalogue.pdf',
        'map' => 'https://www.openstreetmap.org/search?query=FengHuang%20Town%20Zhangjiagang%20Suzhou',
    ],

    'social' => [
        ['name' => 'LinkedIn', 'url' => 'https://www.linkedin.com/company/scil-machinery/', 'icon' => 'linkedin'],
        ['name' => 'YouTube', 'url' => 'https://www.youtube.com/channel/UCVLHb5rAgUPFnxuRLX7rltw', 'icon' => 'youtube'],
        ['name' => 'Facebook', 'url' => 'https://www.facebook.com/infoscilmachinery/', 'icon' => 'facebook'],
        ['name' => 'Instagram', 'url' => 'https://www.instagram.com/scil_machinery/', 'icon' => 'instagram'],
        ['name' => 'X / Twitter', 'url' => 'https://twitter.com/Scil_Machinery', 'icon' => 'x'],
    ],

    // Languages. The first one is the default.
    'locales' => [
        'en' => ['name' => 'English', 'dir' => 'ltr', 'og' => 'en_US'],
        'ar' => ['name' => 'العربية', 'dir' => 'rtl', 'og' => 'ar_AR'],
        'zh' => ['name' => '中文', 'dir' => 'ltr', 'og' => 'zh_CN', 'html' => 'zh-Hans'],
    ],

    // The line, in order. Water treatment (00) feeds the filler.
    'stations' => [
        'injection' => ['no' => '01', 'token' => 'preform'],
        'blowing' => ['no' => '02', 'token' => 'bottle'],
        'filling' => ['no' => '03', 'token' => 'filled'],
        'labeling' => ['no' => '04', 'token' => 'labelled'],
        'packaging' => ['no' => '05', 'token' => 'pack'],
        'palletizing' => ['no' => '06', 'token' => 'pallet'],
    ],
    'water' => ['key' => 'water-treatment', 'no' => '00', 'token' => 'water'],

    // Home page picks (machine ids)
    'hero_pick' => ['blowing' => 34, 'filling' => 33, 'labeling' => 39, 'packaging' => 20, 'palletizing' => 18],
    'walk_pick' => ['blowing' => [34, 48, 42], 'filling' => [33, 21, 13], 'labeling' => [39, 40, 16], 'packaging' => [20, 19, 22], 'palletizing' => [18, 47]],
    'home_solo' => [0, 7, 4],
    'home_testimonials_skip' => ['Safira', 'Najd Water'],

    // Machines: id => slug (kept from the old site), station, photo in public/assets/img/products
    'machines' => [
        49 => [
            'slug' => 'sc-hsp-ts-pet-blowing-machine',
            'station' => 'blowing',
            'image' => 'm49.jpeg',
        ],
        48 => [
            'slug' => '3rd-generation-sc-hsp8-fully-servo-blowing-machine',
            'station' => 'blowing',
            'image' => 'm48.png',
        ],
        34 => [
            'slug' => 'sc-hsp-fully-automatic-blowing-machine',
            'station' => 'blowing',
            'image' => 'm34.jpg',
        ],
        42 => [
            'slug' => 'sc-3000-6s-fully-automatic-blowing-machine',
            'station' => 'blowing',
            'image' => 'm42.jpg',
        ],
        45 => [
            'slug' => 'sc-3000-4s-fully-automatic-blowing-machine',
            'station' => 'blowing',
            'image' => 'm45.jpg',
        ],
        38 => [
            'slug' => 'sc-4000-4sl-fully-automatic-blowing-machine',
            'station' => 'blowing',
            'image' => 'm38.jpg',
        ],
        37 => [
            'slug' => 'sc-880b-3sl-fully-automatic-blowing-machine',
            'station' => 'blowing',
            'image' => 'm37.jpg',
        ],
        6 => [
            'slug' => 'sc-880b-semi-automatic-blowing-machine',
            'station' => 'blowing',
            'image' => 'm6.jpg',
        ],
        43 => [
            'slug' => 'scb-00bc-oil-bottle-w-handle-fully-automatic-blowing-machine',
            'station' => 'blowing',
            'image' => 'm43.jpg',
        ],
        8 => [
            'slug' => 'scu-fully-automatic-hydraulic-extrusion-blow-machine',
            'station' => 'blowing',
            'image' => 'm8.jpg',
        ],
        36 => [
            'slug' => 'sc-90-1sl-fully-automatic-blowing-machine',
            'station' => 'blowing',
            'image' => 'm36.jpg',
        ],
        30 => [
            'slug' => 'sc-90-manual-blowing-machine',
            'station' => 'blowing',
            'image' => 'm30.jpg',
        ],
        41 => [
            'slug' => 'sc-880-manual-blowing-machine',
            'station' => 'blowing',
            'image' => 'm41.jpg',
        ],
        33 => [
            'slug' => 'water-filling-machine',
            'station' => 'filling',
            'image' => 'm33.jpg',
        ],
        21 => [
            'slug' => 'csd-carbonated-drinks-filling-machine',
            'station' => 'filling',
            'image' => 'm21.jpg',
        ],
        13 => [
            'slug' => 'juice-filling-machine',
            'station' => 'filling',
            'image' => 'm13.jpg',
        ],
        3 => [
            'slug' => 'ultra-clean-filling',
            'station' => 'filling',
            'image' => 'm3.jpg',
        ],
        10 => [
            'slug' => '5-gallon-water-filling-line',
            'station' => 'filling',
            'image' => 'm10.jpg',
        ],
        35 => [
            'slug' => 'aseptic-bricks-shaped-filling-machine',
            'station' => 'filling',
            'image' => 'm35.jpg',
        ],
        31 => [
            'slug' => 'oil-filling-machine-series',
            'station' => 'filling',
            'image' => 'm31.jpg',
        ],
        50 => [
            'slug' => 'automatic-edible-oil-tin-filling-machine',
            'station' => 'filling',
            'image' => 'm50.jpg',
        ],
        23 => [
            'slug' => 'oil-filling-liner-machine',
            'station' => 'filling',
            'image' => 'm23.jpg',
        ],
        46 => [
            'slug' => 'anti-corrosive-liquids-filling-machine',
            'station' => 'filling',
            'image' => 'm46.jpg',
        ],
        12 => [
            'slug' => 'filling-liner-machine',
            'station' => 'filling',
            'image' => 'm12.jpg',
        ],
        11 => [
            'slug' => 'automatic-plastic-cup-forming-filling-sealing-machine',
            'station' => 'filling',
            'image' => 'm11.jpg',
        ],
        25 => [
            'slug' => 'automatic-plastic-cup-filling-sealing-machine',
            'station' => 'filling',
            'image' => 'm25.jpg',
        ],
        39 => [
            'slug' => 'rotary-hot-melt-labeling-machine',
            'station' => 'labeling',
            'image' => 'm39.jpg',
        ],
        40 => [
            'slug' => 'rotary-self-adhesive-label-machine',
            'station' => 'labeling',
            'image' => 'm40.jpg',
        ],
        14 => [
            'slug' => 'liner-hot-melt-labeling-machine',
            'station' => 'labeling',
            'image' => 'm14.jpg',
        ],
        15 => [
            'slug' => 'liner-self-adhesive-label-machine',
            'station' => 'labeling',
            'image' => 'm15.jpg',
        ],
        16 => [
            'slug' => 'sleeve-labeling-machine',
            'station' => 'labeling',
            'image' => 'm16.jpg',
        ],
        20 => [
            'slug' => 'wrap-around-case-packer',
            'station' => 'packaging',
            'image' => 'm20.jpg',
        ],
        22 => [
            'slug' => 'grapping-case-packer',
            'station' => 'packaging',
            'image' => 'm22.jpg',
        ],
        17 => [
            'slug' => 'shrink-wrapper-for-traypak',
            'station' => 'packaging',
            'image' => 'm17.jpg',
        ],
        19 => [
            'slug' => 'automatic-heat-shrink-packing-machine',
            'station' => 'packaging',
            'image' => 'm19.jpg',
        ],
        26 => [
            'slug' => 'lc-automatic-heat-shrink-packing-machine',
            'station' => 'packaging',
            'image' => 'm26.jpg',
        ],
        18 => [
            'slug' => 'automatic-palletizer-machine',
            'station' => 'palletizing',
            'image' => 'm18.jpg',
        ],
        47 => [
            'slug' => 'economic-palletizer-lc-md15',
            'station' => 'palletizing',
            'image' => 'm47.jpeg',
        ],
        32 => [
            'slug' => 'water-treatment-equipment',
            'station' => 'water-treatment',
            'image' => 'm32.jpg',
        ],
    ],

    // Published specification tables. Labels are translated in lang/*/specs.php
    'specs' => [
        34 => [
            'caption' => 'SC-HSP series',
            'head' => [
                'Model',
                'Cavities',
                'Capacity up to',
                'Bottle size up to',
            ],
            'rows' => [
                [
                    'SC-HSP4',
                    '4',
                    '7,000 BPH',
                    '2.25 L',
                ],
                [
                    'SC-HSP6',
                    '6',
                    '10,000 BPH',
                    '0.90 L',
                ],
                [
                    'SC-HSP8',
                    '8',
                    '13,000 BPH',
                    '1.5 L',
                ],
                [
                    'SC-HSP10',
                    '10',
                    '16,000 BPH',
                    '0.80 L',
                ],
                [
                    'SC-HSP12',
                    '12',
                    '18,000 BPH',
                    '0.60 L',
                ],
            ],
        ],
        48 => [
            'caption' => 'Equipment parameters',
            'rows' => [
                [
                    'Max. product volume',
                    '1,500 ml',
                ],
                [
                    'Max. product diameter',
                    'Ø110 mm',
                ],
                [
                    'Bottle neck size',
                    '30 mm',
                ],
                [
                    'Max. product height',
                    '< 320 mm',
                ],
                [
                    'Max. preform height',
                    '< 125 mm',
                ],
                [
                    'Preform spacing',
                    '38 mm',
                ],
                [
                    'Bottle spacing',
                    '120 mm',
                ],
                [
                    'Mould standard thickness',
                    '200 mm',
                ],
                [
                    'Output (500 ml water, 13 g)',
                    '14,000–16,000 BPH',
                ],
                [
                    'Mould cavities',
                    '8',
                ],
                [
                    'Heating units',
                    '6',
                ],
                [
                    'Heating lamp layers',
                    '10',
                ],
                [
                    'Preform holders',
                    '208',
                ],
                [
                    'Voltage / frequency',
                    '220/380 V · 50/60 Hz',
                ],
                [
                    'Power in use / installed',
                    '45 kW / 180 kW',
                ],
                [
                    'High-pressure air',
                    '25–30 bar · 10.0 m³/min',
                ],
                [
                    'Cooling water (≤12 °C)',
                    '3 bar · 5 m³/h',
                ],
                [
                    'Weight (blower, heater, control box)',
                    '7.5 t',
                ],
                [
                    'Machine (L×W×H)',
                    '7500 × 1900 × 2300 mm',
                ],
                [
                    'Preform feeder (L×W×H)',
                    '2100 × 1350 × 2700 mm',
                ],
            ],
        ],
        42 => [
            'caption' => 'Specifications',
            'rows' => [
                [
                    'Cavities',
                    '6',
                ],
                [
                    'Theoretical output',
                    '7,500 pcs/h',
                ],
                [
                    'Container size up to',
                    '1.5 L',
                ],
                [
                    'Max. neck diameter',
                    '38 mm',
                ],
                [
                    'Max. container height',
                    '340 mm',
                ],
                [
                    'Heating power',
                    '45 kW',
                ],
                [
                    'Blowing pressure',
                    '4 MPa',
                ],
                [
                    'Machine dimensions',
                    '2.8 × 2.6 × 2.7 m',
                ],
            ],
        ],
        45 => [
            'caption' => 'Specifications',
            'rows' => [
                [
                    'Cavities',
                    '4',
                ],
                [
                    'Theoretical output',
                    '4,000 pcs/h',
                ],
                [
                    'Container size up to',
                    '2.25 L',
                ],
                [
                    'Max. neck diameter',
                    '38 mm',
                ],
                [
                    'Max. container height',
                    '340 mm',
                ],
                [
                    'Heating power',
                    '50 kW',
                ],
                [
                    'Blowing pressure',
                    '3.5 MPa',
                ],
                [
                    'Machine dimensions',
                    '3.5 × 1.55 × 2.7 m',
                ],
            ],
        ],
    ],

    // SOLO fixed-price machines (USD), same order as lang/*/solo.php
    'solo' => [
        [
            'image' => 'solo3.jpg',
            'station' => 'blowing',
            'prices' => [
                '$5,350',
                '$6,350',
            ],
        ],
        [
            'image' => 'solo1.jpg',
            'station' => 'blowing',
            'prices' => [
                '$13,950',
            ],
        ],
        [
            'image' => 'solo2.jpg',
            'station' => 'blowing',
            'prices' => [
                '$16,850',
            ],
        ],
        [
            'image' => 'solo4.jpeg',
            'station' => 'blowing',
            'prices' => [
                '$23,775',
            ],
        ],
        [
            'image' => 'solo5.jpg',
            'station' => 'filling',
            'prices' => [
                '$12,850',
                '$18,250',
                '$19,850',
                '$17,890',
            ],
        ],
        [
            'image' => 'solo8.jpg',
            'station' => 'filling',
            'prices' => [
                '$17,250',
                '$25,000',
            ],
        ],
        [
            'image' => 'solo6.jpg',
            'station' => 'filling',
            'prices' => [
                '$16,800',
                '$22,450',
            ],
        ],
        [
            'image' => 'solo7.jpg',
            'station' => 'filling',
            'prices' => [
                '$8,800',
            ],
        ],
        [
            'image' => 'solo9.jpg',
            'station' => 'filling',
            'prices' => [
                '$14,280',
                '$18,950',
            ],
        ],
        [
            'image' => 'solo10.jpg',
            'station' => 'labeling',
            'prices' => [
                '$13,400',
            ],
        ],
        [
            'image' => 'solo11.jpg',
            'station' => 'labeling',
            'prices' => [
                '$3,850',
            ],
        ],
        [
            'image' => 'solo12.jpeg',
            'station' => 'packaging',
            'prices' => [
                '$2,200',
            ],
        ],
        [
            'image' => 'solo13.jpeg',
            'station' => 'packaging',
            'prices' => [
                '$3,100',
            ],
        ],
        [
            'image' => 'solo14.jpeg',
            'station' => 'palletizing',
            'prices' => [
                '$29,600',
                '$48,200',
            ],
        ],
        [
            'image' => 'solo15.jpeg',
            'station' => 'conveying',
            'prices' => [
                '$280',
                '$380',
            ],
        ],
        [
            'image' => 'solo16.jpeg',
            'station' => 'conveying',
            'prices' => [
                '$750',
            ],
        ],
        [
            'image' => 'solo17.jpg',
            'station' => 'water-treatment',
            'prices' => [
                '$8,300',
                '$9,300',
            ],
        ],
    ],

    'team' => [
        [
            'image' => 't1.png',
            'name' => 'YanFeng Liang',
            'name_zh' => '梁彦峰',
            'role' => 'CEO & Shareholder',
        ],
        [
            'image' => 't2.png',
            'name' => 'Brad Zhang',
            'name_zh' => '张腾宇',
            'role' => 'Asia Regional Manager & Shareholder',
        ],
        [
            'image' => 't3.png',
            'name' => 'Layth Alkhateeb',
            'name_zh' => '',
            'role' => 'Regional Manager & Shareholder',
        ],
        [
            'image' => 't4.png',
            'name' => 'Bo Liu',
            'name_zh' => '刘勃',
            'role' => 'Production Manager',
        ],
        [
            'image' => 't5.png',
            'name' => 'YuZhong Wang',
            'name_zh' => '王玉中',
            'role' => 'Engineering Manager',
        ],
        [
            'image' => 't6.png',
            'name' => 'XinHe Su',
            'name_zh' => '苏新河',
            'role' => 'Service Department Manager',
        ],
        [
            'image' => 't7.png',
            'name' => 'Yannic Su',
            'name_zh' => '苏健阳',
            'role' => 'Sales Manager',
        ],
        [
            'image' => 't8.png',
            'name' => 'Amer Alkhateeb',
            'name_zh' => '',
            'role' => 'Marketing Department Manager',
        ],
        [
            'image' => 't9.png',
            'name' => 'Joan Huan',
            'name_zh' => '',
            'role' => 'Logistics Department Manager',
        ],
    ],

];
