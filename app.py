import requests
from bs4 import BeautifulSoup

def scrape_website(url, output_file):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Exclude common header and footer tags in the websites
            excluded_tags = ['header', 'footer', 'nav']

            for tag_name in excluded_tags:
                for tag in soup.find_all(tag_name):
                    tag.decompose()

            all_text = soup.get_text()

            with open(output_file, 'a', encoding='utf-8') as file:
                file.write(all_text)
                
            print(f"Scraping successful. Appended to Markdown file: {output_file}")
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# List of websites to scrape
websites_to_scrape = [
    ('https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4028/gst-hst-new-housing-rebate.html', 'output.md'),
    ('https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-home-construction/new-housingrebate.html', 'output.md'),
    ('https://wowa.ca/calculators/gst-hst-rebate-new-homecanada#:~:text=Ontario%20New%20Housing%20Rebate&text=The%20amount%20of%20rebate%20you,on%2C%20and%20%2416%2C080%20if%20not', 'output.md'),
    ('https://www.ontario.ca/document/land-transfer-tax/land-transfer-taxrefunds-first-time-homebuyers', 'output.md'),
    ('https://www.canada.ca/en/revenue-agency/programs/about-canadarevenue-agency-cra/federal-government-budgets/budget-2022-plan-groweconomy-make-life-more-affordable/first-time-home-buyers-tax-credit.html', 'output.md'),
    ('https://www.placetocallhome.ca/fthbi/first-time-homebuyer-incentive', 'output.md'),
    ('https://www.cibc.com/en/personal-banking/mortgages/resource-centre/home-buyers-plan.html', 'output.md'),
    ('https://www.rebgv.org/content/rebgv-org/news-archive/canada-amendsforeign-buyer-ban-regulations.html', 'output.md'),
    ('https://www.ratehub.ca/land-transfer-tax', 'output.md'),
    ('https://wowa.ca/calculators/land-transfer-tax', 'output.md'),
    ('https://www.ratehub.ca/land-transfer-tax-rebate', 'output.md'),
    ('https://www.kelownanow.com/news/news/Sponsored/The_down_low_on_purchasing_a_home_on_leased_land_at_West_Harbour_in_West_Kelowna/', 'output.md'),
    ('https://www.ontario.ca/document/non-resident-speculation-tax/nonresident-speculation-tax-rebates-and-refunds', 'output.md'),
    ('https://www.ontario.ca/document/non-resident-speculation-tax', 'output.md'),
    ('https://www2.gov.bc.ca/gov/content/taxes/property-taxes/propertytransfer-tax/additional-property-transfer-tax/refunds', 'output.md'),
    ('https://www2.gov.bc.ca/gov/content/taxes/property-taxes/propertytransfer-tax/additional-property-transfer-tax', 'output.md'),
    ('https://www2.gov.bc.ca/gov/content/taxes/speculation-vacancy-tax/howtax-works', 'output.md'),
    ('https://www.toronto.ca/services-payments/property-taxes-utilities/vacanthome-tax/', 'output.md'),
    ('https://www.sorbaralaw.com/resources/knowledge-centre/publication/understanding-the-vacant-home-tax', 'output.md'),
    ('https://bridgewellgroup.ca/bc-speculation-and-vacancy-tax/', 'output.md'),
    ('https://money.ca/mortgages/homebuying/mortgages-101-a-guide-to-getting-your-mortgage', 'output.md'),
    ('https://shumanlaw.ca/what-is-a-parcel-of-tied-land-potl/', 'output.md'),
    ('https://www.nbc.ca/personal/advice/immigration/home-buying-newcomerscanada.html#:~:text=In%20Canada%2C%20both%20permanent%20resident,they%20hold%20a%20work%20permit', 'output.md'),
    ('https://tribunalsontario.ca/documents/ltb/Brochures/How%20a%20Landlord%20Can%20End%20a%20Tenancy%20(EN).html', 'output.md'),
    ('https://www2.gov.bc.ca/gov/content/housing-tenancy/residential-tenancies/ending-a-tenancy/landlord-notice', 'output.md'),
    ('https://www.alberta.ca/ending-a-tenancy', 'output.md'),
    ('https://wowa.ca/mortgage-rates', 'output.md'),
    ('https://www.ratehub.ca/prime-rate', 'output.md'),
    ('https://www.toronto.ca/community-people/housing-shelter/short-termrentals/', 'output.md'),
    ('https://vancouver.ca/doing-business/short-termrentals.aspx#:~:text=A%20short%2Dterm%20rental%20can,%2C%20identification%2C%20taxes%2C%20and%20insurance', 'output.md'),
    ('https://www.calgary.ca/for-business/licences/short-term-rentals.html', 'output.md'),
    ('https://www.canada.ca/en/financial-consumer-agency/services/mortgages/downpayment.html#:~:text=If%20your%20down%20payment%20is,to%20buy%20mortgage%20loan%20insurance.&text=If%20you%27re%20self%2Demployed,come%20from%20your%20own%20funds', 'output.md'),
    ('https://www.tarion.com/homeowners/the-new-home-warranty', 'output.md'),
    ('https://www.bchousing.org/licensing-consumer-services/new-homes/homewarranty-insurance-new-homes', 'output.md'),
    ('https://www.alberta.ca/new-home-warranty-overview', 'output.md'),
    ('https://www.zolo.ca/toronto-real-estate/trends', 'output.md'),
    ('https://creastats.crea.ca/board/vanc', 'output.md'),
    ('https://canadaimmigrants.com/average-house-price-in-toronto/#:~:text=The%20average%20house%20price%20in,compared%20to%20the%20year%20prior', 'output.md'),
    ('https://canadaimmigrants.com/average-house-price-in-vancouver/', 'output.md'),
    ('https://canadaimmigrants.com/average-house-price-in-calgary/', 'output.md'),
    ('https://canadaimmigrants.com/average-house-price-in-edmonton/#:~:text=The%20average%20house%20price%20in,by%203.8%25%20year%20over%20year', 'output.md'),
    ('https://canadaimmigrants.com/average-house-price-in-ottawa/#:~:text=The%20average%20house%20price%20in,same%20month%20a%20year%20ago', 'output.md'),
    ('https://canadaimmigrants.com/average-house-price-in-montreal/#:~:text=The%20average%20house%20price%20in,%25%20year%2Dover%2Dyear', 'output.md'),
    ('https://wowa.ca/reports/canada-housing-market', 'output.md'),
    ('https://creastats.crea.ca/en-CA/', 'output.md'),
]

# Loop through the list of websites and scrape each one
for website, output_file in websites_to_scrape:
    print(f"Scraping {website}...")
    scrape_website(website, output_file)
    print("\n")