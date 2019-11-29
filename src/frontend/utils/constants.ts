// constants.ts
import { Dict } from '~/types'

// - Model related
export const enumSettingType: Dict<number> = {
  STRING: 1,
  INTEGER: 2,
  FLOAT: 3,
  BOOLEAN: 4,
  DATETIME: 5,
  UUID: 6,
}

// - Contact-related constants
export const contactConstants = {
  other: {
    types: [
      'Facebook',
      'Signal',
      'Telegram',
      'WhatsApp'
    ]
  }
}

// - Geography-related constants
export const geographyConstants = {
  country: {
    names: [
      "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Anguilla",
      "Antigua & Barbuda", "Argentina", "Armenia", "Aruba", "Australia",
      "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
      "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia",
      "Bosnia & Herzegovina", "Botswana", "Brazil", "British Virgin Islands",
      "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon",
      "Canada", "Cape Verde", "Cayman Islands", "Chad", "Chile", "China",
      "Colombia", "Congo", "Cook Islands", "Costa Rica", "Cote D Ivoire",
      "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti",
      "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
      "Equatorial Guinea", "Estonia", "Ethiopia", "Falkland Islands",
      "Faroe Islands", "Fiji", "Finland", "France", "French Polynesia",
      "French West Indies", "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
      "Gibraltar", "Greece", "Greenland", "Grenada", "Guam", "Guatemala",
      "Guernsey", "Guinea", "Guinea Bissau", "Guyana", "Haiti", "Honduras",
      "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq",
      "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jersey",
      "Jordan", "Kazakhstan", "Kenya", "Kuwait", "Kyrgyz Republic", "Laos",
      "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
      "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi",
      "Malaysia", "Maldives", "Mali", "Malta", "Mauritania", "Mauritius",
      "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat",
      "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands",
      "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua",
      "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palestine", "Panama",
      "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland",
      "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russia",
      "Rwanda", "Saint Pierre & Miquelon", "Samoa", "San Marino",
      "Satellite", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
      "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "South Africa",
      "South Korea", "Spain", "Sri Lanka", "St Kitts & Nevis", "St Lucia",
      "St Vincent", "St. Lucia", "Sudan", "Suriname", "Swaziland", "Sweden",
      "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand",
      "Timor L'Este", "Togo", "Tonga", "Trinidad & Tobago", "Tunisia",
      "Turkey", "Turkmenistan", "Turks & Caicos", "Uganda", "Ukraine",
      "United Arab Emirates", "United Kingdom", "United States",
      "United States Minor Outlying Islands", "Uruguay", "Uzbekistan",
      "Venezuela", "Vietnam", "Virgin Islands (US)", "Yemen", "Zambia",
      "Zimbabwe"
    ]
  },
  state: {
    codes: [
      'AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL',
      'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH',
      'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM',
      'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC',
      'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY'
    ]
  }
}

// - Name-related constants
export const nameConstants = {
  prefixes: [
    'Mr.',
    'Mrs.',
    'Ms.',
    'Dr.'
  ],
  suffixes: [
    'Sr.',
    'Jr.',
    'I',
    'II',
    'III',
    'IV'
  ]
}
