# Access point load sample interval in seconds. (60 seconds is preferred)
SAMPLE_INTERVAL = 60

# Specifies how many seconds ago from now to start calculating. A good value would be a bit more than the
# "Reporting Period" you've set when creating the api-clientsessions report in Cisco Prime Infra
CALCULATE_AP_LOAD_LAG = 3900

# Specifies what the minimum average session throughput in Mbits should be to take the session into account and use it
# for Access Point Load calculations. Set to 0 if you don't want to filter sessions out.
BW_LOW_WATERMARK = 0.01

# Specifies RED/YELLOW/GREEN thresholds used to determine the User Experience.
# SNR <= SNR_LOW_WATERMARK == RED experience
# SNR_LOW_WATERMARK < SNR < SNR_HIGH_WATERMARK == YELLOW experience
# SRR >= SNR_HIGH_WATERMARK == GREEN experience
SNR_LOW_WATERMARK = 15
SNR_HIGH_WATERMARK = 20

# Specify which access point specs to use by default
DEFAULT_AP_TYPE = 'AIRONET2600'

# Mapping of RSSI to MCS index per access point type
RSSI_MCS_MAP = {'AIRONET2600': {0: -91, 1: -90, 2: -89, 3: -88, 4: -85, 5: -80, 6: -78, 7: -75},
                'AIRONET1550': {0: -93, 1: -91, 2: -89, 3: -86, 4: -82, 5: -78, 6: -77, 7: -75},
                }
# Mapping of MCS index to datarate per access point type
MCS_DATARATE_MAP = {'AIRONET2600': {0: 7.2, 1: 14.3, 2: 21.7, 3: 28.9, 4: 43.3, 5: 57.8, 6: 65, 7: 72.2},
                    'AIRONET1550': {0: 7.2, 1: 14.3, 2: 21.7, 3: 28.9, 4: 43.3, 5: 57.8, 6: 65, 7: 72.2},
                    }