# postcode_scripts_data
A repo of scripts to do ETL operations on postcodes

## Postcode sector data
A postcode sector comprises of the first letters / numbers before the space in a postcode e.g. postcode sector in bold text,  **EH8** 9DD,**PE29** 2HW

The data was avalaible for download at https://www.freemaptools.com/download-uk-postcode-lat-lng.htm (it was not uoploaded here)

The center latitude longitude was calculated by taking a simple average of the latitudes or longitudes. 

The following assumptions were made
1. The area of the sector is small in relation to the earth and can be considered 'flat'

2. Following from '1' , curvature of the Earth will not significantly effect the calculated result.

3. The center latitude / longitude is taken as the coordinates to use for any query on a postcode within that sector.

Note:

Average UK postcode sector size 33 square miles.

Average population 23,595

Generally larger postcode sectors are more sparsley populated.

Sample data results were checked against Google Maps and the http://postcodes.io service.

Source https://beacon-dodsworth.co.uk/blog/all-you-need-to-know-about-postcodes-but-were-afraid-to-ask/
