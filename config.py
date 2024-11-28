from Scraper import ScraperReq, ScraperWeb
from utils import Site


fashionjobs = Site()
fashionjobs.url = "https://it.fashionjobs.com/s/?categories%5B%5D=6&metier%5B6%5D%5B%5D=96&metier%5B6%5D%5B%5D=95&metier%5B6%5D%5B%5D=94&metier%5B6%5D%5B%5D=269&metier%5B6%5D%5B%5D=270&metier%5B6%5D%5B%5D=260&metier%5B6%5D%5B%5D=88&metier%5B6%5D%5B%5D=191&metier%5B6%5D%5B%5D=93&metier%5B6%5D%5B%5D=265&metier%5B6%5D%5B%5D=90&metier%5B6%5D%5B%5D=91&metier%5B6%5D%5B%5D=236&metier%5B6%5D%5B%5D=89&metier%5B6%5D%5B%5D=258&metier%5B1%5D%5B%5D=224&metier%5B1%5D%5B%5D=9&metier%5B1%5D%5B%5D=15&metier%5B1%5D%5B%5D=24&metier%5B1%5D%5B%5D=252&metier%5B1%5D%5B%5D=213&metier%5B1%5D%5B%5D=1&metier%5B1%5D%5B%5D=179&metier%5B1%5D%5B%5D=14&metier%5B1%5D%5B%5D=253&metier%5B1%5D%5B%5D=5&metier%5B1%5D%5B%5D=2&categories%5B%5D=3&metier%5B3%5D%5B%5D=208&metier%5B3%5D%5B%5D=60&metier%5B3%5D%5B%5D=210&metier%5B3%5D%5B%5D=62&metier%5B3%5D%5B%5D=52&metier%5B3%5D%5B%5D=66&metier%5B3%5D%5B%5D=229&metier%5B3%5D%5B%5D=53&metier%5B3%5D%5B%5D=31&metier%5B3%5D%5B%5D=197&metier%5B3%5D%5B%5D=45&metier%5B3%5D%5B%5D=51&metier%5B3%5D%5B%5D=39&metier%5B3%5D%5B%5D=33&metier%5B3%5D%5B%5D=46&metier%5B3%5D%5B%5D=214&metier%5B3%5D%5B%5D=215&metier%5B3%5D%5B%5D=32&metier%5B3%5D%5B%5D=55&metier%5B3%5D%5B%5D=54&metier%5B3%5D%5B%5D=56&metier%5B3%5D%5B%5D=59&metier%5B3%5D%5B%5D=64&metier%5B3%5D%5B%5D=50&metier%5B3%5D%5B%5D=58&metier%5B3%5D%5B%5D=256&metier%5B3%5D%5B%5D=63&metier%5B3%5D%5B%5D=232&metier%5B3%5D%5B%5D=40&metier%5B3%5D%5B%5D=38&metier%5B3%5D%5B%5D=47&metier%5B3%5D%5B%5D=36&metier%5B3%5D%5B%5D=37&metier%5B3%5D%5B%5D=196&metier%5B3%5D%5B%5D=231&metier%5B3%5D%5B%5D=230&categories%5B%5D=14&metier%5B14%5D%5B%5D=207&metier%5B14%5D%5B%5D=237&metier%5B14%5D%5B%5D=218&metier%5B14%5D%5B%5D=209&metier%5B14%5D%5B%5D=217&metier%5B14%5D%5B%5D=219&metier%5B14%5D%5B%5D=8&metier%5B14%5D%5B%5D=84&categories%5B%5D=15&metier%5B15%5D%5B%5D=162&metier%5B15%5D%5B%5D=234&metier%5B15%5D%5B%5D=158&regions%5B%5D=266&departements%5B266%5D%5B%5D=4426&departements%5B266%5D%5B%5D=4427&departements%5B266%5D%5B%5D=4428&departements%5B266%5D%5B%5D=4429&departements%5B266%5D%5B%5D=4430&departements%5B266%5D%5B%5D=4431&departements%5B266%5D%5B%5D=4432&departements%5B266%5D%5B%5D=4433&departements%5B266%5D%5B%5D=4435&departements%5B266%5D%5B%5D=4436&departements%5B266%5D%5B%5D=4437&departements%5B266%5D%5B%5D=4434&regions%5B%5D=258&departements%5B258%5D%5B%5D=4496&departements%5B258%5D%5B%5D=4495&departements%5B258%5D%5B%5D=4390&departements%5B258%5D%5B%5D=4391&contrats%5B%5D=5"
fashionjobs.paths["xpath_list"] = (
    "/html/body/div[2]/div[2]/div/div[2]/div/div/main/div/section[2]/div/ul/li"
)
fashionjobs.paths["xpath_offer_name"] = (
    "/html/body/div[2]/div[2]/div/div[2]/div/div/main/div/section[2]/div/ul/li[{index}]/div/div[2]/div/a/h3/span/text()"
)
fashionjobs.paths["xpath_offer_link"] = (
    "/html/body/div[2]/div[2]/div/div[2]/div/div/main/div/section[2]/div/ul/li[{index}]/div/div[2]/div/a/@href"
)


kering = Site()
kering.url = "https://www.kering.com/it/talenti/offerte-di-lavoro/?countriesList=Italy&jobFamiliesList=Communication_%26_Marketing%2CGeneral_Management%2CMerchandising%2CSupply_Chain&workerSubTypesList=Trainee+%2F+Apprentice%2CStudent+%28Fixed+Term%29+%28Trainee%29%2CApprentice+%28Fixed+Term%29"
kering.paths["xpath_list"] = (
    "/html/body/div[1]/div/div[3]/section/div[2]/div[2]/div/div"
)
kering.paths["xpath_offer_name"] = (
    "/html/body/div[1]/div/div[3]/section/div[2]/div[2]/div/div[{index}]/div[2]/div[1]/div[1]/h2/a/text()"
)
kering.paths["xpath_offer_link"] = (
    "/html/body/div[1]/div/div[3]/section/div[2]/div[2]/div/div[{index}]/div[2]/div[1]/div[1]/h2/a/@href"
)

lvmh = Site()
lvmh.url = "https://www.lvmh.com/api/search"
lvmh.body = '{"queries":[{"indexName":"PRD-en-us-timestamp-desc","params":{"facetFilters":[["contractFilter:Apprenticeship","contractFilter:Internship"],["functionFilter:Design & Creation","functionFilter:General Management","functionFilter:Marketing","functionFilter:Merchandising","functionFilter:Sales","functionFilter:Supply Chain & Logistics"],["regionStateFilter:Lombardia","regionStateFilter:Veneto"],["requiredExperienceFilter:Beginner"]],"facets":["businessGroupFilter","cityFilter","contractFilter","countryRegionFilter","fullTimePartTimeFilter","functionFilter","geographicAreaFilter","maison","regionStateFilter","requiredExperienceFilter","workModeFilter"],"filters":"category:job","highlightPostTag":" ","highlightPreTag":" ","hitsPerPage":10,"maxValuesPerFacet":10,"page":0,"query":"","tagFilters":""}},{"indexName":"PRD-en-us-timestamp-desc","params":{"analytics":false,"clickAnalytics":false,"facetFilters":[["functionFilter:Design & Creation","functionFilter:General Management","functionFilter:Marketing","functionFilter:Merchandising","functionFilter:Sales","functionFilter:Supply Chain & Logistics"],["regionStateFilter:Lombardia","regionStateFilter:Veneto"],["requiredExperienceFilter:Beginner"]],"facets":"contractFilter","filters":"category:job","highlightPostTag":" ","highlightPreTag":" ","hitsPerPage":0,"maxValuesPerFacet":10,"page":0,"query":""}},{"indexName":"PRD-en-us-timestamp-desc","params":{"analytics":false,"clickAnalytics":false,"facetFilters":[["contractFilter:Apprenticeship","contractFilter:Internship"],["regionStateFilter:Lombardia","regionStateFilter:Veneto"],["requiredExperienceFilter:Beginner"]],"facets":"functionFilter","filters":"category:job","highlightPostTag":" ","highlightPreTag":" ","hitsPerPage":0,"maxValuesPerFacet":10,"page":0,"query":""}},{"indexName":"PRD-en-us-timestamp-desc","params":{"analytics":false,"clickAnalytics":false,"facetFilters":[["contractFilter:Apprenticeship","contractFilter:Internship"],["functionFilter:Design & Creation","functionFilter:General Management","functionFilter:Marketing","functionFilter:Merchandising","functionFilter:Sales","functionFilter:Supply Chain & Logistics"],["requiredExperienceFilter:Beginner"]],"facets":"regionStateFilter","filters":"category:job","highlightPostTag":" ","highlightPreTag":" ","hitsPerPage":0,"maxValuesPerFacet":10,"page":0,"query":""}},{"indexName":"PRD-en-us-timestamp-desc","params":{"analytics":false,"clickAnalytics":false,"facetFilters":[["contractFilter:Apprenticeship","contractFilter:Internship"],["functionFilter:Design & Creation","functionFilter:General Management","functionFilter:Marketing","functionFilter:Merchandising","functionFilter:Sales","functionFilter:Supply Chain & Logistics"],["regionStateFilter:Lombardia","regionStateFilter:Veneto"]],"facets":"requiredExperienceFilter","filters":"category:job","highlightPostTag":" ","highlightPreTag":" ","hitsPerPage":0,"maxValuesPerFacet":10,"page":0,"query":""}}]}'
lvmh.paths["xpath_list"] = (
    "/html/body/div[1]/div/div/div/div[2]/div/main/div/section/div[2]/div/ul/li"
)
lvmh.paths["xpath_offer_name"] = (
    "/html/body/div[1]/div/div/div/div[2]/div/main/div/section/div[2]/div/ul/li[{index}]/div/div/div[2]/div/div[1]/h3/a/span[2]/span/span/text()"
)
lvmh.paths["xpath_offer_link"] = (
    "/html/body/div[1]/div/div/div/div[2]/div/main/div/section/div[2]/div/ul/li[{index}]/div/div/div[2]/div/div[1]/h3/a/@href"
)


scrapers = (ScraperWeb(fashionjobs), ScraperWeb(kering), ScraperReq(lvmh))
