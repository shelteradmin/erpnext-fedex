import frappe

COUNTRY_CODES = {
    "Aaland Islands": {"iso_code_2": "AX", "iso_code_3": "ALA"},
    "Afghanistan": {"iso_code_2": "AF", "iso_code_3": "AFG"},
    "Albania": {"iso_code_2": "AL", "iso_code_3": "ALB"},
    "Algeria": {"iso_code_2": "DZ", "iso_code_3": "DZA"},
    "American Samoa": {"iso_code_2": "AS", "iso_code_3": "ASM"},
    "Andorra": {"iso_code_2": "AD", "iso_code_3": "AND"},
    "Angola": {"iso_code_2": "AO", "iso_code_3": "AGO"},
    "Anguilla": {"iso_code_2": "AI", "iso_code_3": "AIA"},
    "Antarctica": {"iso_code_2": "AQ", "iso_code_3": "ATA"},
    "Antigua and Barbuda": {"iso_code_2": "AG", "iso_code_3": "ATG"},
    "Argentina": {"iso_code_2": "AR", "iso_code_3": "ARG"},
    "Armenia": {"iso_code_2": "AM", "iso_code_3": "ARM"},
    "Aruba": {"iso_code_2": "AW", "iso_code_3": "ABW"},
    "Ascension Island (British)": {"iso_code_2": "AC", "iso_code_3": "ASC"},
    "Australia": {"iso_code_2": "AU", "iso_code_3": "AUS"},
    "Austria": {"iso_code_2": "AT", "iso_code_3": "AUT"},
    "Azerbaijan": {"iso_code_2": "AZ", "iso_code_3": "AZE"},
    "Bahamas": {"iso_code_2": "BS", "iso_code_3": "BHS"},
    "Bahrain": {"iso_code_2": "BH", "iso_code_3": "BHR"},
    "Bangladesh": {"iso_code_2": "BD", "iso_code_3": "BGD"},
    "Barbados": {"iso_code_2": "BB", "iso_code_3": "BRB"},
    "Belarus": {"iso_code_2": "BY", "iso_code_3": "BLR"},
    "Belgium": {"iso_code_2": "BE", "iso_code_3": "BEL"},
    "Belize": {"iso_code_2": "BZ", "iso_code_3": "BLZ"},
    "Benin": {"iso_code_2": "BJ", "iso_code_3": "BEN"},
    "Bermuda": {"iso_code_2": "BM", "iso_code_3": "BMU"},
    "Bhutan": {"iso_code_2": "BT", "iso_code_3": "BTN"},
    "Bolivia": {"iso_code_2": "BO", "iso_code_3": "BOL"},
    "Bonaire, Sint Eustatius and Saba": {"iso_code_2": "BQ", "iso_code_3": "BES"},
    "Bosnia and Herzegovina": {"iso_code_2": "BA", "iso_code_3": "BIH"},
    "Botswana": {"iso_code_2": "BW", "iso_code_3": "BWA"},
    "Bouvet Island": {"iso_code_2": "BV", "iso_code_3": "BVT"},
    "Brazil": {"iso_code_2": "BR", "iso_code_3": "BRA"},
    "British Indian Ocean Territory": {"iso_code_2": "IO", "iso_code_3": "IOT"},
    "Brunei Darussalam": {"iso_code_2": "BN", "iso_code_3": "BRN"},
    "Bulgaria": {"iso_code_2": "BG", "iso_code_3": "BGR"},
    "Burkina Faso": {"iso_code_2": "BF", "iso_code_3": "BFA"},
    "Burundi": {"iso_code_2": "BI", "iso_code_3": "BDI"},
    "Cambodia": {"iso_code_2": "KH", "iso_code_3": "KHM"},
    "Cameroon": {"iso_code_2": "CM", "iso_code_3": "CMR"},
    "Canada": {"iso_code_2": "CA", "iso_code_3": "CAN"},
    "Canary Islands": {"iso_code_2": "IC", "iso_code_3": "ICA"},
    "Cape Verde": {"iso_code_2": "CV", "iso_code_3": "CPV"},
    "Cayman Islands": {"iso_code_2": "KY", "iso_code_3": "CYM"},
    "Central African Republic": {"iso_code_2": "CF", "iso_code_3": "CAF"},
    "Chad": {"iso_code_2": "TD", "iso_code_3": "TCD"},
    "Chile": {"iso_code_2": "CL", "iso_code_3": "CHL"},
    "China": {"iso_code_2": "CN", "iso_code_3": "CHN"},
    "Christmas Island": {"iso_code_2": "CX", "iso_code_3": "CXR"},
    "Cocos (Keeling) Islands": {"iso_code_2": "CC", "iso_code_3": "CCK"},
    "Colombia": {"iso_code_2": "CO", "iso_code_3": "COL"},
    "Comoros": {"iso_code_2": "KM", "iso_code_3": "COM"},
    "Congo": {"iso_code_2": "CG", "iso_code_3": "COG"},
    "Cook Islands": {"iso_code_2": "CK", "iso_code_3": "COK"},
    "Costa Rica": {"iso_code_2": "CR", "iso_code_3": "CRI"},
    "Cote D'Ivoire": {"iso_code_2": "CI", "iso_code_3": "CIV"},
    "Croatia": {"iso_code_2": "HR", "iso_code_3": "HRV"},
    "Cuba": {"iso_code_2": "CU", "iso_code_3": "CUB"},
    "Curacao": {"iso_code_2": "CW", "iso_code_3": "CUW"},
    "Cyprus": {"iso_code_2": "CY", "iso_code_3": "CYP"},
    "Czech Republic": {"iso_code_2": "CZ", "iso_code_3": "CZE"},
    "Democratic Republic of Congo": {"iso_code_2": "CD", "iso_code_3": "COD"},
    "Denmark": {"iso_code_2": "DK", "iso_code_3": "DNK"},
    "Djibouti": {"iso_code_2": "DJ", "iso_code_3": "DJI"},
    "Dominica": {"iso_code_2": "DM", "iso_code_3": "DMA"},
    "Dominican Republic": {"iso_code_2": "DO", "iso_code_3": "DOM"},
    "East Timor": {"iso_code_2": "TL", "iso_code_3": "TLS"},
    "Ecuador": {"iso_code_2": "EC", "iso_code_3": "ECU"},
    "Egypt": {"iso_code_2": "EG", "iso_code_3": "EGY"},
    "El Salvador": {"iso_code_2": "SV", "iso_code_3": "SLV"},
    "Equatorial Guinea": {"iso_code_2": "GQ", "iso_code_3": "GNQ"},
    "Eritrea": {"iso_code_2": "ER", "iso_code_3": "ERI"},
    "Estonia": {"iso_code_2": "EE", "iso_code_3": "EST"},
    "Ethiopia": {"iso_code_2": "ET", "iso_code_3": "ETH"},
    "Falkland Islands (Malvinas)": {"iso_code_2": "FK", "iso_code_3": "FLK"},
    "Faroe Islands": {"iso_code_2": "FO", "iso_code_3": "FRO"},
    "Fiji": {"iso_code_2": "FJ", "iso_code_3": "FJI"},
    "Finland": {"iso_code_2": "FI", "iso_code_3": "FIN"},
    "France, Metropolitan": {"iso_code_2": "FR", "iso_code_3": "FRA"},
    "French Guiana": {"iso_code_2": "GF", "iso_code_3": "GUF"},
    "French Polynesia": {"iso_code_2": "PF", "iso_code_3": "PYF"},
    "French Southern Territories": {"iso_code_2": "TF", "iso_code_3": "ATF"},
    "FYROM": {"iso_code_2": "MK", "iso_code_3": "MKD"},
    "Gabon": {"iso_code_2": "GA", "iso_code_3": "GAB"},
    "Gambia": {"iso_code_2": "GM", "iso_code_3": "GMB"},
    "Georgia": {"iso_code_2": "GE", "iso_code_3": "GEO"},
    "Germany": {"iso_code_2": "DE", "iso_code_3": "DEU"},
    "Ghana": {"iso_code_2": "GH", "iso_code_3": "GHA"},
    "Gibraltar": {"iso_code_2": "GI", "iso_code_3": "GIB"},
    "Greece": {"iso_code_2": "GR", "iso_code_3": "GRC"},
    "Greenland": {"iso_code_2": "GL", "iso_code_3": "GRL"},
    "Grenada": {"iso_code_2": "GD", "iso_code_3": "GRD"},
    "Guadeloupe": {"iso_code_2": "GP", "iso_code_3": "GLP"},
    "Guam": {"iso_code_2": "GU", "iso_code_3": "GUM"},
    "Guatemala": {"iso_code_2": "GT", "iso_code_3": "GTM"},
    "Guernsey": {"iso_code_2": "GG", "iso_code_3": "GGY"},
    "Guinea": {"iso_code_2": "GN", "iso_code_3": "GIN"},
    "Guinea-Bissau": {"iso_code_2": "GW", "iso_code_3": "GNB"},
    "Guyana": {"iso_code_2": "GY", "iso_code_3": "GUY"},
    "Haiti": {"iso_code_2": "HT", "iso_code_3": "HTI"},
    "Heard and Mc Donald Islands": {"iso_code_2": "HM", "iso_code_3": "HMD"},
    "Honduras": {"iso_code_2": "HN", "iso_code_3": "HND"},
    "Hong Kong": {"iso_code_2": "HK", "iso_code_3": "HKG"},
    "Hungary": {"iso_code_2": "HU", "iso_code_3": "HUN"},
    "Iceland": {"iso_code_2": "IS", "iso_code_3": "ISL"},
    "India": {"iso_code_2": "IN", "iso_code_3": "IND"},
    "Indonesia": {"iso_code_2": "ID", "iso_code_3": "IDN"},
    "Iran (Islamic Republic of)": {"iso_code_2": "IR", "iso_code_3": "IRN"},
    "Iraq": {"iso_code_2": "IQ", "iso_code_3": "IRQ"},
    "Ireland": {"iso_code_2": "IE", "iso_code_3": "IRL"},
    "Isle of Man": {"iso_code_2": "IM", "iso_code_3": "IMN"},
    "Israel": {"iso_code_2": "IL", "iso_code_3": "ISR"},
    "Italy": {"iso_code_2": "IT", "iso_code_3": "ITA"},
    "Jamaica": {"iso_code_2": "JM", "iso_code_3": "JAM"},
    "Japan": {"iso_code_2": "JP", "iso_code_3": "JPN"},
    "Jersey": {"iso_code_2": "JE", "iso_code_3": "JEY"},
    "Jordan": {"iso_code_2": "JO", "iso_code_3": "JOR"},
    "Kazakhstan": {"iso_code_2": "KZ", "iso_code_3": "KAZ"},
    "Kenya": {"iso_code_2": "KE", "iso_code_3": "KEN"},
    "Kiribati": {"iso_code_2": "KI", "iso_code_3": "KIR"},
    "Korea, Republic of": {"iso_code_2": "KR", "iso_code_3": "KOR"},
    "Kosovo, Republic of": {"iso_code_2": "XK", "iso_code_3": "UNK"},
    "Kuwait": {"iso_code_2": "KW", "iso_code_3": "KWT"},
    "Kyrgyzstan": {"iso_code_2": "KG", "iso_code_3": "KGZ"},
    "Lao People's Democratic Republic": {"iso_code_2": "LA", "iso_code_3": "LAO"},
    "Latvia": {"iso_code_2": "LV", "iso_code_3": "LVA"},
    "Lebanon": {"iso_code_2": "LB", "iso_code_3": "LBN"},
    "Lesotho": {"iso_code_2": "LS", "iso_code_3": "LSO"},
    "Liberia": {"iso_code_2": "LR", "iso_code_3": "LBR"},
    "Libyan Arab Jamahiriya": {"iso_code_2": "LY", "iso_code_3": "LBY"},
    "Liechtenstein": {"iso_code_2": "LI", "iso_code_3": "LIE"},
    "Lithuania": {"iso_code_2": "LT", "iso_code_3": "LTU"},
    "Luxembourg": {"iso_code_2": "LU", "iso_code_3": "LUX"},
    "Macau": {"iso_code_2": "MO", "iso_code_3": "MAC"},
    "Madagascar": {"iso_code_2": "MG", "iso_code_3": "MDG"},
    "Malawi": {"iso_code_2": "MW", "iso_code_3": "MWI"},
    "Malaysia": {"iso_code_2": "MY", "iso_code_3": "MYS"},
    "Maldives": {"iso_code_2": "MV", "iso_code_3": "MDV"},
    "Mali": {"iso_code_2": "ML", "iso_code_3": "MLI"},
    "Malta": {"iso_code_2": "MT", "iso_code_3": "MLT"},
    "Marshall Islands": {"iso_code_2": "MH", "iso_code_3": "MHL"},
    "Martinique": {"iso_code_2": "MQ", "iso_code_3": "MTQ"},
    "Mauritania": {"iso_code_2": "MR", "iso_code_3": "MRT"},
    "Mauritius": {"iso_code_2": "MU", "iso_code_3": "MUS"},
    "Mayotte": {"iso_code_2": "YT", "iso_code_3": "MYT"},
    "Mexico": {"iso_code_2": "MX", "iso_code_3": "MEX"},
    "Micronesia, Federated States of": {"iso_code_2": "FM", "iso_code_3": "FSM"},
    "Moldova, Republic of": {"iso_code_2": "MD", "iso_code_3": "MDA"},
    "Monaco": {"iso_code_2": "MC", "iso_code_3": "MCO"},
    "Mongolia": {"iso_code_2": "MN", "iso_code_3": "MNG"},
    "Montenegro": {"iso_code_2": "ME", "iso_code_3": "MNE"},
    "Montserrat": {"iso_code_2": "MS", "iso_code_3": "MSR"},
    "Morocco": {"iso_code_2": "MA", "iso_code_3": "MAR"},
    "Mozambique": {"iso_code_2": "MZ", "iso_code_3": "MOZ"},
    "Myanmar": {"iso_code_2": "MM", "iso_code_3": "MMR"},
    "Namibia": {"iso_code_2": "NA", "iso_code_3": "NAM"},
    "Nauru": {"iso_code_2": "NR", "iso_code_3": "NRU"},
    "Nepal": {"iso_code_2": "NP", "iso_code_3": "NPL"},
    "Netherlands": {"iso_code_2": "NL", "iso_code_3": "NLD"},
    "Netherlands Antilles": {"iso_code_2": "AN", "iso_code_3": "ANT"},
    "New Caledonia": {"iso_code_2": "NC", "iso_code_3": "NCL"},
    "New Zealand": {"iso_code_2": "NZ", "iso_code_3": "NZL"},
    "Nicaragua": {"iso_code_2": "NI", "iso_code_3": "NIC"},
    "Niger": {"iso_code_2": "NE", "iso_code_3": "NER"},
    "Nigeria": {"iso_code_2": "NG", "iso_code_3": "NGA"},
    "Niue": {"iso_code_2": "NU", "iso_code_3": "NIU"},
    "Norfolk Island": {"iso_code_2": "NF", "iso_code_3": "NFK"},
    "North Korea": {"iso_code_2": "KP", "iso_code_3": "PRK"},
    "Northern Mariana Islands": {"iso_code_2": "MP", "iso_code_3": "MNP"},
    "Norway": {"iso_code_2": "NO", "iso_code_3": "NOR"},
    "Oman": {"iso_code_2": "OM", "iso_code_3": "OMN"},
    "Pakistan": {"iso_code_2": "PK", "iso_code_3": "PAK"},
    "Palau": {"iso_code_2": "PW", "iso_code_3": "PLW"},
    "Palestinian Territory, Occupied": {"iso_code_2": "PS", "iso_code_3": "PSE"},
    "Panama": {"iso_code_2": "PA", "iso_code_3": "PAN"},
    "Papua New Guinea": {"iso_code_2": "PG", "iso_code_3": "PNG"},
    "Paraguay": {"iso_code_2": "PY", "iso_code_3": "PRY"},
    "Peru": {"iso_code_2": "PE", "iso_code_3": "PER"},
    "Philippines": {"iso_code_2": "PH", "iso_code_3": "PHL"},
    "Pitcairn": {"iso_code_2": "PN", "iso_code_3": "PCN"},
    "Poland": {"iso_code_2": "PL", "iso_code_3": "POL"},
    "Portugal": {"iso_code_2": "PT", "iso_code_3": "PRT"},
    "Puerto Rico": {"iso_code_2": "PR", "iso_code_3": "PRI"},
    "Qatar": {"iso_code_2": "QA", "iso_code_3": "QAT"},
    "Reunion": {"iso_code_2": "RE", "iso_code_3": "REU"},
    "Romania": {"iso_code_2": "RO", "iso_code_3": "ROM"},
    "Russian Federation": {"iso_code_2": "RU", "iso_code_3": "RUS"},
    "Rwanda": {"iso_code_2": "RW", "iso_code_3": "RWA"},
    "Saint Kitts and Nevis": {"iso_code_2": "KN", "iso_code_3": "KNA"},
    "Saint Lucia": {"iso_code_2": "LC", "iso_code_3": "LCA"},
    "Saint Vincent and the Grenadines": {"iso_code_2": "VC", "iso_code_3": "VCT"},
    "Samoa": {"iso_code_2": "WS", "iso_code_3": "WSM"},
    "San Marino": {"iso_code_2": "SM", "iso_code_3": "SMR"},
    "Sao Tome and Principe": {"iso_code_2": "ST", "iso_code_3": "STP"},
    "Saudi Arabia": {"iso_code_2": "SA", "iso_code_3": "SAU"},
    "Senegal": {"iso_code_2": "SN", "iso_code_3": "SEN"},
    "Serbia": {"iso_code_2": "RS", "iso_code_3": "SRB"},
    "Seychelles": {"iso_code_2": "SC", "iso_code_3": "SYC"},
    "Sierra Leone": {"iso_code_2": "SL", "iso_code_3": "SLE"},
    "Singapore": {"iso_code_2": "SG", "iso_code_3": "SGP"},
    "Slovak Republic": {"iso_code_2": "SK", "iso_code_3": "SVK"},
    "Slovenia": {"iso_code_2": "SI", "iso_code_3": "SVN"},
    "Solomon Islands": {"iso_code_2": "SB", "iso_code_3": "SLB"},
    "Somalia": {"iso_code_2": "SO", "iso_code_3": "SOM"},
    "South Africa": {"iso_code_2": "ZA", "iso_code_3": "ZAF"},
    "South Georgia &amp; South Sandwich Islands": {"iso_code_2": "GS", "iso_code_3": "SGS"},
    "South Sudan": {"iso_code_2": "SS", "iso_code_3": "SSD"},
    "Spain": {"iso_code_2": "ES", "iso_code_3": "ESP"},
    "Sri Lanka": {"iso_code_2": "LK", "iso_code_3": "LKA"},
    "St. Barthelemy": {"iso_code_2": "BL", "iso_code_3": "BLM"},
    "St. Helena": {"iso_code_2": "SH", "iso_code_3": "SHN"},
    "St. Martin (French part)": {"iso_code_2": "MF", "iso_code_3": "MAF"},
    "St. Pierre and Miquelon": {"iso_code_2": "PM", "iso_code_3": "SPM"},
    "Sudan": {"iso_code_2": "SD", "iso_code_3": "SDN"},
    "Suriname": {"iso_code_2": "SR", "iso_code_3": "SUR"},
    "Svalbard and Jan Mayen Islands": {"iso_code_2": "SJ", "iso_code_3": "SJM"},
    "Swaziland": {"iso_code_2": "SZ", "iso_code_3": "SWZ"},
    "Sweden": {"iso_code_2": "SE", "iso_code_3": "SWE"},
    "Switzerland": {"iso_code_2": "CH", "iso_code_3": "CHE"},
    "Syrian Arab Republic": {"iso_code_2": "SY", "iso_code_3": "SYR"},
    "Taiwan": {"iso_code_2": "TW", "iso_code_3": "TWN"},
    "Tajikistan": {"iso_code_2": "TJ", "iso_code_3": "TJK"},
    "Tanzania, United Republic of": {"iso_code_2": "TZ", "iso_code_3": "TZA"},
    "Thailand": {"iso_code_2": "TH", "iso_code_3": "THA"},
    "Togo": {"iso_code_2": "TG", "iso_code_3": "TGO"},
    "Tokelau": {"iso_code_2": "TK", "iso_code_3": "TKL"},
    "Tonga": {"iso_code_2": "TO", "iso_code_3": "TON"},
    "Trinidad and Tobago": {"iso_code_2": "TT", "iso_code_3": "TTO"},
    "Tristan da Cunha": {"iso_code_2": "TA", "iso_code_3": "SHN"},
    "Tunisia": {"iso_code_2": "TN", "iso_code_3": "TUN"},
    "Turkey": {"iso_code_2": "TR", "iso_code_3": "TUR"},
    "Turkmenistan": {"iso_code_2": "TM", "iso_code_3": "TKM"},
    "Turks and Caicos Islands": {"iso_code_2": "TC", "iso_code_3": "TCA"},
    "Tuvalu": {"iso_code_2": "TV", "iso_code_3": "TUV"},
    "Uganda": {"iso_code_2": "UG", "iso_code_3": "UGA"},
    "Ukraine": {"iso_code_2": "UA", "iso_code_3": "UKR"},
    "United Arab Emirates": {"iso_code_2": "AE", "iso_code_3": "ARE"},
    "United Kingdom": {"iso_code_2": "GB", "iso_code_3": "GBR"},
    "United States": {"iso_code_2": "US", "iso_code_3": "USA"},
    "United States Minor Outlying Islands": {"iso_code_2": "UM", "iso_code_3": "UMI"},
    "Uruguay": {"iso_code_2": "UY", "iso_code_3": "URY"},
    "Uzbekistan": {"iso_code_2": "UZ", "iso_code_3": "UZB"},
    "Vanuatu": {"iso_code_2": "VU", "iso_code_3": "VUT"},
    "Vatican City State (Holy See)": {"iso_code_2": "VA", "iso_code_3": "VAT"},
    "Venezuela": {"iso_code_2": "VE", "iso_code_3": "VEN"},
    "Viet Nam": {"iso_code_2": "VN", "iso_code_3": "VNM"},
    "Virgin Islands (British)": {"iso_code_2": "VG", "iso_code_3": "VGB"},
    "Virgin Islands (U.S.)": {"iso_code_2": "VI", "iso_code_3": "VIR"},
    "Wallis and Futuna Islands": {"iso_code_2": "WF", "iso_code_3": "WLF"},
    "Western Sahara": {"iso_code_2": "EH", "iso_code_3": "ESH"},
    "Yemen": {"iso_code_2": "YE", "iso_code_3": "YEM"},
    "Zambia": {"iso_code_2": "ZM", "iso_code_3": "ZMB"},
    "Zimbabwe": {"iso_code_2": "ZW", "iso_code_3": "ZWE"}
}


COUNTRY_STATE_CODES = {
    "United States": {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "District of Columbia": "DC",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington State": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY",
        "Puerto Rico": "PR"
    },
    "Canada": {
        "Alberta": "AB",
        "British Columbia": "BC",
        "Manitoba": "MB",
        "New Brunswick": "NB",
        "Newfoundland": "NL",
        "Northwest Territories": "NT",
        "Nova Scotia": "NS",
        "Nunavut": "NU",
        "Ontario": "ON",
        "Prince Edward Island": "PE",
        "Quebec": "QC",
        "Saskatchewan": "SK",
        "Yukon": "YT"
    },
    "Mexico": {
        "Aguascalientes": "AG",
        "Baja California Norte": "BC",
        "Baja California Sur": "BS",
        "Campeche": "CM",
        "Chiapas": "CS",
        "Chihuahua": "CH",
        "Coahuila": "CO",
        "Colima": "CL",
        "Distrito Federal": "DF",
        "Durango": "DG",
        "Guanajuato": "GT",
        "Guerrero": "GR",
        "Hidalgo": "HG",
        "Jalisco": "JA",
        "Mexico": "MX",
        "Michoacan": "MI",
        "Morelos": "MO",
        "Nayarit": "NA",
        "Nuevo Leon": "NL",
        "Oaxaca": "OA",
        "Puebla": "PU",
        "Queretaro": "QT",
        "Quintana Roo": "QR",
        "San Luis Potosi": "SL",
        "Sinaloa": "SI",
        "Sonora": "SO",
        "Tabasco": "TB",
        "Tamaulipas": "TM",
        "Tlaxcala": "TL",
        "Veracruz": "VE",
        "Yucatan": "YU",
        "Zacatecas": "ZA"
    }
}


def get_country_code(country):
    code = COUNTRY_CODES.get(country, {}).get('iso_code_2')
    if not code:
        frappe.throw('Cannot get country code for country "%s"' % country)
    return code


def get_country_state_code(country, state):
    state_code = COUNTRY_STATE_CODES.get(country, {}).get(state, '')
    if not state_code and state:
        state = state.upper().strip()
        if state in COUNTRY_STATE_CODES.get(country, {}).values():
            state_code = state
    return state_code
