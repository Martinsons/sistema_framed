# Step 3: Define the conditions
conditions = {
    'dhl.xlsx': [
        lambda row: row['width'] == 120 and row['length'] == 120 and row['recipientCountry'] == 'US',
        lambda row: row['width'] == 80 and row['length'] == 160 and row['recipientCountry'] == 'US',
        lambda row: row['width'] == 100 and row['length'] == 200 and row['recipientCountry'] == 'US',
        lambda row: row['width'] == 80 and row['length'] == 80 and row['recipientCountry'] == 'GB',
        lambda row: row['width'] == 90 and row['length'] == 90 and row['recipientCountry'] == 'GB',
        lambda row: row['width'] == 120 and row['length'] == 120 and row['recipientCountry'] == 'GB',
        lambda row: row['width'] == 100 and row['length'] == 150 and row['recipientCountry'] == 'GB',
        lambda row: row['width'] == 80 and row['length'] == 160 and row['recipientCountry'] == 'GB',
        lambda row: row['width'] == 100 and row['length'] == 200 and row['recipientCountry'] == 'GB',
        lambda row: row['width'] == 100 and row['length'] == 100 and row['recipientCountry'] == 'GB' and row['serviceType'] == 'INTERNATIONAL_ECONOMY',
        lambda row: row['width'] == 80 and row['length'] == 120 and row['recipientCountry'] == 'GB' and row['serviceType'] == 'INTERNATIONAL_ECONOMY',
        lambda row: row['width'] == 90 and row['length'] == 120 and row['recipientCountry'] == 'GB' and row['serviceType'] == 'INTERNATIONAL_ECONOMY',
        lambda row: row['width'] == 75 and row['length'] == 150 and row['recipientCountry'] == 'GB' and row['serviceType'] == 'INTERNATIONAL_ECONOMY',
        lambda row: row['width'] == 60 and row['length'] == 180 and row['recipientCountry'] == 'GB' and row['serviceType'] == 'INTERNATIONAL_ECONOMY'
    ],
    'dpd.xlsx': [
        lambda row: row['width'] == 60 and row['length'] == 90 and row['recipientCountry'] == 'US' and row['serviceType'] == 'INTERNATIONAL_ECONOMY',
    ],
    'dhl.xlsx': [
        lambda row: row['width'] == 100 and row['length'] == 150 and row['recipientCountry'] == 'US'
    ],
    'dhl.xlsx': [
        lambda row: row['width'] == 70 and row['length'] == 140 and row['recipientCountry'] == 'GB'
    ],
    'dhl.xlsx': [
        lambda row: row['width'] == 40 and row['length'] == 160 and row['recipientCountry'] == 'GB'
    ]

    # Add more condition sets here
}


